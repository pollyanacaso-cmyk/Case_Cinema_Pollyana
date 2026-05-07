import sqlite3

class FilmeRepository:

    def conectar(self):
        return sqlite3.connect("cinema.db")

    def criar_tabela(self):

        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            genero TEXT NOT NULL,
            diretor TEXT NOT NULL,
            elenco TEXT NOT NULL,
            duracao INTEGER NOT NULL
        )
        """)

        conexao.commit()
        conexao.close()

    def salvar(self, filme):

        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO filmes
        (titulo, genero, diretor, elenco, duracao)
        VALUES (?, ?, ?, ?, ?)
        """, (
            filme.titulo,
            filme.genero,
            filme.diretor,
            filme.elenco,
            filme.duracao
        ))

        conexao.commit()
        conexao.close()

    def listar_filmes(self):

        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM filmes")

        filmes = cursor.fetchall()

        conexao.close()

        return filmes