from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.sky import Sky
from ursina.shaders import lit_with_shadows_shader


app = Ursina()

Entity.default_shader = lit_with_shadows_shader


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


for z in range(-8,8):
    for x in range(-8, 8):
        block = Block(position=(x,0,z))

# ground = Entity(model="plane", collider='box', texture="grass",
#                 scale=64, texture_scale=(4, 4))
sky = Sky(texture="sky_sunset")
player = FirstPersonController()
tree = Entity(model = "assets/minecraft_tree/scene", scale =3,  origin_y=0.5)
house = Entity(model = "assets/minecraft_tree/minecraft_house/scene.gltf",scale = 3, origin_y = 0.5)
app.run()
