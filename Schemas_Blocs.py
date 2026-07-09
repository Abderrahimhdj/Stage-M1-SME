
import random

f = open("/Users/macbookpro/Desktop/stage_sme/schemas_blocs.xml", "w")
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<quiz>\n')

total = 0

# ============================================================
# Schémas blocs — Boucle fermée avec retour unitaire
# H(p) = K/(p+a)  ->  FBF = K/(p+a+K)
# ============================================================

for i in range(1):
    K = random.randint(1, 10)
    a = random.randint(1, 10)
    denom_const = a + K  # coefficient constant du denominateur de la FBF

    # Question 1 : numérateur de la FBF
    f.write('  <question type="shortanswer">\n')
    f.write('    <name><text>BF Ordre 1 - Q' + str(i) + ' - Numerateur</text></name>\n')
    f.write('    <questiontext format="html"><text>')
    f.write('Soit \\(H(p) = \\frac{' + str(K) + '}{p+' + str(a) + '}\\) en boucle fermée avec retour unitaire.')
    f.write('La fonction de transfert en boucle fermée est de la forme \\(\\frac{N}{p+D}\\).')
    f.write('Quelle est la valeur de \\(N\\) (numérateur) ?')
    f.write('</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>' + str(K) + '</text></answer>\n')
    f.write('  </question>\n')
    total += 1

    # Question 2 : coefficient constant du dénominateur
    f.write('  <question type="shortanswer">\n')
    f.write('    <name><text>BF Ordre 1 - Q' + str(i) + ' - Denominateur</text></name>\n')
    f.write('    <questiontext format="html"><text>')
    f.write('Soit \\(H(p) = \\frac{' + str(K) + '}{p+' + str(a) + '}\\) en boucle fermée avec retour unitaire.')
    f.write('La fonction de transfert en boucle fermée est de la forme \\(\\frac{N}{p+D}\\).')
    f.write('Quelle est la valeur de \\(D\\) (coefficient constant du dénominateur) ?')
    f.write('</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>' + str(denom_const) + '</text></answer>\n')
    f.write('  </question>\n')
    total += 1

f.write('</quiz>\n')
f.close()
print("Succes !")
print("Total : " + str(total) + " questions generees !")
