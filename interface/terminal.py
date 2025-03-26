import re
from models.usuario import Usuario
from models.alimento import Alimento
from models.consumo import ConsumoDiario
from models.relatorio import Relatorio
from storage.json_storage import salvar_usuarios, carregar_usuarios

usuarios = carregar_usuarios()

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

def cadastrar_usuario():
    nome = input_nome("Nome: ")
    idade = input_validado("Idade: ", int, lambda x: 0 < x <= 150, "Idade inválida")
    peso = input_validado("Peso (kg): ", float, lambda x: 0 < x < 500, "Peso inválido")
    altura = input_validado("Altura (cm): ", float, lambda x: 50 < x < 300, "Altura inválida")
    objetivo = input_opcao("Objetivo (perda, manutenção, ganho): ", ["perda", "manutenção", "ganho"])
    nivel = input_opcao("Nível de atividade (sedentario, leve, moderado, intenso, muito intenso): ",
                        ["sedentario", "leve", "moderado", "intenso", "muito intenso"])
    usuario = Usuario(nome, idade, peso, altura, objetivo, nivel)
    usuarios.append(usuario)
    salvar_usuarios(usuarios)
    return usuario

def selecionar_usuario():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return None
    print("\nUsuários cadastrados:")
    for i, u in enumerate(usuarios):
        print(f"{i + 1}. {u.nome}")
    idx = input_validado("Escolha o número do usuário: ", int, lambda x: 1 <= x <= len(usuarios))
    return usuarios[idx - 1]

def registrar_alimentos(usuario):
    alimentos = []
    while True:
        nome = input_nome("Nome do alimento (ou 'fim'): ")
        if nome.lower() == 'fim':
            break
        quantidade = input_validado("Quantidade consumida em gramas: ", float, lambda x: x > 0)
        porcao = input_validado("Peso da porção (g): ", float, lambda x: x > 0)
        calorias = input_validado("Calorias por porção: ", float, lambda x: x >= 0)
        proteina = input_validado("Proteína: ", float, lambda x: x >= 0)
        carbo = input_validado("Carboidrato: ", float, lambda x: x >= 0)
        gordura = input_validado("Gordura: ", float, lambda x: x >= 0)
        alimentos.append(Alimento(nome, quantidade, porcao, calorias, proteina, carbo, gordura))
    usuario.adicionar_consumo(ConsumoDiario(alimentos))

def menu_usuario(usuario):
    while True:
        print(f"\nUsuário atual: {usuario.nome}")
        print("1. Registrar alimentos consumidos")
        print("2. Ver relatório")
        print("3. Voltar para seleção de usuário")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            registrar_alimentos(usuario)
        elif opcao == "2":
            Relatorio(usuario).gerar_resumo()
        elif opcao == "3":
            salvar_usuarios(usuarios)
            break
        else:
            print("Opção inválida.")

def iniciar_interface():
    print("Bem-vindo ao Sistema de Controle de Dieta!")
    while True:
        print("\n1. Cadastrar novo usuário")
        print("2. Selecionar usuário existente")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario = cadastrar_usuario()
            menu_usuario(usuario)
        elif opcao == "2":
            usuario = selecionar_usuario()
            if usuario:
                menu_usuario(usuario)
        elif opcao == "3":
            print("Saindo...")
            salvar_usuarios(usuarios)
            break
        else:
            print("Opção inválida.")
