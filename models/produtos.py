class Produto:
    def __init__(self, id, nome, imagem, preco) -> None:
        self.__id = id
        self.__nome = nome
        self.__imagem = imagem  # Nome da imagem
        self.__preco = preco

    def __getattribute__(self, name):
        return super().__getattribute__(f"_Produto_{name}")

lista_Produtos = []
lista_Produtos.append(Produto(1, "Rios de Sangue ", "imagens/rios_de_sangue.png", 500.00))
lista_Produtos.append(Produto(2, "Presa do Cão de Caça (3ª geração)", "imagens/presa_cao_de_caca.png", 400.00))
lista_Produtos.append(Produto(3, "Poleblade", "imagens/poleblade_de_eleanor.png", 350.00))
lista_Produtos.append(Produto(4, "Roupa de Samurai", "imagens/samurai.png", 100,00))
lista_Produtos.append(Produto(5, "Roupa de Cavaleiro Lunar", "imagens/cavaleiro_lunar.png", 250.00))
lista_Produtos.append(Produto(6, "Roupa de Cavaleiro do Crisol", "imagens/cavaleiro_crisol.png", 400.00))
