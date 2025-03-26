import json
import os
from models.usuario import Usuario
from models.consumo import ConsumoDiario
from models.alimento import Alimento

ARQUIVO_USUARIOS = "usuarios.json"

def salvar_usuarios(usuarios):
    dados = []
    for u in usuarios:
        dados.append({
            "nome": u.nome,
            "idade": u.idade,
            "peso": u.peso,
            "altura": u.altura,
            "objetivo": u.objetivo,
            "nivel_atividade": u.nivel_atividade
        })
    with open(ARQUIVO_USUARIOS, "w") as f:
        json.dump([u.to_dict() for u in usuarios], f, indent=2)

def carregar_usuarios():
    if not os.path.exists(ARQUIVO_USUARIOS):
        return []
    with open(ARQUIVO_USUARIOS, "r") as f:
        dados = json.load(f)
    usuarios = []
    for u in dados:
        usuario = Usuario(u["nome"], u["idade"], u["peso"], u["altura"], u["objetivo"], u["nivel_atividade"])
        for c in u.get("consumo_diario", []):
            alimentos = [Alimento(**a) for a in c["alimentos"]]
            consumo = ConsumoDiario(alimentos)
            consumo.data = c["data"]
            usuario.adicionar_consumo(consumo)
        usuarios.append(usuario)
    return usuarios