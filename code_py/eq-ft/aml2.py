import random

f = open("/Users/macbookpro/Desktop/stage_sme/questions.xml", "w")
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<quiz>\n')
total = 0

#----------------------------------------------------------
# Equation differentielle -> Fonction de transfert
#----------------------------------------------------------

# Ordre 1 : dy/dt + ay = u  ->  H(p) = 1/(p+a)
for i in range(2):
    a = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    total += 1
    f.write('    <name><text>Eq->FT Ordre 1 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext><text>Soit dy/dt + ' + str(a) + 'y = u. Quelle est H(p) ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>H(p) = 1/(p+' + str(a) + ')</text></answer>\n')
    f.write('    <answer fraction="0"><text>H(p) = 1/(p-' + str(a) + ')</text></answer>\n')
    f.write('    <answer fraction="0"><text>H(p) = 1/(' + str(a) + 'p+1)</text></answer>\n')
    f.write('    <answer fraction="0"><text>H(p) = p/(p+' + str(a) + ')</text></answer>\n')
    f.write('  </question>\n')

# Ordre 2 : d²y/dt² + a dy/dt + by = u  ->  H(p) = 1/(p²+ap+b)
for i in range(2):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    total += 1
    f.write('    <name><text>Eq->FT Ordre 2 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext><text>Soit d²y/dt² + ' + str(a) + ' dy/dt + ' + str(b) + 'y = u. Quelle est H(p) ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>H(p) = 1/(p²+' + str(a) + 'p+' + str(b) + ')</text></answer>\n')
    f.write('    <answer fraction="0"><text>H(p) = 1/(p²-' + str(a) + 'p+' + str(b) + ')</text></answer>\n')
    f.write('    <answer fraction="0"><text>H(p) = 1/(p+' + str(a) + ')</text></answer>\n')
    f.write('    <answer fraction="0"><text>H(p) = p/(p²+' + str(a) + 'p+' + str(b) + ')</text></answer>\n')
    f.write('  </question>\n')

# Ordre 3 : d³y/dt³ + a d²y/dt² + b dy/dt + cy = u  ->  H(p) = 1/(p³+ap²+bp+c)
for i in range(2):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    total += 1
    f.write('    <name><text>Eq->FT Ordre 3 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext><text>Soit d³y/dt³ + ' + str(a) + ' d²y/dt² + ' + str(b) + ' dy/dt + ' + str(c) + 'y = u. Quelle est H(p) ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>H(p) = 1/(p³+' + str(a) + 'p²+' + str(b) + 'p+' + str(c) + ')</text></answer>\n')
    f.write('    <answer fraction="0"><text>H(p) = 1/(p³-' + str(a) + 'p²+' + str(b) + 'p+' + str(c) + ')</text></answer>\n')
    f.write('    <answer fraction="0"><text>H(p) = 1/(p²+' + str(a) + 'p+' + str(b) + ')</text></answer>\n')
    f.write('    <answer fraction="0"><text>H(p) = p/(p³+' + str(a) + 'p²+' + str(b) + 'p+' + str(c) + ')</text></answer>\n')
    f.write('  </question>\n')

# Ordre 4 : d⁴y/dt⁴ + a d³y/dt³ + b d²y/dt² + c dy/dt + dy = u
for i in range(2):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    total += 1
    f.write('    <name><text>Eq->FT Ordre 4 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext><text>Soit d⁴y/dt⁴ + ' + str(a) + ' d³y/dt³ + ' + str(b) + ' d²y/dt² + ' + str(c) + ' dy/dt + ' + str(d) + 'y = u. Quelle est H(p) ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>H(p) = 1/(p⁴+' + str(a) + 'p³+' + str(b) + 'p²+' + str(c) + 'p+' + str(d) + ')</text></answer>\n')
    f.write('    <answer fraction="0"><text>H(p) = 1/(p⁴-' + str(a) + 'p³+' + str(b) + 'p²+' + str(c) + 'p+' + str(d) + ')</text></answer>\n')
    f.write('    <answer fraction="0"><text>H(p) = 1/(p³+' + str(a) + 'p²+' + str(b) + 'p+' + str(c) + ')</text></answer>\n')
    f.write('    <answer fraction="0"><text>H(p) = p/(p⁴+' + str(a) + 'p³+' + str(b) + 'p²+' + str(c) + 'p+' + str(d) + ')</text></answer>\n')
    f.write('  </question>\n')

# ------------------------------------------------------------
# Fonction de transfert -> Equation differentielle
# ------------------------------------------------------------

# Ordre 1 inverse
for i in range(2):
    a = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    total += 1
    f.write('    <name><text>FT->Eq Ordre 1 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext><text>Soit H(p) = 1/(p+' + str(a) + '). Quelle est l equation differentielle ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>dy/dt + ' + str(a) + 'y = u</text></answer>\n')
    f.write('    <answer fraction="0"><text>dy/dt - ' + str(a) + 'y = u</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + str(a) + ' dy/dt + y = u</text></answer>\n')
    f.write('    <answer fraction="0"><text>d²y/dt² + ' + str(a) + 'y = u</text></answer>\n')
    f.write('  </question>\n')

# Ordre 2 inverse
for i in range(2):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    total += 1
    f.write('    <name><text>FT->Eq Ordre 2 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext><text>Soit H(p) = 1/(p²+' + str(a) + 'p+' + str(b) + '). Quelle est l equation differentielle ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>d²y/dt² + ' + str(a) + ' dy/dt + ' + str(b) + 'y = u</text></answer>\n')
    f.write('    <answer fraction="0"><text>d²y/dt² - ' + str(a) + ' dy/dt + ' + str(b) + 'y = u</text></answer>\n')
    f.write('    <answer fraction="0"><text>dy/dt + ' + str(a) + 'y = u</text></answer>\n')
    f.write('    <answer fraction="0"><text>d²y/dt² + ' + str(b) + ' dy/dt + ' + str(a) + 'y = u</text></answer>\n')
    f.write('  </question>\n')

# Ordre 3 inverse
for i in range(2):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    total += 1
    f.write('    <name><text>FT->Eq Ordre 3 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext><text>Soit H(p) = 1/(p³+' + str(a) + 'p²+' + str(b) + 'p+' + str(c) + '). Quelle est l equation differentielle ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>d³y/dt³ + ' + str(a) + ' d²y/dt² + ' + str(b) + ' dy/dt + ' + str(c) + 'y = u</text></answer>\n')
    f.write('    <answer fraction="0"><text>d³y/dt³ - ' + str(a) + ' d²y/dt² + ' + str(b) + ' dy/dt + ' + str(c) + 'y = u</text></answer>\n')
    f.write('    <answer fraction="0"><text>d²y/dt² + ' + str(a) + ' dy/dt + ' + str(b) + 'y = u</text></answer>\n')
    f.write('    <answer fraction="0"><text>d³y/dt³ + ' + str(c) + ' d²y/dt² + ' + str(b) + ' dy/dt + ' + str(a) + 'y = u</text></answer>\n')
    f.write('  </question>\n')

# Ordre 4 inverse
for i in range(2):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    f.write('  <question type="multichoice">\n')
    total += 1
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <name><text>FT->Eq Ordre 4 - Q' + str(i) + '</text></name>\n')
    f.write('    <questiontext><text>Soit H(p) = 1/(p⁴+' + str(a) + 'p³+' + str(b) + 'p²+' + str(c) + 'p+' + str(d) + '). Quelle est l equation differentielle ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>d⁴y/dt⁴ + ' + str(a) + ' d³y/dt³ + ' + str(b) + ' d²y/dt² + ' + str(c) + ' dy/dt + ' + str(d) + 'y = u</text></answer>\n')
    f.write('    <answer fraction="0"><text>d⁴y/dt⁴ - ' + str(a) + ' d³y/dt³ + ' + str(b) + ' d²y/dt² + ' + str(c) + ' dy/dt + ' + str(d) + 'y = u</text></answer>\n')
    f.write('    <answer fraction="0"><text>d³y/dt³ + ' + str(a) + ' d²y/dt² + ' + str(b) + ' dy/dt + ' + str(c) + 'y = u</text></answer>\n')
    f.write('    <answer fraction="0"><text>d⁴y/dt⁴ + ' + str(d) + ' d³y/dt³ + ' + str(c) + ' d²y/dt² + ' + str(b) + ' dy/dt + ' + str(a) + 'y = u</text></answer>\n')
    f.write('  </question>\n')

f.write('</quiz>\n')
f.close()
print("Fichier questions.xml cree")
print("Total : "+ str(total) +" questions generees ")
