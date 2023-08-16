# def info(weight, start, end):
operator = ["lbs", "pound", "pounds", "kg", "kilo", "kgs", "kilos"]
kilo = ["kg", "kilo", "kgs", "kilos"]
pound = ["lbs", "pound", "pounds"]

def kg_lbs(weight):
    pound = weight * 2.205
    return round(pound, 2)

def lbs_kg(weight):
    kilo = weight / 2.205
    return round(kilo, 2)

def welcome():
    print("              Welcome to THE CONVERTER")
    print("Please Enter the Operator and Weight you wish to Convert")

def info():
    while True:
        print("Possible Operator 'lbs/pound', 'kg/kilo'  ")
        start = input("\nConvert From: ")
        end = input("To: ")
        start = start.lower()
        end = end.lower()
        print("--------------------------------")

        
        if (start in operator) and (end in operator):
            if (start in kilo and end in pound) or (start in pound and end in kilo):
                while True:
                    weight = input(f"How many {start} do you wish to convert: ")
                    try:
                        weight = float(weight)
                        break
                    except ValueError:
                        print("\nPlease Enter a Number")
                        print("--------------------------------")   
                weight = float(weight) 
                break
            else:
                print("Please Input Different Operators")
                print("--------------------------------")     
        else:   
            if start not in operator:
                print(f"Invalid Operator ({start})")
            if end not in operator:
                print(f"Invalid Operator ({end})")
            print("--------------------------------")
    return start, end, weight

def converter(start, end, weight):
    result = 0
    if (start in kilo) and (end in pound):
        result = kg_lbs(weight)
        end = "lbs"
    elif (start in pound) and (end in kilo):
        result = lbs_kg(weight)
        end = "kgs"
    print(f"Result = {result} {end}")

def main():
    welcome()
    while True:
        start, end, weight = info()
        converter(start, end, weight)
        next = input("Do you wish to retry? (y/n): ")
        if next.lower() == "n":
            break
        else:
            print("\n")
            print("--------------------------------")


main()

    