# Sistema de Vendas - Migração SQL para NoSQL (MongoDB)

Este projeto consiste na reestruturação e implementação de um Sistema de Vendas, migrando de um banco de dados relacional (SQL/Oracle) para um banco de dados orientado a documentos (**MongoDB**).

O sistema foi desenvolvido em **Python** utilizando o padrão de arquitetura **MVC (Model-View-Controller)**.

---

## 📋 Pré-requisitos

Para executar este projeto, certifique-se de ter instalado em sua máquina:

* **Python 3.8+**
* **MongoDB Community Server** (O serviço deve estar em execução)
* **Git**

---

## 🐧 Como executar no Linux (Ambiente Proposto)

Siga os passos abaixo para configurar e rodar a aplicação em um ambiente Linux (Ubuntu/Debian/Mint).

### 1. Clonar o repositório
Abra o terminal e execute:

```bash
git clone [https://github.com/Luiz-HenriqueGomes/TrabalhoNOSQL.git]
cd TrabalhoNOSQL

### 2. Configurar o Ambiente Python
É necessário criar um ambiente virtual (venv) para isolar as dependências do projeto.

Passo 2.1: Instalar o módulo venv (caso não tenha)
    Bash

    sudo apt-get update
    sudo apt-get install python3-venv

Passo 2.2: Criar a pasta do ambiente virtual    
    python3 -m venv venv 

Passo 2.3: Ativar o ambiente
    Bash
    source venv/bin/activate

3. Instalar Dependências do Projeto
Com o ambiente virtual ativo, instale as bibliotecas pymongo e pandas listadas no arquivo de requisitos:
    Bash
    pip install -r requirements.txt

4. Verificar o Serviço MongoDB
    O banco de dados precisa estar ativo para o sistema conectar.
Passo 4.1: Iniciar o serviço
    Bash
    sudo systemctl start mongod

Passo 4.2: Verificar se está rodando
    Bash
    sudo systemctl status mongod

5. Executar a Aplicação
Com tudo configurado e o venv ativo, inicie o sistema:
    Bash
    python3 principal.py




🪟 MANUAL DE EXECUÇÃO (WINDOWS)
    Caso deseje rodar o projeto em ambiente Windows (PowerShell/VS Code):

    1. Criar e Ativar o Ambiente Virtual:
    PowerShell
    python -m venv venv
    .\venv\Scripts\activate


2. Instalar Dependências:
    PowerShell
    pip install -r requirements.txt

3. Verificar MongoDB: Certifique-se de que o serviço MongoDB Server está com status "Em Execução" no gerenciador de 
    serviços do Windows (services.msc).

4. Executar:
    PowerShell
    python principal.py




📂 Organização do Código (Arquitetura MVC)
O projeto segue estritamente a divisão de responsabilidades solicitada:

src/conexion: Contém a classe MongoQueries responsável pela conexão e encerramento de sessão com o MongoDB.

src/model: Classes POJO que representam as entidades (Cliente, Produto, Venda) e seus métodos to_string.

src/controller: Classes controladoras (ControllerCliente, ControllerProduto) que contêm a regra de negócio, validações de existência e chamadas de persistência.

src/reports: Classe Relatorio centralizando as consultas de agregação e formatação de dados com Pandas.

src/utils: Scripts auxiliares para limpeza de console, menus e a tela de Splash Screen com contagem de registros.

principal.py: Script raiz que orquestra a execução do sistema.




👥 Autores
[Luiz Henrique Gomes de Oliveira]

[Rodrigo Araujo Schenberg]

[Gabriely Azevedo]

[Guilherme Gonçalves]

[Ricardo da Silva Junior]



                    📝 Licença
                    Projeto acadêmico - Disciplina de Banco de Dados.