# exemplo.py

def saudacao():
    print("Olá, Mundo!")

def soma(a, b):
    return a + b

if __name__ == "__main__":
    saudacao()
    resultado = soma(5, 3)
    print(f"A soma de 5 e 3 é {resultado}")

    input("Pressione Enter para sair...")  # Adiciona uma pausa para manter a janela aberta
