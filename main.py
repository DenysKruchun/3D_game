from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.sky import Sky
from ursina.shaders import lit_with_shadows_shader, basic_lighting_shader
from perlin_noise import PerlinNoise
from random import randint
import math
import os
from settings import *
from models import Tree,Block,Chest




app = Ursina()

Entity.default_shader = lit_with_shadows_shader 
files = os.listdir(BLOCKS_PATH)

print(files)
block_images = []

for image in files:
    texture1 = load_texture(os.path.join(BLOCKS_PATH, image))

    block_images.append(texture1)

print(block_images)

class Controller(Entity):
    def __init__(self, ):
        super(). __init__ ()
        self.sky = Sky(texture="sky_sunset")
        self.player = FirstPersonController()

        # house = Entity(model = "assets/minecraft_house/scene",scale = 1, origin_y = 0, collider   = "box")
        pivot = Entity()
        DirectionalLight(parent=pivot, y=3, z=3, shadows=True,rotation = (45,-45,45))
        window.fullscreen = True

    def new_game(self, ):

        noise = PerlinNoise(octaves = 4, seed = randint(0,1000))
        for z in range(-MAP_SIZE,MAP_SIZE):
            for x in range(-MAP_SIZE,MAP_SIZE):
                height = noise([x*0.02,z*0.02])
                height = math.floor(height*7.5)
                block = Block(position=(x,height,z))
                trees_ammont = randint(0,100)
                if trees_ammont == 25:
                    tree = Tree(x,height,z)
                chest_ammount = randint(0,700)
                if chest_ammount == 25:
                    chest = Chest(x,height,z)

# ground = Entity(model="plane", collider='box', texture="grass",
#                 scale=64, texture_scale=(4, 4))
game = Controller()
game.new_game()
app.run()
