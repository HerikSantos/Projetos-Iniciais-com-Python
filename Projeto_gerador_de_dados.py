from operator import itemgetter
import random
import os

#dados que podem ser solicitados pelo usuário
nomes =  ["Ivania Holanda", "Bernardo Sousa", "Cris Nazare", "Dayverson Alfradique", "Gilberto Felizardo"]
numero_de_celular =  ["(83) 97263-9844", "(71) 99967-6154","(82) 99577-4262","(68) 98966-6538"]
email= ["bawolaw248@jobbrett.com", "jipab65007@in2reach.com", "giwevan774@meidecn.com", "naxidif968@in2reach.com", "diwaxep798@meidecn.com"]
cidades= ["Alcobaça", "Caravelas", "Teixeira de Freitas", "Prado", "Itamaraju"]
Estados= ["Bahia", "Pernambuco", "Goiás", "Minas Gerais", "Amazonas"]


print("------------------------------------Bem-Vindo ao Gerador de dados-(Caso desejar parar basta escrever 'parar')------------------------------------")


continuar = "s"
while  continuar == "s":
    estados2 = ""
    nomes2 = ""
    email2 = ""
    cidades2 = ""
    numero_de_celular2 = ""
    valor_recebido = (input("Escolha quais dados você deseja gerar:\n [1] Gerador de nomes\n [2] Gerador de email\n [3] Gerador de numero de celular\n [4] Gerador de cidades\n [5] Gerador de estados\nDigite as opções: "))
    if valor_recebido.lower() == "parar":
        print("Programa finalizado")
        break
    else:
        pass
    gerar_arquivo = input("Deseja gerar um arquivo.txt com as informações geradas? [S/N]\n")
    for valor in valor_recebido:
        if valor == "1":
            nomes2 = random.choice(list(nomes))
            print(nomes2)
        elif valor == "2":
            email2 = random.choice(list(email))
            print(email2)
        elif valor == "3":
            numero_de_celular2 = random.choice(list(numero_de_celular))
            print(numero_de_celular2)
        elif valor == "4":
            cidades2 = random.choice(list(cidades))
            print(cidades2)
        elif valor == "5":
            estados2 = random.choice(list(Estados))
            print(estados2)
        elif valor == ",":
            pass
        else:
            print("Porfavor digite o valor de 1 a 5")
    if gerar_arquivo.lower() == "s":
        with open("dados.txt", "a", encoding="utf-8") as arquivo_de_txt:
             if nomes2 == "":
                pass
             else: arquivo_de_txt.write(nomes2 + "\n")
             if email2 == "":
                pass
             else: arquivo_de_txt.write(email2 + "\n")
             if numero_de_celular2 == "":
                pass
             else: arquivo_de_txt.write(numero_de_celular2 + "\n")
             if cidades2 == "":
                pass
             else: arquivo_de_txt.write(cidades2 + "\n")
             if estados2 == "":
                pass
             else: arquivo_de_txt.write(estados2 + "\n")
    else:
        pass
            


        
            
       




    


 


