from replit import clear
from art import logo
print(logo)

def bidders(name, bid):
  bidder_details[name] = bid

highest_bid = 0
highest_bidder = ""
another_bidder = 'yes'
bidder_details = {}

while another_bidder == 'yes':
  name = input("What is your name?: ")
  bid = input("What is your bid?:$ ")
  bidders(name, bid)
  another_bidder = str.lower(input("Is there another bidder? Type yes or no\n")) 
  clear()

for bidder in bidder_details:
  if int(bidder_details[bidder]) > int(highest_bid):
      highest_bid = bidder_details[bidder]
      highest_bidder = bidder

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")






