# Você gostaria de saber quantos segundos se passaram desde a meia-noite?Escreva um programa que
# leia valores inteiros para hora, minuto e segundo. Em seguida, o programa deve calcular e imprimir
# quantos segundos se passaram no total desde a última meia-noite até a hora lida.

h = int (input()) 
m = int (input())
s = int (input())



h = h*3600
m = m*60
s = s//1

g = h+m+s

print(g)
 