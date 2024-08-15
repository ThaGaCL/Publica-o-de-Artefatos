import matplotlib.pyplot as plt

needed = input("Digite o número de artigos que cabe artefato: ")
exists = input("Digite o número de artigos que existe artefato: ")

needed = int(needed)
exists = int(exists)

need_but_not_exists = needed - exists


# Data to plot
labels = 'Artefato Indisponivel', 'Artefato Dísponível'
sizes = [need_but_not_exists, exists]
colors = ['orangered', 'springgreen']

# Plot and save in ./graficos
plt.bar(labels, sizes, color=colors)
plt.title('Gráfico de Disponibilidade de Artefato')
plt.ylabel('Quantidade de Artigos')
plt.xlabel('Disponibilidade de Artefato')
plt.show()
plt.axis('equal')
plt.savefig('./graficos/grafico.png')

plt.show()

