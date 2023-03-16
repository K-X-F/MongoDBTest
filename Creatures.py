import os
from random import randint, sample
import logging

from mongoengine import *
from filler_creatures import creatures,abilities

logging.basicConfig(level=logging.DEBUG)

class Ability(Document):
    name = StringField(required=True, unique=True)
    effect_stat = IntField()
    effect_status = StringField()

    description = StringField()

    meta = {'strict': False}

class Creature(Document):
    name = StringField(required=True, unique=True)

    image = StringField()


    hp = IntField(default=50, required=True)
    attack = IntField(required=True)
    defense = IntField(required=True)
    speed = IntField(required=True)
    ability = ReferenceField(Ability)
    description = StringField()
    lore = StringField()

    meta = {'strict': False}

    def __repr__(self):
        ability_name = self.ability.name if self.ability else "NO ability yet"
        return f"<Creature {self.name} - Atk {self.attack}: {ability_name}>"
if os.getenv("USE_LOCAL"):
    connect("Creatures")
    logging.debug("Running on cloud database")
else:

    connect(host=os.getenv("CREATURE_DEN_DATABASE_URL"))
    logging.debug("Running on local database")
    # ojala my internet fuera asi

Creature.drop_collection()
Ability.drop_collection()

#my code goes here

a = Ability(name="brave", effect_stat=10)

c = Creature(name="foxexox", hp = 30,image="772",speed = 50,attack=25,defense=10,description="fox like creature that thrives in wooded areas")

a.save()
c.ability = a
c.save()

a = Ability(name="cowerdly", effect_stat=-15)

c = Creature(name="amogus", hp = 40,image="730",speed = 70,attack=20,defense=15,description="A geko like creaturesthat likes to fight in water")

a.save()
c.ability = a
c.save()

a = Ability(name="fire breath", effect_status="burn")

c = Creature(name="pepurn", hp = 80,image="635",speed = 10,attack=80,defense=55,description="oink oink is all this creature says")

a.save()
c.ability = a
c.save()

a = Ability(name="blurb", effect_stat=20)

c = Creature(name="guber", hp = 20,image="549",speed = 45,attack=20,defense=15,description="fast fish like creature, likes to nibble feet")

a.save()
c.ability = a
c.save()

a = Ability(name="bulky", effect_stat=30)

c = Creature(name="big boy", hp = 100,image="322",speed = 5,attack=100,defense=155,description="his muscles are soo big that they defy the laws of life")

a.save()
c.ability = a
c.save()

a = Ability(name="little", effect_stat=5)

c = Creature(name="ping", hp = 25,image="175",speed = 15,attack=10,defense=15,description="the smallest of the 3 brothers")

a.save()
c.ability = a
c.save()

a = Ability(name="medium", effect_stat=10)

c = Creature(name="pingi", hp = 30,image="176",speed = 30,attack=20,defense=25,description="the middle brother of the 3 brothers")

a.save()
c.ability = a
c.save()

a = Ability(name="big", effect_stat=20)

c = Creature(name="pingiling", hp = 50,image="177",speed = 40,attack=40,defense=40,description="the biggest brother of the 3 brothers")

a.save()
c.ability = a
c.save()

a = Ability(name="yummy", effect_status="poison")

c = Creature(name="strawbrr", hp = 25,image="139",speed = 60,attack=20,defense=30,description="this is the only creature that can be eating, only presitine chef can cook this ")

a.save()
c.ability = a
c.save()

a = Ability(name="flirty", effect_stat=5)

c = Creature(name="gaaimy", hp = 15,image="100",speed = 45,attack=10,defense=20,description="Watch out he is coming for you, BE MY VALENTINE!!!")

a.save()
c.ability = a
c.save()







# Genereting filler creatures

# find alredy used images
pics_already_used = Creature.objects().distinct("image")

all_pics = [str(n) for n in range(1, 829)]

unused_pics = list(set(all_pics).difference("image"))

for each_filler_creature,each_ability in zip(creatures,abilities):

    creature_name = each_filler_creature
    ability_name = each_ability

    creature_description = creatures[creature_name]["description"]
    creature_lore = creatures[creature_name]["lore"]
    ability_description = abilities[ability_name]

    hp = randint(1, 100)
    attack = randint(1, 100)
    defense = randint(1,100)
    speed = randint(1, 100)
    image = sample(unused_pics, 1)[0]

    c = Creature(name=creature_name, description=creature_description,hp=hp,attack=attack,
                 defense=defense, speed=speed, lore=creature_lore,image=image)

    a = Ability(name=ability_name, description=ability_description)

    a.save()
    c.ability = a
    c.save()


    pass
pass
