from ursina import *



class ButtonMenu(Button):
    def __init__(self, text='',  **kwargs):
        super().__init__(text, ignore_paused = True,scale = (0.8,0.1),texture = "assets/blocks/Andesite_(texture)_JE3_BE2.png", texture_scale = (0.5, 0.5), model= "quad", radius=0.1, origin=(0,0),  text_size=1, color= color.white, collider='box', highlight_scale=1, pressed_scale=1.05, **kwargs)


class Menu(Entity):
    def __init__(self, game, **kwargs):
        super().__init__(parent= camera.ui, ignore_paused=True, **kwargs)
        self.bg = Sprite(parent = self, texture = "assets/wallpaperflare.com_wallpaper.jpg", scale = 0.1)
        Text.default_font = "assets/font/minecraft.ttf"
        self.title = Text(parent = self, text = "Blockcraft",scale = 5,origin=(0,0),x=0,y=0.30,color = color.rgb(0,0,0))
        self.title2 = Text(parent = self, text = "Blockcraft",scale = 4.9,origin=(0,0),x=0.01,y=0.295,color = color.rgb(233,233,233))

        self.button1 = ButtonMenu(text = "Save", on_click= game.save_game, y=0.01, parent = self)
        self.button_2  = ButtonMenu(text = "Load Game",on_click = game.load_game,y = 0.15, parent = self)
        self.button_3 = ButtonMenu(text= "New Game",on_click = game.new_game,y=-0.13,  parent = self)
        self.button_4 = ButtonMenu(text = "Escape",on_click  = application.quit,y = -0.27,parent = self)

