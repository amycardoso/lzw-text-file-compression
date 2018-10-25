import argparse
import os
import pickle

#função que realiza a compressao da entrada
def compressao(entrada):
    tamanhoDicionario = 256
    dicionario = {} #armazena o dicionário

    #Adicionando tabela ASCII ao dicionário
    for i in range(0, tamanhoDicionario):
        dicionario[str(chr(i))] = i #Como fica o dicionário {'a': 97, 'b': 98}
    
    temp = ""
    resultado = [] #armazena o resultado comprimido

    for c in entrada: #Percorre a string
        temp2 = temp+str(chr(c)) #temp2 recebe o caractere atual mais o anterior para verificar se existe no dicionário
        if temp2 in dicionario.keys(): #se estiver no dicionário temp = temp2 para ser concatenado posteriormente com o próximo caractere
            temp = temp2
        else:
            resultado.append(dicionario[temp]) # se não, adiciona ao resultado da compressão e
            dicionario[temp2] = tamanhoDicionario #adiciona a string ao dicionário
            tamanhoDicionario+=1
            temp = ""+str(chr(c)) #reseta a string temporária com o caractere atual

    if temp != "": #caso a string temporária não esteja vazia, deve-se adicionar ao resultado
        resultado.append(dicionario[temp])    
        
    return resultado

#função que realiza a descompressao da entrada
def descompressao(entrada):
    tamanhoDicionario = 256
    dicionario = {} #armazena o dicionário
    resultado = [] #armazena o resultado descomprimido

    #inicializando dicionário com tabela ASCII
    for i in range(0, tamanhoDicionario):
        dicionario[i] = str(chr(i)) #Como o dicionário fica, ex: {97: 'a', 98: 'b'}

    anterior = chr(entrada[0]) #pega o primeiro caractere e marca como anterior, por exemplo: chr(97) retorna a string 'a'
    entrada = entrada[1:] #remove o primeiro caractere da entrada
    resultado.append(anterior) #adiciona o primeiro caractere ao resultado

    for bit in entrada:
        aux = ""
        if bit in dicionario.keys():
            aux = dicionario[bit] #pega o caractere correspondente ao bit no dicionário
        else: #Quando o bit não ta no dicionário, deve se pegar
            aux = anterior+anterior[0] #o ultimo caractere impresso + a primeira posição do último caractere impresso 
            #pois devemos decodificar bits que não estão presentes no dicionário, então temos que adivinhar o que ele representa, por exemplo:
            #digamos que o bit 37768 não ta no dicionário, então pegamos o último caractere impresso, por exemplo foi 'uh'
            #e pegamos ele 'uh' mais sua primeira posição 'u', resultando em 'uhu', que é a representação do bit 37768
            #o único caso em que isso pode ocorrer é se a substring começar e terminar com o mesmo caractere ("uhuhu").
                
        resultado.append(aux) #adiciona ao resultado
        #Resimulando como as substrings foram adicionadas durante a compactação
        dicionario[tamanhoDicionario] = anterior + aux[0] #adiciona ao dicionário o caractere anterior mais a primeira posição do caractere atual
        tamanhoDicionario+= 1 #incrementa tamanho do dicionário
        anterior = aux #anterior recebe o caractere atual
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

    comprimido = compressao(entrada)
    pickle.dump(comprimido, saida) #escreve no arquivo binário a compressão
else:
    entrada = pickle.load(open(ABSOLUTE_PATH+"//"+arguments.input, "rb"))
    saida = open(ABSOLUTE_PATH+"//"+arguments.output, "w")
    
    descomprimido = descompressao(entrada)
    for l in descomprimido: #grava no arquivo o resultado da descompressão
            saida.write(l)
    saida.close()
