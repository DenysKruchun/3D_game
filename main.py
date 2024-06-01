from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.sky import Sky
from ursina.shaders import lit_with_shadows_shader, basic_lighting_shader
from perlin_noise import PerlinNoise
from random import randint
import math
import os

MAP_SIZE = 30
app = Ursina()

Entity.default_shader = lit_with_shadows_shader 


# files = os.listdir("blocks")

class Block(Button):
    def __init__(self, position):
        super().__init__(parent=scene, model="cube",  
                         collider='box', texture="grass", 
                         color=color.hsv(0, 0, random.uniform(.9, 1.0)),
                          highlight_color=color.rgb(111, 112, 111))
        self.position = position

    def input (self,key):
        if self.hovered:
            if key == "right mouse down":
                destroy(mouse.hovered_entity)
            if key == "left mouse down":
                block = Block(self.position + mouse.normal)

noise = PerlinNoise(octaves = 4, seed = randint(0,1000))
for z in range(-MAP_SIZE,MAP_SIZE):
    for x in range(-MAP_SIZE,MAP_SIZE):
        height = noise([x*0.02,z*0.02])
        height = math.floor(height*7.5)
        block = Block(position=(x,height,z))
        trees_ammont = randint(0,100)
        if trees_ammont == 25:

            tree = Entity(model = "assets/minecraft_tree/scene",position = (x,height,z), scale = randint(4,7),  origin_y=0.5,collider = 'box')
        chest_ammount = randint(0,700)
        if chest_ammount == 25:
            chest = Entity(model = "assets/minecraft_chest/scene.gltf",position = (x,height + 0.9 ,z), scale = 0.5, collider = 'box')

# ground = Entity(model="plane", collider='box', texture="grass",
#                 scale=64, texture_scale=(4, 4))
sky = Sky(texture="sky_sunset")
player = FirstPersonController()

# house = Entity(model = "assets/minecraft_house/scene",scale = 1, origin_y = 0, collider   = "box")
pivot = Entity()
DirectionalLight(parent=pivot, y=3, z=3, shadows=True,rotation = (45,-45,45))
window.fullscreen = True
app.run()
