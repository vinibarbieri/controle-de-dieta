import re
from models.usuario import Usuario
from models.alimento import Alimento
from models.consumo import ConsumoDiario
from models.relatorio import Relatorio

usuarios = []

def input_validado(prompt, tipo=float, condicao=lambda x: True, erro="Valor inválido"):
    while True:
        try:
            valor = tipo(input(prompt))
            if not condicao(valor):
                raise ValueError
            return valor
        except ValueError:
            print(erro)

def input_nome(prompt):
    while True:
        nome = input(prompt).strip()
        if nome and re.match(r"^[A-Za-zÀ-ÿ ']+$", nome):
            return nome
        print("Nome inválido. Use apenas letras e espaços.")

def input_opcao(prompt, opcoes):
    while True:
        valor = input(prompt).strip().lower()
        if valor in opcoes:
            return valor
        print(f"Opção inválida. Escolha entre: {', '.join(opcoes)}")

def iniciar_interface():
    print("Bem-vindo ao Sistema de Controle de Dieta!")
    while True:
        print("\n1. Cadastrar Usuário")
        print("2. Adicionar Consumo Diário")
        print("3. Ver Relatório")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input_nome("Nome: ")
            idade = input_validado("Idade: ", int, lambda x: 0 < x <= 150, "Idade inválida")
            peso = input_validado("Peso (kg): ", float, lambda x: 0 < x < 500, "Peso inválido")
            altura = input_validado("Altura (cm): ", float, lambda x: 50 < x < 270, "Altura inválida")
            objetivo = input_opcao("Objetivo (perda, manutenção, ganho): ", ["perda", "manutenção", "ganho"])
            nivel = input_opcao("Nível de atividade (sedentario, leve, moderado, intenso, muito intenso): ",
                                ["sedentario", "leve", "moderado", "intenso", "muito intenso"])
            usuarios.append(Usuario(nome, idade, peso, altura, objetivo, nivel))

        elif opcao == "2":
            if not usuarios:
                print("Nenhum usuário cadastrado.")
                continue
            usuario = usuarios[0]  # Para simplificar, usa o primeiro usuário
            alimentos = []
            while True:
                nome = input_nome("Nome do alimento (ou 'fim'): ")
                if nome.lower() == 'fim':
                    break
                quantidade = input_validado("Quantidade em gramas: ", float, lambda x: x > 0)
                porcao = input_validado("Gramas por porção: ", float, lambda x: x > 0)
                calorias = input_validado(f"Calorias por {porcao:.0f}g: ", float, lambda x: x >= 0)
                proteina = input_validado(f"Proteína por {porcao:.0f}g: ", float, lambda x: x >= 0)
                carbo = input_validado(f"Carboidrato por {porcao:.0f}g: ", float, lambda x: x >= 0)
                gordura = input_validado(f"Gordura por {porcao:.0f}g: ", float, lambda x: x >= 0)
                alimentos.append(Alimento(nome, quantidade, porcao, calorias, proteina, carbo, gordura))
            usuario.adicionar_consumo(ConsumoDiario(alimentos))

        elif opcao == "3":
            if not usuarios:
                print("Nenhum usuário cadastrado.")
                continue
            Relatorio(usuarios[0]).gerar_resumo()

        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
