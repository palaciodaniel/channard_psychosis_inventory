from packages.channard_questions import channard_items

def channard_run():

    """
    Executes Channard's Psychosis Inventory
    and stores the input of every chosen option.
    
    :return: List of chosen options.
    """

    choices = {}
    subchoices = {}
    i = 0

    while i < len(channard_items):

        print("-"*10, "\n")
        print("Item " + str(i + 1) + ": " + str(channard_items[i]), "\n")

        user_input = input("ANSWER: ")

        if (i == 15) or (i == 17):

            user_input = user_input.upper()

            if user_input not in ["0", "1A", "1B", "2A", "2B", "3A", "3B"]:
                print("ERROR: Wrong input. Please retry.")
                continue

            elif len(user_input) == 2:
                subchoices[i + 1] = user_input

            print("\n")
            choices[i + 1] = int(user_input[0])
            i += 1
            continue

        elif user_input not in ["0", "1", "2", "3"]:
            print("ERROR: Wrong input. Please retry.")
            print("\n")
            continue

        print("\n")
        choices[i + 1] = int(user_input)
        i += 1

    return choices, subchoices