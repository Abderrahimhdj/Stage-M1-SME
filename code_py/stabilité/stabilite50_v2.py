import random

f = open("/Users/macbookpro/Desktop/stage_sme/stabilite50fnl.xml", "w")
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<quiz>\n')

total = 0

#----------------------------------------------------------
#               ordre 1
#----------------------------------------------------------
for i in range(1):
    choix = random.randint(1, 2)
    if choix == 1:
        a = random.randint(1, 10)
        bonne = 'Oui, car le pole est a partie reelle negative'
        mauvaise = 'Non, car le pole est a partie reelle positive'
    else:
        a = random.randint(-10, 0)
        if a == 0:
            bonne = 'On ne peut pas savoir, le pole est nul'
            mauvaise = 'Oui, car le pole est a partie reelle negative'
        else:
            bonne = 'Non, car le pole est a partie reelle positive'
            mauvaise = 'Oui, car le pole est a partie reelle negative'

    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Stabilite Ordre 1 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext><text>Soit H(p) = 1/(p+' + str(a) + '). Ce systeme est-il stable ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>' + bonne + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + mauvaise + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>On ne peut pas savoir</text></answer>\n')
    f.write('    <answer fraction="0"><text>Oui, car le gain est positif</text></answer>\n')
    f.write('  </question>\n')
    total += 1

#----------------------------------------------------------
#               ordre 2
#----------------------------------------------------------
for i in range(1):
    choix = random.randint(1, 2)
    if choix == 1:
        # stable garanti : a > 0 et b > 0
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        bonne = 'Oui, car tous les coefficients sont positifs'
        mauvaise = 'Non, car un coefficient est negatif'
    else:
        # instable ou marginal
        a = random.randint(-10, 0)
        b = random.randint(-10, 0)
        if a == 0 or b == 0:
            bonne = 'On ne peut pas savoir, un coefficient est nul'
            mauvaise = 'Oui, car tous les coefficients sont positifs'
        else:
            bonne = 'Non, car un coefficient est negatif'
            mauvaise = 'Oui, car tous les coefficients sont positifs'

    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Stabilite Ordre 2 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext><text>Soit H(p) = 1/(p²+' + str(a) + 'p+' + str(b) + '). Ce systeme est-il stable ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>' + bonne + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + mauvaise + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>On ne peut pas savoir</text></answer>\n')
    f.write('    <answer fraction="0"><text>Oui, car le gain est positif</text></answer>\n')
    f.write('  </question>\n')
    total += 1

#----------------------------------------------------------
#               ordre 3
#----------------------------------------------------------
for i in range(1):
    choix = random.randint(1, 2)
    if choix == 1:
        # stable garanti : a > 0, c > 0, ab > c
        a = random.randint(1, 10)
        c = random.randint(1, 10)
        b = random.randint(c // a + 1, c // a + 10)
        bonne = 'Oui, car le critere de Routh est satisfait'
        mauvaise = 'Non, car le critere de Routh n est pas satisfait'
    else:
        # instable ou marginal
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        while a > 0 and c > 0 and a * b > c:
            a = random.randint(-10, 10)
            b = random.randint(-10, 10)
            c = random.randint(-10, 10)
        if a == 0 or b == 0 or c == 0:
            bonne = 'On ne peut pas savoir, un coefficient est nul'
            mauvaise = 'Oui, car le critere de Routh est satisfait'
        else:
            bonne = 'Non, car le critere de Routh n est pas satisfait'
            mauvaise = 'Oui, car le critere de Routh est satisfait'

    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Stabilite Ordre 3 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext><text>Soit H(p) = 1/(p³+' + str(a) + 'p²+' + str(b) + 'p+' + str(c) + '). Ce systeme est-il stable ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>' + bonne + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + mauvaise + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>On ne peut pas savoir</text></answer>\n')
    f.write('    <answer fraction="0"><text>Oui, car le gain est positif</text></answer>\n')
    f.write('  </question>\n')
    total += 1

#----------------------------------------------------------
#               ordre 4
#----------------------------------------------------------
for i in range(1):
    choix = random.randint(1, 2)
    if choix == 1:
        # stable garanti : toutes les conditions de Routh satisfaites
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        d = random.randint(1, 10)
        c = random.randint(1, a * b - 1) if a * b > 1 else 1
        while not (a * b * c > a * a * d + c * c):
            d = random.randint(1, 5)
            c = random.randint(1, a * b - 1) if a * b > 1 else 1
        bonne = 'Oui, car le critere de Routh est satisfait'
        mauvaise = 'Non, car le critere de Routh n est pas satisfait'
    else:
        # instable ou marginal
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        d = random.randint(-10, 10)
        while (a > 0 and d > 0 and (a * b - c) > 0 and (a * b * c - a * a * d - c * c) > 0):
            a = random.randint(-10, 10)
            b = random.randint(-10, 10)
            c = random.randint(-10, 10)
            d = random.randint(-10, 10)
        if a == 0 or b == 0 or c == 0 or d == 0:
            bonne = 'On ne peut pas savoir, un coefficient est nul'
            mauvaise = 'Oui, car le critere de Routh est satisfait'
        else:
            bonne = 'Non, car le critere de Routh n est pas satisfait'
            mauvaise = 'Oui, car le critere de Routh est satisfait'

    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Stabilite Ordre 4 - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext><text>Soit H(p) = 1/(p⁴+' + str(a) + 'p³+' + str(b) + 'p²+' + str(c) + 'p+' + str(d) + '). Ce systeme est-il stable ?</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>' + bonne + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + mauvaise + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>On ne peut pas savoir</text></answer>\n')
    f.write('    <answer fraction="0"><text>Oui, car le gain est positif</text></answer>\n')
    f.write('  </question>\n')
    total += 1

f.write('</quiz>\n')
f.close()
print("Succes !")
print("Total : " + str(total) + " questions generees !")
