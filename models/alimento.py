class Alimento:
    def __init__(self, nome, quantidade_gramas, peso_por_porcao, calorias, proteinas, carboidratos, gorduras):
        self.nome = nome
        self.quantidade_gramas = quantidade_gramas
        self.peso_por_porcao = peso_por_porcao
        self.calorias = calorias
        self.proteinas = proteinas
        self.carboidratos = carboidratos
        self.gorduras = gorduras

    def nutrientes_totais(self):
        porcoes_consumidas = self.quantidade_gramas / self.peso_por_porcao

        calorias = self.calorias * porcoes_consumidas
        proteinas = self.proteinas * porcoes_consumidas
        carboidratos = self.carboidratos * porcoes_consumidas
        gorduras = self.gorduras * porcoes_consumidas
        
        return calorias, proteinas, carboidratos, gorduras

