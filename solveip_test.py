from scipy.integrate import solve_ivp
import numpy as np
from math import exp
# Définition de l'équation différentielle
# Solve y(t)' = -ay(t)-b avec y0=0
def equation(t, y):
    a = 1
    b = 2
    return -a*y-b


t0 = 0  # seconde
tf = 1  # seconde
y0 = 0  # Condition initiale

# Résolution
solution = solve_ivp(equation, [t0, tf], [y0], max_step=0.1)

print(solution.t)  # Affichage de la table des instants
print(solution.y[0])  # Affichage des résultats

print([-2*(1-exp(-1*t)) for t in solution.t])