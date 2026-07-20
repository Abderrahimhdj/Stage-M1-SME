import random
import math

f = open("/Users/macbookpro/Desktop/stage_sme/FT_k_tau.xml", "w")
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<quiz>\n')

total = 0

CD_START = '<![CDATA['
CD_END = ']]>'

# ============================================================
# Ordre 1 : H(p) = c/(ap+b) -> K = c/b, tau = a/b
# ============================================================
for i in range(1):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)

    K = round(c / b, 4)
    tau = round(a / b, 4)

    texte = (
        'Soit \\(H(p) = \\frac{' + str(c) + '}{' + str(a) + 'p+' + str(b) + '}\\). '
        'Donnez les parametres canoniques.'
        '<br/><br/>'
        '\\(K =\\) {1:NUMERICAL:=' + str(K) + ':0.001}'
        '<br/>'
        '\\(\\tau =\\) {1:NUMERICAL:=' + str(tau) + ':0.001}'
    )

    f.write('  <question type="cloze">\n')
    f.write('    <name><text>FT vers canonique Ordre 1 - Q' + str(i) + '</text></name>\n')
    f.write('    <questiontext format="html"><text>' + CD_START + texte + CD_END + '</text></questiontext>\n')
    f.write('  </question>\n')
    total += 1

# ============================================================
# Ordre 2 : H(p) = d/(ap²+bp+c) -> K = d/c, wn = sqrt(c/a), zeta = b/(2*sqrt(ac))
# ============================================================
for i in range(1):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)

    K = round(d / c, 4)
    wn = round(math.sqrt(c / a), 4)
    zeta = round(b / (2 * math.sqrt(a * c)), 4)

    texte = (
        'Soit \\(H(p) = \\frac{' + str(d) + '}{' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\). '
        'Donnez les parametres canoniques (3 chiffres apres la virgule).'
        '<br/><br/>'
        '\\(K =\\) {1:NUMERICAL:=' + str(K) + ':0.001}'
        '<br/>'
        '\\(\\omega_n =\\) {1:NUMERICAL:=' + str(wn) + ':0.001}'
        '<br/>'
        '\\(\\zeta =\\) {1:NUMERICAL:=' + str(zeta) + ':0.001}'
    )

    f.write('  <question type="cloze">\n')
    f.write('    <name><text>FT vers canonique Ordre 2 - Q' + str(i) + '</text></name>\n')
    f.write('    <questiontext format="html"><text>' + CD_START + texte + CD_END + '</text></questiontext>\n')
    f.write('  </question>\n')
    total += 1

f.write('</quiz>\n')
f.close()
print("Succes !")
print("Total : " + str(total) + " questions generees !")
