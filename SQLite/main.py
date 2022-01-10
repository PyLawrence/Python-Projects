"""
All unused code should either be collapsed or within a collapsable region based on your IDE
I recommend running the program within your command prompt on windows
Written in python 3.9.7
"""

import sqlite3
import os
# import sys



status = 'manual'

def continuityDecorator(func):
    def inner1(*args, **kwargs):
        func(*args, **kwargs)
        if status != 'auto':
            input("\nPress enter to continue...")
            os.system('cls')
            main()
    return inner1


def create_exec_string(fileName):
    """
    generates a string that can be used to insert data into the table
    :param fileName:
    :return: return string(or if multiple sets of data, we would use a dict) that we can use to execute the query
    """
    returnString = "INSERT INTO tbl_files (col_fileName) VALUES ('" + fileName + "')"

    return returnString

    # use a dictionary to return multiple values if needbe
    # string2 = fileName
    # returnDict = dict()
    # returnDict['template'] = string1
    # returnDict['fileName'] = string2

@continuityDecorator
def createDatabase(dbName):
    if not dbName.endswith('.db'):
        dbName = dbName + ".db"
    conn = sqlite3.connect(dbName)

    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fileName TEXT)")
        conn.commit()

    conn.close()

@continuityDecorator
def generateData(dbName, dataTuple):
    """
    Name is misleading at this point, just adds data to the table based on the given input
    :param dbName:
    :param dataTuple: tuple of given data, in this case just strings
    :return: void
    """
    if not dbName.endswith('.db'):
        dbName = dbName + ".db"
    conn = sqlite3.connect(dbName)
    with conn:
        cur = conn.cursor()
        tmpList = list()
        for item in getValidData('txt', dataTuple):
            # temp = create_exec_string(item)
            # cur.execute(temp['template'], (temp['fileName']))
            tmpList.append(create_exec_string(item))
            cur.execute(create_exec_string(item))
        conn.commit()
        print("Commands executed:")
        for item in tmpList:
            print(item)
        print("\n")
    conn.close()

    # region Testing
    # with conn:
    #     cur = conn.cursor()
    #     # a = create_exec_string('Michael', 'Ross', 'mike.ross@gmail.com')
    #     b = create_exec_string('Josh', 'Jones', 'josh.jones@gmail.com')
    #     c = create_exec_string('Jennifer', 'Kirkland', 'jennifer.kirkland@gmail.com')
    #     # cur.execute(a['template'], (a['fname'], a['lname'], a['email']))
    #
    #     cur.execute(b['template'], (b['fname'], b['lname'], b['email']))
    #     cur.execute(c['template'], (c['fname'], c['lname'], c['email']))
    #
    #
    #     conn.commit()
    # conn.close()
    # endregion


def getValidData(query, dataTuple):
    """
    turns the given tuple into a list of data based on our parameter
    :param query: file type e.g. .txt, .png, .jpg, etc.
    :param dataTuple: tuple of items we would like to sort through
    :return: list of items that pass the check
    """
    items = list()
    for item in dataTuple:
        if item.endswith(query):
            items.append(item)
    return items

def printData(items):
    print("The files that pass the check are:")
    for i in range(len(items)):
        print("{}. {}".format(i+1, items[i]))
    input("\nPress enter to continue...")
    os.system("cls")
    main()

# region UNUSED
# def queryDatabase(dbName):
#     """
#     currently unused
#     :param dbName:
#     :return:
#     """
#     if not dbName.endswith('.db'):
#         dbName = dbName + ".db"
#     conn = sqlite3.connect(dbName)
#     with conn:
#         pass
#     #     cur = conn.cursor()
#     #     cur.execute("SELECT col_fname,col_lname,col_email FROM tbl_persons WHERE col_fname = 'Jennifer'")
#     #     r_Person = cur.fetchall()
#     #     # only have one return value in this test, so this will return the data needed
#     #     # msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(r_Person[0][0], r_Person[0][1], r_Person[0][2])
#     #     for item in r_Person:
#     #         # print(r_Person)
#     #         # in a situation where we did have multiple return values and we wanted to print each one
#     #         # we would manage the data within the for loop
#     #         print("First Name: {}\nLast Name: {}\nEmail: {}".format(item[0], item[1], item[2]))
#     # conn.close()
# endregion

@continuityDecorator
def sysClear():
    if os.path.exists('files.db'):
        try:
            os.remove('files.db')
            print("Done.\n")
        except PermissionError:
            print("\n File may be open in your database viewer, close the connection before deleting the file.")

def autoExec():
    """
    this will auto run through the program instead of having the user go through the menu
    :return:
    """
    filesTuple = ('information.docx', 'hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
    createDatabase('files')
    generateData('files', filesTuple)
    printData(getValidData(".txt", filesTuple))

def main():
    print("Mainly so if you run this multiple times, it doesn't unnecessarily add data to the database\n"
          "Please run in a windows command prompt for the best experience.\n"
          "Here's a short menu\n")
    temp = int(input("What would you like to do?\n1. Auto run through the whole program \n2. Create the DB \n"
                 "3. Add the data to the DB\n4. Print files that pass the default check\n"
                 "5. Clear all data and start over\n6. Exit\n"))
    filesTuple = ('information.docx', 'hello.txt', 'myImage.png', 'myMovie.mpg',
                  'World.txt', 'data.pdf', 'myPhoto.jpg')

    # region 3.10
    # global status
    # if sys.version_info >= (3, 10):
    #     match temp:
    #         case 1:
    #             status = 'auto'
    #             os.system('cls')
    #             autoExec()
    #         case 2:
    #             status = 'manual'
    #             os.system('cls')
    #             createDatabase('files')
    #         case 3:
    #             status = 'manual'
    #             os.system('cls')
    #             generateData('files', filesTuple)
    #         case 4:
    #             status = 'manual'
    #             os.system('cls')
    #             printData(getValidData('.txt', filesTuple))
    #         case 5:
    #             status = 'manual'
    #             os.system('cls')
    #             sysClear()
    #
    #         case _:
    #             os.system('cls')
    #             print("Please use a number from 1 to 5 to choose what you would like to do")
    #             input("Press enter to continue...")
    #             os.system('cls')
    #             main()

    # endregion

    # region < 3.10
    global status
    if temp == 1:
        status = 'auto'
        os.system('cls')
        autoExec()
    elif temp == 2:
        status = 'manual'
        os.system('cls')
        createDatabase('files')
    elif temp == 3:
        status = 'manual'
        os.system('cls')
        generateData('files', filesTuple)
    elif temp == 4:
        status = 'manual'
        os.system('cls')
        printData(getValidData('.txt', filesTuple))
    elif temp == 5:
        status = 'manual'
        os.system('cls')
        sysClear()
    elif temp == 6:
        exit()
    else:
        os.system('cls')
        print("Please use a number from 1 to 5 to choose what you would like to do")
        input("Press enter to continue...")
        os.system('cls')
        main()

    # endregion

if __name__ == '__main__':
    main()

