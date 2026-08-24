import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import base64
import io
import random

def generer_nichols(a, b, K):
    num = [1]
    den = [1, a, b, K]
    w = np.logspace(-2, 2, 1000)
    w, H = signal.freqs(num, den, worN=w)
    gain_dB = 20 * np.log10(np.abs(H))
    phase_deg = np.degrees(np.angle(H))
    return gain_dB, phase_deg

def calculer_stabilite(a, b, K):
    return K < a * b

def image_nichols_base64(gain_dB, phase_deg):
    fig, ax = plt.subplots(figsize=(6, 5))
    # limiter les valeurs pour garder le graphe lisible
    gain_dB_clipped = np.clip(gain_dB, -50, 30)
    ax.plot(phase_deg, gain_dB_clipped, 'b-', linewidth=2, label='Lieu de Nichols')
    ax.plot(-180, 0, 'r+', markersize=15, markeredgewidth=2, label='Point critique (-180°, 0dB)')
    ax.axvline(-180, color='green', linewidth=1, linestyle='--', label='Phase = -180°')
    ax.axhline(0, color='orange', linewidth=1, linestyle='--', label='Gain = 0 dB')
    ax.set_xlabel('Phase (deg)')
    ax.set_ylabel('Gain (dB)')
    ax.set_title('Diagramme de Nichols')
    ax.grid(True)
    ax.legend(loc='lower right', fontsize=7)
    ax.set_xlim([-360, 0])
    ax.set_ylim([-50, 30])
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=100)
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode()

f = open("/Users/macbookpro/Desktop/stage_sme/nichols_final.xml", "w")
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<quiz>\n')

total = 0
CD_START = '<![CDATA['
CD_END = ']]>'

for i in range(2):
    a = random.randint(3, 8)
    b = random.randint(3, 8)
    seuil = a * b

    choix = random.randint(1, 2)
    if choix == 1:
        K = round(random.uniform(0.1, seuil * 0.5), 1)
        stable = True
    else:
        K = round(random.uniform(seuil * 1.2, seuil * 2), 1)
        stable = False

    gain_dB, phase_deg = generer_nichols(a, b, K)
    stable_calcule = calculer_stabilite(a, b, K)

    img_base64 = image_nichols_base64(gain_dB, phase_deg)
    img_tag = '<img src="data:image/png;base64,' + img_base64 + '" width="450"/>'

    if stable_calcule:
        bonne = 'Oui, le systeme est stable'
        mauvaise = 'Non, le systeme est instable'
    else:
        bonne = 'Non, le systeme est instable'
        mauvaise = 'Oui, le systeme est stable'

    texte = (
        'Soit \\(H(p) = \\frac{1}{p^3+' + str(a) + 'p^2+' + str(b) + 'p+' + str(K) + '}\\). '
        'En appliquant le critere de Routh, ce systeme est-il stable ? Le diagramme de Nichols est donne a titre indicatif. '
        + img_tag
    )

    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Nichols - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>' + CD_START + texte + CD_END + '</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>' + bonne + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + mauvaise + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>On ne peut pas savoir</text></answer>\n')
    f.write('    <answer fraction="0"><text>Le systeme est marginalement stable</text></answer>\n')
    f.write('  </question>\n')
    total += 1

f.write('</quiz>\n')
f.close()
print("Succes !")
print("Total : " + str(total) + " questions generees !")