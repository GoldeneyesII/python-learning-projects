import json
import random
from abc import ABC, abstractmethod

class Serializable:

    def to_dict(self):
        pass

class Character(Serializable, ABC):
    def __init__(self, name, health, attack, defense, magic_atk, magic_def, energy=0):
        self.name = name
        self.max_health = 100
        self.health = health
        self.base_attack = attack
        self.base_defense = defense
        self.attack = attack
        self.defense = defense
        self.magic_atk = magic_atk
        self.magic_def = magic_def
        self.max_energy = energy
        self.energy = energy
        self.level = 1
        self.experience = 0
        self.physical_resistance = 0
        self.magical_resistance = 0
        self.resist = 0

    def take_damage(self, damage):
        # Calculate damage after defense
        actual_damage = max(1, damage - self.defense)
        self.health = max(0, self.health - actual_damage)
        return actual_damage
    
    def take_magic_dmg(self, damage):
        # Use this to separate magic damage from physical damage if needed.
        pass
    
    def is_alive(self):
        return self.health > 0

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)

    @abstractmethod
    def special_ability(self, target=None):
        """Each character class must implement their special ability"""
        pass

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name} (HP: {self.health}/{self.max_health}, Energy: {self.energy}/{self.max_energy})"

    def aux_check(self, required):
        return True if self.energy >= required else print(f"Not enough energy")

class Warrior(Character):
    def __init__(self, name, health, attack, defense, energy):
        super().__init__(name, health, attack, defense, attack, defense, energy)
        self.physical_resistance += 10 #Warriors start with physical resistance to disarms.


    def special_ability(self, target=None ):
        """
        Disarm - attempts to disarm the targeted enemy.
        Will finish building once other systems are built fully.
        """
        #Check to see if the target is armed
        #If the target is armed, generate a random number for the disarm value.
        #Generate a random number for the resist value.
        #If the disarm value is greater than the resist value, the target drops the weapon.
        if target is None or not target.is_alive():
            #Optional - disable the ability to select this as an option.
            return "Invalid target"

        if self.energy < 1:
            #Optional - disable the ability to select this as an option.
            return "Not enough energy"

        self.energy -= 1
        # TODO: Implement full disarm when equipment system is ready.
        
        print(f"{self.name} attempts to disarm {target.name}!")
        disarm_val = random.randint(1,20) #Assigning to variable so value can be logged at a later time for debugging.
        return f"Disarm was successful!" if disarm_val > target.resist else f"Disarm failed!"

class Mage(Character):
    def __init__(self, name, health, attack, defense, energy):
        super().__init__(name, health, attack, defense, attack, defense, energy=100)
        self.magical_resistance += 10

    def special_ability(self, target=None):
        """
        Drain - drains the target of life, gaining a percentage back as HP
        """

        min_heal, max_heal = 4, 12
        cost = 5
        if self.aux_check(cost):
            if target is None or not target.is_alive():
                return "Invalid target"
            self.energy -= cost
            
            #Attempt magical attack against target
            damage = random.randint(1,20) + (self.magic_atk - target.__magic_def)
            healing = random.randint(min_heal, max_heal) / 100

            actual_damage = target.take_damage(damage)
            healed = healing * actual_damage
            return healed, actual_damage


class Rogue(Character):
    def __init__(self, name, health, attack, defense, energy):
        super().__init__(name, health, attack, defense, attack, defense, energy)

    def special_ability(self, target):
        """
        Kidney Shot - reduces target's attack and defense slightly
        """

        cost = 2

        if self.aux_check(cost):
            if target is None or not target.is_alive():
                return "Invalid target"
            self.energy -= cost

            #Only succeed if self.attack - target.defense > 0
            #Be more effective based on how much stronger the attack is
            difference = self.attack - target.defense
            if difference <= 0:
                weaken = 0
            elif difference <= 5:
                weaken = random.randint(1,3)
            elif difference <= 10:
                weaken = random.randint(2,5)
            elif difference <= 20:
                weaken = random.randint(4,8)
            else:
                weaken = 9

            if weaken == 0:
                return "You strike at their kidneys, but they are not effected!"

            target.attack -= weaken
            target.defense -= weaken
            return f"You strike the targets kidneys and weaken them by {weaken} points!"
