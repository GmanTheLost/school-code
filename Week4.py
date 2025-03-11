# werewolf = {
#     "name": "Werewolf",
#     "health": 250,
#     "attack_power": 40,
#     "defense": 30,
#     "speed": 35
# }

class Monster:
    
    def __init__(self, name, health, attack_power, defense, speed): # init short for initilazing 
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.speed = speed
    
    def __str__(self):
        return f"{self.name} (Monster)"
    
    def attack(self, opponent):
        """These are notes because I like notes"""

        damage = max(0, self.attack_power - opponent.defense)
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        opponent.take_damage(damage)
    
    def take_damage(self, damage):
        """Reduce the health when damage is recieved from an attack"""
        
        self.health -= damage # self.health = self.health - damage
        print(f"{self.name} now has {self.health} health remaining!")\

    def is_defeated(self):
        """Check if the monster is defeated"""
        return self.health <= 0
# Creating an instance of the class; also known as the object
werewolf = Monster(name="Werewolf", health=250, attack_power=400, defense=30, speed=35)
goblin = Monster(name="Goblin", health=75, attack_power=10, defense=5, speed=15)

werewolf.attack(goblin)