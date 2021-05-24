import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro(enemyCreature, initialItem):
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemyCreature} is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(f"In your hand you hold your trusty (but not very "
                f"effective) {initialItem}.\n")


def valid_number_input(prompt, option1, option2):
    while True:
        response = input(prompt)

        if response == option1 or response == option2:
            break
        else:
            print_pause("Try again.")

    return response


def valid_text_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()

        if option1 in response or option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")

    return response


def field(enemyCreature, initialItem, items, advancedItem):
    # Things that happen when the player runs back to the field
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print("What would you like to do?")

    option1 = '1'
    option2 = '2'

    response = valid_number_input("(Please enter 1 or 2).\n", option1, option2)

    if response == option1:
        house(enemyCreature, initialItem, items, advancedItem)
    elif response == option2:
        cave(enemyCreature, initialItem, items, advancedItem)


def cave(enemyCreature, initialItem, items, advancedItem):
    # Things that happen to the player goes in the cave
    print_pause("You peer cautiously into the cave.")

    if initialItem in items:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of "
                    "Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword with"
                    " you.")

        items.clear()
        items.append(advancedItem)
    elif advancedItem in items:
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")

    print_pause("You walk back out to the field.\n")

    field(enemyCreature, initialItem, items, advancedItem)


def house(enemyCreature, initialItem, items, advancedItem):
    # Things that happen to the player in the house
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens and out steps "
                f"a {enemyCreature}.")
    print_pause(f"Eep! This is the {enemyCreature}'s house!")
    print_pause(f"The {enemyCreature} attacks you!")

    if initialItem in items:
        print_pause("You feel a bit under-prepared for this, what with only "
                    "having a tiny dagger.")

    option1 = '1'
    option2 = '2'

    response = valid_number_input("Would you like to (1) fight or (2) run "
                                  "away?\n", option1, option2)

    if response == option1:
        fight(enemyCreature, initialItem, items, advancedItem)
    elif response == option2:
        print_pause("You run back into the field. Luckily, you don't seem to "
                    "have been followed.\n")
        field(enemyCreature, initialItem, items, advancedItem)


def fight(enemyCreature, initialItem, items, advancedItem):
    # Things that happen when the player fights
    if initialItem in items:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {enemyCreature}.")
        print_pause("You have been defeated!")

        play_again()
    elif advancedItem in items:
        print_pause(f"As the {enemyCreature} moves to attack, you unsheath "
                    "your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand as you "
                    "brace yourself for the attack.")
        print_pause(f"But the {enemyCreature} takes one look at your shiny new"
                    " toy and runs away!")
        print_pause(f"You have rid the town of the {enemyCreature}. "
                    "You are victorious!")

        play_again()


def play_again():
    print_pause("GAME OVER\n")

    option1 = 'y'
    option2 = 'n'

    response = valid_text_input("Would you like to play again? (y/n)\n",
                                option1, option2)

    if option1 in response:
        print_pause("Excellent! Restarting the game ...")

        play_game()
    elif option2 in response:
        print("Thanks for playing! See you next time.")
        return


def play_game():
    enemyCreatures = ['wicked fairie', 'pirate', 'troll', 'dragon']
    enemyCreature = random.choice(enemyCreatures)
    initialItem = 'dagger'
    advancedItem = 'sword'
    items = [initialItem]

    intro(enemyCreature, initialItem)
    field(enemyCreature, initialItem, items, advancedItem)


play_game()
