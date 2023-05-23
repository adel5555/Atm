from datetime import date
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Customer,Card
def end_date_checker(end_date):
    current_date = date.today()
    if current_date >= end_date:
        print("logging in.. ")
        return True
    else:
        print("your card is out of date")
        return False

def check_balance(balance, negative, withdrawal, allowed,request):
    if withdrawal <= allowed:
        if balance-withdrawal >= 0:
            balance = balance-withdrawal
            print(" Withdrawal successful, your balance is ;{}".format(balance))
            return True
        else:
            if negative:
                balance = balance-withdrawal
                print("withdrawal successful, your balance now is :{}" .format(balance))
                return True
            else:
                print("Not allowed")
                return False
    else:
        print("the amount you entered is not allowed")
        return False



# card_id = input("enter your card ID:  ")
# # while True:
# #     print(1)
# if check_if_card_id_exist(card_id):
#     info = get_card_info(card_id)
#     if not info["blocked"] and end_date_checker(info["end_date"]):
#         print(1)
#         if atm_password(card_id, info["password"]):
#             print(2)

#             Withdraw = float(input("Enter your Withdraw: "))
#             if check_balance(info["balance"], info["negative"], Withdraw, info["allowed"]):
#                 print(3)
#                 Withdraw_money(card_id, Withdraw, info["balance"])
#     else:
#         if info["blocked"]:
#             print("your card is blocked")
#         else:
#             print("your card is expired")


# else:
#     print("Enter correct card id:  ")
