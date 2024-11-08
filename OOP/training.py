# class Warrior:
#     def __init__(self, name, power):
#       self.name = name
#       self.power = power



# class Pokemon:
#   def __init__(self, name, hp):
#     self.name = name
#     self.hp = hp

#   def take_damage(self):
#     self.hp -= 10
#     if self.hp <= 0:
#         print(f"{self.name} fainted!")

# class Wizard:
#   def __init__(self, name, mana):
#     self.name = name
#     self.mana = mana


#   def cast_spell(self, target):
#     if self.mana > 0:
#       self.mana -= 1
#       print(f"{self.name} casts spell on {target.name}")
#     elif self.mana <= 0:
#       print(f"{self.name} is out of mana!")


# class Fighter:
#   def __init__(self, name, health, strength):
#     self.name = name
#     self.health = health
#     self.strength = strength

#   def attack(self, target):
#     target.health -= self.strength
#     if target.health <= 0:
#       raise Exception(f"{target.name} has been defeated!")


# class Mage:
#   def __init__(self, name, mana, spells):
#     self.name = name
#     self.mana = mana
#     self.spells = spells

#   def cast(self, target):
#     if self.spells > 0:
#       self.spells -= 1
#       target.take_damage()

#     elif self.spells <= 0:
#       raise Exception(f"{self.name} is out of spells!")

#   def take_damage(self):
#     self.mana -= 1
#     if self.mana <= 0:
#       raise Exception(f"{self.name} is dead")


class Song:
  def __init__(self, title, artist):
    self.title = title
    self.artist = artist


class MusicStore:
  def __init__(self, store_name):
    self.name = store_name
    self.songs = []


  def add_song(self, song):