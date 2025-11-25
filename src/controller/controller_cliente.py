import pandas as pd
from src.conexion.mongo_queries import MongoQueries
from src.model.cliente import Cliente

class ControllerCliente:
    def __init__(self):
        self.mongo = MongoQueries()
        
    def inserir_cliente(self):
        # Cria uma nova conexão para verificar
        self.mongo.connect()
        
        print("\n--- Inserindo Novo Cliente ---")
        cpf = input("CPF (apenas números): ")
        
        # Verifica se já existe 
        if self.verifica_existencia_cliente(cpf):
            print(f"O CPF {cpf} já está cadastrado!")
            return None

        # Solicita os dados
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        
        print("--- Endereço ---")
        logradouro = input("Logradouro: ")
        numero = input("Número: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        cep = input("CEP: ")

        # Monta o objeto Endereço (incorporado)
        endereco = {
            "logradouro": logradouro,
            "numero": numero,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "cep": cep
        }

        # Instancia o objeto Cliente (Model)
        novo_cliente = Cliente(cpf, nome, email, telefone, endereco)

        # Insere no MongoDB
        # Transforma o objeto em dicionário para o Mongo entender
        documento = {
            "cpf": novo_cliente.cpf,
            "nome": novo_cliente.nome,
            "email": novo_cliente.email,
            "telefone": novo_cliente.telefone,
            "endereco": novo_cliente.endereco
        }
        
        self.mongo.db["clientes"].insert_one(documento)
        print("✅ Cliente cadastrado com sucesso!")
        self.mongo.close()

    def atualizar_cliente(self):
        self.mongo.connect()
        print("\n--- Atualizar Cliente ---")
        cpf = input("Informe o CPF do cliente a ser alterado: ")

        if not self.verifica_existencia_cliente(cpf):
            print(f"O CPF {cpf} NÃO foi encontrado.")
            return

        # No MongoDB, usamos $set para atualizar campos específicos
        novo_nome = input("Novo Nome (Enter para manter): ")
        novo_email = input("Novo Email (Enter para manter): ")
        
        update_fields = {}
        if novo_nome: update_fields["nome"] = novo_nome
        if novo_email: update_fields["email"] = novo_email
        
        if update_fields:
            self.mongo.db["clientes"].update_one(
                {"cpf": cpf}, 
                {"$set": update_fields}
            )
            print("✅ Cliente atualizado com sucesso!")
        else:
            print("Nenhuma alteração realizada.")
        
        self.mongo.close()

    def excluir_cliente(self):
        self.mongo.connect()
        print("\n--- Excluir Cliente ---")
        cpf = input("Informe o CPF do cliente a ser excluído: ")

        if not self.verifica_existencia_cliente(cpf):
            print(f"O CPF {cpf} NÃO foi encontrado.")
            return

        # Verifica se o cliente tem vendas associadas (integridade referencial simulada)
        # [cite: 476] O edital pede para verificar referencias
        venda_associada = self.mongo.db["vendas"].find_one({"cliente_cpf": cpf}) # Assumindo que venda guarda CPF ou ID
        # Nota: Nossa venda guarda _id, então precisariamos buscar o _id do cliente primeiro.
        # Simplificação para o exemplo:
        
        cliente = self.mongo.db["clientes"].find_one({"cpf": cpf})
        venda_com_id = self.mongo.db["vendas"].find_one({"cliente_id": cliente["_id"]})
        
        if venda_com_id:
            print("❌ Não é possível excluir: Este cliente possui vendas registradas.")
        else:
            self.mongo.db["clientes"].delete_one({"cpf": cpf})
            print("✅ Cliente excluído com sucesso!")
            
        self.mongo.close()

    def verifica_existencia_cliente(self, cpf):
        # Método auxiliar exigido pelo edital 
        resultado = self.mongo.db["clientes"].find_one({"cpf": cpf})
        return resultado is not None