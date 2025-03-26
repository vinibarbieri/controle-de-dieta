class Usuario:
    def __init__(self, nome, idade, peso, altura, objetivo, nivel_atividade):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.objetivo = objetivo
        self.nivel_atividade = nivel_atividade
        self.consumo_diario = []

    def to_dict(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "peso": self.peso,
            "altura": self.altura,
            "objetivo": self.objetivo,
            "nivel_atividade": self.nivel_atividade,
            "consumo_diario": [c.to_dict() for c in self.consumo_diario]
        }

    def calcular_tmb(self):
        return 10 * self.peso + 6.25 * self.altura - 5 * self.idade + 5  # Fórmula de Mifflin-St Jeor (masculino)

    def calcular_get(self):
        fator = {
            "sedentario": 1.2,
            "leve": 1.375,
            "moderado": 1.55,
            "intenso": 1.725,
            "muito intenso": 1.9
        }
        return self.calcular_tmb() * fator.get(self.nivel_atividade, 1.2)

    def adicionar_consumo(self, consumo):
        self.consumo_diario.append(consumo)

    def resumo_diario(self):
        return [consumo.resumo() for consumo in self.consumo_diario]
