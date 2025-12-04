#match is like switch in js

day = "Tuesday"
match day:
    case "Monday":
        print("It's Monday!")
    case "Tuesday":
        print("It's Tuesday!")
    case "Wednesday":
        print("It's Wednesday!")
    case "Thursday":
        print("It's Thursday!")
    case "Friday":
        print("It's Friday!")
    case "Saturday":
        print("It's Saturday!")
    case "Sunday":
        print("It's Sunday!")
    case _:
        print("Invalid day!")


weekday = 2
match weekday:
    case 1 | 2 | 3 | 4 | 5:
        print("It's a working day.")
    case 6 | 7:
        print("It's a weekend.")