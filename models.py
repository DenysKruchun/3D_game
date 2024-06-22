from ursina import *
from random import randint


class Block(Button):
    def __init__(self, position):
        super().__init__(parent=scene, model="cube",
                         collider='box', texture="grass",
                         color=color.hsv(0, 0, random.uniform(.9, 1.0)),
                         highlight_color=color.rgb(111, 112, 111))
        self.position = position

    def input(self, key):
        if self.hovered:
            if key == "right mouse down":
                destroy(mouse.hovered_entity)
            if key == "left mouse down":
                block = Block(self.position + mouse.normal)


class Tree(Entity):
    def __init__(self, x, y, z ):
        super().__init__(parent=scene, model="assets/minecraft_tree/scene",
                         position=(x, y, z), scale=randint(4, 7),  origin_y=0.5, collider='box')

class Chest(Entity):
    def __init__(self, x, y, z,):
         super().__init__(parent=scene,model = "assets/minecraft_chest/scene.gltf",position = (x,y + 0.9 ,z), scale = 0.5, collider = 'box')

