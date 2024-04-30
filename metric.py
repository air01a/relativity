from sympy import symbols, diff, Matrix, simplify, lambdify
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Définition des symboles
x, y = symbols('x y')
z = -1 / (x**2 + y**2 + 1)
# Calcul des dérivées partielles
df_dx = diff(z, x)
df_dy = diff(z, y)

# Construction de la métrique
g11 = 1 + df_dx**2
g22 = 1 + df_dy**2
g12 = g21 = df_dx * df_dy
metric = Matrix([[g11, g12], [g21, g22]])
metric_inv = metric.inv()

# Calcul des symboles de Christoffel
Gamma = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)]
for i in range(2):
    for j in range(2):
        for k in range(2):
            Gamma[i][j][k] = simplify(sum(
                metric_inv[i, l] * (diff(metric[l, j], x if k == 0 else y) +
                                    diff(metric[l, k], x if j == 0 else y) -
                                    diff(metric[j, k], x if l == 0 else y)) / 2
                for l in range(2)))

# Conversion des symboles en fonctions numériques
Gamma_func = [[[lambdify((x, y), Gamma[i][j][k], 'numpy') for k in range(2)] for j in range(2)] for i in range(2)]

# Équations des géodésiques
def geodesic_equations(t, y):
    x, dx, y, dy = y
    ddx = -sum(Gamma_func[0][j][k](x, y) * (dx if j == 0 else dy) * (dx if k == 0 else dy) for j in range(2) for k in range(2))
    ddy = -sum(Gamma_func[1][j][k](x, y) * (dx if j == 0 else dy) * (dx if k == 0 else dy) for j in range(2) for k in range(2))
    return [dx, ddx, dy, ddy]

# Conditions initiales
initial_conditions = [-4, 0.001, -4, 0.00085]  # x0, dx0, y0, dy0

# Résolution des équations
t_span = [0, 10000]
sol = solve_ivp(geodesic_equations, t_span, initial_conditions, method='RK45', t_eval=np.linspace(t_span[0], t_span[1], 1000))

# Tracé en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x_grid, y_grid = np.meshgrid(np.linspace(-4, 4, 50), np.linspace(-4, 4, 50))
z_grid = -1 / (x_grid**2 + y_grid**2 + 1)
ax.plot_surface(x_grid, y_grid, z_grid, alpha=0.5, cmap='viridis')

# Tracé de la géodésique
x_path, dx_path, y_path, dy_path = sol.y

z_path = -1 / (x_path**2 + y_path**2 + 1)

ax.plot(x_path, y_path, z_path, color='red', linewidth=2, label='Geodesic')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.legend()
plt.show()
