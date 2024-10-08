from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.sky import Sky
from ursina.shaders import lit_with_shadows_shader, basic_lighting_shader
from perlin_noise import PerlinNoise
from random import randint
import math
import pickle

app = Ursina()
from settings import MAP_SIZE
from models import Tree,Block,Chest
from ui import Menu

Entity.default_shader = lit_with_shadows_shader 


class Controller(Entity):
    def __init__(self, ):
        super(). __init__ (ignore_paused = True)
        self.sky = Sky(texture="sky_sunset")
        self.player = FirstPersonController()
       
        # house = Entity(model = "assets/minecraft_house/scene",scale = 1, origin_y = 0, collider   = "box")
        pivot = Entity()
        DirectionalLight(parent=pivot, y=3, z=3, shadows=True,rotation = (45,-45,45))
        window.fullscreen = True    
        self.menu = Menu(self)
        mouse.visible = True
        mouse.locked = False
        self.toggle_menu()
        self.start = False

    def toggle_menu(self):
        application.paused = not application.paused
        mouse.visible = application.paused
        mouse.locked = not application.paused
        self.menu.enabled = application.paused



    def new_game(self, ):
        self.start  = True
        for block in Block.list + Tree.list + Chest.list:
            destroy(block)
        Block.list = []
        Chest.list = []
        Tree.list = []

        noise = PerlinNoise(octaves = 4, seed = randint(0,1000))
        for z in range(-MAP_SIZE,MAP_SIZE):
            for x in range(-MAP_SIZE,MAP_SIZE):
                height = noise([x*0.02,z*0.02])
                height = math.floor(height*7.5)
                block = Block(position=(x,height,z))
                trees_ammont = randint(0,100)
                if trees_ammont == 25:
                    tree = Tree(x,height,z)
                # chest_ammount = randint(0,700)
                # if chest_ammount == 25:
                #     chest = Chest(x,height,z)
        self.toggle_menu()
    
    def save_game(self, ):
        with open("savings", "wb") as f:
            pickle.dump(self.player.position, f)
            pickle.dump(len(Block.list),f)
            for block in Block.list:
                pickle.dump(block.position,f) 
                pickle.dump(block.id,f) 
            pickle.dump(len(Tree.list),f)
            for tree in Tree.list:
                pickle.dump(tree.position,f)
                pickle.dump(tree.scale,f)
            pickle.dump(len(Chest.list),f)
            for chest in Chest.list:
                pickle.dump(chest.position,f)
            
    def input (self, key):
        if key == "o":
            self.save_game()
        elif key == "p":
            self.load_game()
        elif key == "escape" and self.start:
            self.toggle_menu()
    
    def load_game(self):
        self.start  = True
        for block in Block.list + Tree.list + Chest.list:
            destroy(block)
        Block.list = []
        Chest.list = []
        Tree.list = []

        try:
            with open("savings", "rb") as f:
                self.player.position = pickle.load(f)
                k = pickle.load(f)
                for i in range(k):
                    block_pos = pickle.load(f)
                    Block.id = pickle.load(f) 
                    block = Block(position=block_pos)
                k_tree = pickle.load(f)
                for i in range (k_tree):
                    tree_position = pickle.load(f)
                    tree_scale = pickle.load(f)
                    tree = Tree(*tree_position)
                    tree.scale = tree_scale

                k_chest = pickle.load(f)   
                for i in range (k_chest):
                    chest_position = pickle.load(f)
                    chest = Chest(*chest_position)
            self.toggle_menu()
        except:
            self.new_game()
        
              
window.exit_button.visible =False
window.fps_counter.visible = False
window.entity_counter.visible = False
window.collider_counter.visible = False


# ground = Entity(model="plane", collider='box', texture="grass",
#                 scale=64, texture_scale=(4, 4))
game = Controller()
# game.new_game()
app.run()
