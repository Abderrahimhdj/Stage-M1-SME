# derniere version de code (ft - eq)
import random

f = open("/Users/macbookpro/Desktop/stage_sme/222.xml", "w")
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<quiz>\n')

total = 0

# ============================================================
# SENS 1 : Equation differentielle -> Fonction de transfert
# ============================================================

# Ordre 1 : dy/dt + ay = eu  ->  H(p) = e/(p+a)
for i in range(1):
    a = random.randint(1, 10)
    e = random.randint(1, 10)
    while e == a:  # eviter que la mauvaise reponse soit identique a la bonne
        e = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Eq->FT Ordre 1 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(\\frac{dy}{dt} + ' + str(a) + 'y = ' + str(e) + 'u\\). Quelle est \\(H(p)\\) ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(H(p) = \\frac{' + str(e) + '}{p+' + str(a) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{1}{p+' + str(a) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{' + str(e) + '}{p-' + str(a) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{' + str(a) + '}{p+' + str(e) + '}\\)</text></answer>\n')
    f.write('  </question>\n')
    total += 1

# Ordre 2 : d²y/dt² + a dy/dt + by = d_coef*du/dt + eu  ->  H(p) = (d_coef*p+e)/(p²+ap+b)
for i in range(1):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    d_coef = random.randint(1, 10)
    e = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Eq->FT Ordre 2 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(\\frac{d^2y}{dt^2} + ' + str(a) + '\\frac{dy}{dt} + ' + str(b) + 'y = ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\). Quelle est \\(H(p)\\) ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(H(p) = \\frac{' + str(d_coef) + 'p+' + str(e) + '}{p^2+' + str(a) + 'p+' + str(b) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{1}{p^2+' + str(a) + 'p+' + str(b) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{' + str(d_coef) + 'p+' + str(e) + '}{p^2-' + str(a) + 'p+' + str(b) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{' + str(e) + 'p+' + str(d_coef) + '}{p^2+' + str(a) + 'p+' + str(b) + '}\\)</text></answer>\n')
    f.write('  </question>\n')
    total += 1

# Ordre 3 : d³y/dt³ + a d²y/dt² + b dy/dt + cy = f_coef*d²u/dt² + d_coef*du/dt + eu
# H(p) = (f_coef*p²+d_coef*p+e)/(p³+ap²+bp+c)
for i in range(1):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    f_coef = random.randint(1, 10)
    d_coef = random.randint(1, 10)
    e = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Eq->FT Ordre 3 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(\\frac{d^3y}{dt^3} + ' + str(a) + '\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(c) + 'y = ' + str(f_coef) + '\\frac{d^2u}{dt^2} + ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\). Quelle est \\(H(p)\\) ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(H(p) = \\frac{' + str(f_coef) + 'p^2+' + str(d_coef) + 'p+' + str(e) + '}{p^3+' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{1}{p^3+' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{' + str(f_coef) + 'p^2+' + str(d_coef) + 'p+' + str(e) + '}{p^3-' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{' + str(e) + 'p^2+' + str(d_coef) + 'p+' + str(f_coef) + '}{p^3+' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\)</text></answer>\n')
    f.write('  </question>\n')
    total += 1

# Ordre 4 : H(p) = (g_coef*p³+f_coef*p²+d_coef*p+e)/(p⁴+ap³+bp²+cp+d)
for i in range(1):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    g_coef = random.randint(1, 10)
    f_coef = random.randint(1, 10)
    d_coef = random.randint(1, 10)
    e = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Eq->FT Ordre 4 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(\\frac{d^4y}{dt^4} + ' + str(a) + '\\frac{d^3y}{dt^3} + ' + str(b) + '\\frac{d^2y}{dt^2} + ' + str(c) + '\\frac{dy}{dt} + ' + str(d) + 'y = ' + str(g_coef) + '\\frac{d^3u}{dt^3} + ' + str(f_coef) + '\\frac{d^2u}{dt^2} + ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\). Quelle est \\(H(p)\\) ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(H(p) = \\frac{' + str(g_coef) + 'p^3+' + str(f_coef) + 'p^2+' + str(d_coef) + 'p+' + str(e) + '}{p^4+' + str(a) + 'p^3+' + str(b) + 'p^2+' + str(c) + 'p+' + str(d) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{1}{p^4+' + str(a) + 'p^3+' + str(b) + 'p^2+' + str(c) + 'p+' + str(d) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{' + str(g_coef) + 'p^3+' + str(f_coef) + 'p^2+' + str(d_coef) + 'p+' + str(e) + '}{p^4-' + str(a) + 'p^3+' + str(b) + 'p^2+' + str(c) + 'p+' + str(d) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{' + str(e) + 'p^3+' + str(d_coef) + 'p^2+' + str(f_coef) + 'p+' + str(g_coef) + '}{p^4+' + str(a) + 'p^3+' + str(b) + 'p^2+' + str(c) + 'p+' + str(d) + '}\\)</text></answer>\n')
    f.write('  </question>\n')
    total += 1

# ============================================================
# SENS 2 : Fonction de transfert -> Equation differentielle
# ============================================================
"""
# Ordre 1 inverse : H(p) = e/(p+a)  ->  dy/dt + ay = eu
for i in range(1):
    a = random.randint(1, 10)
    e = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>FT->Eq Ordre 1 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(H(p) = \\frac{' + str(e) + '}{p+' + str(a) + '}\\). Quelle est l\'équation différentielle correspondante ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(\\frac{dy}{dt} + ' + str(a) + 'y = ' + str(e) + 'u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{dy}{dt} + ' + str(a) + 'y = u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{dy}{dt} - ' + str(a) + 'y = ' + str(e) + 'u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{dy}{dt} + ' + str(e) + 'y = ' + str(a) + 'u\\)</text></answer>\n')
    f.write('  </question>\n')
    total += 1

# Ordre 2 inverse : H(p) = (d_coef*p+e)/(p²+ap+b)  ->  d²y/dt² + ady/dt + by = d_coef*du/dt + eu
for i in range(1):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    d_coef = random.randint(1, 10)
    e = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>FT->Eq Ordre 2 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(H(p) = \\frac{' + str(d_coef) + 'p+' + str(e) + '}{p^2+' + str(a) + 'p+' + str(b) + '}\\). Quelle est l\'équation différentielle correspondante ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(\\frac{d^2y}{dt^2} + ' + str(a) + '\\frac{dy}{dt} + ' + str(b) + 'y = ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{d^2y}{dt^2} + ' + str(a) + '\\frac{dy}{dt} + ' + str(b) + 'y = u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{d^2y}{dt^2} - ' + str(a) + '\\frac{dy}{dt} + ' + str(b) + 'y = ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{d^2y}{dt^2} + ' + str(a) + '\\frac{dy}{dt} + ' + str(b) + 'y = ' + str(e) + '\\frac{du}{dt} + ' + str(d_coef) + 'u\\)</text></answer>\n')
    f.write('  </question>\n')
    total += 1

# Ordre 3 inverse : H(p) = (f_coef*p²+d_coef*p+e)/(p³+ap²+bp+c)
for i in range(1):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    f_coef = random.randint(1, 10)
    d_coef = random.randint(1, 10)
    e = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>FT->Eq Ordre 3 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(H(p) = \\frac{' + str(f_coef) + 'p^2+' + str(d_coef) + 'p+' + str(e) + '}{p^3+' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\). Quelle est l\'équation différentielle correspondante ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(\\frac{d^3y}{dt^3} + ' + str(a) + '\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(c) + 'y = ' + str(f_coef) + '\\frac{d^2u}{dt^2} + ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{d^3y}{dt^3} + ' + str(a) + '\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(c) + 'y = u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{d^3y}{dt^3} - ' + str(a) + '\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(c) + 'y = ' + str(f_coef) + '\\frac{d^2u}{dt^2} + ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{d^3y}{dt^3} + ' + str(a) + '\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(c) + 'y = ' + str(e) + '\\frac{d^2u}{dt^2} + ' + str(d_coef) + '\\frac{du}{dt} + ' + str(f_coef) + 'u\\)</text></answer>\n')
    f.write('  </question>\n')
    total += 1

# Ordre 4 inverse : H(p) = (g_coef*p³+f_coef*p²+d_coef*p+e)/(p⁴+ap³+bp²+cp+d)
for i in range(1):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    g_coef = random.randint(1, 10)
    f_coef = random.randint(1, 10)
    d_coef = random.randint(1, 10)
    e = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>FT->Eq Ordre 4 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(H(p) = \\frac{' + str(g_coef) + 'p^3+' + str(f_coef) + 'p^2+' + str(d_coef) + 'p+' + str(e) + '}{p^4+' + str(a) + 'p^3+' + str(b) + 'p^2+' + str(c) + 'p+' + str(d) + '}\\). Quelle est l\'équation différentielle correspondante ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(\\frac{d^4y}{dt^4} + ' + str(a) + '\\frac{d^3y}{dt^3} + ' + str(b) + '\\frac{d^2y}{dt^2} + ' + str(c) + '\\frac{dy}{dt} + ' + str(d) + 'y = ' + str(g_coef) + '\\frac{d^3u}{dt^3} + ' + str(f_coef) + '\\frac{d^2u}{dt^2} + ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{d^4y}{dt^4} + ' + str(a) + '\\frac{d^3y}{dt^3} + ' + str(b) + '\\frac{d^2y}{dt^2} + ' + str(c) + '\\frac{dy}{dt} + ' + str(d) + 'y = u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{d^4y}{dt^4} - ' + str(a) + '\\frac{d^3y}{dt^3} + ' + str(b) + '\\frac{d^2y}{dt^2} + ' + str(c) + '\\frac{dy}{dt} + ' + str(d) + 'y = ' + str(g_coef) + '\\frac{d^3u}{dt^3} + ' + str(f_coef) + '\\frac{d^2u}{dt^2} + ' + str(d_coef) + '\\frac{du}{dt} + ' + str(e) + 'u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{d^4y}{dt^4} + ' + str(a) + '\\frac{d^3y}{dt^3} + ' + str(b) + '\\frac{d^2y}{dt^2} + ' + str(c) + '\\frac{dy}{dt} + ' + str(d) + 'y = ' + str(e) + '\\frac{d^3u}{dt^3} + ' + str(d_coef) + '\\frac{d^2u}{dt^2} + ' + str(f_coef) + '\\frac{du}{dt} + ' + str(g_coef) + 'u\\)</text></answer>\n')
    f.write('  </question>\n')
    total += 1
"""
f.write('</quiz>\n')
f.close()
print("Succes !")
print("Total : " + str(total) + " questions generees !")
