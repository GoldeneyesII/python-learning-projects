import json
import random
from abc import ABC, abstractmethod

class Serialization:

    def to_dict(self):
        pass

class Character(Serializable, ABC):
    def __init__(self, name, health, attack, defense, mana=0):
        self.name = name
        self.max_health = health
        self.health = health
        self.base_attack = attack
        self.base_defense = defense
        self.max_mana = mana
        self.mana = mana
        self.level = 1
        self.experience = 0

    def take_damage(self, damage):
        # Calculate damage after defense
        actual_damage = max(1, damage - self.base_defense)
        self.health = max(0, self.health - actual_damage)
        return actual_damage

    def is_alive(self):
        return self.health > 0

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)

    @abstractmethod
    def special_ability(self, target=None):
        """Each character class must implement their special ability"""
        pass

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name} (HP: {self.health}/{self.max_health}, MP: {self.mana}/{self.max_mana})"
