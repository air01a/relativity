import numpy as np
from einsteinpy.coordinates import SphericalDifferential
from einsteinpy.metric import Schwarzschild
from einsteinpy.geodesic import Geodesic
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from astropy import units as u
from einsteinpy.bodies import Body
from einsteinpy.plotting import GeodesicPlotter

# Draw sun on graph
def draw_sun(ax):
    radius = 696000*10000

    # Create theta and phi
    theta = np.linspace(0, 2 * np.pi, 100)
    phi = np.linspace(0, np.pi, 100)

    # Grid creation
    theta, phi = np.meshgrid(theta, phi)

    # Shperical conversion to cartesian
    x = radius * np.sin(phi) * np.cos(theta)
    y = radius * np.sin(phi) * np.sin(theta)
    z = radius * np.cos(phi)
    ax.plot_surface(x, y, z, color='y', alpha=0.9)
    return ax

year_number=100

M = 1.989e30 * u.kg  # mass of sun
distance = 46e6 * u.km # distance to perihelion
speed_at_perihelion = 58.98 * u.km / u.s # speed at perihelion
omega = (u.rad * speed_at_perihelion) / distance

position = SphericalDifferential(distance, np.pi / 2 * u.rad, np.pi * u.rad,
                               0 * u.km / u.s, 0 * u.rad / u.s, omega)
Sun = Body(name="Sun", mass=M, parent=None)
Object = Body(name="Mercury", differential=position, parent=Sun)
# Schwarzschild metric
metric = Schwarzschild.from_coords(position,M)
end_lambda = ((year_number * u.year).to(u.s)).value
step=((150 * u.min).to(u.s)).value
geod = Geodesic(body=Object,metric=metric, end_lambda=end_lambda, step_size=step)
# coordinates extraction
x = geod.trajectory[:, 1]
y = geod.trajectory[:, 2] 
z = geod.trajectory[:, 3] 

sgp = GeodesicPlotter()
sgp.plot(geod)
sgp.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
fig.set_dpi(150)

# Drawing
line, = ax.plot([], [], [], 'r-', label='Mercury Trajectory')
point, = ax.plot([], [], [], 'go')

def init():
    line.set_data([], [])
    line.set_3d_properties([])
    point.set_data([], [])
    point.set_3d_properties([])
    return line, point

def update(num):
    line.set_data(x[:num], y[:num])
    line.set_3d_properties(z[:num])
    point.set_data([x[num]], [y[num]])
    point.set_3d_properties([z[num]])
    return line, point




ani = FuncAnimation(fig, update, frames=len(x), init_func=init, blit=True)


ax.set_xlim([-1e11, 1e11])
ax.set_ylim([-1e11, 1e11])
ax.set_zlim([-1e11, 1e11])
ax.set_xlabel("X (km)")
ax.set_ylabel("Y (km)")
ax.set_zlabel("Z (km)")
ax.set_title("Trajectoire autour du Soleil")
ax=draw_sun(ax)
plt.show()

