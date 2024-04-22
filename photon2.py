from scipy.integrate import solve_ivp

import matplotlib.pyplot as plt
import numpy as np
# Constantes
G = 1  # Utiliser une valeur symbolique pour simplifier
M = 1  # Masse de l'objet central
c = 1  # Vitesse de la lumière

# Fonction dérivée pour l'intégration
def dudphi(phi, u):
    return [u[1], 3*G*M*u[0]**2 - u[0]]

# Conditions initiales
# u[0] = 1/r, où r est la distance initiale du photon à la masse centrale
# u[1] = du/dphi à phi=0, dépendant de la trajectoire initiale du photon
u0 = [1/10, 0]  # Supposons que le photon commence à une distance radiale de 10, avec une trajectoire tangentielle initiale

# Intervalles d'angle pour l'intégration
phi_eval = np.linspace(-np.pi, np.pi, 40)  # De 0 à 2*pi

# Résoudre l'équation différentielle
sol = solve_ivp(dudphi, [-np.pi, np.pi], u0, t_eval=phi_eval)

# Convertir la solution en coordonnées polaires (r, phi) et puis en coordonnées cartésiennes (x, y)
r_sol = 1 / sol.y[0]  # Convertir u en r
x_sol = r_sol * np.cos(sol.t)
y_sol = r_sol * np.sin(sol.t)

# Dessiner la trajectoire du photon
plt.figure(figsize=(10, 10))
plt.plot(x_sol, y_sol, label="Trajectoire du photon")
plt.scatter([0], [0], color='red', label="Masse centrale")  # Marquer la position de la masse centrale
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.title("Trajectoire du photon autour d'une masse centrale")
plt.grid(True)
plt.show()
