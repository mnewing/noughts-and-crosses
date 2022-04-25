def getMovePlayX():
    row = input("your move, which row: ")
    col = input("your move, which col: ")
    if row == "1":
        if col == "a" or col == "A" :
            row1[0] = "X"
        elif col == "B" or col == "b" :
            row1[1] = "X"
        else:
            row1[1] = "X"

def displayBoard():
    print("   A  | B | C ")
    print(" 1  "+row1[0]+" |   |   ")
    print("   -----------")
    print(" 2    |   |   ")
    print("   -----------")
    print(" 3    |   |   ")

#main program
row1 = ["", "", ""]
row2 = ["", "", ""]
row3 = ["", "", ""]


displayBoard()
getMovePlayX()
displayBoard()
