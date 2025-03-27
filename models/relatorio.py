class Relatorio:
    def __init__(self, usuario):
        self.usuario = usuario

    # Gera um resumo diario do usuario com base no historico de consumo
    def gerar_resumo(self):
        historico = self.usuario.resumo_diario()
        print("\nResumo Diário:\n")

        ultima_data = None
        refeicao_num = 1

        for dia in historico:
            if dia["data"] != ultima_data:
                refeicao_num = 1
                ultima_data = dia["data"]

            print(f"Refeição {refeicao_num} do dia {dia['data']}:")
            print(f"Calorías: {dia['calorias']}\nProteínas: {dia['proteina']}\nCarboidratos: {dia['carboidrato']}\nGorduras: {dia['gordura']}")
            print(f"Alimentos: {', '.join(dia['alimentos'])}\n")

            refeicao_num += 1

        print("\nTMB (Metabolismo Basal): {:.2f} kcal".format(self.usuario.calcular_tmb()))
        print("GET (Gasto Energético Total): {:.2f} kcal".format(self.usuario.calcular_get()))
        print("============================================================================================================")
