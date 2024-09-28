#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
altura = float(input("Diga-me a sua altura para saber o seu peso ideal: "))
cal_h = (72.7*altura) - 58
cal_m =  (62.1*altura) - 44.7
print("O seu peso ideal se for homem é: "+ str(cal_h)+ " caso seja mulher este é seu peso ideal: " + str(cal_m))
