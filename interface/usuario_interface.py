from utils.input_utils import input_nome, input_validado, input_opcao
from models.usuario import UsuarioAtleta, UsuarioComum, UsuarioSedentario
from storage.json_storage import salvar_usuarios, carregar_usuarios

usuarios = carregar_usuarios()

def cadastrar_usuario():
    nome = input_nome("Nome: ")
    idade = input_validado("Idade: ", int, lambda x: 0 < x <= 150, "Idade inválida")
    peso = input_validado("Peso (kg): ", float, lambda x: 0 < x < 500, "Peso inválido")
    altura = input_validado("Altura (cm): ", float, lambda x: 50 < x < 300, "Altura inválida")
    objetivo = input_opcao("Objetivo (perda, manutenção, ganho): ", ["perda", "manutenção", "ganho"])
    nivel_atividade = input_validado("Quantas vezes na semana pratica esporte?: ", int, lambda x: 0 < x <= 7, "Valor inválido")

    if (nivel_atividade >= 6):
        usuario = UsuarioAtleta(nome, idade, peso, altura, objetivo, nivel_atividade)
    elif (nivel_atividade >= 2):
        usuario = UsuarioComum(nome, idade, peso, altura, objetivo, nivel_atividade)
    else:
        usuario = UsuarioSedentario(nome, idade, peso, altura, objetivo, nivel_atividade)

    usuarios.append(usuario)
    salvar_usuarios(usuarios)
    return usuario

def alterar_usuario(usuario):
    print("\nInformações atuais:")
    print(f"Nome: {usuario.get_nome()}")
    print(f"Idade: {usuario.get_idade()}")
    print(f"Peso: {usuario.get_peso()} kg")
    print(f"Altura: {usuario.get_altura()} cm")
    print(f"Objetivo: {usuario.get_objetivo()}")
    print(f"Nível de atividade: {usuario.get_nivel_atividade()} vezes por semana")
    print(f"Voltar")

    opcao = input_opcao("\nO que deseja alterar (nome, idade, peso, altura, objetivo, nivel, voltar)? ", ["nome", "idade", "peso", "altura", "objetivo", "nivel", "voltar"])
    if opcao == "nome":
        usuario.set_nome(input_nome("Novo nome: "))
    elif opcao == "idade":
        usuario.set_idade(input_validado("Nova idade: ", int, lambda x: 0 < x <= 150, "Idade inválida"))
    elif opcao == "peso":
        usuario.set_peso(input_validado("Novo peso (kg): ", float, lambda x: 0 < x < 500, "Peso inválido"))
    elif opcao == "altura":
        usuario.set_altura(input_validado("Nova altura (cm): ", float, lambda x: 50 < x < 300, "Altura inválida"))
    elif opcao == "objetivo":
        usuario.set_objetivo(input_opcao("Novo objetivo (perda, manutenção, ganho): ", ["perda", "manutenção", "ganho"]))
    elif opcao == "nivel":
        usuario.set_nivel_atividade(input_validado("Quantas vezes na semana pratica esporte?: ", int, lambda x: 0 < x <= 7, "Valor inválido"))
        if (usuario.get_nivel_atividade() >= 6):
            usuario_atualizado = UsuarioAtleta(usuario.get_nome(), usuario.get_idade(), usuario.get_peso(), usuario.get_altura(), usuario.get_objetivo(), usuario.get_nivel_atividade(), id=usuario.get_id())
        elif (usuario.get_nivel_atividade() >= 2):
            usuario_atualizado = UsuarioComum(usuario.get_nome(), usuario.get_idade(), usuario.get_peso(), usuario.get_altura(), usuario.get_objetivo(), usuario.get_nivel_atividade(), id=usuario.get_id())
        else:
            usuario_atualizado = UsuarioSedentario(usuario.get_nome(), usuario.get_idade(), usuario.get_peso(), usuario.get_altura(), usuario.get_objetivo(), usuario.get_nivel_atividade(), id=usuario.get_id())

        usuario_atualizado.consumo_diario = usuario.consumo_diario

        for i, u in enumerate(usuarios):
            if u.get_id() == usuario.get_id():
                usuarios[i] = usuario_atualizado
                break
        
        salvar_usuarios(usuarios)

    elif opcao == "voltar":
        return