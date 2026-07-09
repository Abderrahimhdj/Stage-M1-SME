import random
import base64

# Charger l'image en base64
with open("/Users/macbookpro/Desktop/stage_sme/schema_bloc.png", "rb") as img:
    img_base64 = base64.b64encode(img.read()).decode()

img_tag = '<img src="data:image/png;base64,' + img_base64 + '" width="400"/>'

CD_START = '<![CDATA['
CD_END = ']]>'

f = open("/Users/macbookpro/Desktop/stage_sme/schemas_blocs_cloze.xml", "w")
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<quiz>\n')

total = 0

# ============================================================
# Ordre 1 : H(p) = K/(p+a)  ->  FBF = K/(p+a+K)
# Numerateur : K
# Denominateur : p + (a+K)
# ============================================================
for i in range(1):
    K = random.randint(1, 10)
    a = random.randint(1, 10)
    aK = a + K

    texte = (
        'Soit \\(H(p) = \\frac{' + str(K) + '}{p+' + str(a) + '}\\) '
        'dans le schema blocs ci-dessous. '
        'Calculez la fonction de transfert en boucle fermee et donnez les coefficients. '
        + img_tag +
        '<br/><br/>'
        'Numerateur : {1:NUMERICAL:=' + str(K) + '}'
        '<br/>'
        'Denominateur : \\(p +\\) {1:NUMERICAL:=' + str(aK) + '}'
    )

    f.write('  <question type="cloze">\n')
    f.write('    <name><text>BF Ordre 1 - Q' + str(i) + '</text></name>\n')
    f.write('    <questiontext format="html"><text>' + CD_START + texte + CD_END + '</text></questiontext>\n')
    f.write('  </question>\n')
    total += 1

# ============================================================
# Ordre 2 : H(p) = K/(p²+ap+b)  ->  FBF = K/(p²+ap+b+K)
# Numerateur : K
# Denominateur : p² + ap + (b+K)
# ============================================================
for i in range(1):
    K = random.randint(1, 10)
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    bK = b + K

    texte = (
        'Soit \\(H(p) = \\frac{' + str(K) + '}{p^2+' + str(a) + 'p+' + str(b) + '}\\) '
        'dans le schema blocs ci-dessous. '
        'Calculez la fonction de transfert en boucle fermee et donnez les coefficients. '
        + img_tag +
        '<br/><br/>'
        'Numerateur : {1:NUMERICAL:=' + str(K) + '}'
        '<br/>'
        'Denominateur : \\(p^2 +\\) {1:NUMERICAL:=' + str(a) + '} \\(p +\\) {1:NUMERICAL:=' + str(bK) + '}'
    )

    f.write('  <question type="cloze">\n')
    f.write('    <name><text>BF Ordre 2 - Q' + str(i) + '</text></name>\n')
    f.write('    <questiontext format="html"><text>' + CD_START + texte + CD_END + '</text></questiontext>\n')
    f.write('  </question>\n')
    total += 1

# ============================================================
# Ordre 3 : H(p) = K/(p³+ap²+bp+c)  ->  FBF = K/(p³+ap²+bp+c+K)
# Numerateur : K
# Denominateur : p³ + ap² + bp + (c+K)
# ============================================================
for i in range(1):
    K = random.randint(1, 10)
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    cK = c + K

    texte = (
        'Soit \\(H(p) = \\frac{' + str(K) + '}{p^3+' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}\\) '
        'dans le schema blocs ci-dessous. '
        'Calculez la fonction de transfert en boucle fermee et donnez les coefficients. '
        + img_tag +
        '<br/><br/>'
        'Numerateur : {1:NUMERICAL:=' + str(K) + '}'
        '<br/>'
        'Denominateur : \\(p^3 +\\) {1:NUMERICAL:=' + str(a) + '} \\(p^2 +\\) {1:NUMERICAL:=' + str(b) + '} \\(p +\\) {1:NUMERICAL:=' + str(cK) + '}'
    )

    f.write('  <question type="cloze">\n')
    f.write('    <name><text>BF Ordre 3 - Q' + str(i) + '</text></name>\n')
    f.write('    <questiontext format="html"><text>' + CD_START + texte + CD_END + '</text></questiontext>\n')
    f.write('  </question>\n')
    total += 1

f.write('</quiz>\n')
f.close()
print("Succes !")
print("Total : " + str(total) + " questions generees !")
