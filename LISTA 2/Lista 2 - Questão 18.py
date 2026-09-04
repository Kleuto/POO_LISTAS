inventario = {
    "PAT001": {
        "Equipamento": "Computador",
        "Marca": "Dell",
        "Situação": "Funcionando"
    },
    "PAT002": {
        "Equipamento": "Projetor",
        "Marca": "Epson",
        "Situação": "Em manutenção"
    },
    "PAT003": {
        "Equipamento": "Notebook",
        "Marca": "Lenovo",
        "Situação": "Funcionando"
    }
}

for patrimonio in inventario:
    print("Patrimônio:", patrimonio)
    print("Equipamento:", inventario[patrimonio]["Equipamento"])
    print("Marca:", inventario[patrimonio]["Marca"])
    print("Situação:", inventario[patrimonio]["Situação"])
    print() 
