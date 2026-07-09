import random
import base64

# Charger l'image en base64
with open("/Users/macbookpro/Desktop/stage_sme/schema_bloc.png", "rb") as img:
    img_base64 = base64.b64encode(img.read()).decode()

img_tag = '<img src="data:image/png;base64,' + img_base64 + '" width="400"/>'

# CDATA : permet d'inclure du HTML et du LaTeX dans le XML sans erreur
CD_START = '<![CDATA['
CD_END = ']]>'

f = open("/Users/macbookpro/Desktop/stage_sme/schema_bloc_img.xml", "w")
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<quiz>\n')

total = 0

# H(p) = K/(p+a)  ->  FBF = K/(p+a+K)  de la forme N/(p+D)

for i in range(1):
    K = random.randint(1, 10)
    a = random.randint(1, 10)
    denom_const = a + K

    # Question 1 : numerateur
    f.write('  <question type="shortanswer">\n')
    f.write('    <name><text>BF Ordre 1 - Q' + str(i) + ' - Numerateur</text></name>\n')
    texte1 = 'Soit \\(H(p) = \\frac{' + str(K) + '}{p+' + str(a) + '}\\) dans le schema blocs ci-dessous. La FBF est de la forme \\(\\frac{N}{p+D}\\). Quelle est la valeur de \\(N\\) ? ' + img_tag
    f.write('    <questiontext format="html"><text>' + CD_START + texte1 + CD_END + '</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>' + str(K) + '</text></answer>\n')
    f.write('  </question>\n')
    total += 1

    # Question 2 : denominateur
    f.write('  <question type="shortanswer">\n')
    f.write('    <name><text>BF Ordre 1 - Q' + str(i) + ' - Denominateur</text></name>\n')
    texte2 = 'Soit \\(H(p) = \\frac{' + str(K) + '}{p+' + str(a) + '}\\) dans le schema blocs ci-dessous. La FBF est de la forme \\(\\frac{N}{p+D}\\). Quelle est la valeur de \\(D\\) ? ' + img_tag
    f.write('    <questiontext format="html"><text>' + CD_START + texte2 + CD_END + '</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>' + str(denom_const) + '</text></answer>\n')
    f.write('  </question>\n')
    total += 1

f.write('</quiz>\n')
f.close()
print("Succes !")
print("Total : " + str(total) + " questions generees !")