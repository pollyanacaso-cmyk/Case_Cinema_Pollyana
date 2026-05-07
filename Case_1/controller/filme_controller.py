from model.filme import Filme
from service.filme_service import FilmeService

class FilmeController:

    def __init__(self):
        self.service = FilmeService()

    def cadastrar(
        self,
        titulo,
        genero,
        diretor,
        elenco,
        duracao
    ):

        filme = Filme(
            titulo,
            genero,
            diretor,
            elenco,
            duracao
        )

        self.service.cadastrar_filme(filme)

    def listar(self):
        return self.service.listar_filmes()