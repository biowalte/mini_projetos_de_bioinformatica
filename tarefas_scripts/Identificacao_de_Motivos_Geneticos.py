'''
O objetivo desse script é procurar padrões específicos em sequências 
genéticas, podendo ser uma ferramenta na análise pro padrões.
'''


from Bio.Seq import Seq
import re

# criando uma função para identificar motivos genéticos
def identificar_motivos_geneticos(sequencia, padrao):
    matches = re.finditer(padrao, str(sequencia))
    
    if matches:
        for match in matches:
            print(f"Motivo encontrado na posição {match.start() + 1}")

# sequencia aleatória, mas pode ser substituida por uma de interesse
sequencia_dna = Seq("ATGCTAGCTAATGCGATACTAGCTAGCGATCGATCGATCGATCGATCGATCGATCGATCGAT")

# Padrão a ser procurado, tambem pode ser substituido por outro padrão
padrao = re.compile(r"ATCG")

# printando o resultado
identificar_motivos_geneticos(sequencia_dna, padrao)
