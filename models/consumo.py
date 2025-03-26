from datetime import date

class ConsumoDiario:
    def __init__(self, alimentos):
        self.data = str(date.today())
        self.alimentos = alimentos  # Lista de objetos Alimento

    def to_dict(self):
        return {
            "data": self.data,
            "alimentos": [a.__dict__ for a in self.alimentos]
        }


    def nutrientes_totais(self):
        total_calorias = 0
        total_proteinas = 0
        total_carboidratos = 0
        total_gorduras = 0

        for alimento in self.alimentos:
            calorias, proteinas, carboidratos, gorduras = alimento.nutrientes_totais()
            total_calorias += calorias
            total_proteinas += proteinas
            total_carboidratos += carboidratos
            total_gorduras += gorduras

        return total_calorias, total_proteinas, total_carboidratos, total_gorduras


    def resumo(self):
        calorias, proteinas, carboidratos, gorduras = self.nutrientes_totais()
        return {
            "data": self.data,
            "calorias": round(calorias),
            "proteina": round(proteinas, 1),
            "carboidrato": round(carboidratos, 1),
            "gordura": round(gorduras, 1),
            "alimentos": [a.nome for a in self.alimentos]
        }
