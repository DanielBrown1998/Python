from datetime import datetime, timedelta
from typing import List, Any
class Livro:
    def __init__(self, nome, autor, ano_publicacao):
        self.nome: Any = nome
        self.autor: Any = autor
        self.ano_publicacao: Any = ano_publicacao
        self.foi_emprestado: bool = False
        self.data_emprestimo: Any = None
        self.data_fim_emprestimo: Any = None
        self.historico: List[Any] = []

    def __str__(self):
        return f'{self.nome} escrito por {self.autor} e publicado em {self.ano_publicacao}'
    

    def emprestar(self):
        self.foi_emprestado = True
        self.data_emprestimo = datetime.now().date()
        self.data_fim_emprestimo = datetime.now().date() + timedelta(days=7)

    def devolver(self):
        self.historico.append(f'Emprestado em {self.data_emprestimo} e devolvido em {self.data_fim_emprestimo}')
        self.foi_emprestado = False
        self.data_emprestimo = None
        self.data_fim_emprestimo = None

    def historico(self):
        for data in self.historico:
            print(data)
        if self.foi_emprestado:
            print(f'Emprestado em {self.data_emprestimo} e data de devolução prevista em {self.data_fim_emprestimo}')


class Biblioteca:
    def __init__(self):
        self.livros: List[Livro] = []

    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)

    def listar_livros(self):
        for livro in self.livros:
            print(livro)

    def buscar_livro_por_nome(self, nome: str):
        for livro in self.livros:
            if livro.nome == nome:
                return livro
        return None

    def buscar_livro_por_autor(self, autor: str):
        for livro in self.livros:
            if livro.autor == autor:
                return livro
        return None

    def buscar_livro_por_ano(self, ano: int):
        for livro in self.livros:
            if livro.ano_publicacao == ano:
                return livro
        return None

    def emprestar_livro(self, nome: str):
        livro = self.buscar_livro_por_nome(nome)
        if livro and livro.foi_emprestado == False:
            livro.emprestar()
        else:
            print('Livro já foi emprestado')

    def devolver_livro(self, nome: str):
        livro = self.buscar_livro_por_nome(nome)
        if livro and livro.foi_emprestado and livro.data_fim_emprestimo <= datetime.now().date():
            livro.devolver()
        else:
            print('Livro não encontrado')

    def listar_livros_emprestados(self):
        for livro in self.livros:
            if livro.foi_emprestado:
                print(livro)

    def listar_historico(self, nome: str):
        livro = self.buscar_livro_por_nome(nome)
        if livro:
            livro.historico()
        else:
            print('Livro não encontrado')