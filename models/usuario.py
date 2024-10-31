from hashlib import sha256

class Usuario:
    def __init__(self, id, nome, senha, tipo=0) -> None:
        self.__id = id
        self.__nome = nome
        self.__senha = senha
        self.__tipo = tipo

    def __getattribute__(self, name):
        # Acessa os atributos corretamente
        if name in ['id', 'nome', 'senha', 'tipo']:
            return object.__getattribute__(self, f'_{self.__class__.__name__}__{name}')
        return object.__getattribute__(self, name)

# Lista de usuários
lista_Usuarios = []
lista_Usuarios.append(Usuario(1, "Igor", sha256("1234".encode()).hexdigest()))
lista_Usuarios.append(Usuario(2, "Aluno", sha256("1234".encode()).hexdigest(), 1))
