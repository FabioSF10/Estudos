from builtins import print, bytes
import random

cpfValido = False

while cpfValido == False:
    # Gera um numero aleatorio de ate 11 digitos
    cpfAleatorio = random.randint(11111111112, 99999999999)
    print(cpfAleatorio)
    # calculo primeiro digito
    # processo de calculo de multiplicação de cada um dos 9 primeiros digitos do CPF por 10 descrecente ate 2
    resultadoMultipli = []
    contadorListaCPF = 0
    cpfAleatorioStr = str(cpfAleatorio)
    for contadorFor in range(10, 1, -1):
        resultadoMultipli.append(int(cpfAleatorioStr[contadorListaCPF]) * contadorFor)
        contadorListaCPF += 1

    # processo de soma de todos os 9 resultados
    somaCpf = sum(resultadoMultipli)
    restoDigito = (somaCpf*10) % 11
    #subtracaoDigito = 11 - restoDigito

    # processo de verificar se o primeiro digito verificador esta correto
    if restoDigito >= 10 and int(cpfAleatorioStr[9]==0):
        print(f'O primeiro digito verificador do CPF ({cpfAleatorioStr[9]}) é válido')
    elif restoDigito < 10 and int(cpfAleatorioStr[9])==restoDigito:
        print(f'O primeiro digito verificador do CPF ({cpfAleatorioStr[9]}) é válido')
    else:
        continue


    # calculo segundo digito
    # mesmo processo de multiplicação do primeiro digito porém contando até 10 com o primeiro digito verificador confirmado
    contadorListaCPF = 0
    resultadoMultipli.clear()
    for contadorFor in range(11, 1, -1):
        resultadoMultipli.append(int(cpfAleatorioStr[contadorListaCPF]) * contadorFor)
        contadorListaCPF += 1

        # processo de soma de todos os 10 resultados
    somaCpf = sum(resultadoMultipli)
    restoDigito = (somaCpf*10) % 11
    #subtracaoDigito = 11 - restoDigito
    #processo de verificar se o segundo digito verificador esta correto

    if restoDigito >= 10 and int(cpfAleatorioStr[10])==0:
        print(f'O segundo digito verificador do CPF ({cpfAleatorioStr[10]}) é válido')
        cpfFinal = '{}.{}.{}-{}'.format(cpfAleatorioStr[:3], cpfAleatorioStr[3:6], cpfAleatorioStr[6:9], cpfAleatorioStr[9:])
        print(f'O programa gerou um CPF valido de numero: {cpfFinal}')
        cpfValido = True
        break
    elif restoDigito < 10 and int(cpfAleatorioStr[10])==restoDigito:
        print(f'O segundo digito verificador do CPF ({cpfAleatorioStr[10]}) é válido')
        cpfFinal = '{}.{}.{}-{}'.format(cpfAleatorioStr[:3], cpfAleatorioStr[3:6], cpfAleatorioStr[6:9], cpfAleatorioStr[9:])
        print(f'O programa gerou um CPF valido de numero: {cpfFinal}')
        cpfValido = True
        break
    else:
        continue
