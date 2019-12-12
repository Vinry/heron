import math

def inputs():
    antaliterations = int(input("Hur många gånger vill du iterata?:"))
    talattrakna = int(input("Vilket tal vill du räkna?:"))
    gissning = float(input("Gissning på rot:"))
    return heronsmetod(antaliterations, talattrakna, gissning)


def heronsmetod(antaliterations, talattrakna, gissning):
    nygissning = 1/2 * (gissning + talattrakna/gissning)
    resultat = False
    counter = 0
    while not resultat:
        counter += 1
        senastegissning = nygissning
        print("Gissning " + str(counter) + " är " + str(nygissning))
        nygissning = 1/2 * (nygissning + talattrakna/nygissning)
        if abs(nygissning - senastegissning) == 0 or counter == antaliterations:
            resultat = True
    print("Bästa gissning av kvadratrot är " + str(nygissning) + " och använder " + str(counter) + " iterationer")
    print("sqrt() funktionen säger: " + str(math.sqrt(talattrakna)))

if __name__ == '__main__':
    inputs()
