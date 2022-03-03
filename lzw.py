import argparse
import os
import pickle

DICTIONARY_SIZE = 256

def compress(input):
    global DICTIONARY_SIZE
    dictionary = {}
    result = []
    temp = ""

    for i in range(0, DICTIONARY_SIZE):
        dictionary[str(chr(i))] = i

    for c in input:
        temp2 = temp+str(chr(c))
        if temp2 in dictionary.keys():
            temp = temp2
        else:
            result.append(dictionary[temp])
            dictionary[temp2] = DICTIONARY_SIZE
            DICTIONARY_SIZE+=1
            temp = ""+str(chr(c))

    if temp != "":
        result.append(dictionary[temp])  
        
    return result

def decompress(input):
    global DICTIONARY_SIZE
    dictionary = {}
    result = []

    for i in range(0, DICTIONARY_SIZE):
        dictionary[i] = str(chr(i))

    previous = chr(input[0])
    input = input[1:]
    result.append(previous)

    for bit in input:
        aux = ""
        if bit in dictionary.keys():
            aux = dictionary[bit]
        else:
            aux = previous+previous[0] 
            #Bit is not in the dictionary
                 # Get the last character printed + the first position of the last character printed
                 #because we must decode bits that are not present in the dictionary, so we have to guess what it represents, for example:
                 #let's say bit 37768 is not in the dictionary, so we get the last character printed, for example it was 'uh'
                 #and we take it 'uh' plus its first position 'u', resulting in 'uhu', which is the representation of bit 37768
                 #the only case where this can happen is if the substring starts and ends with the same character ("uhuhu").
        result.append(aux)
        dictionary[DICTIONARY_SIZE] = previous + aux[0]
        DICTIONARY_SIZE+= 1
        previous = aux
    return result

parser = argparse.ArgumentParser(description = 'Text compressor and decompressor.')
parser.add_argument('action', choices={"compress", "decompress"}, help="Define action to be performed.")
parser.add_argument('-i', action = 'store', dest = 'input', required = True,
                           help = 'Input file.')
parser.add_argument('-o', action = 'store', dest = 'output', required = True,
                           help = 'Output file.')
arguments = parser.parse_args()

ABSOLUTE_PATH = os.getcwd()

if arguments.action == 'compress':
    input = open(ABSOLUTE_PATH+"//"+arguments.input, "rb").read()
    output = open(ABSOLUTE_PATH+"//"+arguments.output, "wb")

    compressedFile = compress(input)
    pickle.dump(compressedFile, output)
else:
    input = pickle.load(open(ABSOLUTE_PATH+"//"+arguments.input, "rb"))
    output = open(ABSOLUTE_PATH+"//"+arguments.output, "w")
    
    uncompressedFile = decompress(input)
    for l in uncompressedFile:
            output.write(l)
    output.close()
           