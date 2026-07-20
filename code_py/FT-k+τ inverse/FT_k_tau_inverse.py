import random
import math

f = open("/Users/macbookpro/Desktop/stage_sme/FT_k_tau_inverse.xml", "w")
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<quiz>\n')

total = 0

# ============================================================
# Ordre 1 : on donne K et tau, on demande la bonne H(p)
# ============================================================
for i in range(1):
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    c = random.randint(1, 10)

    K = round(c / b, 4)
    tau = round(a / b, 4)

    bonne = '\\(H(p) = \\frac{' + str(c) + '}{' + str(a) + 'p+' + str(b) + '}\\)'

    mauvaises = [
        '\\(H(p) = \\frac{' + str(c) + '}{' + str(b) + 'p+' + str(a) + '}\\)',
        '\\(H(p) = \\frac{1}{' + str(a) + 'p+' + str(b) + '}\\)',
        '\\(H(p) = \\frac{' + str(c) + '}{' + str(a) + 'p-' + str(b) + '}\\)',
        '\\(H(p) = \\frac{' + str(b) + '}{' + str(a) + 'p+' + str(c) + '}\\)',
        '\\(H(p) = \\frac{' + str(c) + '}{' + str(a+1) + 'p+' + str(b) + '}\\)',
        '\\(H(p) = \\frac{' + str(c) + '}{' + str(a) + 'p+' + str(b+1) + '}\\)',
    ]

    choix = random.sample(mauvaises, 3)

    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Canonique vers FT Ordre 1 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit un systeme du premier ordre avec \\(K = ' + str(K) + '\\) et \\(\\tau = ' + str(tau) + '\\). Quelle est \\(H(p)\\) ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>' + bonne + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[0] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[1] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[2] + '</text></answer>\n')
    f.write('  </question>\n')
    total += 1

# ============================================================
# Ordre 2 : on donne K, wn, zeta, on demande la bonne H(p)
# ============================================================
for i in range(1):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)

    K = round(d / c, 4)
    wn = round(math.sqrt(c / a), 4)
    zeta = round(b / (2 * math.sqrt(a * c)), 4)

    bonne = '\\(H(p) = \\frac{' + str(d) + '}{' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\)'

    mauvaises = [
        '\\(H(p) = \\frac{1}{' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\)',
        '\\(H(p) = \\frac{' + str(d) + '}{' + str(a) + 'p^2-' + str(b) + 'p+' + str(c) + '}\\)',
        '\\(H(p) = \\frac{' + str(d) + '}{' + str(c) + 'p^2+' + str(b) + 'p+' + str(a) + '}\\)',
        '\\(H(p) = \\frac{' + str(c) + '}{' + str(a) + 'p^2+' + str(b) + 'p+' + str(d) + '}\\)',
        '\\(H(p) = \\frac{' + str(d) + '}{' + str(a+1) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\)',
        '\\(H(p) = \\frac{' + str(d) + '}{' + str(a) + 'p^2+' + str(b) + 'p+' + str(c+1) + '}\\)',
    ]

    choix = random.sample(mauvaises, 3)

    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Canonique vers FT Ordre 2 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit un systeme du deuxieme ordre avec \\(K = ' + str(K) + '\\), \\(\\omega_n = ' + str(wn) + '\\) et \\(\\zeta = ' + str(zeta) + '\\). Quelle est \\(H(p)\\) ?</text></questiontext>\n')
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
