from Repository.filme_repository import FilmeRepository

class FilmeService:

    def __init__(self):
        self.repository = FilmeRepository()
        self.repository.criar_tabela()

    def cadastrar_filme(self, filme):

        if filme.titulo == "":
            print("Título inválido!")
            return

        self.repository.salvar(filme)

        print("Filme cadastrado com sucesso!")

    def listar_filmes(self):
        return self.repository.listar_filmes()