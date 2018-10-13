# Compressor e Descompressor de Texto LZW

O objetivo principal deste projeto é colocar em prática conceitos teóricos abordados em sala de aula relacionados a técnicas de codificação de mídias. Para isso, foi desenvolvido um compressor e um descompressor aplicado a texto em geral, utilizando o algoritmo Lempel-Ziv-Welsh (LZW) com tamanho de dicionário fixo.

A entrada dos dados é um documento no formato TXT, cuja saída, o
codificador gera um arquivo binário contendo os dados comprimidos.
#

### Requirements
* Python 3

### Usage

O compressor opera por linha de comando, aceitando como parâmetro o nome e caminho do arquivo TXT original, e também o nome e caminho do arquivo binário a ser gerado. O descompressor,
por sua vez, também será operado por linha de comando, aceitando ambos os parâmetros também
(arquivo binário de entrada e arquivo TXT de saída). O seguinte formato de execução deverá ser obedecido:

Para compressão:

```
$ python3 encode -i arquivo_original.txt -o arquivo_binario.bin

```
Para descompressão:
```
$ python3 decode -i arquivo_binario.bin -o arquivo_descomprimido.txt

```
