import time
import random


items = []


def sleepy_print(str):
    time.sleep(2)
    print(str)


def valid_answer():
    while True:
        ans = ""
        ans = input("(Please enter 1 or 2) Your input:")
        if ans == "1" or ans == "2":
            break
        else:
            sleepy_print("I only understand 1 or 2")
    return ans


def switch_hub(select, one, two):
    if select() == "1":
        return one(items)
    else:
        return two(items)


def end(items):
    return


def start_craw(items):
    sleepy_print("Play the craw game?")
    sleepy_print("1. Sure!\n"
                 "2. Nope!")
    switch_hub(valid_answer, craw_game, hotel_entrance)


def craw_game(items):
    prize = ""
    prize = random.choice(["Ugly medal", "None"])
    sleepy_print("You inserted a coin to the craw machine")
    sleepy_print("Boop... You just got ")
    sleepy_print(f"{prize}...")
    if prize == "Ugly medal":
        items.append("Ugly medal")
        sleepy_print("You: I guess I just won...?")
        sleepy_print("(Wow... This is ugly...)")
        sleepy_print("You: let's go to the entrance now")
        hotel_entrance(items)
    else:
        sleepy_print("You lost..")
        start_craw(items)


def slope(items):
    items.clear()
    sleepy_print("You came to ski with Mikiko.  The snow is shinning.")
    sleepy_print("Mikiko looks tired.")
    sleepy_print("You said to her...")
    sleepy_print(
        "1. We had fun today, let's go to the hotel before it gets dark.\n"
        "2. Let's get back to the lift again for another round!")
    switch_hub(valid_answer, hotel_front, hotel_entrance)


def hotel_front(items):
    sleepy_print("We arrived at the hotel in the middle of the mountain.")
    sleepy_print("There was an old craw game machine making"
                 " nostalgic melody outside of the hotel.")
    sleepy_print("Hotel looked empty and I had a bad feeling.")
    sleepy_print("Mikiko: I don't see anyone.")
    sleepy_print("Mikiko: We should check inside of the hotel.")
    sleepy_print("You told her...")
    sleepy_print("1. Wait..Let me play with this craw game first.\n"
                 "2. Sure, I will go and check.  You should stay here!")
    switch_hub(valid_answer, craw_game, hotel_entrance)


def hotel_entrance(items):
    sleepy_print("...At the hotel entrance.....")
    sleepy_print("It was already dark")
    sleepy_print("(Something is strange....)")
    sleepy_print("(Everyone is ..dead....)")
    sleepy_print("I noticed someone is standing"
                 " behind me with a sharp knife and...")
    sleepy_print("coming to stub me! ")
    if "Ugly medal" in items:
        return good_end()
    else:
        return bad_end()


def bad_end():
    sleepy_print("The next moment, I saw Mikiko was"
                 " covering her face with bloody hands..")
    sleepy_print("You: Mi..ki..ko..?")
    sleepy_print(".....")
    sleepy_print(".....")
    sleepy_print("The end")
    sleepy_print("Starting a new story?")
    sleepy_print("1. Yes\n"
                 "2. No")
    switch_hub(valid_answer, slope, end)


def good_end():
    sleepy_print("Luckily the ugly medal in your chest"
                 " pocket stopped the knife.")
    sleepy_print("The next moment, I saw Mikiko kicked him"
                 " at his head and he fall down.")
    sleepy_print("He did not move anymore.")
    sleepy_print("Mikiko: We are safe now.")
    sleepy_print(".....")
    sleepy_print(".....")
    sleepy_print("Congratulations! You survived this game.")
    sleepy_print("Starting a new story?")
    sleepy_print("1. Yes\n"
                 "2. No")
    switch_hub(valid_answer, slope, end)


slope(items)
