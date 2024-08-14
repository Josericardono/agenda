# Lista com os nomes dos meses por extenso
meses_por_extenso = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

# Função para validar e converter a data para o formato por extenso
def converter_data_por_extenso(data_str):
    try:
        # Verifica se a data está no formato correto (DD/MM/AAAA)
        partes = data_str.split("/")
        if len(partes) != 3:
            raise ValueError("Formato inválido")

        dia = int(partes[0])
        mes = int(partes[1])
        ano = int(partes[2])

        # Verifica se o dia, mês e ano são valores válidos
        if not (1 <= dia <= 31):
            raise ValueError("Dia inválido")
        if not (1 <= mes <= 12):
            raise ValueError("Mês inválido")
        if ano < 1:
            raise ValueError("Ano inválido")

        # Converte a data para o formato por extenso
        mes_por_extenso = meses_por_extenso[mes - 1]
        data_por_extenso = f"{dia} de {mes_por_extenso} de {ano}"

        return data_por_extenso

    except ValueError as e:
        print(f"Erro: {e}. Por favor, digite a data corretamente.")
        return None

# Função para salvar as datas convertidas em um arquivo
def salvar_data_arquivo(data_por_extenso):
    with open("datas_convertidas.txt", "a") as arquivo:
        arquivo.write(data_por_extenso + "\n")

# Função que exibe o menu de opções e processa a escolha do usuário
def menu():
    datas_convertidas = []

    while True:
        print("\nMenu de opções:")
        print("1 – Converter Data")
        print("2 – Listar Datas por extenso")
        print("3 – Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            data_str = input("Digite uma data no formato DD/MM/AAAA: ")
            data_por_extenso = converter_data_por_extenso(data_str)
            if data_por_extenso:
                datas_convertidas.append(data_por_extenso)
                salvar_data_arquivo(data_por_extenso)
                print("Data convertida:", data_por_extenso)

        elif opcao == "2":
            if datas_convertidas:
                print("\nDatas convertidas por extenso:")
                for data in datas_convertidas:
                    print(data)
            else:
                print("Nenhuma data convertida até o momento.")

        elif opcao == "3":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
menu()