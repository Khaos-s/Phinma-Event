class Character:
    def __init__ (self,name,health,damage):
        self.name = name
        self.health = health
        self.damage = damage

    def heal(self, add):
            self.health += add
            print("Adding Health: ", add)

        
    def power_up(self, damage, buffing):
        buffing = damage + 10
        print("powering up", buffing)

    def check_details(self):
            print("Name: ", self.name)
            print("Current Health: ", self.health)
            print("Taken damage: ", self.damage)
            print("")


char = Character("Char", 100, 100)
char.heal(10)
char.power_up(10,10)
char.check_details()
