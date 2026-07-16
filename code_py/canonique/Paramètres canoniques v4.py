import random

f = open("/Users/macbookpro/Desktop/stage_sme/parametres_canoniques_v2.xml", "w")
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<quiz>\n')

total = 0

CD_START = '<![CDATA['
CD_END = ']]>'

# ============================================================
# Exercice : on donne a, b, c, on demande K et tau
# a*dy/dt + b*y = c*u  ->  K = c/b, tau = a/b
# ============================================================
for i in range(10):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)

    K = round(c / b, 4)
    tau = round(a / b, 4)

    texte = (
        'Soit \\(' + str(a) + '\\dot{y} + ' + str(b) + 'y = ' + str(c) + 'u\\). '
        'Donnez les parametres canoniques.'
        '<br/><br/>'
        '\\(K =\\) {1:NUMERICAL:=' + str(K) + ':0.001}'
        '<br/>'
        '\\(\\tau =\\) {1:NUMERICAL:=' + str(tau) + ':0.001}'
    )

    f.write('  <question type="cloze">\n')
    f.write('    <name><text>Parametres canoniques - Q' + str(i) + '</text></name>\n')
    f.write('    <questiontext format="html"><text>' + CD_START + texte + CD_END + '</text></questiontext>\n')
    f.write('  </question>\n')
    total += 1

f.write('</quiz>\n')
f.close()
print("Succes !")
print("Total : " + str(total) + " questions generees !")
