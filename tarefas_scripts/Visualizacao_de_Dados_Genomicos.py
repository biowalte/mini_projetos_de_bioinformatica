'''
O objetivo desse scritp é realizar uma visualização de dados genômicos, 
de maneira básica. Utilizei uma das bibliotecas mais conhecidas em python
para visualização gráfica, a lib Matplotlib. Vou criar um gráfico de 
cobertura de leitura de uma amostra qualquer, mas vocês podem substituir
pelos dados própios
'''

import matplotlib.pyplot as plt
import numpy as np

# vamos definir uma função com dados de cobertura de leitura ficticia
def gerar_dados_cobertura_leitura(tamanho_genoma=1000):
    posicoes = np.arange(1, tamanho_genoma + 1)
    cobertura_leitura = np.random.randint(10, 50, size=tamanho_genoma)
    return posicoes, cobertura_leitura

# Função para visualizar a cobertura de leitura
def visualizar_cobertura_leitura(posicoes, cobertura_leitura):
    plt.plot(posicoes, cobertura_leitura, marker='o', linestyle='-', color='b')
    plt.title('Cobertura de Leitura Genômica')
    plt.xlabel('Posição no Genoma')
    plt.ylabel('Cobertura de Leitura')
    plt.grid(True)
    plt.show()

# Gerar dados fictícios
posicoes, cobertura_leitura = gerar_dados_cobertura_leitura()

# Visualizar cobertura de leitura
visualizar_cobertura_leitura(posicoes, cobertura_leitura)