import GameObject


class headpiece(GameObject.GameObject):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.timer = 0

    def render(self, events):
        self.timer -= -1
    
