class Relatorio:
    def __init__(self, usuario):
        self.usuario = usuario

    def gerar_resumo(self):
        historico = self.usuario.resumo_diario()
        print("\nResumo Diário:\n")
        for dia in historico:
            print(f"Data: {dia['data']}")
            print(f"Calorías: {dia['calorias']}\nProteínas: {dia['proteina']}\nCarboidratos: {dia['carboidrato']}\nGorduras: {dia['gordura']}")
            print(f"Alimentos: {', '.join(dia['alimentos'])}\n")

        print("\nTMB (Metabolismo Basal): {:.2f} kcal".format(self.usuario.calcular_tmb()))
        print("GET (Gasto Energético Total): {:.2f} kcal".format(self.usuario.calcular_get()))
        print("============================================================================================================")
