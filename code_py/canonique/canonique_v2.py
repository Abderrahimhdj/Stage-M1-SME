import random

f = open("/Users/macbookpro/Desktop/stage_sme/parametres_canoniques.xml", "w")
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<quiz>\n')

total = 0

CD_START = '<![CDATA['
CD_END = ']]>'

# b choisi parmi ces valeurs pour avoir des decimales propres
# 1 -> K=1, 2 -> K=0.5, 4 -> K=0.25, 5 -> K=0.2, 10 -> K=0.1
valeurs_b = [1, 2, 4, 5, 10]

# ============================================================
# Exercice 1 : on donne a et b, on demande K et tau
# ============================================================
for i in range(10):
    a = random.randint(1, 10)
    b = random.choice(valeurs_b)

    K = round(1 / b, 4)
    tau = round(a / b, 4)

    texte = (
        'Soit \\(' + str(a) + '\\dot{y} + ' + str(b) + 'y = u\\). '
        'Donnez les parametres canoniques.'
        '<br/><br/>'
        '\\(K =\\) {1:NUMERICAL:=' + str(K) + ':0.001}'
        '<br/>'
        '\\(\\tau =\\) {1:NUMERICAL:=' + str(tau) + ':0.001}'
    )

    f.write('  <question type="cloze">\n')
    f.write('    <name><text>Parametres canoniques Ordre 1 - Q' + str(i) + '</text></name>\n')
    f.write('    <questiontext format="html"><text>' + CD_START + texte + CD_END + '</text></questiontext>\n')
    f.write('  </question>\n')
    total += 1

f.write('</quiz>\n')
f.close()
print("Succes !")
print("Total : " + str(total) + " questions generees !")
