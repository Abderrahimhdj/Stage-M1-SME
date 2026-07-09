import random

f = open("/Users/macbookpro/Desktop/stage_sme/nvqs.xml", "w")
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<quiz>\n')

total = 0

# ============================================================
# SENS 1 : Equation differentielle -> Fonction de transfert
# ============================================================

"""
# Ordre 1 : dy/dt + ay = u  ->  H(p) = 1/(p+a)
for i in range(5):
    a = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Eq->FT Ordre 1 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(\\frac{dy}{dt} + ' + str(a) + 'y = u\\). Quelle est \\(H(p)\\) ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(H(p) = \\frac{1}{p+' + str(a) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{1}{p-' + str(a) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{1}{' + str(a) + 'p+1}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{p}{p+' + str(a) + '}\\)</text></answer>\n')
    f.write('  </question>\n')
    total += 1
''
# Ordre 2 : d²y/dt² + a dy/dt + by = u  ->  H(p) = 1/(p²+ap+b)
for i in range(5):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Eq->FT Ordre 2 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(\\frac{d^2y}{dt^2} + ' + str(a) + '\\frac{dy}{dt} + ' + str(b) + 'y = u\\). Quelle est \\(H(p)\\) ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(H(p) = \\frac{1}{p^2+' + str(a) + 'p+' + str(b) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{1}{p^2-' + str(a) + 'p+' + str(b) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{1}{p+' + str(a) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{p}{p^2+' + str(a) + 'p+' + str(b) + '}\\)</text></answer>\n')
    f.write('  </question>\n')
    total += 1

# Ordre 3 : d³y/dt³ + a d²y/dt² + b dy/dt + cy = u  ->  H(p) = 1/(p³+ap²+bp+c)
for i in range(5):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Eq->FT Ordre 3 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(\\frac{d^3y}{dt^3} + ' + str(a) + '\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(c) + 'y = u\\). Quelle est \\(H(p)\\) ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(H(p) = \\frac{1}{p^3+' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{1}{p^3-' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{1}{p^2+' + str(a) + 'p+' + str(b) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{p}{p^3+' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\)</text></answer>\n')
    f.write('  </question>\n')
    total += 1

# Ordre 4
for i in range(5):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Eq->FT Ordre 4 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(\\frac{d^4y}{dt^4} + ' + str(a) + '\\frac{d^3y}{dt^3} + ' + str(b) + '\\frac{d^2y}{dt^2} + ' + str(c) + '\\frac{dy}{dt} + ' + str(d) + 'y = u\\). Quelle est \\(H(p)\\) ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(H(p) = \\frac{1}{p^4+' + str(a) + 'p^3+' + str(b) + 'p^2+' + str(c) + 'p+' + str(d) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{1}{p^4-' + str(a) + 'p^3+' + str(b) + 'p^2+' + str(c) + 'p+' + str(d) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{1}{p^3+' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(H(p) = \\frac{p}{p^4+' + str(a) + 'p^3+' + str(b) + 'p^2+' + str(c) + 'p+' + str(d) + '}\\)</text></answer>\n')
    f.write('  </question>\n')
    total += 1

# ============================================================
# SENS 2 : Fonction de transfert -> Equation differentielle
# ============================================================

# Ordre 1 inverse
for i in range(5):
    a = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>FT->Eq Ordre 1 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(H(p) = \\frac{1}{p+' + str(a) + '}\\). Quelle est l\'équation différentielle correspondante ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(\\frac{dy}{dt} + ' + str(a) + 'y = u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{dy}{dt} - ' + str(a) + 'y = u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(' + str(a) + '\\frac{dy}{dt} + y = u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{d^2y}{dt^2} + ' + str(a) + 'y = u\\)</text></answer>\n')
    f.write('  </question>\n')
    total += 1

# Ordre 2 inverse
for i in range(5):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>FT->Eq Ordre 2 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(H(p) = \\frac{1}{p^2+' + str(a) + 'p+' + str(b) + '}\\). Quelle est l\'équation différentielle correspondante ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(\\frac{d^2y}{dt^2} + ' + str(a) + '\\frac{dy}{dt} + ' + str(b) + 'y = u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{d^2y}{dt^2} - ' + str(a) + '\\frac{dy}{dt} + ' + str(b) + 'y = u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{dy}{dt} + ' + str(a) + 'y = u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(a) + 'y = u\\)</text></answer>\n')
    f.write('  </question>\n')
    total += 1

# Ordre 3 inverse
for i in range(5):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>FT->Eq Ordre 3 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(H(p) = \\frac{1}{p^3+' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\). Quelle est l\'équation différentielle correspondante ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(\\frac{d^3y}{dt^3} + ' + str(a) + '\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(c) + 'y = u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{d^3y}{dt^3} - ' + str(a) + '\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(c) + 'y = u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{d^2y}{dt^2} + ' + str(a) + '\\frac{dy}{dt} + ' + str(b) + 'y = u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{d^3y}{dt^3} + ' + str(c) + '\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(a) + 'y = u\\)</text></answer>\n')
    f.write('  </question>\n')
    total += 1
"""
# Ordre 4 inverse
for i in range(1):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>FT->Eq Ordre 4 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>Soit \\(H(p) = \\frac{1}{p^4+' + str(a) + 'p^3+' + str(b) + 'p^2+' + str(c) + 'p+' + str(d) + '}\\). Quelle est l\'équation différentielle correspondante ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>\\(\\frac{d^4y}{dt^4} + ' + str(a) + '\\frac{d^3y}{dt^3} + ' + str(b) + '\\frac{d^2y}{dt^2} + ' + str(c) + '\\frac{dy}{dt} + ' + str(d) + 'y = u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{d^4y}{dt^4} - ' + str(a) + '\\frac{d^3y}{dt^3} + ' + str(b) + '\\frac{d^2y}{dt^2} + ' + str(c) + '\\frac{dy}{dt} + ' + str(d) + 'y = u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{d^3y}{dt^3} + ' + str(a) + '\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(c) + 'y = u\\)</text></answer>\n')
    f.write('    <answer fraction="0"><text>\\(\\frac{d^4y}{dt^4} + ' + str(d) + '\\frac{d^3y}{dt^3} + ' + str(c) + '\\frac{d^2y}{dt^2} + ' + str(b) + '\\frac{dy}{dt} + ' + str(a) + 'y = u\\)</text></answer>\n')
    f.write('  </question>\n')
    total += 1

f.write('</quiz>\n')
f.close()
print("Succes !")
print("Total : " + str(total) + " questions generees !")
