
def msg(checkerboard,flagNum):
    print("\033[1;37;41m---------Gobang(simple vision)---------\033[0m")
    print("\033[1;37;41m-----------------------")
    print("  1  2  3  4  5  6  7  8  9 ")
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

def main():
    finish=False
    flagNum=1
    flagch="*"
    x=0
    y=0
    checkerboard = []
    for i in range(9):
        checkerboard.append([])
        for j in range(9):
            checkerboard[i].append("-")

    while finish != True:
        print("\033[1;37;41m---------Gobang(simple vision)---------\033[0m")
        print("\033[1;30;46m-------------------------------")
        print("  1  2  3  4  5  6  7  8  9 ")
        for i in range (len(checkerboard)):
            print(chr(i+ord("A"))+" ", end="")
            for j in range(len(checkerboard[i])):
                print(checkerboard[i][j]+ " ", end= " ")
            print()
        print("-------------------------------\033[0m")

        if flagNum==1:
            flagch="*"
            print("\033[1;30;43m Please * enter the coordinator(ex:A1): \033[0m",end=" ")
        else:
            flagch="o"
            print("\033[1;30;42m Please o enter the coordinator(ex:I5): \033[0m",end=" ")

        str=input()
        ch=str[0]
        x=ord(ch)-65
        y=int(str[1])-1

        if (x<0 or x>=9 or y<0 or y>=9):
            print("\033[31m***The coordinator is invalid, please enter again!***\033[0m")
            continue

        if checkerboard[x][y]=="-":
            checkerboard[x][y] = flagch
        else:
            print("\033[31m*********This point has been localed, please select another point.")
            continue

        if (y-4>=0):
            if checkerboard[x][y-1]==flagch and checkerboard[x][y-2]==flagch and checkerboard[x][y-3]==flagch and checkerboard[x][y-4]==flagch:
                finish=True
                msg(checkerboard,flagNum)

        if (y+4<=9):
            if checkerboard[x][y+1]==flagch and checkerboard[x][y+2]==flagch and checkerboard[x][y+3]==flagch and checkerboard[x][y+4]==flagch:
                finish=True
                msg(checkerboard,flagNum)

        if (x-4>=0):
            if checkerboard[x-1][y]==flagch and checkerboard[x-2][y]==flagch and checkerboard[x-3][y]==flagch and checkerboard[x-4][y]==flagch:
                finish=True
                msg(checkerboard,flagNum)

        if (x+4<=0):
            if checkerboard[x+1][y]==flagch and checkerboard[x+2][y]==flagch and checkerboard[x+3][y]==flagch and checkerboard[x+4][y]==flagch:
                finish=True
                msg(checkerboard,flagNum)

        if (x-4>=0 and y-4>=0):
            if (checkerboard[x-1][y-1]==flagch and checkerboard[x-2][y-2]==flagch and checkerboard[x-3][y-3]==flagch and checkerboard[x-4][y-4]==flagch):
                finish = True
                msg(checkerboard,flagNum)

        if (x+4<=9 and y-4>=0):
            if (checkerboard[x+1][y-1]==flagch and checkerboard[x+2][y-2]==flagch and checkerboard[x+3][y-3]==flagch and checkerboard[x+4][y-4]==flagch):
                finish = True
                msg(checkerboard,flagNum)

        if (x-4>=0 and y+4<=9):
            if (checkerboard[x-1][y+1]==flagch and checkerboard[x-2][y+2]==flagch and checkerboard[x-3][y+3]==flagch and checkerboard[x-4][y+4]==flagch):
                finish = True
                msg(checkerboard,flagNum)

        if (x+4<=9 and y+4<=9):
            if (checkerboard[x+1][y+1]==flagch and checkerboard[x+2][y+2]==flagch and checkerboard[x+3][y+3]==flagch and checkerboard[x+4][y+4]==flagch):
                finish = True
                msg(checkerboard,flagNum)

        flagNum*=-1

main()


