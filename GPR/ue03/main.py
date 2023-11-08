'''GPR Übungsblatt 03'''
__author__ = "7987847, Werner"

def dec_to_bin(zahl:int) -> str:
    '''Umwandlung einer Dezimalzahl in eine Binärzahl
    zahl: Dezimalzahl
    '''
    if zahl == 0:
        return '0'
    binzahl = ''
    while zahl > 0:
        binzahl = str(zahl % 2) + binzahl
        zahl //= 2
    return binzahl


print("Es wird eine Dezimalzahl in eine Binärzahl umgewandelt.")
print("Geben Sie eine Dezimalzahl ein.")
print(dec_to_bin(int(input("Dezimalzahl: "))))

# Testfälle

# dec_to_bin(0)
# Ausgabe: 0

# dec_to_bin(1)
# Ausgabe: 1

# dec_to_bin(69)
# Ausgabe: 1000101
