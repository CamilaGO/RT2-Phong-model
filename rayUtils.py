from lib import *
from dataclasses import dataclass

BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)

class Light(object):
  def __init__(self, position=V3(0,0,0), intensity=1):
    self.position = position
    self.intensity = intensity

class Material(object):
  def __init__(self, diffuse=WHITE, albedo=(1, 0), spec=0):
    self.diffuse = diffuse
    self.albedo = albedo
    self.spec = spec

class Intersect(object):
  def __init__(self, distance, point, normal):
    self.distance = distance
    self.point = point
    self.normal = normal

# ===============================================================
# MATERIALES
# ===============================================================
ivory = Material(diffuse=color(100, 100, 80), albedo=(0.6,  0.3), spec=50)
rubber = Material(diffuse=color(125, 0, 0), albedo=(0.9,  0.9), spec=13)
coffee = Material(diffuse=color(170, 80, 40), albedo=(0.9,  0.3), spec=7)
softcoffee = Material(diffuse=color(230, 170, 135), albedo=(0.9,  0.9), spec=35)
dark = Material(diffuse=color(0, 0, 0), albedo=(0.3,  0.3), spec=3)
lightGreen = Material(diffuse=color(130, 223, 36), albedo=(0.9,  0.9), spec=10)
iron = Material(diffuse=color(200, 200, 200), albedo=(1,  1), spec=20)
snow = Material(diffuse=color(250, 250, 250), albedo=(0.9,  0.9), spec=35)
