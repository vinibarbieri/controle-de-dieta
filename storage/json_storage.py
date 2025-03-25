import json

def salvar_usuarios(usuarios, arquivo="usuarios.json"):
    with open(arquivo, "w") as f:
        json.dump([u.__dict__ for u in usuarios], f)

def carregar_usuarios(arquivo="usuarios.json"):
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []