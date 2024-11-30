while True:
    #inputs
    cost = input("Enter in the total cost: ")
    tip = input("Enter the tip percentage: ")
    amountOfPpl = input("Enter the amount of people paying: ")
    


    # Calculate the total cost using this formula (Cost + Tip) / The amount of people
    try:
        ttlCost = (float(cost) + float(tip)) / float(amountOfPpl)
        print(ttlCost)
        break
    except ValueError:
        print("Please enter a float")
    except TypeError:
        print("Please enter a float")

