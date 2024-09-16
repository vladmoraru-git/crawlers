import datetime
import django

user_input = input("enter goal seperated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

dateline_date = (datetime.datetime.strptime(deadline, "%d.%m.%Y"))
today_date = (datetime.datetime.today())

diff = dateline_date - today_date

print(f"You have {diff} days left to learn {goal}!")
