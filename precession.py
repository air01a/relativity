import numpy as np
import matplotlib.pyplot as plt
from math import pi



years = 200
# Constantes
G = 6.67430e-11  # constante gravitationnelle
M = 1.989e30  # masse du Soleil
T = 88  # période orbitale de Mercure en jours
a = 57.91e9  # demi-grand axe de l'orbite de Mercure en mètres
e = 0.2056  # excentricité de l'orbite de Mercure
c = 299792e3 # célérité en m/s
# Précession du périhélie


# Calcul de l'orbite de Mercure pour une année
def compute_orbit(num_orbits, shift=0):
    theta = np.linspace(0, 2 * np.pi * num_orbits, 1000 * num_orbits)
    r = a * (1 - e**2) / (1 + e * np.cos(theta - shift))
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y


delta_theta_newton = 6.20*10**-6
delta_theta_relativity = 24*(pi**3)*(a**2)/((T*24*3600)**2*(c**2)*(1-e**2))
delta_theta = delta_theta_relativity+delta_theta_newton


print("Precession due to RR")
print("--------------------")

print("rad per revolution : ",delta_theta)
print("Arc sec per revolution :",delta_theta * 180/(pi)*60*60)
print("Arc sec per century", delta_theta * 180/(pi)*60*60 * (365.25 / T) *100)

precession_per_orbit = delta_theta  # radians par orbite, valeur simplifiée


# Orbite initiale
x1, y1 = compute_orbit(1)

# Orbite 400 ans plus tard

shift_years = years * (365.25 / T) * precession_per_orbit
print(f"After {years} years (rad) : {shift_years}")
print(f"After {years} years : {shift_years* 180/(pi)*60*60 }")

precession_period=2*pi / ((365.25 / T)*delta_theta)
print("Precession period", precession_period)


# Tracer les orbites
plt.figure(figsize=(10, 5))
plt.plot(x1, y1, label="Orbite initiale")

num_orbit=5
shift=precession_period/num_orbit
for i in range(1,num_orbit-1):
    shift_years = shift*i * (365.25 / T) * precession_per_orbit
    print(shift_years)
    x2, y2 = compute_orbit(1, shift_years)
    plt.plot(x2, y2, label=f"Orbite {int(shift)} ans plus tard", linestyle='--')
#plt.plot(x2, y2, label="Orbite 400 ans plus tard", linestyle='--')
plt.scatter([0], [0], color='yellow', label="Soleil")  # position du Soleil
plt.title("Trajectoire de Mercure sur une année et 400 ans plus tard")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
