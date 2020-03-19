import random
restart="Y"
while restart=="Y" or restart=="y":
    # showing user where to apply X
    board = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]
             ]
    while True:
        try:
            usr=int(input("\t\t\t +++++++++++[ WELCOME ]+++++++++++\n+++++++++++++++[ Heads or Tails press 1 or Head and 2 for Tails ]++++++++++++\n --> "))
            break
        except Exception:
            print("+++++++++++++++++++[ WRONG INPUT ENTER AGAIN]+++++++++++++++++++++++")
    toss=random.randint(1,2)
    if toss != usr:
        board[1][1]="O"
        print("++++++++++[ Computer won hence computer will do his first turn ]++++++++++++++++\n")
    else:
        print("+++++++++++++++++[ YOU WON HENCE YOU WILL DO THE FIRST TURN ]++++++++++++++++++++\n")

    for i in range(3):
        for j in range(3):
            print("  ",board[i][j],end=" |  ")
        print("\n")
        print("---------------------------")
    def win():
        if board[0][0]==board[0][1]==board[0][2]=="X" or board[1][0]==board[1][1]==board[1][2]=="X" or board[2][0]==board[2][1]==board[2][2]=="X" or board[0][1]==board[1][1]==board[2][1]=="X" or board[0][0]==board[1][0]==board[2][0]=="X" or board[0][2]==board[1][2]==board[2][2]=="X" or board[0][0]==board[1][1]==board[2][2]=="X" or board[0][2]==board[1][1]==board[2][0]=="X":
            return True
        elif board[0][0]==board[0][1]==board[0][2]=="O" or board[1][0]==board[1][1]==board[1][2]=="O" or board[2][0]==board[2][1]==board[2][2]=="O" or board[0][1]==board[1][1]==board[2][1]=="O" or board[0][0]==board[1][0]==board[2][0]=="O" or board[0][2]==board[1][2]==board[2][2]=="O" or board[0][0]==board[1][1]==board[2][2]=="O" or board[0][2]==board[1][1]==board[2][0]=="O":
            return False
    def winpossiblefortrick():
        counts=0
        while counts<10:
            counts+=1
            for i in range(3):
                for j in range(3):
                    if board[i][j] != "X" and board[i][j] != "O":
                        tmp=board[i][j]
                        board[i][j]="X"
                        if win():
                            board[i][j]=tmp
                            return True
                        else:
                            board[i][j]=tmp
                            if i==2 and j==2:
                                return False
                            else:
                                continue
                    else:
                        if i==2 and j==2:
                            return False

    def winpossible():
        counts=0
        while counts<10:
            counts+=1
            for i in range(3):
                for j in range(3):
                    if board[i][j] != "X" and board[i][j] != "O":
                        tmp=board[i][j]
                        board[i][j]="X"
                        if win():
                            board[i][j]="O"
                            return True
                        else:
                            board[i][j]=tmp
                            if i==2 and j==2:
                                return False
                            else:
                                continue
                    else:
                        if i==2 and j==2:
                            return False
    def winpossibleforcompfortrick():
        while True:
            for i in range(3):
                for j in range(3):
                    if board[i][j] != "X" and board[i][j] != "O":
                        tmp=board[i][j]
                        board[i][j]="O"
                        if win()==False:
                            board[i][j]=tmp
                            return True
                        else:
                            board[i][j]=tmp
                            if i==2 and j==2:
                                return False
                            else:
                                continue
                    else:
                        if i==2 and j==2:
                            return False
    def winpossibleforcomp():
        while True:
            for i in range(3):
                for j in range(3):
                    if board[i][j] != "X" and board[i][j] != "O":
                        tmp=board[i][j]
                        board[i][j]="O"
                        if win()==False:
                            board[i][j]="O"
                            return True
                        else:
                            board[i][j]=tmp
                            if i==2 and j==2:
                                return False
                            else:
                                continue
                    else:
                        if i==2 and j==2:
                            return False
    def sirtrick(User_input):
        if User_input==9 and board[2][0]==7:
            board[2][0]="O"
            if winpossible():
                board[2][0]=7
                return False
            else:
                board[2][0]=7
                return True

    def trick(User_input,boards):
        if (User_input == 3 or User_input == 1 or User_input == 7 or User_input == 9):
            if boards[2][1] == 8:
                boards[2][1] = "O"
                if winpossiblefortrick():
                    boards[2][1] = 8
                    return True
                elif win():
                    boards[2][1]=8
                    return True
                else:
                    boards[2][1] = 8
            elif boards[0][1] == 2:
                boards[0][1] = "O"
                if winpossiblefortrick():
                    boards[0][1]=2
                    return True
                elif win():
                    boards[2][1]=8
                    return True
                else:
                    boards[0][1]=2
            elif boards[1][0] == 4:
                boards[1][0] = "O"
                if winpossiblefortrick():
                    boards[1][0] = 4
                    return True
                elif win():
                    boards[2][1]=8
                    return True
                else:
                    boards[1][0] = 4
            elif boards[1][2] == 6:
                boards[1][2] = "O"
                if winpossiblefortrick():
                    boards[1][2] = 6
                    return True
                elif win():
                    boards[2][1]=8
                    return True
                else:
                    boards[1][2] = 6
            return False
        elif (User_input == 2 or User_input == 4 or User_input == 6 or User_input == 8):
            if boards[2][2] == 9:
                boards[2][2] = "O"
                if winpossiblefortrick():
                    boards[2][2]=9
                    return True
                elif win():
                    boards[2][1]=8
                    return True
                else:
                    boards[2][2]=9
            elif boards[2][0] == 7:
                boards[2][0] = "O"
                if winpossiblefortrick():
                    boards[2][0] = 7
                    return True
                elif win():
                    boards[2][1]=8
                    return True
                else:
                    boards[2][0] = 7
            elif boards[0][0] == 1:
                boards[0][0] = "O"
                if winpossiblefortrick():
                    boards[0][0] = 1
                    return True
                elif win():
                    boards[2][1]=8
                    return True
                else:
                    boards[0][0] = 1
            elif boards[0][2] == 3:
                boards[0][2] = "O"
                if winpossiblefortrick():
                    boards[0][2] = 3
                    return True
                elif win():
                    boards[2][1]=8
                    return True
                else:
                    boards[0][2] = 3
            return False
    def check(boards):
        drw = 0
        while True:
            if trick(User_input,boards)==False and winpossibleforcompfortrick()==False:
                if (User_input==3 or User_input==1 or User_input==7 or User_input==9) and (boards[1][1]=="O"):
                    if boards[2][1]==8:
                        boards[2][1]="O"
                        return boards
                    elif boards[0][1]==2:
                        boards[0][1]="O"
                        return boards
                    elif boards[1][0]==4:
                        boards[1][0]="O"
                        return boards
                    elif boards[1][2]==6:
                        boards[1][2]="O"
                        return boards
                    else:
                        continue
                elif (User_input==2 or User_input==4 or User_input==6 or User_input==8) and (boards[1][1]=="O"):
                    if boards[2][2]==9:
                        boards[2][2]="O"
                        return boards
                    elif boards[2][0]==7:
                        boards[2][0]="O"
                        return boards
                    elif boards[0][0]==1:
                        boards[0][0]="O"
                        return boards
                    elif boards[0][2]==3:
                        boards[0][2]="O"
                        return boards
                    else:
                        continue
                else:
                    count=0
                    for i in range(3):
                        if drw<20:
                            drw+=1
                            for j in range(3):
                                if boards[i][j] != "X" and boards[i][j] != "O":
                                    tmp=boards[i][j]
                                    if count==0 and boards[1][1]==5:
                                        boards[1][1] = "O"
                                        return boards
                                    else:
                                        boards[i][j]="O"
                                        if win()==False:
                                             return boards
                                        boards[i][j]=tmp
                                        if winpossibleforcomp():
                                            boards[i][j]=tmp
                                            return boards
                                        elif winpossible():
                                            return boards
                                        elif sirtrick(User_input):
                                            boards[2][0]="O"
                                            return boards
                                        else:
                                            boards[i][j]="O"
                                            return boards
                                            break
                            count+=1
                        else:
                            print("")
                            return boards
            else:
                count = 0
                for i in range(3):
                    if drw < 20:
                        drw += 1
                        for j in range(3):
                            if boards[i][j] != "X" and boards[i][j] != "O":
                                tmp = boards[i][j]
                                if count == 0 and boards[1][1] == 5:
                                    boards[1][1] = "O"
                                    return boards
                                else:
                                    boards[i][j] = "O"
                                    if win() == False:
                                        return boards
                                    boards[i][j] = tmp
                                    if winpossibleforcomp():
                                        boards[i][j] = tmp
                                        return boards
                                    elif winpossible():
                                        return boards
                                    else:
                                        boards[i][j] = "O"
                                        return boards
                                        break
                        count += 1
                    else:
                        print("")
                        return boards

    while True:
        while True:
            try:
                User_input = int(input("\n++++++++[ Please enter the NUMBER on which YOU WANT TO ASSIGN IN NUMBERS ONLY ]+++++++++++++++++ \n :->"))
                break
            except Exception:
                print("+++++++++++++++[ Wrong buttton Enter again ]+++++++++++++++++++++")
        #the process of game
        if User_input ==1:
            if  board[0][0]=="X" or board[0][0]=="O":
                print("++++++++++++++++++++++[ The box is already assigned ]+++++++++++++++++++")
            else:
                board[0][0]="X"
                if (board[0][0]!=1 and board[0][1]!=2 and board[0][2]!=3 and board[1][0]!=4 and board[1][1]!=5  and board[1][2]!=6  and board[2][0]!=7 and board[2][1]!=8 and board[2][2]!=9):
                    print("++++++++++++++[ THE MATCH IS DRAW ]+++++++++++++++++++++++")
                    break
                else:
                    board = check(board)
        elif User_input == 2:
            if board[0][1]=="X" or board[0][1]=="O":
                print("++++++++++++++++++++++[ The box is already assigned ]+++++++++++++++++++")
            else:
                board[0][1] = "X"
                if (board[0][0]!=1 and board[0][1]!=2 and board[0][2]!=3 and board[1][0]!=4 and board[1][1]!=5  and board[1][2]!=6  and board[2][0]!=7 and board[2][1]!=8 and board[2][2]!=9):
                    print("++++++++++++++[ THE MATCH IS DRAW ]+++++++++++++++++++++++")
                    break
                else:
                    board = check(board)
        elif User_input == 3:
            if board[0][2]=="X" or board[0][2]=="O":
                print("++++++++++++++++++++++[ The box is already assigned ]+++++++++++++++++++")
            else:
                board[0][2] = "X"
                if (board[0][0]!=1 and board[0][1]!=2 and board[0][2]!=3 and board[1][0]!=4 and board[1][1]!=5  and board[1][2]!=6  and board[2][0]!=7 and board[2][1]!=8 and board[2][2]!=9):
                    print("++++++++++++++[ THE MATCH IS DRAW ]+++++++++++++++++++++++")
                    break
                else:
                    board = check(board)
        elif User_input == 4:
            if board[1][0]=="X" or board[1][0]=="O":
                print("++++++++++++++++++++++[ The box is already assigned ]+++++++++++++++++++")
            else:
                board[1][0] = "X"
                if (board[0][0]!=1 and board[0][1]!=2 and board[0][2]!=3 and board[1][0]!=4 and board[1][1]!=5  and board[1][2]!=6  and board[2][0]!=7 and board[2][1]!=8 and board[2][2]!=9):
                    print("++++++++++++++[ THE MATCH IS DRAW ]+++++++++++++++++++++++")
                    break
                else:
                    board = check(board)
        elif User_input == 5:
            if board[1][1]=="X" or board[1][1]=="O":
                print("++++++++++++++++++++++[ The box is already assigned ]+++++++++++++++++++")
            else:
                board[1][1] = "X"
                if (board[0][0]!=1 and board[0][1]!=2 and board[0][2]!=3 and board[1][0]!=4 and board[1][1]!=5  and board[1][2]!=6  and board[2][0]!=7 and board[2][1]!=8 and board[2][2]!=9):
                    print("++++++++++++++[ THE MATCH IS DRAW ]+++++++++++++++++++++++")
                    break
                else:
                    board = check(board)
        elif User_input == 6:
            if board[1][2]=="X" or board[1][2]=="O":
                print("++++++++++++++++++++++[ The box is already assigned ]+++++++++++++++++++")
            else:
                board[1][2] = "X"
                if (board[0][0]!=1 and board[0][1]!=2 and board[0][2]!=3 and board[1][0]!=4 and board[1][1]!=5  and board[1][2]!=6  and board[2][0]!=7 and board[2][1]!=8 and board[2][2]!=9):
                    print("++++++++++++++[ THE MATCH IS DRAW ]+++++++++++++++++++++++")
                    break
                else:
                    board = check(board)

        elif User_input == 7:
            if board[2][0]=="X" or board[2][0]=="O":
                print("++++++++++++++++++++++[ The box is already assigned ]+++++++++++++++++++")
            else:
                board[2][0] = "X"
                if (board[0][0]!=1 and board[0][1]!=2 and board[0][2]!=3 and board[1][0]!=4 and board[1][1]!=5  and board[1][2]!=6  and board[2][0]!=7 and board[2][1]!=8 and board[2][2]!=9):
                    print("++++++++++++++[ THE MATCH IS DRAW ]+++++++++++++++++++++++")
                    break
                else:
                    board = check(board)

        elif User_input == 8:
            if board[2][1]=="X" or board[2][1]=="O":
                print("++++++++++++++++++++++[ The box is already assigned ]+++++++++++++++++++")
            else:
                board[2][1] = "X"
                if (board[0][0]!=1 and board[0][1]!=2 and board[0][2]!=3 and board[1][0]!=4 and board[1][1]!=5  and board[1][2]!=6  and board[2][0]!=7 and board[2][1]!=8 and board[2][2]!=9):
                    print("++++++++++++++[ THE MATCH IS DRAW ]+++++++++++++++++++++++")
                    break
                else:
                    board = check(board)

        elif User_input == 9:
            if board[2][2]=="X" or board[2][2]=="O":
                print("++++++++++++++++++++++[ The box is already assigned ]+++++++++++++++++++")
            else:
                board[2][2] = "X"
                if (board[0][0]!=1 and board[0][1]!=2 and board[0][2]!=3 and board[1][0]!=4 and board[1][1]!=5  and board[1][2]!=6  and board[2][0]!=7 and board[2][1]!=8 and board[2][2]!=9):
                    print("++++++++++++++[ THE MATCH IS DRAW ]+++++++++++++++++++++++")
                    break
                else:
                    board = check(board)

        for i in range(3):
            for j in range(3):
                    print("  ", board[i][j], end=" |  ")
            print("\n")
            print("---------------------------")
        if win():
            print("+++++++++++++++++++[ YOU WON ]+++++++++++++++++++++++++++++++")
            break
        elif win()==False:
            print("+++++++++++++++++++[ YOU LOOSE ]+++++++++++++++++++++++++++++")
            break
        elif (board[0][0]!=1 and board[0][1]!=2 and board[0][2]!=3 and board[1][0]!=4 and board[1][1]!=5  and board[1][2]!=6  and board[2][0]!=7 and board[2][1]!=8 and board[2][2]!=9):
            print("++++++++++++++[ THE MATCH IS DRAW ]+++++++++++++++++++++++")
            break



    restart=input("Do you want to Play Again (Y/N)? ")
