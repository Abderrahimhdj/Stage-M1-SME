import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import base64
import io
import random

def generer_nichols_ordre2(K, wn, zeta):
    num = [K * wn**2]
    den = [1, 2 * zeta * wn, wn**2]
    w = np.logspace(-2, 2, 1000)
    w, H = signal.freqs(num, den, worN=w)
    gain_dB = 20 * np.log10(np.abs(H))
    phase_deg = np.degrees(np.angle(H))
    return gain_dB, phase_deg

def image_nichols_base64(gain_dB, phase_deg):
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.plot(phase_deg, gain_dB, 'b-', linewidth=2, label='Lieu de Nichols')
    ax.plot(-180, 0, 'r+', markersize=15, markeredgewidth=2, label='Point critique')
    ax.set_xlabel('Phase (deg)')
    ax.set_ylabel('Gain (dB)')
    ax.set_title('Diagramme de Nichols')
    ax.grid(True)
    ax.legend()
    ax.set_xlim([-360, 0])
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=100)
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode()

# zeta force entre 0.1 et 0.4 pour passer pres du point critique
K = round(random.uniform(0.5, 3), 2)
wn = round(random.uniform(1, 5), 2)
zeta = round(random.uniform(0.1, 0.4), 2)

print("K=" + str(K) + ", wn=" + str(wn) + ", zeta=" + str(zeta))

gain_dB, phase_deg = generer_nichols_ordre2(K, wn, zeta)
img = image_nichols_base64(gain_dB, phase_deg)

import base64 as b64
with open("/Users/macbookpro/Desktop/stage_sme/nichols_test.png", "wb") as f:
    f.write(b64.b64decode(img))
print("Image sauvegardee !")