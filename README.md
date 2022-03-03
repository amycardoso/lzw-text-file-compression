# LZW Text Compressor and Decompressor
[![GitHub license](https://img.shields.io/github/license/amycardoso/LZW-Text-File-Compression)](https://github.com/amycardoso/LZW-Text-File-Compression/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/amycardoso/LZW-Text-File-Compression)](https://github.com/amycardoso/LZW-Text-File-Compression/stargazers)

The main objective of this project is to put into practice the theoretical concepts approached in the classroom related to media coding techniques. For this, a compressor and a decompressor of text were developed using the Lempel-Ziv-Welch (LZW) algorithm with fixed dictionary size. 
Data entry is a TXT document whose output is a binary file containing the compressed data.

### Requirements
* Python 3

### Usage

The compressor operates by command-line, accepting as parameter the name and path of the original TXT file, as well as the name and path of the binary file to be generated. The decompressor will also be command-line operated, accepting both parameters as well (binary input file and output TXT file). The following execution format must be obeyed: 

For compression:

```
$ python3 lzw.py compress -i original_file.txt -o binary_file.bin

```
For decompression:
```
$ python3 lzw.py decompress -i binary_file.bin -o uncompressed_file.txt

```
For help:
```
$ python3 lzw.py -h

```
