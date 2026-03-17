import matplotlib.pyplot as plt

def plotar_curvas():
    # Dados da demanda
    preco = [4, 8, 12, 16, 20]
    quantidade_demanda = [10000, 8000, 6000, 4000, 2000]

    # Oferta constante
    quantidade_oferta = [8000] * len(preco)

    # Criando o gráfico
    plt.figure(figsize=(8, 6))

    # Curva de demanda
    plt.plot(quantidade_demanda, preco, marker='o', label='Demanda', color='blue')

    # Curva de oferta
    plt.plot(quantidade_oferta, preco, marker='o', label='Oferta (Q = 8000)', color='red')

    # Ponto de equilíbrio
    preco_eq = 8
    quantidade_eq = 8000
    plt.scatter(quantidade_eq, preco_eq, color='black')
    plt.text(quantidade_eq, preco_eq, '  Equilíbrio')

    # Configurações
    plt.xlabel('Quantidade')
    plt.ylabel('Preço (R$)')
    plt.title('Curvas de Oferta e Demanda')
    plt.legend()
    plt.grid(True)

    # Exportar como PNG
    plt.savefig('grafico_oferta_demanda.png', dpi=300, bbox_inches='tight')

    # Exibir gráfico
    plt.show()


if __name__ == "__main__":
    plotar_curvas()
