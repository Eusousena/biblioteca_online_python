class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = {}


    def adicionar_livros(self, titulo, autor, ano):
        self.livros.append({"titulo": titulo, "autor": autor, "ano": ano, "status": "disponivel"})


    def emprestar_livros(self, nome_usuario, titulo_livro):
        for livro in self.livros:
            if livro["titulo"] == titulo_livro:
                if livro.get("status") == "disponivel":
                    livro["status"] = "Emprestado"
                print(f"O livro {titulo_livro} foi emprestado com sucesso {nome_usuario}.")
                return
            else:
                print(f"o livro {titulo_livro} já foi emprestado")
                return
        print('Esse livro não existe')


    def Devolver_livros(self, nome_usuario, titulo_livro):
        for livros in self.livros:
            if livros["titulo"] == titulo_livro and livros.get("status") == "Emprestado":
                livros["Status"] = "disponivel"
                print(f"O livro {titulo_livro} foi emprestado com sucesso {nome_usuario}")
                return
        print('Esse livro não existe')
    
minha_biblioteca = Biblioteca()

while True:
    try:
        print("Proximo Usuario!")
        #Solicita informações do livro
        titulo = str(input("Titulo do livro: "))
        autor = str(input("Autor do livro: "))
        ano = int(input("Ano do livro: "))

         # Adiciona o livro à biblioteca
        minha_biblioteca.adicionar_livros(titulo, autor, ano)
        print(minha_biblioteca.livros)

         # Pergunta se o usuário quer emprestar livro ou devolver um livro
        continuar = input('Você deseja continuar? [S/N]: ').upper()
        if continuar == 'N':
            print("Volte sempre!")
            break
        elif continuar != "S":
            print("Desculpe, não entendi.")
            continue   

         # Pergunta se o usuário quer emprestar ou devolver um livro
        acao = input("Você quer emprestar (E) ou devolver (D) um livro? ").upper()
        if acao == 'E':
            minha_biblioteca.emprestar_livros(nome_usuario=input("Qual o seu nome: "), titulo_livro=input("Qual o nome do livro que você quer emprestar: "))
        elif acao == 'D':
            minha_biblioteca.devolver_livros(nome_usuario=input("Qual o seu nome: "), titulo_livro=input("Qual o nome do livro: "))
        else:
            print("Ação inválida.")
    except ValueError:
        print("Valor inválido.")                  