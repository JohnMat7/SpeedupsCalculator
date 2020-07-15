def speedups_calc():
    print("Enter the amount of following speeds you have   :")
    mins_5 = int(input("Amount of 5 mins :"))
    mins_10 = int(input("Amount of 10 mins :"))
    mins_15 = int(input("Amount of 15 mins :"))
    mins_30 = int(input("Amount of 30 mins :"))
    hr_1 = int(input("Amount of 1 hour :"))
    hr_3 = int(input("Amount of 3 hour   :"))
    hr_8 = int(input("Amount of 8 hour   :"))
    hr_15 = int(input("Amount of 15 hour  :"))
    hr_24 = int(input("Amount of 24 hour  :"))
    days_3 = int(input("Amount of 3 days  :"))
    days_7 = int(input("Amount of 7 days  :"))
    days_30 = int(input("Amount of  30 days  :"))
    # CALCULATOR
    total_hours = (mins_5*5*0.0166667)+(mins_10*10*0.0166667)+(mins_15*15*0.0166667)+(mins_30*30*0.0166667) + (hr_1) + \
        (hr_3*3) + (hr_8*8) + (hr_15*15) + (hr_24*24) + \
        (days_3*3*24)+(days_7*7*24)+(days_30*30*24)
    total_days = total_hours/24
    print(f"total_days are   :{total_days}")
    return


speedups_calc()
# 192days research in CARN ALT          date : 29th June 2020
# 79 DAYS normal speeds in carn alt
