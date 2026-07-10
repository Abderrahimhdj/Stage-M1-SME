import random
import base64

with open("/Users/macbookpro/Desktop/stage_sme/schema_bloc.png", "rb") as img:
    img_base64 = base64.b64encode(img.read()).decode()

img_tag = '<img src="data:image/png;base64,' + img_base64 + '" width="400"/>'

CD_START = '<![CDATA['
CD_END = ']]>'

f = open("/Users/macbookpro/Desktop/stage_sme/schemas_blocs_cloze_v3.xml", "w")
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<quiz>\n')

total = 0

# ============================================================
# Ordre 1 : H(p) = (a*p + b) / (c*p + d)
# FBF = (a*p + b) / ((c+a)*p + (d+b))
# ============================================================
for i in range(1):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)

    den_p = c + a
    den_0 = d + b

    texte = (
        'Soit \\(H(p) = \\frac{' + str(a) + 'p+' + str(b) + '}{' + str(c) + 'p+' + str(d) + '}\\) '
        'dans le schema blocs ci-dessous. '
        'Calculez la FBF et donnez les coefficients. '
        + img_tag +
        '<br/><br/>'
        'Numerateur : {1:NUMERICAL:=' + str(a) + '} \\(p +\\) {1:NUMERICAL:=' + str(b) + '}'
        '<br/>'
        'Denominateur : {1:NUMERICAL:=' + str(den_p) + '} \\(p +\\) {1:NUMERICAL:=' + str(den_0) + '}'
    )

    f.write('  <question type="cloze">\n')
    f.write('    <name><text>BF Ordre 1 - Q' + str(i) + '</text></name>\n')
    f.write('    <questiontext format="html"><text>' + CD_START + texte + CD_END + '</text></questiontext>\n')
    f.write('  </question>\n')
    total += 1

# ============================================================
# Ordre 2 : H(p) = (a*p² + b*p + c) / (d*p² + e*p + f)
# FBF = (a*p² + b*p + c) / ((d+a)*p² + (e+b)*p + (f+c))
# ============================================================
for i in range(1):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    e = random.randint(1, 10)
    f_coef = random.randint(1, 10)

    den_p2 = d + a
    den_p1 = e + b
    den_0 = f_coef + c

    texte = (
        'Soit \\(H(p) = \\frac{' + str(a) + 'p^2+' + str(b) + 'p+' + str(c) + '}{' + str(d) + 'p^2+' + str(e) + 'p+' + str(f_coef) + '}\\) '
        'dans le schema blocs ci-dessous. '
        'Calculez la FBF et donnez les coefficients. '
        + img_tag +
        '<br/><br/>'
        'Numerateur : {1:NUMERICAL:=' + str(a) + '} \\(p^2 +\\) {1:NUMERICAL:=' + str(b) + '} \\(p +\\) {1:NUMERICAL:=' + str(c) + '}'
        '<br/>'
        'Denominateur : {1:NUMERICAL:=' + str(den_p2) + '} \\(p^2 +\\) {1:NUMERICAL:=' + str(den_p1) + '} \\(p +\\) {1:NUMERICAL:=' + str(den_0) + '}'
    )

    f.write('  <question type="cloze">\n')
    f.write('    <name><text>BF Ordre 2 - Q' + str(i) + '</text></name>\n')
    f.write('    <questiontext format="html"><text>' + CD_START + texte + CD_END + '</text></questiontext>\n')
    f.write('  </question>\n')
    total += 1

# ============================================================
# Ordre 3 : H(p) = (a*p³ + b*p² + c*p + d) / (e*p³ + f*p² + g*p + h)
# FBF = (a*p³+b*p²+c*p+d) / ((e+a)*p³+(f+b)*p²+(g+c)*p+(h+d))
# ============================================================
for i in range(1):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    e = random.randint(1, 10)
    f_coef = random.randint(1, 10)
    g = random.randint(1, 10)
    h = random.randint(1, 10)

    den_p3 = e + a
    den_p2 = f_coef + b
    den_p1 = g + c
    den_0 = h + d

    texte = (
        'Soit \\(H(p) = \\frac{' + str(a) + 'p^3+' + str(b) + 'p^2+' + str(c) + 'p+' + str(d) + '}{' + str(e) + 'p^3+' + str(f_coef) + 'p^2+' + str(g) + 'p+' + str(h) + '}\\) '
        'dans le schema blocs ci-dessous. '
        'Calculez la FBF et donnez les coefficients. '
        + img_tag +
        '<br/><br/>'
        'Numerateur : {1:NUMERICAL:=' + str(a) + '} \\(p^3 +\\) {1:NUMERICAL:=' + str(b) + '} \\(p^2 +\\) {1:NUMERICAL:=' + str(c) + '} \\(p +\\) {1:NUMERICAL:=' + str(d) + '}'
        '<br/>'
        'Denominateur : {1:NUMERICAL:=' + str(den_p3) + '} \\(p^3 +\\) {1:NUMERICAL:=' + str(den_p2) + '} \\(p^2 +\\) {1:NUMERICAL:=' + str(den_p1) + '} \\(p +\\) {1:NUMERICAL:=' + str(den_0) + '}'
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
