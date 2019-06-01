import os
import re

# Array com os caracteres válidos
caracteresValidos = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","v","x","y","z", "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","W","V","X","Y","Z",
" ","\n","'","#","@","0","1","2","3","4","5","6","7","8","9"];

# Abre o arquivo para leitura
fileIn = open('PATH_OF_FILE', 'r')
corpus = fileIn.read()

# Substitui caracteres acentuados por caracteres simples
corpus = corpus.replace('á', 'a').replace('ã', 'a').replace('â', 'a').replace('à', 'a');
corpus = corpus.replace('é', 'e').replace('ê', 'e').replace('&', 'e').replace('ë','e');
corpus = corpus.replace('í', 'i');
corpus = corpus.replace('õ', 'o').replace('ô', 'o').replace('ó', 'o').replace('ò', 'o');
corpus = corpus.replace('ú', 'u').replace('ü', 'u');
corpus = corpus.replace('ç', 'c');

corpus = corpus.replace('Á', 'a').replace('Ã', 'a').replace('Â', 'a').replace('À', 'a');
corpus = corpus.replace('É', 'e').replace('Ê', 'e').replace('&', 'e');
corpus = corpus.replace('Í', 'i');
corpus = corpus.replace('Õ', 'o').replace('Ô', 'o').replace('Ó', 'o').replace('Ò', 'o');
corpus = corpus.replace('Ú', 'u').replace('Ü', 'u');
corpus = corpus.replace('ç', 'c');

newCorpus = []

# Loop para ler os caracteres
for char in corpus:
	if char in caracteresValidos:
		newCorpus.append(char);
	else:
		newCorpus.append(' ');

newCorpus = ''.join(newCorpus);

# Corrige espaços em branco
newCorpus = re.sub(r'[ ]{2,}', r' ', newCorpus)

# Corrige linhas em branco
newCorpus = newCorpus.replace('\n \n', '\n');

# Abre o arquivo de output
fileOut = open('rt-polarity', 'w+');
fileOut.write(str(newCorpus));
fileOut.close()
