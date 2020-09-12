from lib import *
from sphere import *
from math import pi, tan
from rayUtils import *

BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)
FONDO = color(0, 0, 250)


class Raytracer(object):
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.background_color = BLACK
    self.light = None
    self.scene = []
    self.clear()

  def clear(self):
    self.pixels = [
      [self.background_color for x in range(self.width)]
      for y in range(self.height)
    ]

  def write(self, filename):
  	writebmp(filename, self.width, self.height, self.pixels)

  def display(self, filename='outOsos.bmp'):
  	self.render()
  	self.write(filename)

  def point(self, x, y, c = None):
    try:
      self.pixels[y][x] = c or self.current_color
    except:
      pass

  def scene_intersect(self, orig, direction):
    zbuffer = float('inf')

    material = None
    intersect = None

    for obj in self.scene:
      hit = obj.ray_intersect(orig, direction)
      if hit is not None:
        if hit.distance < zbuffer:
          zbuffer = hit.distance
          material = obj.material
          intersect = hit

    return material, intersect

  def cast_ray(self, orig, direction):
    material, intersect = self.scene_intersect(orig, direction)

    if material is None:
      return self.background_color

    light_dir = norm(sub(self.light.position, intersect.point))
    light_distance = length(sub(self.light.position, intersect.point))

    offset_normal = mul(intersect.normal, 1.1)  # avoids intercept with itself
    shadow_orig = sub(intersect.point, offset_normal) if dot(light_dir, intersect.normal) < 0 else sum(intersect.point, offset_normal)
    shadow_material, shadow_intersect = self.scene_intersect(shadow_orig, light_dir)
    shadow_intensity = 0

    if shadow_material and length(sub(shadow_intersect.point, shadow_orig)) < light_distance:
      shadow_intensity = 0.9

    intensity = self.light.intensity * max(0, dot(light_dir, intersect.normal)) * (1 - shadow_intensity)

    reflection = reflect(light_dir, intersect.normal)
    specular_intensity = self.light.intensity * (
      max(0, -dot(reflection, direction))**material.spec
    )

    diffuse = material.diffuse * intensity * material.albedo[0]
    specular = color(255, 255, 255) * specular_intensity * material.albedo[1]
    return diffuse + specular

  """def cast_ray(self, orig, direction, sphere):
    if sphere.ray_intersect(orig, direction):
      return color(255, 0, 0)
    else:
      return color(0, 0, 255)"""

  def render(self):
    alfa = int(pi/2)
    for y in range(self.height):
      for x in range(self.width):
        i =  (2*(x + 0.5)/self.width - 1)*self.width/self.height*tan(alfa/2)
        j =  (2*(y + 0.5)/self.height - 1 )*tan(alfa/2)
        # x = int(x)
        # y = int(y)
        # print(x, y)
        direction = norm(V3(i, j, -1))
        self.pixels[y][x] = self.cast_ray(V3(0,0,0), direction)

  """def basicRender(self):
  #Esto llena la pantalla de colores degradado
    for x in range(self.width):
      for y in range(self.height):
        r = int((x/self.width)*255) if x/self.width < 1 else 1
        g = int((y/self.height)*255) if y/self.height < 1 else 1
        b = 0
        self.pixels[y][x] = color(r, g, b)"""


r = Raytracer(1000, 1000)

r.light = Light(
  position=V3(0, 0, 20),
  intensity=1.5
)

r.background_color = WHITE

r.scene = [
    #OSO CAFE (derecha)
    #cuerpo y adorno 
    Sphere(V3(2.5, -1, -10), 1.5, rubber),
    Sphere(V3(2.2, 0.2, -8.6), 0.2, lightGreen),
    Sphere(V3(1.8, 0.2, -8.6), 0.17, lightGreen),
    Sphere(V3(2.5, 0.2, -8.6), 0.17, lightGreen),
    #cabeza
    Sphere(V3(2.5, 1.5, -10), 1.25, softcoffee),
    #osico y orejas
    Sphere(V3(2.3, 1.1, -9), 0.4, coffee),
    Sphere(V3(3.4, 2.3, -9), 0.35, coffee),
    Sphere(V3(1.4, 2.3, -9), 0.35, coffee),
    #extremidades
    Sphere(V3(4, 0, -10), 0.45, softcoffee),
    Sphere(V3(1, 0, -10), 0.45, softcoffee),
    Sphere(V3(4, -2.2, -10), 0.5, softcoffee),
    Sphere(V3(1, -2.2, -10), 0.5, softcoffee),
    #nariz y ojos
    Sphere(V3(2, 1, -8), 0.1, dark),
    Sphere(V3(2.3, 1.5, -8), 0.1, dark),
    Sphere(V3(1.7, 1.5, -8), 0.1, dark),
    #OSO BLANCO (izquierda)
    #cuerpo y adorno
    Sphere(V3(-2.5, -1, -10), 1.5, iron),
    Sphere(V3(-2.2, 0.2, -8.6), 0.2, rubber),
    Sphere(V3(-1.9, 0.2, -8.6), 0.17, rubber),
    Sphere(V3(-2.5, 0.2, -8.6), 0.17, rubber),
    #cabeza
    Sphere(V3(-2.5, 1.5, -10), 1.25, snow),
    #osico y orejas
    Sphere(V3(-2.4, 1.1, -9), 0.4, snow),
    Sphere(V3(-3.3, 2.3, -9), 0.35, snow),
    Sphere(V3(-1.3, 2.3, -9), 0.35, snow),
    #extremidades
    Sphere(V3(-4, 0, -10), 0.45, snow),
    Sphere(V3(-1, 0, -10), 0.45, snow),
    Sphere(V3(-4, -2.2, -10), 0.5, snow),
    Sphere(V3(-1, -2.2, -10), 0.5, snow),
    #nariz y ojos
    Sphere(V3(-2.1, 1, -8), 0.1, dark),
    Sphere(V3(-2.4, 1.5, -8), 0.1, dark),
    Sphere(V3(-1.8, 1.5, -8), 0.1, dark),
]

"""r.scene = [
  Sphere(V3(0, -1.5, -10), 1.5, ivory),
  Sphere(V3(-2, -1, -12), 2, rubber),
  Sphere(V3(1, 1, -8), 1.7, rubber),
  Sphere(V3(0, 2, -10), 2, ivory)
]"""
r.display()