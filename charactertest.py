from character import Enemy 

dave = Enemy("Dave", "A dangerous robot")
dave.describe()

dave.set_conversation("Hi im Dave I want to fight you")
dave.talk()
dave.set_weakness("fire")
print(dave.weakness)

print("what will you fight with?")
fight_with = input("Enter item here: ")
dave.fight(fight_with)