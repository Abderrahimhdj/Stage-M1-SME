import random

f = open("/Users/macbookpro/Desktop/stage_sme/parametres_canoniques_inverse_v2.xml", "w")
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<quiz>\n')

total = 0

CD_START = '<![CDATA['
CD_END = ']]>'

# ============================================================
# Exercice 2 : on donne K et tau, on demande a et b
# K = 1/b, tau = a/b  ->  b = 1/K, a = tau/K
# ============================================================
for i in range(1):
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    K = round(1 / b, 4)
    tau = round(a / b, 4)

    texte = (
        'Soit un systeme du premier ordre avec \\(K = ' + str(K) + '\\) et \\(\\tau = ' + str(tau) + '\\). '
        'Donnez les coefficients de l\'equation differentielle \\(a\\dot{y} + by = u\\).'
        '<br/><br/>'
        '\\(a =\\) {1:NUMERICAL:=' + str(a) + ':0.001}'
        '<br/>'
        '\\(b =\\) {1:NUMERICAL:=' + str(b) + ':0.001}'
    )

    f.write('  <question type="cloze">\n')
    f.write('    <name><text>Calcul coefficients Ordre 1 - Q' + str(i) + '</text></name>\n')
    f.write('    <questiontext format="html"><text>' + CD_START + texte + CD_END + '</text></questiontext>\n')
    f.write('  </question>\n')
    total += 1

f.write('</quiz>\n')
f.close()
print("Succes !")
print("Total : " + str(total) + " questions generees !")
