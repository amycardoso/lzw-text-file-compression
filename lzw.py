import argparse
import os
import pickle

def comprimir(entrada):
    tamanhoDicionario = 256
    dicionario = {}

    #Adicionando tabela ASCII ao dicionário
    for i in range(0, tamanhoDicionario):
        dicionario[str(chr(i))] = i
    
    temp = ""
    
    #Irá armazenar a codificação
    resultado = []
    #Percorre a string
    for c in entrada:
        temp2 = temp+str(chr(c))
        if temp2 in dicionario.keys():
            temp = temp2
        else:
            resultado.append(dicionario[temp])
            
            dicionario[temp2] = tamanhoDicionario
            tamanhoDicionario+=1
            temp = ""+str(chr(c))

    if temp != "":
        resultado.append(dicionario[temp])    
    

    return resultado

def descompressao(entrada):
    tamanhoDicionario = 256
    dicionario = {}

    resultado = []

    for i in range(0, tamanhoDicionario):
        dicionario[str(chr(i))] = i
    
    anterior = ""
    for bit in entrada:
        if bit in dicionario.keys():
            resultado.append(dicionario[bit])
            aux = anterior + bit
            anterior = bit
            if anterior not in dicionario.keys():
                dicionario[aux] = tamanhoDicionario
                tamanhoDicionario+=1
                aux = ""
            else:
                anterior = aux
                aux = ""
        else:
            dicionario[tamanhoDicionario] = resultado[-1]+ resultado[-1][0]
            tamanhoDicionario+=1
            resultado.append(dicionario[bit])
            anterior = bit

    return resultado

#Instância do objeto ArgumentParser, que será o responsável por fazer a análise dos argumentos fornecidos pela linha de comando.
parser = argparse.ArgumentParser(description = 'Compressor e descompressor de texto.')

#Configuraração do nosso parser, informando a ele quais são os argumentos esperados pelo nosso programa.
parser.add_argument('acao', choices={"encode", "decode"}, help="Definir ação a ser realizada.")
parser.add_argument('-i', action = 'store', dest = 'input', required = True,
                           help = 'Arquivo de entrada.')
parser.add_argument('-o', action = 'store', dest = 'output', required = True,
                           help = 'Arquivo de saída.')
#Solicitação ao nosso parser para que faça a verificação dos argumentos.                  
arguments = parser.parse_args()

#Pega o caminho absoluto do arquivo
ABSOLUTE_PATH = os.getcwd()

if arguments.acao == 'encode':
    entrada = open(ABSOLUTE_PATH+"//"+arguments.input, "rb").read()
    saida = open(ABSOLUTE_PATH+"//"+arguments.output, "wb")

    comprimido = comprimir(entrada)
    pickle.dump(comprimido, saida)
else:
    entrada = pickle.load(open(ABSOLUTE_PATH+"//"+arguments.input, "rb"))
    saida = open(ABSOLUTE_PATH+"//"+arguments.output, "w")
    
    descomprimido = descompressao(entrada)
    for l in descomprimido:
            saida.write(l)
    saida.close()










