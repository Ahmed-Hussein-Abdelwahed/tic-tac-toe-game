# player X
# player O  
def confirmExit():
    while True:
        print('[1] Play another Round\n[2] Exit  ')
        userChoice = input()
        if userChoice == '1':
            return True
        elif userChoice == '2':
            return False
        else:
            print('Invalid choice try again')
            while userChoice != '1' or userChoice != '2':
                userChoice = input()


def checkGameEnd(row1, row2, row3, isPlayerWin):
    if isPlayerWin or ('1' not in row1 and '2' not in row1 and '3' not in row1 and \
                       '4' not in row2 and '5' not in row2 and '6' not in row2 and \
                       '7' not in row3 and '8' not in row3 and '9' not in row3):
        return False
    else:
        return True


def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


def checkXWin(row1, row2, row3):
    if (['X', 'X', 'X'] == row1 or ['X', 'X', 'X'] == row2 or ['X', 'X', 'X'] == row3) or \
            (row1[0] == 'X' and row2[0] == 'X' and row3[0] == 'X') or \
            (row1[1] == 'X' and row2[1] == 'X' and row3[1] == 'X') or \
            (row1[2] == 'X' and row2[2] == 'X' and row3[2] == 'X') or \
            (row1[0] == 'X' and row2[1] == 'X' and row3[2] == 'X') or \
            (row3[0] == 'X' and row2[1] == 'X' and row1[2] == 'X'):
        print('Player X win')
        return True


def checkOWin(row1, row2, row3):
    if (['O', 'O', 'O'] == row1 or ['O', 'O', 'O'] == row2 or ['O', 'O', 'O'] == row3) or \
            (row1[0] == 'O' and row2[0] == 'O' and row3[0] == 'O') or \
            (row1[1] == 'O' and row2[1] == 'O' and row3[1] == 'O') or \
            (row1[2] == 'O' and row2[2] == 'O' and row3[2] == 'O') or \
            (row1[0] == 'O' and row2[1] == 'O' and row3[2] == 'O') or \
            (row3[0] == 'O' and row2[1] == 'O' and row1[2] == 'O'):
        print('Player O win')
        return True


line1 = ['1', '2', '3']
line2 = ['4', '5', '6']
line3 = ['7', '8', '9']

roleX = True
roleO = False
confirm = True
flag = False

display(line1, line2, line3)

while confirm:

    if roleX:

        try:
            position = int(input('Enter position for X:  '))

            if position <= 3:

                if line1[position - 1] == str(position):
                    line1[position - 1] = 'X'
                    roleX = False
                    roleO = True

                else:
                    print('Invalid cell')

            elif 3 < position <= 6:

                if line2[position - 4] == str(position):
                    line2[position - 4] = 'X'
                    roleX = False
                    roleO = True
                else:
                    print('Invalid cell')
            elif 6 < position <= 9:

                if line3[position - 7] == str(position):
                    line3[position - 7] = 'X'
                    roleX = False
                    roleO = True
                else:
                    print('Invalid cell')
            display(line1, line2, line3)
            print()
            flag = checkXWin(line1, line2, line3)
            confirm = checkGameEnd(line1, line2, line3, flag)

        except:
            print('Invalid position')
            continue

    elif roleO:

        try:
            position = int(input('Enter position for O:  '))

            if position <= 3:

                if line1[position - 1] == str(position):
                    line1[position - 1] = 'O'
                    roleX = True
                    roleO = False
                else:
                    print('Invalid cell')

            elif 3 < position <= 6:

                if line2[position - 4] == str(position):
                    line2[position - 4] = 'O'
                    roleX = True
                    roleO = False
                else:
                    print('Invalid cell')

            elif 6 < position <= 9:

                if line3[position - 7] == str(position):
                    line3[position - 7] = 'O'
                    roleX = True
                    roleO = False
                else:
                    print('Invalid cell')
            display(line1, line2, line3)
            print()
            flag = checkOWin(line1, line2, line3)
            confirm = checkGameEnd(line1, line2, line3, flag)

        except:
            print('Invalid position')
            continue

    if flag or not confirm:
        if confirmExit():
            confirm = True
            line1 = ['1', '2', '3']
            line2 = ['4', '5', '6']
            line3 = ['7', '8', '9']
