while True:
    try:

        rutine = []

        separator = "------------------------------------------------------------------"

        while True:

            def new_rutine():
                rutine.clear()
                while True:
                    work_name = input("If you write 'off' then no value will be added. Else enter the name of your work -> ")
                    if work_name.lower() == "off":
                        break
                    else:
                        time_spent = float(input("Input your time -> "))
                        e = "Work name: " + work_name + " -- Time: " + str(time_spent)
                        rutine.append(e)

            def add_more():
                while True:
                    work_name = input("If you write 'off' then no value will be added. Else enter the name of your work -> ")
                    if work_name.lower() == "off":
                        break
                    else:
                        time_spent = float(input("Input your time -> "))
                        e = "Work name: " + work_name + " ---> Time: " + str(time_spent)
                        rutine.append(e)

            def del_more():
                for i, item in enumerate(rutine):
                    print("")
                    print(i+1, item)

                while True:
                    index = input("If you want to exit this function type 'off', else enter the number you want to remove -> ")
                    if index.lower() == "off":
                        break
                    else:
                        for i, item in enumerate(rutine):
                            print("")
                            print(i+1, item)
                        index = int(index)
                        if 1 <= index <= len(rutine):
                            rutine.pop(index-1)
                            for i, item in enumerate(rutine):
                                print("")
                                print(i+1, item)
                                print("")
                        else:
                            print("Invalid index ❌")

            def all_clear():
                rutine.clear()
                print(separator)
                print("your routine del compitite")
                print(separator)


            command = input(
                "Input your command: (new -> create a new routine) (add -> add more to old routine) "
                "(clear -> delete all) (show -> show the routine) (del -> delete step by step) -> "
            )

            if __name__ == "__main__":

                if command.lower() == "new":
                    new_rutine()
                elif command.lower() == "add":
                    add_more()
                elif command.lower() == "clear":
                    all_clear()
                elif command.lower() == "show":
                    if len(rutine) == 0:
                        print(separator)
                        print("There is no routine in this list 😒")
                        print(separator)
                    else:
                        print(separator)
                        for i in rutine:
                            print(i)
                        print(separator)
                elif command.lower() == "del":
                    del_more()
                else:
                    print("Something is wrong ❌")

    except Exception as e:
        print("Your program crashed:", e)
