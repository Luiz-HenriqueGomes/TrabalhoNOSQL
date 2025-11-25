from src.conexion.mongo_queries import MongoQueries
import pandas as pd

class Relatorio:
    def __init__(self):
        self.mongo = MongoQueries()

    def get_relatorio_clientes(self):
        # Conecta
        self.mongo.connect()
        
        # Query
        projection = {
            "_id": 0,
            "cpf": 1,
            "nome": 1,
            "email": 1,
            "telefone": 1,
            "endereco.cidade": 1,
            "endereco.estado": 1
        }
        
        print("\n--- RELATÓRIO DE CLIENTES ---")
        cursor = self.mongo.db["clientes"].find({}, projection).sort("nome", 1)
        lista_clientes = list(cursor)

        if not lista_clientes:
            print("Nenhum cliente encontrado.")
        else:
            # Achata o JSON para mostrar bonito no DataFrame
            df = pd.json_normalize(lista_clientes)
            print(df.to_string(index=False))
            
        input("Pressione Enter para sair do relatório...")
        self.mongo.close()

    def get_relatorio_produtos(self):
        self.mongo.connect()
        
        projection = {
            "_id": 0,
            "nome": 1,
            "descricao": 1,
            "preco_unitario": 1,
            "estoque.quantidade": 1 
        }
        
        print("\n--- RELATÓRIO DE PRODUTOS & ESTOQUE ---")
        cursor = self.mongo.db["produtos"].find({}, projection).sort("nome", 1)
        lista_produtos = list(cursor)
        
        # Formata para exibir o Status do Estoque (Lógica da Aplicação)
        lista_formatada = []
        for prod in lista_produtos:
            qtde = prod.get("estoque", {}).get("quantidade", 0)
            if qtde == 0: status = "Sem Estoque"
            elif qtde < 10: status = "Estoque Baixo"
            else: status = "OK"
            
            lista_formatada.append({
                "Produto": prod.get("nome"),
                "Preço": prod.get("preco_unitario"),
                "Qtde": qtde,
                "Status": status
            })

        if not lista_formatada:
            print("Nenhum produto encontrado.")
        else:
            df = pd.DataFrame(lista_formatada)
            print(df.to_string(index=False))
            
        input("Pressione Enter para sair do relatório...")
        self.mongo.close()

    def get_relatorio_vendas(self):
        self.mongo.connect()
        print("\n--- RELATÓRIO DE VENDAS (AGREGAÇÃO) ---")
        
        pipeline = [
            {
                "$lookup": {
                    "from": "clientes",
                    "localField": "cliente_id",
                    "foreignField": "_id",
                    "as": "dados_cliente"
                }
            },
            { "$unwind": "$dados_cliente" },
            {
                "$project": {
                    "_id": 0,
                    "ID Venda": "$_id",
                    "Data": "$data_venda",
                    "Total": "$valor_total",
                    "Cliente": "$dados_cliente.nome",
                    "Itens": { "$sum": "$itens.quantidade" }
                }
            },
            { "$sort": { "Data": -1 } }
        ]
        
        cursor = self.mongo.db["vendas"].aggregate(pipeline)
        lista_vendas = list(cursor)
        
        if not lista_vendas:
            print("Nenhuma venda encontrada.")
        else:
            df = pd.DataFrame(lista_vendas)
            print(df.to_string(index=False))
            
        input("Pressione Enter para sair do relatório...")
        self.mongo.close()