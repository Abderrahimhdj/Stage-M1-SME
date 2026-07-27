import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import base64
import io
import random
import math

def generer_ordre1(K, tau):
    num = [K]
    den = [tau, 1]
    sys = signal.TransferFunction(num, den)
    t = np.linspace(0, 5 * tau, 500)
    t, y = signal.step(sys, T=t)
    return t, y

def generer_ordre2(K, wn, zeta):
    num = [K * wn**2]
    den = [1, 2 * zeta * wn, wn**2]
    sys = signal.TransferFunction(num, den)
    t = np.linspace(0, 10, 500)
    t, y = signal.step(sys, T=t)
    return t, y

def image_to_base64(t, y):
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(t, y, 'b-', linewidth=2)
    ax.axhline(y[-1], color='r', linewidth=1.5, linestyle='--')
    ax.set_xlabel('temps [sec]')
    ax.set_ylabel('y(t)')
    ax.grid(True)
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=100)
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode()

f = open("/Users/macbookpro/Desktop/stage_sme/reponse_indicielle_parametres.xml", "w")
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<quiz>\n')

total = 0
CD_START = '<![CDATA['
CD_END = ']]>'

# ============================================================
# Ordre 1 : l'etudiant tape K et tau
# ============================================================
for i in range(1):
    K = round(random.uniform(0.5, 2), 2)
    tau = round(random.uniform(1, 4), 2)
    t, y = generer_ordre1(K, tau)

    img_base64 = image_to_base64(t, y)
    img_tag = '<img src="data:image/png;base64,' + img_base64 + '" width="400"/>'

    texte = (
        'Voici la reponse indicielle d\'un systeme du premier ordre. '
        'Identifiez les parametres canoniques (tolerance 0.01). '
        + img_tag +
        '<br/><br/>'
        '\\(K =\\) {1:NUMERICAL:=' + str(K) + ':0.01}'
        '<br/>'
        '\\(\\tau =\\) {1:NUMERICAL:=' + str(tau) + ':0.01}'
    )

    f.write('  <question type="cloze">\n')
    f.write('    <name><text>RI Parametres Ordre 1 - Q' + str(i) + '</text></name>\n')
    f.write('    <questiontext format="html"><text>' + CD_START + texte + CD_END + '</text></questiontext>\n')
    f.write('  </question>\n')
    total += 1

# ============================================================
# Ordre 2 pseudo-oscillant : l'etudiant tape K, wn et zeta
# ============================================================
for i in range(2):
    K = round(random.uniform(0.5, 2), 2)
    wn = round(random.uniform(1, 4), 2)
    zeta = round(random.uniform(0.1, 0.6), 2)
    t, y = generer_ordre2(K, wn, zeta)

    img_base64 = image_to_base64(t, y)
    img_tag = '<img src="data:image/png;base64,' + img_base64 + '" width="400"/>'

    texte = (
        'Voici la reponse indicielle d\'un systeme du deuxieme ordre pseudo-oscillant. '
        'Identifiez les parametres canoniques (tolerance 0.01). '
        + img_tag +
        '<br/><br/>'
        '\\(K =\\) {1:NUMERICAL:=' + str(K) + ':0.01}'
        '<br/>'
        '\\(\\omega_n =\\) {1:NUMERICAL:=' + str(wn) + ':0.01}'
        '<br/>'
        '\\(\\zeta =\\) {1:NUMERICAL:=' + str(zeta) + ':0.01}'
    )

    f.write('  <question type="cloze">\n')
    f.write('    <name><text>RI Parametres Ordre 2 - Q' + str(i) + '</text></name>\n')
    f.write('    <questiontext format="html"><text>' + CD_START + texte + CD_END + '</text></questiontext>\n')
    f.write('  </question>\n')
    total += 1

f.write('</quiz>\n')
f.close()
print("Succes !")
print("Total : " + str(total) + " questions generees !")
