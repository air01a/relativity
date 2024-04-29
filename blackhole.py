import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import map_coordinates

def lens_equation(theta, mass, d_lens, d_source):
    """
    Calcule les angles déviés theta pour les angles originaux beta.
    """
    G = 6.67430e-11  # Gravitational constant
    c = 299792458    # Speed of light
    rs = 4 * G * mass / c**2  # Schwarzschild Radius
    r = np.maximum(theta * d_lens, 1e-40)  
    #r=theta*d_lens+1e-40
    # Distance from centre of black hole : d = tan(theta)*d_lens = theta * dlens
    # lens equation : \delta \theta = GM/(c²*d)
    # d_source - d_lens = distance between lens and image
    # return equivalent angle due to lens deviation
    return theta - (rs / r) * (d_source - d_lens) / d_source

def raytrace_channel(channel, mass, d_lens, d_source, scale):
    """
        RayTracing for one channel     
    """
    height, width = channel.shape
    y, x = np.indices((height, width)) # x=[1 2 3 ] [1 2 3]... and y=[0 0 0][1 1 1]...



    theta_x = (x - width // 2) * scale
    theta_y = (y - height // 2) * scale
    theta = np.sqrt(theta_x**2 + theta_y**2) # theta contains the angle from the center for each pixel

    G = 6.67430e-11  # Gravitational constant
    c = 299792458    # So bad name speed of light
    rs = 2 * G * mass / c**2  # Schwarzschild radius

    beta = lens_equation(theta, mass, d_lens, d_source)
    # bet now contains adapted angle

    valid = theta > 1e-20
    schwarzschild = theta * d_lens < rs #0.00081362/3
    print(rs, theta, theta *d_lens)
    beta_x = np.zeros_like(theta_x)
    beta_y = np.zeros_like(theta_y)

    # Recalculate projection on image on x_axis and y_axis
    beta_x[valid] = beta[valid] * theta_x[valid] / theta[valid]
    beta_y[valid] = beta[valid] * theta_y[valid] / theta[valid]


    # Center
    beta_x_pix = beta_x / scale + width // 2
    beta_y_pix = beta_y / scale + height // 2

    # Map coordonnates to scale
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
mass = 1e30  # Object mass
d_lens = 1e06  # Distance to object
d_source = 1.001e06  # Distance to source
scale = 0.0000059  # Radians seen for 1 pixel, equivalent for 1 arcsecond (1/(60*60)*2pi/180)

deformed_image = raytrace_image(image.copy(), mass, d_lens, d_source, scale)

fig, axs = plt.subplots(1, 2) 

axs[0].imshow(image)
axs[0].axis('off')  # no axis
axs[0].set_title('Initial') 
axs[1].imshow(deformed_image)
axs[1].axis('off')  # no axis
axs[1].set_title('Black hole deformation') 

plt.show()
