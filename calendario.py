# Lista com os nomes dos meses
meses_por_extenso = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]


# Função que valida e converte a data
def converter_data_por_extenso(data_str):
    try:
        # Verifica se a data está no formato DD/MM/AAAA
        partes = data_str.split("/")
        if len(partes) != 3:
            raise ValueError("Formato inválido")

        dia = int(partes[0])
        mes = int(partes[1])
        ano = int(partes[2])

        # Confere se os valores são válidos
        if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1:
            raise ValueError("Data inválida")

        # Converte a data para o formato por extenso
        mes_por_extenso = meses_por_extenso[mes - 1]
        data_por_extenso = f"{dia} de {mes_por_extenso} de {ano}"

        return data_por_extenso

    except ValueError as e:
        print(f"Erro: {e}. Por favor, digite a data corretamente.")
        return None


# Função principal que pede a data para o usuário
def obter_data():
    while True:
        data_str = input("Digite uma data no formato DD/MM/AAAA: ")
        data_por_extenso = converter_data_por_extenso(data_str)
        if data_por_extenso:
            print("Data por extenso:", data_por_extenso)
            break


# Executa o programa
obter_data()