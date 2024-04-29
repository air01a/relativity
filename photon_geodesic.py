
import matplotlib.pyplot as plt
import numpy as np

def update_photon(position, velocity, mass, G, c, dt):
    """
    Met à jour la position et la vitesse du photon en utilisant une approximation de la force de gravité
    due à la courbure de l'espace-temps.
    """
    # Calculer la distance radiale du photon à la masse centrale
    r = np.sqrt(position[0]**2 + position[1]**2)
    
    # Calculer l'accélération due à la gravité (approche newtonienne simplifiée pour l'illustration)
    force_magnitude = G * mass / r**2
    force_direction = -position / r  # Vecteur unitaire pointant vers la masse
    acceleration = force_magnitude * force_direction / c**2  # Facteur c² pour la relativité
    
    # Mettre à jour la vitesse et la position en utilisant la méthode d'Euler
    new_velocity = velocity + acceleration * dt
    new_position = position + new_velocity * dt
    
    return new_position, new_velocity

# Conditions initiales
position = np.array([5.0, 0.0])  # Position initiale à une distance de 5 unités avec un paramètre d'impact
velocity = np.array([0.0, 1.0])  # Vitesse initiale (normalisée, direction tangentielle)
mass = 1e30  # Masse de l'objet central (kg)
G = 6.67430e-11  # Constante gravitationnelle (m^3 kg^-1 s^-2)
c = 3e8  # Vitesse de la lumière (m/s)
dt = 0.01  # Pas de temps

# Simulation
positions = [position]
for _ in range(30):  # 1000 pas de temps
    position, velocity = update_photon(position, velocity, mass, G, c, dt)
    positions.append(position)

positions = np.array(positions)

# Dessiner la trajectoire
plt.figure(figsize=(8, 8))
plt.plot(positions[:, 0], positions[:, 1], color='yellow')
plt.scatter([0], [0], color='red', label='Masse centrale')  # Masse centrale
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Trajectoire approximative d\'un photon près d\'une masse')
plt.legend()
plt.grid(True)
plt.show()
