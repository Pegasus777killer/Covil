#!/usr/bin/python3

import os
import time
senha = input("coloca a senha ae krai:  ")
if senha <"67":
    print("acesso não liberado, colocou a Senha errada kkkk")
    exit ()
elif senha == "68":
    print("Senha correta")
    time.sleep(3)
    os.system("clear")
else:
    print("BEM VINDO AO COVIL")
    print("CARREGANDO..")
    time.sleep(3)    
print("▒▒▒▒▒▒▒▒▒▒▒▄▄▄▄░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("▒▒▒▒▒▒▒▒▒▄██████▒▒▒▒▒▄▄▄█▄▒▒▒▒▒▒▒▒▒▒")
print("▒▒▒▒▒▒▒▄██▀░░▀██▄▒▒▒▒████████▄▒▒▒▒▒▒")
print("▒▒▒▒▒▒███░░░░░░██▒▒▒▒▒▒█▀▀▀▀▀██▄▄▒▒▒")
print("▒▒▒▒▒▄██▌░░░░░░░██▒▒▒▒▐▌▒▒▒▒▒▒▒▒▀█▄▒")
print("▒▒▒▒▒███░░▐█░█▌░██▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▀▌")
print("▒▒▒▒████░▐█▌░▐█▌██▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("▒▒▒▐████░▐░░░░░▌██▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("▒▒▒▒████░░░▄█░░░██▒▒▐█▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("▒▒▒▒████░░░██░░██▌▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("▒▒▒▒████▌░▐█░░███▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("▒▒▒▒▐████░░▌░███▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("▒▒▒▒▒████░░░███▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("▒▒▒██████▌░████▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("▒▐████████████▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("▒█████████████▄████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("█████████████████▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("                cOvil                             ")

print("1: ATUALIZAR TERMUX")
print("2: INSTALAR PAINEL COVIL")

escolha = False


while escolha == False:
    nivel = int(input("OQUE DESEJA?  "))
    
    if (nivel == 1):
        os.system ("pkg update && pkg upgrade")
    
    elif (nivel == 2):
          os.system("painel")
