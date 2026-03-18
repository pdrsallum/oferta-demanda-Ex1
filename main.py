import matplotlib.pyplot as plt

def plotar_curvas():
    # Dados da demanda
    preco = [4, 8, 12, 16, 20]
    quantidade_demanda = [10000, 8000, 6000, 4000, 2000]

    # Oferta constante
    quantidade_oferta = [8000] * len(preco)

    # Criando o gráfico
    plt.figure(figsize=(14, 7))

    # Curva de demanda
    plt.plot(quantidade_demanda, preco, marker='o', label='Curva de Demanda', color='blue', linewidth=2)

    # Curva de oferta
    plt.plot(quantidade_oferta, preco, marker='o', label='Curva de Oferta (Q = 8000)', color='red', linewidth=2)

    # Ponto de equilíbrio
    preco_eq = 8
    quantidade_eq = 8000
    plt.scatter(quantidade_eq, preco_eq, color='black', s=100, zorder=5)
    plt.text(quantidade_eq + 200, preco_eq + 0.5, 'Ponto de Equilíbrio', fontsize=10, ha='left', va='bottom')

    # Configurações
    plt.xlabel('Quantidade', fontsize=12)
    plt.ylabel('Preço (R$)', fontsize=12)
    plt.title('Curvas de Oferta e Demanda de um Produto', fontsize=14, fontweight='bold')
    plt.legend(title='Legenda', loc='upper left', bbox_to_anchor=(1.01, 1), ncol=1, frameon=True, fancybox=True, shadow=False, borderpad=1)
    plt.grid(True, linestyle='--', alpha=0.7)

    # Ajustar layout para evitar corte da legenda
    plt.tight_layout(rect=[0, 0, 0.78, 1])

    # Exportar como PNG
    plt.savefig('grafico_oferta_demanda_melhorado.png', dpi=300, bbox_inches='tight')

    # Exibir gráfico
    plt.show()


if __name__ == "__main__":
    plotar_curvas()
