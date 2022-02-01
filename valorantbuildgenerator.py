from purchases import Purchase, purchase_list, agent_list
import pytesseract
import pyautogui
import random
import time
import math
import os

# Todo List
# Todo > have [ be the key to generate the loadout and ss the game and whatnot
# Todo > use template matching to find the money symbol and cut off all of the image on the left of its right side



def get_current_agent():
    current_agent = input("What agent are you currently playing?\n").lower().capitalize()

    # alter KAY/O's name to conform with the Agent.name attr in agent_list
    if current_agent == "Kay/o":
        current_agent = current_agent.upper()

    return current_agent


def get_affordable_items(budget, items):
    affordable_items = []

    for item in items:
        if item.price <= budget:
            affordable_items.append(item)

    return affordable_items


def select_random_item(types, item_list, budget):
    target_items = [item for item in item_list if item.item_type in types]  # get all the items that have the correct type
    quantity = 1

    if not target_items:  # If the list is empty
        return None

    choice = random.choice(target_items)

    # If an ability is chosen, calculate how many to purchase
    if choice.item_type == "ability" and choice.buycap != 1:
        max_purchase = math.floor(budget/choice.price)
        if max_purchase > choice.buycap:
            max_purchase = choice.buycap

        if (buy_num := random.randint(1, max_purchase)) != 1:
            quantity = buy_num

    # Potentially don't purchase anything, makes for more interesting builds
    if random.randint(1, 100) < 20:
        return None

    return Purchase(choice, quantity)


def determine_purchase_strategy(budget):
    if budget < 1200:
        return 1
    else:
        return 0


def remove_random_chars(string):
    numeric_filter = filter(str.isdigit, string)
    numeric_string = "".join(numeric_filter)
    return int(numeric_string)


def screenshot_money():
    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

    money_offset = (235, 123)
    money_size = (115, 30)

    pyautogui.screenshot("money.png", region=(money_offset[0], money_offset[1], money_size[0], money_size[1]))

    money_ = pytesseract.image_to_string("money.png", config='--psm 7', timeout=10)

    money = remove_random_chars(money_)
    print(money)

    return money


def generate_random_loadout():
    budget = screenshot_money()

    purchase_schemes = [
        [["shield"], ["ability"], ["ability"], ["rifle", "shotgun", "smg", "sniper", "heavy"], ["pistol"]],  # standard
        [["pistol"], ["ability"], ["ability"], ["shield"]]]  # eco
    loadout = []

    purchase_scheme = purchase_schemes[determine_purchase_strategy(budget)]  # Figure out whether to eco or not
    items = purchase_list.copy()  # Create a temporary copy of purchase_list

    for i in purchase_scheme:
        can_afford = get_affordable_items(budget, items)
        purchase = select_random_item(i, can_afford, budget)

        # If a purchase has been made
        if purchase is not None:
            items.remove(purchase.item)

            # This is for abilities with a high buy cap
            if purchase.quantity > 1:
                loadout.append(f"{purchase.item.name} x {purchase.quantity}    : {purchase.item.price*purchase.quantity}")
            else:
                loadout.append(f"{purchase.item.name}    : {purchase.item.price}")

            budget -= (purchase.item.price * purchase.quantity)  # Take the price of the purchase off of the budget

    return loadout


def add_abilities_to_purchases(current_agent):
    for agent in agent_list:
        if agent.name == current_agent:
            purchase_list.append(agent.ability_1)
            purchase_list.append(agent.ability_2)


def main():
    current_agent = get_current_agent()
    add_abilities_to_purchases(current_agent)

    os.system("cls")

    while True:
        round_start = input("enter something when the round starts")
        time.sleep(5)
        loadout = generate_random_loadout()

        os.system("cls")

        for item in loadout:
            if item != "":
                print(item)


main()
