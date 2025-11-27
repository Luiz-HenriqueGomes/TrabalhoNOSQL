from src.conexion.mongo_queries import MongoQueries
from src.utils import config

class SplashScreen:
    def __init__(self):
        self.mongo = MongoQueries()

    def get_documents_count(self, collection_name):
        # Conecta, conta e retorna
        self.mongo.connect()
        count = self.mongo.db[collection_name].count_documents({})
        self.mongo.close()
        return count

    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE VENDAS                     #
        #                                                         #
        #  TOTAL DE REGISTROS:                                    #
        #      1 - CLIENTES:         {str(self.get_documents_count('clientes')).ljust(5)}                        #
        #      2 - PRODUTOS:         {str(self.get_documents_count('produtos')).ljust(5)}                        #
        #      3 - VENDAS:           {str(self.get_documents_count('vendas')).ljust(5)}                        #
        #                                                         #
        #  CRIADO POR:  GABRIELY AZEVEDO                          #
        #               GUILHERME DOS SANTOS                      #
        #               LUIZ HENRIQUE                             #
        #                RICARDO DA SILVA                         #
        #                RODRIGO ARAUJO                           #
        #                                                         #
        #                                                         #
        #  DISCIPLINA: BANCO DE DADOS                             #
        #  PROFESSOR: HOWARD ROATTI                               #
        ########################################################
        """
    
