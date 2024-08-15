import matplotlib.pyplot as plt

software = input("Digite o número de artigos que necessitam de artefato de software: ")
data = input("Digite o número de artigos que necessitam de artefato de dados: ")
both = input("Digite o número de artigos que necessitam de ambos os artefatos: ")

software = int(software)
data = int(data)
both = int(both)

# Data to plot
labels = 'Software', 'Data', 'Both'
sizes = [software, data, both]
colors = ['gold', 'yellowgreen', 'lightcoral']

# Plot
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

plt.show()
