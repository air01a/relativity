import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Créer une grille de points (x, y)
x = np.linspace(-4, 4, 400)
y = np.linspace(-4, 4, 400)
x, y = np.meshgrid(x, y)

# Définir une fonction pour la courbure de l'espace-temps
# z est la hauteur du "entonnoir"
z = -1 / (x**2 + y**2 + 1)
z[z<-0.7]=-0.7
# Créer la figure et l'axe
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Tracer la surface
surface = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')


theta = np.linspace(0, 2*np.pi, 200)
x_geo = 2*np.cos(theta)
y_geo = 2*np.sin(theta)
z_geo = -1 / (x_geo**2 + y_geo**2 + 1)
ax.plot(x_geo, y_geo, z_geo, color='r', linewidth=3)

# Ajouter des titres et des labels
ax.set_title('Simulation de la courbure de l’espace-temps autour d’un trou noir')
ax.set_xlabel('X (distances spatiales)')
ax.set_ylabel('Y (distances spatiales)')
ax.set_zlabel('Courbure de l’espace-temps')

# Ajouter une barre de couleur pour la surface
fig.colorbar(surface)

# Afficher le graphique
plt.show()