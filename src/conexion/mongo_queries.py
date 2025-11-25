from pymongo import MongoClient

class MongoQueries:
    def __init__(self):
        # Conecta ao localhost na porta padrão
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client['trabalho_nosql']
        
    def __del__(self):
        # Fecha a conexão quando o objeto é destruído
        if hasattr(self, 'client'):
            self.client.close()

    def get_db(self):
        return self.db
    
    # Métodos utilitários para fechar conexão explicitamente se necessário
    def close(self):
        self.client.close()
        self.client = None
        
    def connect(self):
        # Reconecta se necessário (útil se a conexão caiu)
        if self.client is None:
            self.client = MongoClient("mongodb://localhost:27017/")
            self.db = self.client['trabalho_nosql']