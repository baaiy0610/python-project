finish=False
flagNum=1
flagch="*"
x=0
y=0
print("\033[1;37;41m---------Gobang(simple vision)---------\033[0m")

checkerboard = []
for i in range(10):
    checkerboard.append([])
    for j in range(10):
        checkerboard[i].append("-")

print("\033[1;30;46m-------------------------------")
print("  1  2  3  4  5  6  7  8  9  10")
for i in range (len(checkerboard)):
    print(chr(i+ord("A"))+" ", end="")
    for j in range(len(checkerboard[i])):
        print(checkerboard[i][j]+ " ", end= " ")
    print()
print("-------------------------------\033[0m")

def msg():
    print("\033[1;37;41m-----------------------")
    print("  1  2  3  4  5  6  7  8  9  10")
    for i in range(len(checkerboard)):
        print(chr(i+ord("A"))+ " ", end=" ")
        for j in range(len(checkerboard[i])):
            print(checkerboard[i][j]+ " ", end=" ")
        print()
    print("-------------------------------\033[0m")

    if flagNum==1:
        print("\033[32m* is winner! ***\033[0m")
    else:
        print("\033[32mo is winner! ***\033[0m")


