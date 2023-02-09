import os


class Screens:
    def __init__(self):
        self.screens = []
        self.screenAmount = 0
        self.data = [[]]

    def write(self, screen_num, rows, columns):
        self.data.append([[]])
        self.data[screen_num - 1] = [[" " for _ in range(columns)] for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                self.data[screen_num - 1][i][j] = "E"

    def read_all(self):
        os.system('cls')
        for i in range(1, self.screenAmount + 1):
            print("Screen ", i)
            print("  ", end='')
            for j in range(len(self.data[i - 1][0])):
                if j < 9:
                    print("0" + str(j + 1) + " ", end='')
                else:
                    print(str(j + 1) + " ", end='')
            print()
            for j in range(len(self.data[i - 1])):
                print(chr(ord('A') + j), end='  ')
                for k in range(len(self.data[i - 1][j])):
                    if self.data[i - 1][j][k]:
                        print(self.data[i - 1][j][k], end='  ')
                    else:
                        print("   ", end='  ')
                print()
            print()
        print()

        input("Press ENTER To Continue...\n")

    def read_specific(self, screen_num):
        os.system('cls')
        print("Screen ", screen_num)
        print("  ", end='')
        for j in range(len(self.data[screen_num - 1][0])):
            if j < 9:
                print("0" + str(j + 1) + " ", end='')
            else:
                print(str(j + 1) + " ", end='')
        print()
        for j in range(len(self.data[screen_num - 1])):
            print(chr(ord('A') + j), end='  ')
            for k in range(len(self.data[screen_num - 1][j])):
                if self.data[screen_num - 1][j][k]:
                    print(self.data[screen_num - 1][j][k], end='  ')
                else:
                    print("   ", end='  ')
            print()
        print()

    def book_seat(self, screen_num, row, column, type):
        row = row - 1
        column = column - 1
        self.data[screen_num - 1][row][column] = type


def setup():
    print("CINEMA BOOKING ADMINISTRATION")

    print("\nHow many screens?")
    while 1:
        screens = input("> ")
        if screens.isnumeric():
            screens = int(screens)
            if screens > 0:
                break
            else:
                print("Inputted Number Must Be > 0, Please Try Again")
        else:
            print("Invalid Format, You Must Input An Integer, Please Try Again.")

    screen = Screens()
    screen.screenAmount = screens

    for i in range(1, screens + 1, 1):
        print("\nEnter Rows [Screen ", i, end='' "] (Max: 26)")
        while 1:
            rows = input("\n> ")
            if rows.isnumeric():
                rows = int(rows)
                if rows > 0:
                    if rows < 27:
                        break
                    else:
                        print("Inputted Number Must Be < Or Equal To 26, Please Try Again")
                else:
                    print("Inputted Number Must Be > 0, Please Try Again")
            else:
                print("Invalid Format, You Must Input An Integer, Please Try Again.")

        print("\nEnter Columns [Screen ", i, end='' "] (Max: 40)")
        while 1:
            columns = input("\n> ")
            if columns.isnumeric():
                columns = int(columns)
                if columns > 0:
                    if columns < 41:
                        break
                    else:
                        print("Inputted Number Must Be < Or Equal To 40, Please Try Again")
                else:
                    print("Inputted Number Must Be > 0, Please Try Again")
            else:
                print("Invalid Format, You Must Input An Integer, Please Try Again.")

        screen.write(i, rows, columns)
        screen.screens.append([rows, columns])

    menu(screen)


def menu(screen):
    while 1:
        os.system('cls')
        print("MAIN MENU\n\n1 - Display Cinema\n2 - Book Seat\n3 - Display Screen\n4 - Exit")
        while 1:
            main_input = input("> ")
            if main_input.isnumeric():
                main_input = int(main_input)
                if main_input > 0:
                    if main_input < 5:
                        break
                    else:
                        print("Inputted Number Must Be < Or Equal To 4, Please Try Again")
                else:
                    print("Inputted Number Must Be > 0, Please Try Again")
            else:
                print("Invalid Format, You Must Input An Integer, Please Try Again.")

        if main_input == 1:
            screen.read_all()
        elif main_input == 2:
            while 1:
                os.system('cls')
                print("Enter The Screen Number:")
                while 1:
                    screen_num = input("> ")
                    if screen_num.isnumeric():
                        screen_num = int(screen_num)
                        if screen_num > 0:
                            if screen_num <= screen.screenAmount:
                                break
                            else:
                                print("Inputted Number Must Be < Or Equal To", screen.screenAmount,
                                      end='' " (Amount Of Screens)\n")
                        else:
                            print("Inputted Number Must Be > 0, Please Try Again")
                    else:
                        print("Invalid Format, You Must Input An Integer, Please Try Again.")
                screen.read_specific(screen_num)
                print("Enter The Seat ID [Example: A01, D22, E11]:")
                while 1:
                    seat_id = input("> ")
                    if len(seat_id) <= 3 and len(seat_id) >=3:
                        if seat_id[0].isalpha():
                            conversions = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
                            row = seat_id[0].lower()
                            row = conversions[row]
                            row = int(row)
                            if row <= len(screen.data[screen_num - 1]):
                                if seat_id[1].isnumeric() and seat_id[2].isnumeric():
                                    column = seat_id[1] + seat_id[2]
                                    column = int(column)
                                    if column <= len(screen.data[screen_num - 1][0]):
                                        if column > 0:
                                            break
                                        else:
                                            print("Inputted Number Must Be > 0, Please Try Again")
                                    else:
                                        print("The Inputted Number Must Not Be < Or Equal To", len(screen.data[screen_num - 1][0]), end='' " (The Amount Of Cinema Columns)\n")
                                else:
                                    print("Seat ID Is In The Wrong Format (Number), Please Try Again.")
                            else:
                                print("The Inputted Letter Must Not Be < Or Equal To", len(screen.data[screen_num - 1]), end='' " (The Amount Of Cinema Rows [Corresponds To The Letter Your Inputted])\n")
                        else:
                            print("Seat ID Is In The Wrong Format (Letter), Please Try Again.")
                    else:
                        print("Seat ID Is Longer Than 3 Characters OR Is Shorter Than 3 Characters, Please Try Again.")
                print("Please Choose Patron Type:\nA - Adult, C - Child\nO - Concession, S - Student\nCANCEL - Cancel Booking")
                while 1:
                    patron_type = input("> ")
                    patron_type = patron_type.upper()
                    if patron_type == "A":
                        screen.book_seat(screen_num, row, column, "A")
                        break
                    elif patron_type == "C":
                        screen.book_seat(screen_num, row, column, "C")
                        break
                    elif patron_type == "O":
                        screen.book_seat(screen_num, row, column, "O")
                        break
                    elif patron_type == "S":
                        screen.book_seat(screen_num, row, column, "S")
                        break
                    elif patron_type == "CANCEL":
                        screen.book_seat(screen_num, row, column, "E")
                        break
                    else:
                        print("Invalid Patron Type, Please Try Again.\nTIP: Type CANCEL To Cancel Booking")
                print("\nSeat Booked Successfully!")
                print("Book Another Seat? Y/N:")
                while 1:
                    book_another = input("> ")
                    if book_another.upper() == "Y":
                        break
                    elif book_another.upper() == "N":
                        break
                    else:
                        print("Invalid Input, Please Try Again (Use Y or N).")
                if book_another.upper() == "N":
                    break
        elif main_input == 3:
            os.system('cls')
            if screen.screenAmount > 1:
                print("Enter The Screen Number:")
                while 1:
                    screen_num = input("> ")
                    if screen_num.isnumeric():
                        screen_num = int(screen_num)
                        if screen_num > 0:
                            if screen_num <= screen.screenAmount:
                                screen.read_specific(screen_num)
                                input("Press ENTER To Continue...\n")
                                break
                            else:
                                print("Inputted Number Must Be < Or Equal To", screen.screenAmount, end='' " (Amount Of Screens)\n")
                        else:
                            print("Inputted Number Must Be > 0, Please Try Again")
                    else:
                        print("Invalid Format, You Must Input An Integer, Please Try Again.")
            else:
                screen.read_all()
        elif main_input == 4:
            exit()


if __name__ == '__main__':
    setup()