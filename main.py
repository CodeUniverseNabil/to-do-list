while True:
    try:

        rutine = []

        separator = "------------------------------------------------------------------"

        while True:

            def new_rutine():
                with open("all_list.txt","w") as f:
                    f.write("")
                rutine.clear()
                while True:
                    work_name = input("If you write 'off' then no value will be added. Else enter the name of your work -> ")
                    if (work_name.lower()).strip() == "off":
                        break
                    else:
                        time_spent = float(input("Input your time -> "))

                        e = "Work name: " + work_name + " -- Time: " + str(time_spent)
                        rutine.append(e)
                            
                        # for i ,f in enumerate(rutine):
                        with open("all_list.txt","a") as f:
                            f.write(f"{str(e)}\n")

            def add_more():
                while True:
                    work_name = input("If you write 'off' then no value will be added. Else enter the name of your work -> ")
                    if work_name.lower() == "off":
                        break
                    else:
                        time_spent = float(input("Input your time -> "))
                        e = "Work name: " + work_name + " ---> Time: " + str(time_spent)
                        rutine.append(e)
                        with open("all_list.txt","a") as f:
                            f.write(f"{str(e)}\n")
                        

            def del_more():
                    # file=[]
                with open("all_list.txt","r") as f:
                    file=f.readlines()


                print(separator)
                for i, item in enumerate(file):
                    print(i+1, item)
                   
                print(separator)
                while True:

                    try:
                        index = input("If you want to exit this function type 'off', else enter the number you want to remove -> ")
                        if (index.lower()).strip() == "off":
                            break
                            
                        else:    
                            print(separator)
                            print(separator)
                            index = int(index)
                            with open("all_list.txt","r") as f:
                                file=f.readlines()
                            for i, item in enumerate(file):
                                print("")
                                print(i+1, item)
                                        # for i ,item in enumerate()
                            if 1 <= index <= len(file):
                                file.pop(index-1)
                                print(separator)
                                for i, item in enumerate(file):
                                    
                                    print(i+1, item)
                                print(separator)
                                    

                                with open("all_list.txt","w") as f:
                                    f.write("")

                                with open("all_list.txt","a") as f:
                                    for i in (file):
                                        f.write(i)
                    except :
                        print("please input real number of list")





            def all_clear():
                rutine.clear()
                print(separator)
                print("your routine del compitite")
                print(separator)
                with open("all_list.txt","w") as f:
                    f.write("")


            command = input(
                "Input your command: (new -> create a new routine) (add -> add more to old routine) "
                "(clear -> delete all) (show -> show the routine) (del -> delete step by step) -> "
            )

            if __name__ == "__main__":

                if (command.lower()).strip() == "new":
                    new_rutine()
                elif (command.lower()).strip() == "add":
                    add_more()
                elif (command.lower()).strip() == "clear":
                    all_clear()
                elif (command.lower()).strip() == "show":
                    showa=[]
                    with open("all_list.txt","r") as f:
                        showa=f.readlines()
                    if len(showa) == 0:
                        print(separator)
                        print("There is no routine in this list 😒")
                        print(separator)
                    else:
                        print(separator)
                        with open("all_list.txt","r") as f:
                            e=f.read()
                            print(e)
                        print(separator)
                elif command.lower() == "del":
                    del_more()
                else:
                    print("Something is wrong ❌")

    except Exception as e:
        print("Your program crashed:", e)
