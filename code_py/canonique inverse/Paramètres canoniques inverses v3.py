import random

f = open("/Users/macbookpro/Desktop/stage_sme/parametres_canoniques_inverse_v2.xml", "w")
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<quiz>\n')

total = 0

# ============================================================
# Exercice : on donne K et tau, on demande la bonne equation diff
# K = c/b, tau = a/b  ->  a*dy/dt + b*y = c*u
# ============================================================

for i in range(10):
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    c = random.randint(1, 10)

    K = round(c / b, 4)
    tau = round(a / b, 4)

    # bonne reponse
    bonne = '\\(' + str(a) + '\\dot{y} + ' + str(b) + 'y = ' + str(c) + 'u\\)'

    # mauvaises reponses - memes coefficients mais erreurs logiques
    mauvaises = [
        '\\(' + str(b) + '\\dot{y} + ' + str(a) + 'y = ' + str(c) + 'u\\)',   # a et b inverses
        '\\(' + str(a) + '\\dot{y} + ' + str(b) + 'y = u\\)',                  # oubli du c
        '\\(' + str(a) + '\\dot{y} - ' + str(b) + 'y = ' + str(c) + 'u\\)',   # signe inverse
        '\\(' + str(a) + '\\dot{y} + ' + str(c) + 'y = ' + str(b) + 'u\\)',   # b et c inverses
        '\\(' + str(a+1) + '\\dot{y} + ' + str(b) + 'y = ' + str(c) + 'u\\)', # a decale de 1
        '\\(' + str(a) + '\\dot{y} + ' + str(b+1) + 'y = ' + str(c) + 'u\\)', # b decale de 1
    ]

    choix = random.sample(mauvaises, 3)

    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Canonique inverse QCM - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit un systeme du premier ordre avec \\(K = ' + str(K) + '\\) et \\(\\tau = ' + str(tau) + '\\). Quelle est l\'equation differentielle correspondante ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>' + bonne + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[0] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[1] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[2] + '</text></answer>\n')
    f.write('  </question>\n')
    total += 1

f.write('</quiz>\n')
f.close()
print("Succes !")
print("Total : " + str(total) + " questions generees !")
