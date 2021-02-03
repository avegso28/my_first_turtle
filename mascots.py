'''mascot_list = ["Eagles", "Warriors", "Panthers", "Tigers", "Woodmen", "Patriots", "Cougers", "Wildcats", "Knights", "Trojans"]
i1 = input("Should Eagles be where it is? (yes or no only) ")
if i1 == ("yes") :
    print("You are right so far.")
    i2 = input("Should Warriors be where it is? (yes or no only) ")
    if i2 == ("yes"):
        print("You are right so far.")
        i3 = input("Should Panthers be where it is? (yes or no only) ")
        if i3 == ("yes"):
            print("You are right so far.")
            i4 = input("Should Tigers be where it is? (yes or no only) ")
            if i4 == ("yes"):
                print("You are right so far.")
                i5 = input("Should Woodmen be where it is? (yes or no only) ")
                if i5 == ("no"):
                    print("You are right so far. ")
                    mascot_list.pop(4)
                    r1 = input("What should be the replacement? ")
                    if r1 == ("Bulldogs"):
                        print("You are right so far.")
                        mascot_list.insert(4,"Bulldogs")
                        i6 = input("Should Patriots be where it is? (yes or no only) ")
                        if i6 == ("no"):
                            print("You are right so far. ")
                            mascot_list.pop(5)
                            mascot_list.pop(8)
                            r2 = input("What should be the replacement? ")
                            if r2 == ("Trojans"):
                                print("You are right so far.")
                                mascot_list.insert(5,"Trojans")
                                i7 = input("Should Cougers be where it is? (yes or no only) ")
                                if i7 == ("yes"):
                                    print("You are right so far.")
                                    i8 = input("Should Wildcats be where it is? (yes or no only) ")
                                    if i8 == ("yes"):
                                        print("You are right so far.")
                                        i9 = input("Should Knights be where it is? (yes or no only) ")
                                        if i9 == ("yes"):
                                            print("You are right so far.")
                                            i10 = input("Is everything where it should be? (yes or no only) ")
                                            if i10 == ("no"):
                                                print("You are right so far.")
                                                a = input("What should be added? ")
                                                if a == ("Patriots"):
                                                    print("You are right so far.")
                                                    mascot_list.append("Patriots")
                                                    done = input("Is everything where it should be? (yes or no only) ")
                                                    if done == ("yes"):
                                                        print("That is correct and you are now done. The correct list is", mascot_list)
                                                    else:
                                                        print("You are wrong! You are done now. The correct list is", mascot_list)
                                                else:
                                                    print("You are wrong!")
                                            else:
                                                print("You are wrong!")
                                        else:
                                            print("You are wrong!")
                                    else:
                                        print("You are wrong!")
                                else:
                                    print("You are wrong!")
                            else:
                                print("You are wrong!")
                        else:
                            print("You are wrong!")
                    else:
                        print("You are wrong!")
                else:
                    print("You are wrong!")
            else:
                print("You are wrong!")
        else:
            print("You are wrong!")
    else:
        print("You are wrong!")
else:
    print("You are wrong!")'''
'''mascot_list = ["Eagles", "Warriors", "Panthers", "Tigers", "Woodmen", "Patriots", "Cougers", "Wildcats", "Knights", "Trojans"]

print("The current mascot list is", mascot_list)

remove = input("Which mascot is incorrect? ")
remove_index = mascot_list.index(remove)
mascot_list.pop(remove_index)
print("The new list is...", mascot_list)

add = input("Which mascot is missing? ")
add_index = int(input("Where should the missing mascot go? "))
mascot_list.insert(add_index, add)
print("The current mascot list is", mascot_list)

swap1 = input("What is the first mascot that is out of order? ")
swap2 = input("What is the second mascot that is out of order? ")
swap1_index = mascot_list.index(swap1)
swap2_index = mascot_list.index(swap2)

mascot_list.pop(swap2_index)
mascot_list.pop(swap1_index)

mascot_list.insert(swap1_index, swap2)
mascot_list.insert(swap2_index, swap1)

print("The final list is...", mascot_list)'''