import re

# Verifica se o input é válido
def input_validado(prompt, tipo=float, condicao=lambda x: True, erro="Valor inválido"):
    while True:
        try:
            valor = tipo(input(prompt))
            if not condicao(valor):
                raise ValueError
            return valor
        except ValueError:
            print(erro)

# Verifica se o nome é valido
def input_nome(prompt):
    while True:
        nome = input(prompt).strip()
        if nome and re.match(r"^[A-Za-zÀ-ÿ ']+$", nome):
            return nome
        print("Nome inválido. Use apenas letras e espaços.")

# Verifica se a opção escolhida é válida
def input_opcao(prompt, opcoes):
    while True:
        valor = input(prompt).strip().lower()
        if valor in opcoes:
            return valor
        print(f"Opção inválida. Escolha entre: {', '.join(opcoes)}")
