# Isaac Infante
# Slot Machine
# A functioning slot machine for you to gamble all your money away

#


import time
import random

#load and save function
def load_transactions(filename):
    transactions = []
    try:
        with open(filename, "r") as file:
            for line in file:
                wager, result, profit = line.strip().split(" | ")
                transactions.append({
                    "wager": int(wager),
                    "result": int(result),
                    "profit": int(profit)
                })
    except FileNotFoundError:
        pass
    return transactions


def save_transaction(filename, wager, result):
    profit = result - wager
    with open(filename, "a") as file:
        file.write(f"{wager} | {result} | {profit}\n")


def show_summary(filename):
    transactions = load_transactions(filename)
    if not transactions:
        print("\nNo transaction history found.")
        return
    total_profit = sum(t["profit"] for t in transactions)
    wins = sum(1 for t in transactions if t["profit"] > 0)
    losses = sum(1 for t in transactions if t["profit"] < 0)
    biggest_win = max(transactions, key=lambda t: t["profit"])
    biggest_loss = min(transactions, key=lambda t: t["profit"])

    print("\n===== TRANSACTION SUMMARY =====")
    print(f"Total spins: {len(transactions)}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Total profit: {total_profit}")
    print(f"Biggest win: +{biggest_win['profit']} (Wagered {biggest_win['wager']})")
    print(f"Biggest loss: {biggest_loss['profit']} (Wagered {biggest_loss['wager']})")
    print("================================\n")


#main function/slotmachine
def slotmachine():
    slots = ["7", "♥", "♦", "☆"]
    net_balance = 0
    credits = 1000
    history_file = "slot_history.txt"

    print("Welcome to slot machine!")
    time.sleep(1)
    print("If your first two slots are the same, but you are not a winner, you get a FREE re-roll!")
    time.sleep(3)
    print("You start with 1000 credits!")
    time.sleep(2)

    play = input("Enter 's' to play or 'h' to view history: ")
    if play.lower() == "h":
        show_summary(history_file)
        return
    if play.lower() == "s":

        while True:
            try:
                wager = int(input(f"How many credits would you like to wager (Available: {credits})?: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if wager <= 0:
                print("Wager must be greater than 0.")
                continue
            if wager > credits:
                print("You cannot wager more credits than you have!")
                continue
            credits -= wager

            #first roll
            slot_one = random.choice(slots)
            slot_two = random.choice(slots)
            slot_three = random.choice(slots)
            print("...")
            time.sleep(1)
            print(f"| {slot_one} | . | . |")
            time.sleep(1)
            print(f"| {slot_one} | {slot_two} | . |")
            time.sleep(1)
            print(f"| {slot_one} | {slot_two} | {slot_three} |")
            #free re-roll
            if slot_one == slot_two and slot_two != slot_three:
                print("Two in a row! You get a FREE re-roll!")
                time.sleep(1)
                slot_three = random.choice(slots)
                print(f"Re-roll result: | {slot_one} | {slot_two} | {slot_three} |")
            # JACKPOT
            if slot_one == slot_two == slot_three == "7":
                winnings = wager * 17
                credits += winnings
                net_balance += (winnings - wager)
                print("JACKPOT")
                time.sleep(1)
                print("JACKPOT")
                time.sleep(1)
                print("JACKPOT")
                time.sleep(1)
                print(f"You win {winnings} credits!")
                save_transaction(history_file, wager, winnings)
            #normal win
            elif slot_one == slot_two == slot_three:
                winnings = wager * 5
                credits += winnings
                net_balance += (winnings - wager)
                print(f"Winner! You win {winnings} credits!")
                save_transaction(history_file, wager, winnings)
            #loss
            else:
                net_balance -= wager
                print(f"You lost {wager} credits.")
                save_transaction(history_file, wager, 0)
            #out of credits
            if credits <= 0:
                print("You are out of credits! Game over.")
                break
            #play again
            play_again = input("Play again? (y/n): ").lower()
            if play_again != "y":
                print(f"Final credits: {credits}")
                print(f"Net balance: {net_balance}")
                print("Thanks for playing!")
                break


#simulation
def simulate_spin(wager):
    slots = ["7", "♥", "♦", "☆"]
    slot_one = random.choice(slots)
    slot_two = random.choice(slots)
    slot_three = random.choice(slots)
    if slot_one == slot_two and slot_two != slot_three:
        slot_three = random.choice(slots)
    if slot_one == slot_two == slot_three == "7":
        return wager * 17
    elif slot_one == slot_two == slot_three:
        return wager * 5
    else:
        return -wager

def simulate_1000_spins():
    credits = 100000
    net_balance = 0
    wager = 100
    for _ in range(1000):
        if credits < wager:
            break
        credits -= wager
        result = simulate_spin(wager)
        credits += max(result, 0)
        net_balance += result
    return credits, net_balance

#main
slotmachine()
#final_credits, net = simulate_1000_spins()
#print("After 1000 simulated spins:")
#print(f"Final credits: {final_credits}")
#print(f"Net balance: {net}")


