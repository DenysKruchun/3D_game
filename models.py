from ursina import *
from random import randint
from settings import BLOCKS_PATH
import os

block_images = []
files = os.listdir(BLOCKS_PATH)
for image in files:
    texture1 = load_texture("assets/blocks/" + image)
    block_images.append(texture1)

print(block_images)
class Block(Button):
    id = 1
    list = []
    def __init__(self, position):
        super().__init__(parent=scene, model="cube",
                         collider='box', texture=block_images[Block.id],
                         color=color.hsv(0, 0, random.uniform(.9, 1.0)),
                         highlight_color=color.gray)
        self.position = position
        self.id = Block.id
        Block.list.append(self)


    def input(self, key):


        if self.hovered:
            if key == "right mouse down":
                destroy(mouse.hovered_entity)
            if key == "left mouse down":
                block = Block(self.position + mouse.normal)
        for i in range (9) :
            if key == str(i):
                Block.id = i



class Tree(Entity):
    def __init__(self, x, y, z ):
        super().__init__(parent=scene, model="assets/minecraft_tree/scene",
                         position=(x, y, z), scale=randint(4, 7),  origin_y=0.5, collider='box')

class Chest(Entity):
    def __init__(self, x, y, z,):
         super().__init__(parent=scene,model = "assets/minecraft_chest/scene",position = (x,y + 0.9 ,z), scale = 0.5,origin_y=0.5, collider = 'box')

