import random


def take_damage(hp, damage):
    hp = hp - damage

    if hp < 0:
        hp = 0

    return hp


def heal(hp, heal_amount):
    return hp + heal_amount


def choose_action():
    action = int(input("Choose an action: "))
    return action


def perform_action(action, pokemon, target):
    if action == 1:
        if pokemon["paralyzed"]:
            roll = random.randint(1, 100)

            if roll <= 10:
                print("Pokemon is paralyzed and cannot move")
            else:
                target["hp"] = take_damage(target["hp"], damage)
                print("Attack!")
                print(target["hp"])

        else:
            target["hp"] = take_damage(target["hp"], damage)
            print("Attack!")
            print(target["hp"])

    elif action == 2:
        target["paralyzed"] = True
        print("Pokemon is paralyzed")

    elif action == 3:
        if pokemon["heals"] > 0:
            pokemon["hp"] = heal(pokemon["hp"], heal_amount)
            pokemon["heals"] -= 1
            pokemon["paralyzed"] = False

            if pokemon["hp"] > 100:
                pokemon["hp"] = 100

            print("Heal!")
            print(pokemon["hp"])

        else:
            print("No heals left")

    else:
        print("Invalid action")


player = {
    "hp": 100,
    "heals": 3,
    "paralyzed": False
}

enemy = {
    "hp": 100,
    "heals": 3,
    "paralyzed": False
}

damage = 30
heal_amount = 60
player_turn = True


while player["hp"] > 0 and enemy["hp"] > 0:

    if player_turn:
        print("\n--- PLAYER TURN ---")

        action = choose_action()

        perform_action(action, player, enemy)

        player_turn = False

    else:
        print("\n--- ENEMY TURN ---")

        enemy_action = random.randint(1, 3)

        print("Enemy chose:", enemy_action)

        perform_action(enemy_action, enemy, player)

        player_turn = True


if player["hp"] <= 0:
    print("\nPlayer fainted!")
else:
    print("\nEnemy fainted!")