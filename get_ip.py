import socket


def get_website():
    website = input("Digite o nome do site aqui: ")
    found_ip(website)

def found_ip(website):
    try:
        ip = socket.gethostbyname(website)
        print(ip)
    except socket.gaierror as e:
        print(f"Um erro aconteceu devido ao URL do site '{website}' ser inválido")
        resposta = input("Deseja tentar novamente? [Y/n]: ").lower()
        if resposta == "y":
            get_website()
        else:
            0

get_website()

