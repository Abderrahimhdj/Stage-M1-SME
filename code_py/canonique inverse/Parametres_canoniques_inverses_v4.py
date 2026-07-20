import random
import math

f = open("/Users/macbookpro/Desktop/stage_sme/parametres_canoniques_inverse_v4.xml", "w")
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<quiz>\n')

total = 0

# ============================================================
# Ordre 1 : on donne K et tau, on demande la bonne equation diff
# ============================================================
for i in range(1):
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    c = random.randint(1, 10)

    K = round(c / b, 4)
    tau = round(a / b, 4)

    bonne = '\\(' + str(a) + '\\dot{y} + ' + str(b) + 'y = ' + str(c) + 'u\\)'

    mauvaises = [
        '\\(' + str(b) + '\\dot{y} + ' + str(a) + 'y = ' + str(c) + 'u\\)',
        '\\(' + str(a) + '\\dot{y} + ' + str(b) + 'y = u\\)',
        '\\(' + str(a) + '\\dot{y} - ' + str(b) + 'y = ' + str(c) + 'u\\)',
        '\\(' + str(a) + '\\dot{y} + ' + str(c) + 'y = ' + str(b) + 'u\\)',
        '\\(' + str(a+1) + '\\dot{y} + ' + str(b) + 'y = ' + str(c) + 'u\\)',
        '\\(' + str(a) + '\\dot{y} + ' + str(b+1) + 'y = ' + str(c) + 'u\\)',
    ]

    choix = random.sample(mauvaises, 3)

    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Canonique inverse Ordre 1 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit un systeme du premier ordre avec \\(K = ' + str(K) + '\\) et \\(\\tau = ' + str(tau) + '\\). Quelle est l\'equation differentielle ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>' + bonne + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[0] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[1] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[2] + '</text></answer>\n')
    f.write('  </question>\n')
    total += 1

# ============================================================
# Ordre 2 : on donne K, wn, zeta, on demande la bonne equation diff
# ============================================================
for i in range(1):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)

    K = round(d / c, 4)
    wn = round(math.sqrt(c / a), 4)
    zeta = round(b / (2 * math.sqrt(a * c)), 4)

    bonne = '\\(' + str(a) + '\\ddot{y} + ' + str(b) + '\\dot{y} + ' + str(c) + 'y = ' + str(d) + 'u\\)'

    mauvaises = [
        '\\(' + str(a) + '\\ddot{y} + ' + str(b) + '\\dot{y} + ' + str(c) + 'y = u\\)',
        '\\(' + str(a) + '\\ddot{y} - ' + str(b) + '\\dot{y} + ' + str(c) + 'y = ' + str(d) + 'u\\)',
        '\\(' + str(c) + '\\ddot{y} + ' + str(b) + '\\dot{y} + ' + str(a) + 'y = ' + str(d) + 'u\\)',
        '\\(' + str(a) + '\\ddot{y} + ' + str(b) + '\\dot{y} + ' + str(d) + 'y = ' + str(c) + 'u\\)',
        '\\(' + str(a+1) + '\\ddot{y} + ' + str(b) + '\\dot{y} + ' + str(c) + 'y = ' + str(d) + 'u\\)',
        '\\(' + str(a) + '\\ddot{y} + ' + str(b+1) + '\\dot{y} + ' + str(c) + 'y = ' + str(d) + 'u\\)',
    ]

    choix = random.sample(mauvaises, 3)

    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Canonique inverse Ordre 2 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit un systeme du deuxieme ordre avec \\(K = ' + str(K) + '\\), \\(\\omega_n = ' + str(wn) + '\\) et \\(\\zeta = ' + str(zeta) + '\\). Quelle est l\'equation differentielle ?</text></questiontext>\n')
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
