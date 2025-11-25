from src.utils import config
from src.utils.splash_screen import SplashScreen
from src.reports.relatorios import Relatorio
from src.controller.controller_produto import ControllerProduto
from src.controller.controller_cliente import ControllerCliente

class Principal:
    def __init__(self):
        # Instancia as classes auxiliares e controladoras
        self.splash = SplashScreen()
        self.relatorio = Relatorio()
        self.ctrl_produto = ControllerProduto()
        self.ctrl_cliente = ControllerCliente()
        self.menu = config.Menu()

    def run(self):
        # 1. Exibe a tela inicial (Splash Screen) com contagem de registros
        print(self.splash.get_updated_screen())
        config.clear_console()

        while True:
            # 2. Exibe o Menu Principal e captura a opção
            opcao = self.menu.show()

            # 3. Redireciona para a função correta
            if opcao == '1': # Relatórios
                self.mostrar_relatorios()
            elif opcao == '2': # Inserir
                self.mostrar_inserir()
            elif opcao == '3': # Remover
                self.mostrar_remover()
            elif opcao == '4': # Atualizar
                self.mostrar_atualizar()
            elif opcao == '5': # Sair
                print("Encerrando o sistema... Até logo!")
                break
            else:
                print("Opção inválida!")
                config.clear_console(1)

    def mostrar_relatorios(self):
        while True:
            config.clear_console()
            print("\n--- MENU RELATÓRIOS ---")
            print("1 - Relatório de Clientes")
            print("2 - Relatório de Produtos e Estoque")
            print("3 - Relatório de Vendas (Agregação)")
            print("0 - Voltar ao Menu Principal")
            
            op = input("Escolha uma opção: ")
            if op == '1':
                self.relatorio.get_relatorio_clientes()
            elif op == '2':
                self.relatorio.get_relatorio_produtos()
            elif op == '3':
                self.relatorio.get_relatorio_vendas()
            elif op == '0':
                break
            else:
                print("Opção inválida!")
                input("Pressione Enter...")

    def mostrar_inserir(self):
        while True:
            config.clear_console()
            print("\n--- MENU INSERIR ---")
            print("1 - Novo Cliente")
            print("2 - Novo Produto")
            print("0 - Voltar ao Menu Principal")
            
            op = input("Escolha: ")
            if op == '1':
                self.ctrl_cliente.inserir_cliente()
                input("Pressione Enter para continuar...")
            elif op == '2':
                self.ctrl_produto.inserir_produto()
                input("Pressione Enter para continuar...")
            elif op == '0':
                break
            else:
                print("Opção inválida!")
                input("Pressione Enter...")

    def mostrar_atualizar(self):
        while True:
            config.clear_console()
            print("\n--- MENU ATUALIZAR ---")
            print("1 - Atualizar Cliente")
            print("2 - Atualizar Produto")
            print("0 - Voltar ao Menu Principal")
            
            op = input("Escolha: ")
            if op == '1':
                self.ctrl_cliente.atualizar_cliente()
                input("Pressione Enter para continuar...")
            elif op == '2':
                self.ctrl_produto.atualizar_produto()
                input("Pressione Enter para continuar...")
            elif op == '0':
                break
            else:
                print("Opção inválida!")
                input("Pressione Enter...")

    def mostrar_remover(self):
        while True:
            config.clear_console()
            print("\n--- MENU REMOVER ---")
            print("1 - Remover Cliente")
            print("2 - Remover Produto")
            print("0 - Voltar ao Menu Principal")
            
            op = input("Escolha: ")
            if op == '1':
                self.ctrl_cliente.excluir_cliente()
                input("Pressione Enter para continuar...")
            elif op == '2':
                self.ctrl_produto.excluir_produto()
                input("Pressione Enter para continuar...")
            elif op == '0':
                break
            else:
                print("Opção inválida!")
                input("Pressione Enter...")

if __name__ == "__main__":
    app = Principal()
    app.run()