# Fórmula de Mifflin-St Jeor:
def calcular_tmb(peso, altura, idade, sexo):
    if sexo == "masculino":
        return (10 * peso) + (6.25 * altura) - (5 * idade) + 5
    elif sexo == "feminino":
        return (10 * peso) + (6.25 * altura) - (5 * idade) - 161
    else:
        return(f"Erro no calculo de TMB para o sexo {sexo}")

def calcular_get(tmb, nivel_atividade):
    fator = {
        "sedentario": 1.2,
        "leve": 1.375,
        "moderado": 1.55,
        "intenso": 1.725,
        "muito intenso": 1.9
    }
    return tmb * fator.get(nivel_atividade, 1.2)