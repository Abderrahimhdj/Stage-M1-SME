# derniere version de code (ft - eq) avec mauvaises reponses variees - les deux sens
import random

f = open("/Users/macbookpro/Desktop/stage_sme/222.xml", "w")
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<quiz>\n')

total = 0

# ============================================================
# SENS 1 : Equation differentielle -> Fonction de transfert
# ============================================================

# Ordre 1 : dy/dt + ay = eu  ->  H(p) = e/(p+a)
for i in range(5):
    a = random.randint(2, 10)
    e = random.randint(1, 10)
    while e == a:
        e = random.randint(1, 10)

    mauvaises = [
        '\\(H(p) = \\frac{' + str(e) + '}{p-' + str(a) + '}\\)',
        '\\(H(p) = \\frac{1}{p+' + str(a) + '}\\)',
        '\\(H(p) = \\frac{' + str(a) + '}{p+' + str(e) + '}\\)',
        '\\(H(p) = \\frac{p}{p+' + str(a) + '}\\)',
        '\\(H(p) = \\frac{' + str(e) + '}{p^2+' + str(a) + '}\\)',
        '\\(H(p) = \\frac{' + str(e) + '}{p}\\)',
        '\\(H(p) = \\frac{' + str(e) + 'p}{p+' + str(a) + '}\\)',
        '\\(H(p) = \\frac{' + str(e) + '}{p+' + str(a+1) + '}\\)',
    ]

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

# Ordre 2 : d²y/dt² + a dy/dt + by = d_coef*du/dt + eu  ->  H(p) = (d_coef*p+e)/(p²+ap+b)
for i in range(5):
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    d_coef = random.randint(1, 10)
    e = random.randint(1, 10)

    mauvaises = [
        '\\(H(p) = \\frac{1}{p^2+' + str(a) + 'p+' + str(b) + '}\\)',
        '\\(H(p) = \\frac{' + str(d_coef) + 'p+' + str(e) + '}{p^2-' + str(a) + 'p+' + str(b) + '}\\)',
        '\\(H(p) = \\frac{' + str(e) + 'p+' + str(d_coef) + '}{p^2+' + str(a) + 'p+' + str(b) + '}\\)',
        '\\(H(p) = \\frac{' + str(d_coef) + 'p+' + str(e) + '}{p+' + str(a) + '}\\)',
        '\\(H(p) = \\frac{p^2+' + str(a) + 'p+' + str(b) + '}{' + str(d_coef) + 'p+' + str(e) + '}\\)',
        '\\(H(p) = \\frac{-' + str(d_coef) + 'p+' + str(e) + '}{p^2+' + str(a) + 'p+' + str(b) + '}\\)',
        '\\(H(p) = \\frac{' + str(e) + '}{p^2+' + str(a) + 'p+' + str(b) + '}\\)',
        '\\(H(p) = \\frac{' + str(d_coef) + 'p}{p^2+' + str(a) + 'p+' + str(b) + '}\\)',
    ]

    choix = random.sample(mauvaises, 3)

    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Eq->FT Ordre 2 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(\\frac{d^2y}{dt^2} + ' + str(a) + '\\frac{dy}{dt} + ' + str(b) + 'y = ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\). Quelle est \\(H(p)\\) ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(H(p) = \\frac{' + str(d_coef) + 'p+' + str(e) + '}{p^2+' + str(a) + 'p+' + str(b) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[0] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[1] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[2] + '</text></answer>\n')
    f.write('  </question>\n')
    total += 1

# Ordre 3 : H(p) = (f_coef*p²+d_coef*p+e)/(p³+ap²+bp+c)
for i in range(5):
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    c = random.randint(2, 10)
    f_coef = random.randint(1, 10)
    d_coef = random.randint(1, 10)
    e = random.randint(1, 10)

    mauvaises = [
        '\\(H(p) = \\frac{1}{p^3+' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\)',
        '\\(H(p) = \\frac{' + str(f_coef) + 'p^2+' + str(d_coef) + 'p+' + str(e) + '}{p^3-' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\)',
        '\\(H(p) = \\frac{' + str(e) + 'p^2+' + str(d_coef) + 'p+' + str(f_coef) + '}{p^3+' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\)',
        '\\(H(p) = \\frac{' + str(f_coef) + 'p^2+' + str(d_coef) + 'p+' + str(e) + '}{p^2+' + str(a) + 'p+' + str(b) + '}\\)',
        '\\(H(p) = \\frac{-' + str(f_coef) + 'p^2+' + str(d_coef) + 'p+' + str(e) + '}{p^3+' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\)',
        '\\(H(p) = \\frac{' + str(e) + '}{p^3+' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\)',
        '\\(H(p) = \\frac{' + str(f_coef) + 'p^2}{p^3+' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\)',
        '\\(H(p) = \\frac{' + str(d_coef) + 'p+' + str(e) + '}{p^3+' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\)',
    ]

    choix = random.sample(mauvaises, 3)

    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Eq->FT Ordre 3 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(\\frac{d^3y}{dt^3} + ' + str(a) + '\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(c) + 'y = ' + str(f_coef) + '\\frac{d^2u}{dt^2} + ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\). Quelle est \\(H(p)\\) ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(H(p) = \\frac{' + str(f_coef) + 'p^2+' + str(d_coef) + 'p+' + str(e) + '}{p^3+' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[0] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[1] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[2] + '</text></answer>\n')
    f.write('  </question>\n')
    total += 1

# Ordre 4 : H(p) = (g_coef*p³+f_coef*p²+d_coef*p+e)/(p⁴+ap³+bp²+cp+d)
for i in range(5):
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    c = random.randint(2, 10)
    d = random.randint(2, 10)
    g_coef = random.randint(1, 10)
    f_coef = random.randint(1, 10)
    d_coef = random.randint(1, 10)
    e = random.randint(1, 10)

    mauvaises = [
        '\\(H(p) = \\frac{1}{p^4+' + str(a) + 'p^3+' + str(b) + 'p^2+' + str(c) + 'p+' + str(d) + '}\\)',
        '\\(H(p) = \\frac{' + str(g_coef) + 'p^3+' + str(f_coef) + 'p^2+' + str(d_coef) + 'p+' + str(e) + '}{p^4-' + str(a) + 'p^3+' + str(b) + 'p^2+' + str(c) + 'p+' + str(d) + '}\\)',
        '\\(H(p) = \\frac{' + str(e) + 'p^3+' + str(d_coef) + 'p^2+' + str(f_coef) + 'p+' + str(g_coef) + '}{p^4+' + str(a) + 'p^3+' + str(b) + 'p^2+' + str(c) + 'p+' + str(d) + '}\\)',
        '\\(H(p) = \\frac{' + str(g_coef) + 'p^3+' + str(f_coef) + 'p^2+' + str(d_coef) + 'p+' + str(e) + '}{p^3+' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\)',
        '\\(H(p) = \\frac{-' + str(g_coef) + 'p^3+' + str(f_coef) + 'p^2+' + str(d_coef) + 'p+' + str(e) + '}{p^4+' + str(a) + 'p^3+' + str(b) + 'p^2+' + str(c) + 'p+' + str(d) + '}\\)',
        '\\(H(p) = \\frac{' + str(e) + '}{p^4+' + str(a) + 'p^3+' + str(b) + 'p^2+' + str(c) + 'p+' + str(d) + '}\\)',
        '\\(H(p) = \\frac{' + str(f_coef) + 'p^2+' + str(d_coef) + 'p+' + str(e) + '}{p^4+' + str(a) + 'p^3+' + str(b) + 'p^2+' + str(c) + 'p+' + str(d) + '}\\)',
        '\\(H(p) = \\frac{' + str(g_coef) + 'p^3+' + str(f_coef) + 'p^2+' + str(d_coef) + 'p+' + str(e) + '}{p^4+' + str(b) + 'p^3+' + str(a) + 'p^2+' + str(c) + 'p+' + str(d) + '}\\)',
    ]

    choix = random.sample(mauvaises, 3)

    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Eq->FT Ordre 4 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(\\frac{d^4y}{dt^4} + ' + str(a) + '\\frac{d^3y}{dt^3} + ' + str(b) + '\\frac{d^2y}{dt^2} + ' + str(c) + '\\frac{dy}{dt} + ' + str(d) + 'y = ' + str(g_coef) + '\\frac{d^3u}{dt^3} + ' + str(f_coef) + '\\frac{d^2u}{dt^2} + ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\). Quelle est \\(H(p)\\) ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(H(p) = \\frac{' + str(g_coef) + 'p^3+' + str(f_coef) + 'p^2+' + str(d_coef) + 'p+' + str(e) + '}{p^4+' + str(a) + 'p^3+' + str(b) + 'p^2+' + str(c) + 'p+' + str(d) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[0] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[1] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[2] + '</text></answer>\n')
    f.write('  </question>\n')
    total += 1

# ============================================================
# SENS 2 : Fonction de transfert -> Equation differentielle
# ============================================================

# Ordre 1 inverse : H(p) = e/(p+a)  ->  dy/dt + ay = eu
for i in range(5):
    a = random.randint(2, 10)
    e = random.randint(1, 10)
    while e == a:
        e = random.randint(1, 10)

    mauvaises = [
        '\\(\\frac{dy}{dt} - ' + str(a) + 'y = ' + str(e) + 'u\\)',
        '\\(\\frac{dy}{dt} + ' + str(a) + 'y = u\\)',
        '\\(\\frac{dy}{dt} + ' + str(e) + 'y = ' + str(a) + 'u\\)',
        '\\(\\frac{d^2y}{dt^2} + ' + str(a) + 'y = ' + str(e) + 'u\\)',
        '\\(' + str(e) + '\\frac{dy}{dt} + ' + str(a) + 'y = u\\)',
        '\\(\\frac{dy}{dt} + ' + str(a) + 'y = 0\\)',
        '\\(\\frac{dy}{dt} + ' + str(a+1) + 'y = ' + str(e) + 'u\\)',
        '\\(\\frac{dy}{dt} + ' + str(a) + 'y = ' + str(e) + 'u + 1\\)',
    ]

    choix = random.sample(mauvaises, 3)

    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>FT->Eq Ordre 1 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(H(p) = \\frac{' + str(e) + '}{p+' + str(a) + '}\\). Quelle est l\'équation différentielle correspondante ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(\\frac{dy}{dt} + ' + str(a) + 'y = ' + str(e) + 'u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[0] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[1] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[2] + '</text></answer>\n')
    f.write('  </question>\n')
    total += 1

# Ordre 2 inverse : H(p) = (d_coef*p+e)/(p²+ap+b)  ->  d²y/dt² + ady/dt + by = d_coef*du/dt + eu
for i in range(5):
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    d_coef = random.randint(1, 10)
    e = random.randint(1, 10)

    mauvaises = [
        '\\(\\frac{d^2y}{dt^2} - ' + str(a) + '\\frac{dy}{dt} + ' + str(b) + 'y = ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\)',
        '\\(\\frac{d^2y}{dt^2} + ' + str(a) + '\\frac{dy}{dt} + ' + str(b) + 'y = u\\)',
        '\\(\\frac{d^2y}{dt^2} + ' + str(a) + '\\frac{dy}{dt} + ' + str(b) + 'y = ' + str(e) + '\\frac{du}{dt} + ' + str(d_coef) + 'u\\)',
        '\\(\\frac{dy}{dt} + ' + str(a) + 'y = ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\)',
        '\\(\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(a) + 'y = ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\)',
        '\\(\\frac{d^2y}{dt^2} + ' + str(a) + '\\frac{dy}{dt} + ' + str(b) + 'y = 0\\)',
        '\\(\\frac{d^2y}{dt^2} + ' + str(a) + '\\frac{dy}{dt} + ' + str(b) + 'y = ' + str(d_coef) + 'u\\)',
        '\\(\\frac{d^2y}{dt^2} + ' + str(a) + '\\frac{dy}{dt} + ' + str(b) + 'y = ' + str(d_coef) + '\\frac{du}{dt}\\)',
    ]

    choix = random.sample(mauvaises, 3)

    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>FT->Eq Ordre 2 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(H(p) = \\frac{' + str(d_coef) + 'p+' + str(e) + '}{p^2+' + str(a) + 'p+' + str(b) + '}\\). Quelle est l\'équation différentielle correspondante ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(\\frac{d^2y}{dt^2} + ' + str(a) + '\\frac{dy}{dt} + ' + str(b) + 'y = ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[0] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[1] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[2] + '</text></answer>\n')
    f.write('  </question>\n')
    total += 1

# Ordre 3 inverse : H(p) = (f_coef*p²+d_coef*p+e)/(p³+ap²+bp+c)
for i in range(5):
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    c = random.randint(2, 10)
    f_coef = random.randint(1, 10)
    d_coef = random.randint(1, 10)
    e = random.randint(1, 10)

    mauvaises = [
        '\\(\\frac{d^3y}{dt^3} - ' + str(a) + '\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(c) + 'y = ' + str(f_coef) + '\\frac{d^2u}{dt^2} + ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\)',
        '\\(\\frac{d^3y}{dt^3} + ' + str(a) + '\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(c) + 'y = u\\)',
        '\\(\\frac{d^3y}{dt^3} + ' + str(a) + '\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(c) + 'y = ' + str(e) + '\\frac{d^2u}{dt^2} + ' + str(d_coef) + '\\frac{du}{dt} + ' + str(f_coef) + 'u\\)',
        '\\(\\frac{d^2y}{dt^2} + ' + str(a) + '\\frac{dy}{dt} + ' + str(b) + 'y = ' + str(f_coef) + '\\frac{d^2u}{dt^2} + ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\)',
        '\\(\\frac{d^3y}{dt^3} + ' + str(c) + '\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(a) + 'y = ' + str(f_coef) + '\\frac{d^2u}{dt^2} + ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\)',
        '\\(\\frac{d^3y}{dt^3} + ' + str(a) + '\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(c) + 'y = 0\\)',
        '\\(\\frac{d^3y}{dt^3} + ' + str(a) + '\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(c) + 'y = ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\)',
        '\\(\\frac{d^3y}{dt^3} + ' + str(a) + '\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(c) + 'y = ' + str(f_coef) + '\\frac{d^2u}{dt^2} + ' + str(e) + 'u\\)',
    ]

    choix = random.sample(mauvaises, 3)

    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>FT->Eq Ordre 3 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(H(p) = \\frac{' + str(f_coef) + 'p^2+' + str(d_coef) + 'p+' + str(e) + '}{p^3+' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\). Quelle est l\'équation différentielle correspondante ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(\\frac{d^3y}{dt^3} + ' + str(a) + '\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(c) + 'y = ' + str(f_coef) + '\\frac{d^2u}{dt^2} + ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[0] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[1] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[2] + '</text></answer>\n')
    f.write('  </question>\n')
    total += 1

# Ordre 4 inverse : H(p) = (g_coef*p³+f_coef*p²+d_coef*p+e)/(p⁴+ap³+bp²+cp+d)
for i in range(5):
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    c = random.randint(2, 10)
    d = random.randint(2, 10)
    g_coef = random.randint(1, 10)
    f_coef = random.randint(1, 10)
    d_coef = random.randint(1, 10)
    e = random.randint(1, 10)

    mauvaises = [
        '\\(\\frac{d^4y}{dt^4} - ' + str(a) + '\\frac{d^3y}{dt^3} + ' + str(b) + '\\frac{d^2y}{dt^2} + ' + str(c) + '\\frac{dy}{dt} + ' + str(d) + 'y = ' + str(g_coef) + '\\frac{d^3u}{dt^3} + ' + str(f_coef) + '\\frac{d^2u}{dt^2} + ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\)',
        '\\(\\frac{d^4y}{dt^4} + ' + str(a) + '\\frac{d^3y}{dt^3} + ' + str(b) + '\\frac{d^2y}{dt^2} + ' + str(c) + '\\frac{dy}{dt} + ' + str(d) + 'y = u\\)',
        '\\(\\frac{d^4y}{dt^4} + ' + str(a) + '\\frac{d^3y}{dt^3} + ' + str(b) + '\\frac{d^2y}{dt^2} + ' + str(c) + '\\frac{dy}{dt} + ' + str(d) + 'y = ' + str(e) + '\\frac{d^3u}{dt^3} + ' + str(d_coef) + '\\frac{d^2u}{dt^2} + ' + str(f_coef) + '\\frac{du}{dt} + ' + str(g_coef) + 'u\\)',
        '\\(\\frac{d^3y}{dt^3} + ' + str(a) + '\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(c) + 'y = ' + str(g_coef) + '\\frac{d^3u}{dt^3} + ' + str(f_coef) + '\\frac{d^2u}{dt^2} + ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\)',
        '\\(\\frac{d^4y}{dt^4} + ' + str(d) + '\\frac{d^3y}{dt^3} + ' + str(c) + '\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(a) + 'y = ' + str(g_coef) + '\\frac{d^3u}{dt^3} + ' + str(f_coef) + '\\frac{d^2u}{dt^2} + ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\)',
        '\\(\\frac{d^4y}{dt^4} + ' + str(a) + '\\frac{d^3y}{dt^3} + ' + str(b) + '\\frac{d^2y}{dt^2} + ' + str(c) + '\\frac{dy}{dt} + ' + str(d) + 'y = 0\\)',
        '\\(\\frac{d^4y}{dt^4} + ' + str(a) + '\\frac{d^3y}{dt^3} + ' + str(b) + '\\frac{d^2y}{dt^2} + ' + str(c) + '\\frac{dy}{dt} + ' + str(d) + 'y = ' + str(f_coef) + '\\frac{d^2u}{dt^2} + ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\)',
        '\\(\\frac{d^4y}{dt^4} + ' + str(a) + '\\frac{d^3y}{dt^3} + ' + str(b) + '\\frac{d^2y}{dt^2} + ' + str(c) + '\\frac{dy}{dt} + ' + str(d) + 'y = ' + str(g_coef) + '\\frac{d^3u}{dt^3} + ' + str(e) + 'u\\)',
    ]

    choix = random.sample(mauvaises, 3)

    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>FT->Eq Ordre 4 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(H(p) = \\frac{' + str(g_coef) + 'p^3+' + str(f_coef) + 'p^2+' + str(d_coef) + 'p+' + str(e) + '}{p^4+' + str(a) + 'p^3+' + str(b) + 'p^2+' + str(c) + 'p+' + str(d) + '}\\). Quelle est l\'équation différentielle correspondante ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(\\frac{d^4y}{dt^4} + ' + str(a) + '\\frac{d^3y}{dt^3} + ' + str(b) + '\\frac{d^2y}{dt^2} + ' + str(c) + '\\frac{dy}{dt} + ' + str(d) + 'y = ' + str(g_coef) + '\\frac{d^3u}{dt^3} + ' + str(f_coef) + '\\frac{d^2u}{dt^2} + ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[0] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[1] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[2] + '</text></answer>\n')
    f.write('  </question>\n')
    total += 1

f.write('</quiz>\n')
f.close()
print("Succes !")
print("Total : " + str(total) + " questions generees !")
