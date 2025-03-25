# Classe responsável por cadastrar um usuário na classe usuário.

class CadastroUsuario:
    def __init__(self):
        self.usuarios = []

    def cadastrar_usuario(self, nome, idade, sexo, peso, altura, objetivo, nivel):
        if self.cadastrar_nome(nome) and self.verificar_idade(idade) and self.verificar_sexo(sexo) and self.verificar_peso(peso) and self.verificar_altura(altura) and self.verificar_objetivo(objetivo) and self.verificar_nivel(nivel):
            self.usuarios.append(Usuario(nome, idade, sexo, peso, altura, objetivo, nivel))
            return True


    def cadastrar_nome(self, nome):
        while not self._nome_valido(nome):
            nome = input("Nome: ")
            _nome_valido(nome)

            return True

    def _nome_valido(nome):
        if nome == "":
            print("Nome inválido.")
            return False
        return True
    
    def verificar_idade(idade):
        if idade < 0:
            print("Idade inválida.")
            return False
        return True

    def verificar_sexo(sexo):
        if sexo not in ['M', 'F']:
            print("Sexo inválido.")
            return False
        return True
    
    def verificar_peso(peso):
        if peso <= 0:
            print("Peso inválido.")
            return False
        return True
    
    def verificar_altura(altura):
        if altura <= 0:
            print("Altura inválida.")
            return False
        return True
    
    def verificar_objetivo(objetivo):
        if objetivo not in ['perda', 'manutenção', 'ganho']:
            print("Objetivo inválido.")
            return False
        return True
    
    def verificar_nivel(nivel):
        if nivel not in ['sedentario', 'leve', 'moderado', 'intenso', 'muito intenso']:
            print("Nível de atividade inválido.")
            return False
        return True
        