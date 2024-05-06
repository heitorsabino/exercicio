nome = input("Digite seu nome: ")

distancia = float(input("Digite a distância da viagem (em km): "))

velocidade = float(input("Digite a velocidade média da viagem (em km/h): "))

tempo = distancia / velocidade

print(f"Olá {nome}, o tempo de viagem será de aproximadamente {tempo:.2f} horas.")
