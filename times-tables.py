import time
def timetables(table):
    for counter in range(1,13):
        answer = table*counter
        print(table , "x" , counter , "=" , answer)
        # print(table + "x" + counter + "=" + answer)
    print()

def askTT():
    print("Hello there")
    print("do you know your times tables?")
    print("yes/no")
    answer = input()
    if answer == "yes":
        print("well here you go anyways")
        time.sleep(2)
        for counter in range(1,13):
            timetables(counter)
    else:
        print("so then take these and go revise")
        time.sleep(2)
        for counter in range(1,13):
            timetables(counter)

askTT()
