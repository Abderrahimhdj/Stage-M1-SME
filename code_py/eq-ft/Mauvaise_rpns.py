# derniere version de code (ft - eq) avec mauvaises reponses variees
import random

f = open("/Users/macbookpro/Desktop/stage_sme/mv_rpns.xml", "w")
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<quiz>\n')

total = 0

# ============================================================
# SENS 1 : Equation differentielle -> Fonction de transfert
# ============================================================

# Ordre 1 : dy/dt + ay = eu  ->  H(p) = e/(p+a)
for i in range(5):
    a = random.randint(2, 10)  # on commence a 2 pour eviter le probleme avec a=1
    e = random.randint(1, 10)
    while e == a:
        e = random.randint(1, 10)

    # liste de mauvaises reponses avec les memes coefficients
    mauvaises = [
        '\\(H(p) = \\frac{' + str(e) + '}{p-' + str(a) + '}\\)',       # signe inverse
        '\\(H(p) = \\frac{1}{p+' + str(a) + '}\\)',                     # oubli du e au numerateur
        '\\(H(p) = \\frac{' + str(a) + '}{p+' + str(e) + '}\\)',        # coefficients inverses
        '\\(H(p) = \\frac{p}{p+' + str(a) + '}\\)',                     # p au numerateur
        '\\(H(p) = \\frac{' + str(e) + '}{p^2+' + str(a) + '}\\)',      # mauvais ordre
        '\\(H(p) = \\frac{' + str(e) + '}{p}\\)',                       # oubli du a
        '\\(H(p) = \\frac{' + str(e) + 'p}{p+' + str(a) + '}\\)',       # p au numerateur avec e
        '\\(H(p) = \\frac{' + str(e) + '}{p+' + str(a+1) + '}\\)',      # a decale de 1
    ]

    # on choisit 3 mauvaises reponses au hasard
    choix = random.sample(mauvaises, 3)

    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Eq->FT Ordre 1 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(\\frac{dy}{dt} + ' + str(a) + 'y = ' + str(e) + 'u\\). Quelle est \\(H(p)\\) ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(H(p) = \\frac{' + str(e) + '}{p+' + str(a) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[0] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[1] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[2] + '</text></answer>\n')
    f.write('  </question>\n')
    total += 1

f.write('</quiz>\n')
f.close()
print("Succes !")
print("Total : " + str(total) + " questions generees !")
