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
        timetables(1)
        timetables(2)
        timetables(3)
        timetables(4)
        timetables(5)
        timetables(6)
        timetables(7)
        timetables(8)
        timetables(9)
        timetables(10)
        timetables(11)
        timetables(12)
    else:
        print("so then take these and go revise")
        time.sleep(2)
        timetables(1)
        timetables(2)
        timetables(3)
        timetables(4)
        timetables(5)
        timetables(6)
        timetables(7)
        timetables(8)
        timetables(9)
        timetables(10)
        timetables(11)
        timetables(12)

askTT()
