from src.conexion.mongo_queries import MongoQueries
from src.model.produto import Produto

class ControllerProduto:
    def __init__(self):
        self.mongo = MongoQueries()

    def inserir_produto(self):
        self.mongo.connect()
        print("\n--- Inserindo Novo Produto ---")
        nome = input("Nome do Produto: ")

        # Verifica duplicidade por nome (simplificação)
        if self.verifica_existencia_produto(nome):
            print(f"O produto '{nome}' já existe!")
            return

        descricao = input("Descrição: ")
        preco = float(input("Preço Unitário: "))
        
        print("--- Dados de Estoque ---")
        qtde = int(input("Quantidade Inicial: "))
        custo = float(input("Custo Unitário: "))
        local = input("Localização (ex: Prateleira A): ")
        
        # Calcula total automaticamente
        total_estoque = qtde * custo

        estoque = {
            "quantidade": qtde,
            "custo_unitario": custo,
            "total": total_estoque,
            "localizacao": local
        }

        novo_produto = Produto(nome, descricao, preco, estoque)

        documento = {
            "nome": novo_produto.nome,
            "descricao": novo_produto.descricao,
            "preco_unitario": novo_produto.preco_unitario,
            "estoque": novo_produto.estoque
        }

        self.mongo.db["produtos"].insert_one(documento)
        print("✅ Produto cadastrado com sucesso!")
        self.mongo.close()

    def atualizar_produto(self):
        self.mongo.connect()
        print("\n--- Atualizar Produto ---")
        nome = input("Nome do Produto a alterar: ")

        if not self.verifica_existencia_produto(nome):
            print(f"Produto '{nome}' não encontrado.")
            return

        novo_preco = input("Novo Preço (Enter para manter): ")
        
        # Atualizar estoque
        nova_qtde = input("Nova Quantidade (Enter para manter): ")
        
        update_fields = {}
        if novo_preco: 
            update_fields["preco_unitario"] = float(novo_preco)
        
        if nova_qtde:
            update_fields["estoque.quantidade"] = int(nova_qtde)
            # Nota: Idealmente recalcularia o total do estoque aqui também

        if update_fields:
            self.mongo.db["produtos"].update_one(
                {"nome": nome},
                {"$set": update_fields}
            )
            print("✅ Produto atualizado!")
        else:
            print("Nenhuma alteração.")
        self.mongo.close()

    def excluir_produto(self):
        self.mongo.connect()
        print("\n--- Excluir Produto ---")
        nome = input("Nome do Produto a excluir: ")

        if not self.verifica_existencia_produto(nome):
            print("Produto não encontrado.")
            return

        # Verificação simples se foi vendido (teria que checar array de itens em vendas)
        # Por simplicidade, vamos excluir direto neste exemplo didático
        self.mongo.db["produtos"].delete_one({"nome": nome})
        print("✅ Produto removido.")
        self.mongo.close()

    def verifica_existencia_produto(self, nome):
        resultado = self.mongo.db["produtos"].find_one({"nome": nome})
        return resultado is not None