today=(input("What day is today? \nToday is: "))
match today:
    case 1|"1"|"monday"|"Monday":
        today="monday"
        print(f"Today is {today}")

    case 2|"2"|"tuesday"|"Tuesday":
        today="tuesday"
        print(f"Today is {today}")

    case 3|"3"|"wednesday"|"Wednesday":
        today="wednesday"
        print(f"Today is {today}")

    case 4|"4"|"thursday"|"Thursday":
        today="thursday"
        print(f"Today is {today}")
    case _:
        print("Not programmed yet")