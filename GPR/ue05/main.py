'''GPR Übungsblatt 05'''
__author__ = "7987847, Werner"


def str_find(string, substring):
    """Returns the index of the first occurrence of substring in string or 
    -1 if substring is not part of string"""
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            return i
    return -1




if __name__ == "__main__":

    print("Das Programm sucht nach Teilzeichenketten in Zeichenketten.")
    print("Es wird der index der ersten Teilzeichenkette in der Zeichenkette ausgegeben.")
    print("Ist die Teilzeichenkette nicht in der Zeichenkette enthalten,wird -1 ausgegeben.")
    print("Geben Sie eine Zeichenkette und eine Teilzeichenkette ein.")
    print(str_find(input("Zeichenkette: "), input("Teilzeichenkette: ")))


    # Testfälle
    
    # str_find("Hello World", "ll")
    # Ausgabe: 2

    # str_find("Hello", "World")
    # Ausgabe: -1

    # str_find("Hello", "Hello")
    # Ausgabe: 0
