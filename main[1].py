from replit import clear

from art import logo

print(logo)



total_bid = []
#created a function to add another person if there is another bidder
def add_person(person, bid):
  bidding_amount = {}
  bidding_amount["person"] = person
  bidding_amount["bid"] = bid
  total_bid.append(bidding_amount)

secret_aunction = True

while secret_aunction:
  name = input("What is the your name?\n")
  bid_price = int(input("What is your bid?\n$"))
  add_person(person = name, bid = bid_price)
  anyone_else = input("Is there any other bidders? Please type 'yes' or 'no'\n").lower()

  if anyone_else == "no":
    print(f'The winner is\n {max(total_bid, key=lambda x:x["bid"])}')
    secret_aunction = False
  elif anyone_else == "yes":
    clear()