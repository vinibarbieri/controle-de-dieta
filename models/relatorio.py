class Relatorio:
    def __init__(self, usuario):
        self.usuario = usuario

    def gerar_resumo(self):
        historico = self.usuario.resumo_diario()
        print("\nResumo Diário:")
        for dia in historico:
            print(f"Data: {dia['data']}\nCalorias: {dia['calorias']}\nAlimentos: {', '.join(dia['alimentos'])}")

        print("\nTMB (Metabolismo Basal): {:.2f} kcal".format(self.usuario.calcular_tmb()))
        print("GET (Gasto Energético Total): {:.2f} kcal".format(self.usuario.calcular_get()))
