import numpy as np 				 # pour les calculs mathématiques
import matplotlib.pyplot as plt  # pour dessiner les graphes
from scipy import signal         # pour calculer les reponses indicielles
import base64					 # pour convertir l'image en texte
import io 						 # pour manipuler l'image en memoire
import random					 # pour les parametres aléatoires

# ft ordre 1
def generer_ordre1(K, tau):
    num = [K]
    den = [tau, 1]
    sys = signal.TransferFunction(num, den)
    t = np.linspace(0, 5 * tau, 500)
    t, y = signal.step(sys, T=t)
    return t, y

# ft ordre 2
def generer_ordre2(K, wn, zeta):
    num = [K * wn**2]
    den = [1, 2 * zeta * wn, wn**2]
    sys = signal.TransferFunction(num, den)
    t_end = 10  # limite a 10 secondes
    t = np.linspace(0, t_end, 500)
    t, y = signal.step(sys, T=t)
    return t, y

def image_to_base64(t, y):
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(t, y, 'b-', linewidth=2)
    ax.axhline(y[-1], color='r', linewidth=1.5)
    ax.set_xlabel('temps [sec]')
    ax.set_ylabel('y(t)')
    ax.grid(True)
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=100)
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode()

f = open("/Users/macbookpro/Desktop/stage_sme/reponse_indicielle.xml", "w")
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<quiz>\n')

total = 0
CD_START = '<![CDATA['
CD_END = ']]>'

types = [
    'Mode simple ordre 1',
    'Mode simple ordre 2 aperiodique',
    'Mode simple ordre 2 amorti',
    'Mode simple ordre 2 pseudo-oscillante'
]

for i in range(3):
    choix_type = random.randint(0, 3)

    if choix_type == 0:
        K = round(random.uniform(0.5, 2), 2)
        tau = round(random.uniform(1, 5), 2)
        t, y = generer_ordre1(K, tau)
        bonne = types[0]

    elif choix_type == 1:
        K = round(random.uniform(0.5, 2), 2)
        wn = round(random.uniform(1, 4), 2)
        zeta = round(random.uniform(1.5, 3), 2)
        t, y = generer_ordre2(K, wn, zeta)
        bonne = types[1]

    elif choix_type == 2:
        K = round(random.uniform(0.5, 2), 2)
        wn = round(random.uniform(1, 4), 2)
        zeta = round(random.uniform(0.9, 1.1), 2)
        t, y = generer_ordre2(K, wn, zeta)
        bonne = types[2]

    else:
        K = round(random.uniform(0.5, 2), 2)
        wn = round(random.uniform(1, 4), 2)
        zeta = round(random.uniform(0.1, 0.7), 2)
        t, y = generer_ordre2(K, wn, zeta)
        bonne = types[3]

    img_base64 = image_to_base64(t, y)
    img_tag = '<img src="data:image/png;base64,' + img_base64 + '" width="400"/>'

    mauvaises = [t for t in types if t != bonne]
    choix = random.sample(mauvaises, 3)

    texte = 'Identifiez le type de reponse indicielle ci-dessous. ' + img_tag

    f.write('  <question type="multichoice">\n')
    f.write('    <name><text>Reponse indicielle - Q' + str(i) + '</text></name>\n')
    f.write('    <shuffleanswers>1</shuffleanswers>\n')
    f.write('    <questiontext format="html"><text>' + CD_START + texte + CD_END + '</text></questiontext>\n')
    f.write('    <answer fraction="100"><text>' + bonne + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[0] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[1] + '</text></answer>\n')
    f.write('    <answer fraction="0"><text>' + choix[2] + '</text></answer>\n')
    f.write('  </question>\n')
    total += 1

f.write('</quiz>\n')
f.close()
print("Succes !")
print("Total : " + str(total) + " questions generees !")