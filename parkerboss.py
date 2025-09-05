from enemy import Enemy

class Parker(Enemy):
    def __init__(self, name, color):
        super().__init__(name)
        self.color=color