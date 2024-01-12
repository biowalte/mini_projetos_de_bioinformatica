'''
O objetivo desse programa é realizar um linhamento global 
de sequências com o algoritmo de Needleman-Wunsch. O alinhamento
utilizado é conhecido como "alinhamento par a par", pois ele realiza
o alinhamento sobrepondo 2 sequencias.
'''
# Irei utilizar o módulo "pairwise" da biblioteca biopython

from Bio import pairwise2

# Vamos Função para realizar alinhamento global
def alinhamento_global(seq1, seq2):
    alinhamentos = pairwise2.align.globalxx(seq1, seq2, one_alignment_only=True)
    melhor_alinhamento = alinhamentos[0]
    return melhor_alinhamento

# Sequências de exemplo
sequence1 = "AGTCAGTGA" #mas poderia ser o caminho do seu arquivo fasta
sequence2 = "AGTCAGTCAA" #aqui poderia ser o caminho do seu segundo arquivo fasta

# Realizar alinhamento global
alinhamento_result = alinhamento_global(sequence1, sequence2)

# Imprimir resultados
print(f"Sequência 1: {alinhamento_result.seqA}")
print(f"Sequência 2: {alinhamento_result.seqB}")
print(f"Pontuação do Alinhamento: {alinhamento_result.score}")