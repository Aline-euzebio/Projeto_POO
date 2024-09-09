"""
Criar três classes: Livro, Membro, Biblioteca.
# Classe Livro tem os atributos título, autor, ID, status de empréstimo.
# Classe Membro tem os atributos nome, número de membro e histórico de livros emprestados.
# Classe Biblioteca deve conter um catálogo de livros disponíveis, um registro de membros e métodos para empréstimo, devolução e pesquisa de livros.
* Adiiconar livros ao catálogo.
* Adicionar membro à biblioteca.
* Permitir empréstimo de livros por membros.
* Registrar a devolução de livros.
* Pesquisar livros por título, autor ou ID.
"""
from time import sleep 
class Livro:
    def __init__(self, titulo: str, autor: str, id: int ) -> None:
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.disponivel = True




class Membro:
    def __init__(self, nome: str, numero_de_membro: str ) -> None:
        self.nome = nome
        self.numero_de_membro = numero_de_membro
        self.historico_de_livros_emprestados = []



class Biblioteca:
    def __init__(self) -> None:
        self.catalogo_de_livros_disponiveis = []
        self.registro_membro = []     
        
    def adicionar_livros(self):
        titulo = input("Digite o titulo do livro: ")
        autor = input("Digite o autor do livro: ")
        id = input("Digite o id do livro: ")
        livro = Livro(titulo=titulo,autor=autor,id=id)
        self.catalogo_de_livros_disponiveis.append(vars(livro))

    def adicionar_membro(self):
        nome = input("Digite o nome do membro: ")
        numero_de_membro = input("Digite o número de membro: ")
        membro = Membro(nome=nome,numero_de_membro=numero_de_membro)
        self.registro_membro.append(vars(membro))
        print("Membro adicionado com sucesso!")
        
    def pesquisar_livros(self):
            decisao = input("""
            Deseja pesquisar livros por:
            1- Titulo
            2- Autor
            3- id
            4- Nenhum
""")
            
            if decisao == "1":
                titulo = input("Digite o titulo do livro que deseja pesquisar: ")
                for livro in self.catalogo_de_livros_disponiveis:
                    for c, v in livro.items():
                        if livro['titulo'] == titulo:
                            print(f'{c}:{v}')

            if decisao == "2":
                autor = input("Digite o nome do autor que deseja pesquisar: ")
                for livro in self.catalogo_de_livros_disponiveis:
                    for c, v in livro.items():
                        if livro['autor'] == autor:
                            print(f'{c}:{v}')

            if decisao == "3":
                id = int(input("Digite o número de id que deseja pesquisar: "))
                for livro in self.catalogo_de_livros_disponiveis:
                    for c, v in livro.items():
                        if livro['id'] == id:
                            print(f'{c}:{v}')

            if decisao == "4":
                if self.catalogo_de_livros_disponiveis:
                    for livro in self.catalogo_de_livros_disponiveis:
                        for c, v in livro.items():
                            print (f'{c}:{v}')
                        print()
                else:
                    print("O catalogo de livros disponiveis esta vazio")

    def emprestar_livros(self):
        titulo = input("Digite o livro que deseja empresto: ")
        nome = input("Digite o nome do membro: ")
        for livros in self.catalogo_de_livros_disponiveis:
            if livros["titulo"] == titulo:     
                if livros["disponivel"] == True:
                    livros["disponivel"] = False
                    for nome in self.registro_membro:
                        if nome["nome"] == nome:
                            nome["hitorico_de_livros_emprestados"].append(livros)

    
    def devolver_livros(self):
        
        titulo =  input("Digite o titulo do livro: ")
        for livro in self.catalogo_de_livros_disponiveis:
            for c, v in livro.items():
                if livro ['titulo'] == titulo:
                    livro ['disponivel'] = True
    

#Separando uma ambiente so pra deixar meus objetos de teste
b1 = Biblioteca()#Objeto classe Biblioteca
m1 = Membro("Aline Euzebio", "1234")
l1 = Livro("Por Lugares Incriveis", "Jennifer Niven",1)
l2 = Livro("O sobrinhho do mago", "C S Lewis",2)

while True:
    print("="*30)
    print("Meu geral".center(30))
    print("="*30)
    print("Bem vindo a nossa Biblioteca ! ! !")
    print("Oque voce deseja fazer ?")
    print("1 - Para Adicionar livros")
    print("2 - Para adicionar Membro")
    print("3 - Para Pesquisar livro")
    print("4 - Emprestar livro")
    print("5 - Devolver livro")
    print("q - Para sair")
    opcao:str = input("->")

    match opcao:
        case "1":
            b1.adicionar_livros()
        
        case "2":        
            b1.adicionar_membro()

        case "3":
            b1.pesquisar_livros()

        case "4":
            b1.emprestar_livros()

        case "5":
            b1.devolver_livros()

        case "q":
            print("Programa esta sendo finalizado",end="")
            print(".",end="")
            sleep(1)
            print(".",end="")
            sleep(1)
            print(".")
            sleep(1)
            break




