import random
import base64

# Charger l'image en base64
with open("/Users/macbookpro/Desktop/stage_sme/schema_bloc.png", "rb") as img:
    img_base64 = base64.b64encode(img.read()).decode()

img_tag = '<img src="data:image/png;base64,' + img_base64 + '" width="400"/>'

CD_START = '<![CDATA['
CD_END = ']]>'

f = open("/Users/macbookpro/Desktop/stage_sme/schemas_blocs_cloze_v2.xml", "w")
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<quiz>\n')

total = 0

# ============================================================
# Ordre 1 : H(p) = K/(p+a)  ->  FBF = K/(p+a+K)
# Numerateur : K (degre 0)
# Denominateur : p + (a+K)
# ============================================================
for i in range(1):
    K = random.randint(1, 10)
    a = random.randint(1, 10)
    aK = a + K

    texte = (
        'Soit \\(H(p) = \\frac{' + str(K) + '}{p+' + str(a) + '}\\) '
        'dans le schema blocs ci-dessous. '
        'Calculez la FBF et donnez les coefficients. '
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
# Ordre 2 : H(p) = (b1*p+c1)/(p²+a*p+d)
# FBF = (b1*p+c1) / (p²+(a+b1)*p+(d+c1))
# Numerateur : b1*p + c1
# Denominateur : p² + (a+b1)*p + (d+c1)
# ============================================================
for i in range(1):
    a = random.randint(1, 10)
    d = random.randint(1, 10)
    b1 = random.randint(1, 10)
    c1 = random.randint(1, 10)
    # coefficients de la FBF
    num_p = b1          # coefficient de p au numerateur
    num_0 = c1          # coefficient constant au numerateur
    den_p = a + b1      # coefficient de p au denominateur
    den_0 = d + c1      # coefficient constant au denominateur

    texte = (
        'Soit \\(H(p) = \\frac{' + str(b1) + 'p+' + str(c1) + '}{p^2+' + str(a) + 'p+' + str(d) + '}\\) '
        'dans le schema blocs ci-dessous. '
        'Calculez la FBF et donnez les coefficients. '
        + img_tag +
        '<br/><br/>'
        'Numerateur : {1:NUMERICAL:=' + str(num_p) + '} \\(p +\\) {1:NUMERICAL:=' + str(num_0) + '}'
        '<br/>'
        'Denominateur : \\(p^2 +\\) {1:NUMERICAL:=' + str(den_p) + '} \\(p +\\) {1:NUMERICAL:=' + str(den_0) + '}'
    )

    f.write('  <question type="cloze">\n')
    f.write('    <name><text>BF Ordre 2 - Q' + str(i) + '</text></name>\n')
    f.write('    <questiontext format="html"><text>' + CD_START + texte + CD_END + '</text></questiontext>\n')
    f.write('  </question>\n')
    total += 1

# ============================================================
# Ordre 3 : H(p) = (c1*p²+d1*p+e1)/(p³+a*p²+b*p+f)
# FBF = (c1*p²+d1*p+e1) / (p³+(a+c1)*p²+(b+d1)*p+(f+e1))
# Numerateur : c1*p² + d1*p + e1
# Denominateur : p³ + (a+c1)*p² + (b+d1)*p + (f+e1)
# ============================================================
for i in range(1):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    f_coef = random.randint(1, 10)
    c1 = random.randint(1, 10)
    d1 = random.randint(1, 10)
    e1 = random.randint(1, 10)
    # coefficients de la FBF
    num_p2 = c1
    num_p1 = d1
    num_0 = e1
    den_p2 = a + c1
    den_p1 = b + d1
    den_0 = f_coef + e1

    texte = (
        'Soit \\(H(p) = \\frac{' + str(c1) + 'p^2+' + str(d1) + 'p+' + str(e1) + '}{p^3+' + str(a) + 'p^2+' + str(b) + 'p+' + str(f_coef) + '}\\) '
        'dans le schema blocs ci-dessous. '
        'Calculez la FBF et donnez les coefficients. '
        + img_tag +
        '<br/><br/>'
        'Numerateur : {1:NUMERICAL:=' + str(num_p2) + '} \\(p^2 +\\) {1:NUMERICAL:=' + str(num_p1) + '} \\(p +\\) {1:NUMERICAL:=' + str(num_0) + '}'
        '<br/>'
        'Denominateur : \\(p^3 +\\) {1:NUMERICAL:=' + str(den_p2) + '} \\(p^2 +\\) {1:NUMERICAL:=' + str(den_p1) + '} \\(p +\\) {1:NUMERICAL:=' + str(den_0) + '}'
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
