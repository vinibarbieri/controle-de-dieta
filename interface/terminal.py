import re
from models.usuario import Usuario, UsuarioAtleta, UsuarioComum, UsuarioSedentario
from models.alimento import Alimento
from models.consumo import ConsumoDiario
from models.relatorio import Relatorio
from storage.json_storage import salvar_usuarios, carregar_usuarios
from utils.input_utils import input_validado, input_nome, input_opcao
from interface.usuario_interface import alterar_usuario, cadastrar_usuario

usuarios = carregar_usuarios()

def iniciar_interface():
    print("Bem-vindo ao Sistema de Controle de Dieta!")
    while True:
        print("\n1. Cadastrar novo usuário")
        print("2. Selecionar usuário existente")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario = cadastrar_usuario()
            usuarios.append(usuario)
            menu_usuario(usuario)
        elif opcao == "2":
            usuario = selecionar_usuario()
            if usuario:
                menu_usuario(usuario)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
        
def menu_usuario(usuario):
    while True:
        print(f"\nUsuário atual: {usuario.get_nome()}")
        print("1. Registrar alimentos consumidos hoje")
        print("2. Ver relatório")
        print("3. Alterar informações do usuário")
        print("4. Voltar para seleção de usuário")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            registrar_alimentos(usuario)
        elif opcao == "2":
            Relatorio(usuario).gerar_resumo()
        elif opcao == "3":
            alterar_usuario(usuario)
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

def selecionar_usuario():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return None
    print("\nUsuários cadastrados:")
    for i, u in enumerate(usuarios):
        print(f"{i + 1}. {u.get_nome()}")
    idx = input_validado("Escolha o número do usuário: ", int, lambda x: 1 <= x <= len(usuarios))
    return usuarios[idx - 1]

def registrar_alimentos(usuario):
    alimentos = []
    while True:
        nome = input_nome("\nNome do alimento (ou 'fim'): ")
        if nome.lower() == 'fim':
            print("Registro de alimentos finalizado.")
            print("============================================================================================================")
            break
        quantidade = input_validado("Quantidade consumida em gramas: ", float, lambda x: x > 0)
        porcao = input_validado("Peso da porção (g): ", float, lambda x: x > 0)
        calorias = input_validado("Calorias por porção: ", float, lambda x: x >= 0)
        proteina = input_validado("Proteína: ", float, lambda x: x >= 0)
        carbo = input_validado("Carboidrato: ", float, lambda x: x >= 0)
        gordura = input_validado("Gordura: ", float, lambda x: x >= 0)
        alimentos.append(Alimento(nome, quantidade, porcao, calorias, proteina, carbo, gordura))
    usuario.adicionar_consumo(ConsumoDiario(alimentos))
    
    for i, u in enumerate(usuarios):
        if u.get_id() == usuario.get_id():
            usuarios[i] = usuario
            break
    
    salvar_usuarios(usuarios)




