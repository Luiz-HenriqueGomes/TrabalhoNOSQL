import os

def clear_console(wait_time: int = 3):
    import time
    if wait_time > 0:
        time.sleep(wait_time)
    os.system("cls" if os.name == "nt" else "clear")

class Menu:
    def __init__(self):
        self.menu_str = """
        -------------------------------
        MENU PRINCIPAL
        -------------------------------
        1 - Relatórios
        2 - Inserir Registros
        3 - Remover Registros
        4 - Atualizar Registros
        5 - Sair
        -------------------------------
        """

    def show(self):
        print(self.menu_str)
        return input("Escolha uma opção: ")
    