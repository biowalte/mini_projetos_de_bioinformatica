from Bio import SeqIO

# Defina o nome do arquivo FASTA
fasta_file = 'Henneguya_paraensis.fasta' # no lugar de 'Henneguya_paraensis.fasta', coloque seu / pode ser que haja a necessidade de você passar o caminho completo no argumento

# Use um try-except para leitura do arquivo, é mais simples de identificar caso apresente algum erro
try:
    # Vamos utilizar a dentro de um laço for a biblioteca biopython, ela simplifica muito o processo de leitura das sequências do arquivo
    for fasta in SeqIO.parse(fasta_file, 'fasta'):
        print("ID:", fasta.id)
        print("Sequência:", fasta.seq)
        print("Comprimento:", len(fasta))
        
        
        # Você pode adicionar mais análises aqui, se necessário
        print("-" * 50)  # Uma linha para separar as sequências
except FileNotFoundError:
    print(f"O arquivo '{fasta_file}' não foi encontrado.")
except Exception as e:
    print("Ocorreu um erro durante a leitura do arquivo:", str(e))
