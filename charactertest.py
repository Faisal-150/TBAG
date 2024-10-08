from character import Enemy 

dave = Enemy("Dave", "A smelly zombie")
dave.describe()

dave.set_conversation("Hi im Dave and totally won't eat your brain")
dave.talk()
dave.set_weakness("Cheese")
print(dave.weakness)

print("what will you fight with?")
fight_with = input("Enter item here: ")
dave.fight(fight_with)
# dave.fight(fight_with)


