import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import map_coordinates

def lens_equation(beta, theta, mass, d_lens, d_source):
    """
    Calcule les angles déviés theta pour les angles originaux beta.
    """
    G = 6.67430e-11  # Constante gravitationnelle
    c = 299792458    # Vitesse de la lumière
    rs = 2 * G * mass / c**2  # Rayon de Schwarzschild
    return beta - theta + (rs / np.maximum(theta, 1e-10)) * (d_source - d_lens) / d_source

def raytrace_channel(channel, mass, d_lens, d_source, scale):
    """
        RayTracing for one channel     
    """
    height, width = channel.shape
    y, x = np.indices((height, width)) # x=[1 2 3 ] [1 2 3]... and y=[0 0 0][1 1 1]...



    theta_x = (x - width // 2) * scale
    theta_y = (y - height // 2) * scale
    theta = np.sqrt(theta_x**2 + theta_y**2)

    G = 6.67430e-11  # Constante gravitationnelle
    c = 299792458    # Vitesse de la lumière
    rs = 2 * G * mass / c**2  # Rayon de Schwarzschild

    beta = lens_equation(0, theta, mass, d_lens, d_source)

    valid = theta > 1e-10
    schwarzschild = theta < rs

    beta_x = np.zeros_like(theta_x)
    beta_y = np.zeros_like(theta_y)
    beta_x[valid] = beta[valid] * theta_x[valid] / theta[valid]
    beta_y[valid] = beta[valid] * theta_y[valid] / theta[valid]

    beta_x_pix = beta_x / scale + width // 2
    beta_y_pix = beta_y / scale + height // 2

    deformed_channel = map_coordinates(channel, [beta_y_pix.flatten(), beta_x_pix.flatten()], order=1, mode='wrap').reshape(height, width)

    # Assombrir les pixels qui sont à l'intérieur du rayon de Schwarzschild
    deformed_channel[schwarzschild] = 0

    return deformed_channel


def raytrace_image(image, mass, d_lens, d_source, scale):
    """
        Ray Tracing for 3 channels
    """
    deformed_red = raytrace_channel(image[:, :, 0], mass, d_lens, d_source, scale)
    deformed_green = raytrace_channel(image[:, :, 1], mass, d_lens, d_source, scale)
    deformed_blue = raytrace_channel(image[:, :, 2], mass, d_lens, d_source, scale)
    deformed_image = np.stack([deformed_red, deformed_green, deformed_blue], axis=-1)
    return deformed_image

image = plt.imread('space.jpg')  # Background image (color)
mass = 1e20  # Object mass
d_lens = 1e20  # Distance to object
d_source = 2e20  # Distance to source
scale = 5e-6  # Radians seen for 1 pixel

deformed_image = raytrace_image(image, mass, d_lens, d_source, scale)
plt.imshow(deformed_image)
plt.show()
