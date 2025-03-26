import uuid

class Usuario:
    def __init__(self, nome, idade, peso, altura, objetivo, nivel_atividade, id=None):
        self.id = id or str(uuid.uuid4())
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.objetivo = objetivo
        self.nivel_atividade = nivel_atividade
        self.consumo_diario = []

    def to_dict(self):
        return {
            "id": self.get_id(),
            "tipo": self.__class__.__name__,
            "nome": self.get_nome(),
            "idade": self.get_idade(),
            "peso": self.get_peso(),
            "altura": self.get_altura(),
            "objetivo": self.get_objetivo(),
            "nivel_atividade": self.get_nivel_atividade(),
            "consumo_diario": [c.to_dict() for c in self.consumo_diario]
        }

    def get_id(self):
        return self.id
    
    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        self.nome = nome

    def get_idade(self):
        return self.idade
    def set_idade(self, idade):
        self.idade = idade

    def get_peso(self):
        return self.peso
    def set_peso(self, peso):
        self.peso = peso

    def get_altura(self):
        return self.altura
    def set_altura(self, altura):
        self.altura = altura

    def get_objetivo(self):
        return self.objetivo
    def set_objetivo(self, objetivo):
        self.objetivo = objetivo
    
    def get_nivel_atividade(self):
        return self.nivel_atividade
    def set_nivel_atividade(self, nivel_atividade):
        self.nivel_atividade = nivel_atividade

    def calcular_tmb(self):
        return 10 * self.peso + 6.25 * self.altura - 5 * self.idade + 5  # Fórmula de Mifflin-St Jeor (masculino)

    def adicionar_consumo(self, consumo):
        self.consumo_diario.append(consumo)

    def resumo_diario(self):
        return [consumo.resumo() for consumo in self.consumo_diario]
    
class UsuarioAtleta(Usuario):
    def calcular_get(self):
        tmb = self.calcular_tmb()
        return tmb * 1.9  # Sempre usa o maior fator de atividade

class UsuarioComum(Usuario):
    def calcular_get(self):
        tmb = self.calcular_tmb()
        return tmb * 1.55  # Sempre usa o segundo maior fator de atividade

class UsuarioSedentario(Usuario):
    def calcular_get(self):
        tmb = self.calcular_tmb()
        return tmb * 1.2  # Sempre usa o menor fator de atividade
