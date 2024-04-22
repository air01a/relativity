
import matplotlib.pyplot as plt
import numpy as np

# Étape 1: Définir le quadrillage carré
x = np.linspace(-10, 10, 21)  # 21 points de -10 à 10 inclus
y = np.linspace(-10, 10, 21)
X, Y = np.meshgrid(x, y)
X_flat = X.flatten()
Y_flat = Y.flatten()

# Étape 2: Calculer la distance r à la masse pour chaque point
R = np.sqrt(X_flat**2 + Y_flat**2)

# Étape 3: Appliquer la métrique de Schwarzschild sur r
GM_sur_c2 = 2  # Valeur symbolique pour la constante
R_prime = R *(1 - GM_sur_c2 / R)

# Gérer les divisions par zéro ou les valeurs infinies en remplaçant par les valeurs originales
R_prime[np.isinf(R_prime)] = R[np.isinf(R_prime)]
R_prime[np.isnan(R_prime)] = R[np.isnan(R_prime)]

# Étape 4: Repasser en coordonnées classiques
angles = np.arctan2(Y_flat, X_flat)  # Calculer l'angle pour chaque point par rapport au centre
X_prime = R_prime * np.cos(angles)  # Calculer les nouvelles coordonnées x
Y_prime = R_prime * np.sin(angles)  # Calculer les nouvelles coordonnées y

# Étape 5: Dessiner la grille transformée
# Pour relier les points entre eux et représenter le quadrillage, on dessine des lignes entre les points transformés.

plt.figure(figsize=(10, 10))

# Calculer les indices des points pour les lignes verticales et horizontales
indices = np.arange(len(X_flat)).reshape(X.shape)

# Dessiner les lignes verticales
for i in range(indices.shape[0]):
    plt.plot(X_prime[indices[i, :]], Y_prime[indices[i, :]], color='blue')

# Dessiner les lignes horizontales
for j in range(indices.shape[1]):
    plt.plot(X_prime[indices[:, j]], Y_prime[indices[:, j]], color='blue')

plt.xlim(-11, 11)
plt.ylim(-11, 11)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.title("Quadrillage transformé par la métrique de Schwarzschild")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(False)  # Ne pas afficher le quadrillage de fond
plt.show()

