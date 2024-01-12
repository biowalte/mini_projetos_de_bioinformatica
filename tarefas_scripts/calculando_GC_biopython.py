'''
#1. importei as bibliotecas necessárias 
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

#lendo o arquivo do genoma de vcs
genome_file = "18s_humano.fasta"
genome = SeqIO.read(genome_file, "fasta")

#aqui podemos calcular a % do conteudo GC
gc_content = gc_fraction(genome.seq)
gc_percentage = gc_content * 100

# Exibir o resultado
print(f"Conteúdo GC: {gc_percentage:.2f}%")
'''

#1. importei as bibliotecas necessárias: 
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

#lendo o arquivo do genoma:
genome_file = "Myxobolus freitasi n. sp.fasta" #utilizei esse "Myxobolus", mas deve substituir pela sua sequencia
genome = SeqIO.read(genome_file, "fasta")

#calculando o conteudo GC
gc_content = gc_fraction(str(genome.seq))
gc_count = int(gc_content * len(genome))

print(f"Número de pares de bases GC: {gc_count}")


#aqui podemos calcular a % do conteudo GC
gc_content = gc_fraction(genome.seq)
gc_percentage = gc_content * 100

# Exibir o resultado
print(f"Conteúdo GC: {gc_percentage:.2f}%")
