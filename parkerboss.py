from enemy import Enemy

class Parker(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.attack_power = 25
        self.health = 420

    def attack(self):
        if self.health < 100:
            self.attack_power = 80
        elif self.health < 160:
            self.attack_power = 60
        elif self.health < 50:
            print("bro why u ragebaiting")

        return self.attack_power