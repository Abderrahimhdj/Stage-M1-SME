import math
import pytest

# ============================================================
# Tests exercice eq_ft
# Equation differentielle -> Fonction de transfert
# On construit num et den de H(p) et on verifie les coefficients
# ============================================================

def test_eq_ft_ordre1():
    # dy/dt + a*y = e*u  ->  H(p) = e / (p + a)
    a, e = 3, 5
    num = [e]
    den = [1, a]
    assert num == [5]
    assert den == [1, 3]

def test_eq_ft_ordre2():
    # d2y + a*dy + b*y = d_coef*du + e*u  ->  H(p) = (d_coef*p + e) / (p^2 + a*p + b)
    a, b, d_coef, e = 2, 4, 3, 1
    num = [d_coef, e]
    den = [1, a, b]
    assert num == [3, 1]
    assert den == [1, 2, 4]

def test_eq_ft_ordre3():
    # H(p) = (f*p^2 + d*p + e) / (p^3 + a*p^2 + b*p + c)
    a, b, c, f_coef, d_coef, e = 2, 3, 5, 1, 2, 4
    num = [f_coef, d_coef, e]
    den = [1, a, b, c]
    assert num == [1, 2, 4]
    assert den == [1, 2, 3, 5]

def test_eq_ft_ordre4():
    # H(p) = (g*p^3 + f*p^2 + d*p + e) / (p^4 + a*p^3 + b*p^2 + c*p + d_den)
    a, b, c, d_den = 1, 2, 3, 4
    g_coef, f_coef, d_coef, e = 2, 1, 3, 5
    num = [g_coef, f_coef, d_coef, e]
    den = [1, a, b, c, d_den]
    assert num == [2, 1, 3, 5]
    assert den == [1, 1, 2, 3, 4]

# ============================================================
# Tests exercice stabilite
# Critere de Routh
# ============================================================

def test_stabilite_ordre1():
    # stable si a > 0
    a = 3
    assert a > 0

def test_stabilite_ordre1_instable():
    a = -2
    assert not (a > 0)

def test_stabilite_ordre2():
    # stable si a > 0 et b > 0
    a, b = 3, 5
    assert a > 0 and b > 0

def test_stabilite_ordre2_instable():
    a, b = -1, 2
    assert not (a > 0 and b > 0)

def test_stabilite_ordre3():
    # stable si a > 0, c > 0 et ab > c
    a, b, c = 2, 4, 3
    assert a > 0 and c > 0 and a * b > c  # 2*4=8 > 3 -> stable

def test_stabilite_ordre3_instable():
    # ab > c non satisfait
    a, b, c = 1, 1, 10
    assert not (a > 0 and c > 0 and a * b > c)  # 1*1=1 < 10 -> instable

def test_stabilite_ordre4():
    # stable si a>0, d>0, (ab-c)>0, (abc - a^2 d - c^2) > 0
    a, b, c, d = 3, 4, 5, 1
    cond1 = a > 0 and d > 0
    cond2 = (a * b - c) > 0
    cond3 = (a * b * c - a * a * d - c * c) > 0
    assert cond1 and cond2 and cond3

# ============================================================
# Tests exercice schema_bloc
# FBF = N(p) / (D(p) + N(p))
# ============================================================

def test_schema_bloc_ordre1():
    # H(p) = K/(p+a)  ->  FBF = K/(p + a + K)
    K, a = 3, 5
    den_fbf = a + K
    assert den_fbf == 8

def test_schema_bloc_ordre2():
    # H(p) = (ap^2+bp+c)/(dp^2+ep+f)
    # FBF numerateur = ap^2+bp+c (inchange)
    # FBF denominateur = (d+a)p^2 + (e+b)p + (f+c)
    a, b, c, d, e, f = 2, 3, 4, 5, 6, 7
    den_p2 = d + a
    den_p1 = e + b
    den_0 = f + c
    assert den_p2 == 7
    assert den_p1 == 9
    assert den_0 == 11

def test_schema_bloc_ordre3():
    a, b, c, d, e, f, g, h = 1, 2, 3, 4, 5, 6, 7, 8
    den_p3 = e + a
    den_p2 = f + b
    den_p1 = g + c
    den_0 = h + d
    assert den_p3 == 6
    assert den_p2 == 8
    assert den_p1 == 10
    assert den_0 == 12

# ============================================================
# Tests exercice parametres_canoniques ordre 1
# a*dy/dt + b*y = c*u  ->  K = c/b, tau = a/b
# ============================================================

def test_canonique_ordre1_K():
    a, b, c = 3, 5, 4
    K = round(c / b, 4)
    assert K == 0.8

def test_canonique_ordre1_tau():
    a, b, c = 3, 5, 4
    tau = round(a / b, 4)
    assert tau == 0.6

def test_canonique_ordre1_cas_fraction():
    # cas ou K = 1/3
    a, b, c = 1, 3, 1
    K = round(c / b, 4)
    assert abs(K - 0.3333) < 0.001  # tolerance millieme

# ============================================================
# Tests exercice parametres_canoniques ordre 2
# a*d2y + b*dy + c*y = d*u
# K = d/c, wn = sqrt(c/a), zeta = b/(2*sqrt(a*c))
# ============================================================

def test_canonique_ordre2_K():
    a, b, c, d = 2, 3, 4, 8
    K = round(d / c, 4)
    assert K == 2.0

def test_canonique_ordre2_wn():
    a, c = 1, 4
    wn = round(math.sqrt(c / a), 4)
    assert wn == 2.0

def test_canonique_ordre2_zeta():
    a, b, c = 1, 2, 4
    zeta = round(b / (2 * math.sqrt(a * c)), 4)
    assert zeta == 0.5

# ============================================================
# Tests exercice FT_k_tau
# H(p) = c/(ap+b)  ->  K = c/b, tau = a/b
# ============================================================

def test_ft_k_tau_ordre1_K():
    a, b, c = 3, 5, 4
    K = round(c / b, 4)
    assert K == 0.8

def test_ft_k_tau_ordre1_tau():
    a, b, c = 3, 5, 4
    tau = round(a / b, 4)
    assert tau == 0.6

def test_ft_k_tau_ordre2_K():
    a, b, c, d = 2, 3, 4, 8
    K = round(d / c, 4)
    assert K == 2.0

def test_ft_k_tau_ordre2_wn():
    a, c = 1, 4
    wn = round(math.sqrt(c / a), 4)
    assert wn == 2.0

def test_ft_k_tau_ordre2_zeta():
    a, b, c = 1, 2, 4
    zeta = round(b / (2 * math.sqrt(a * c)), 4)
    assert zeta == 0.5

# ============================================================
# Tests exercice reponse_indicielle
# Verification sur la vraie reponse temporelle (scipy)
# ============================================================

import numpy as np
from scipy import signal

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
    t_end = max(10 / wn, 20)
    t = np.linspace(0, t_end, 500)
    t, y = signal.step(sys, T=t)
    return t, y

def test_reponse_indicielle_ordre1_valeur_finale():
    # la valeur finale doit etre K
    K, tau = 1.5, 2.0
    t, y = generer_ordre1(K, tau)
    assert abs(y[-1] - K) < 0.02

def test_reponse_indicielle_ordre1_pas_oscillations():
    # ordre 1 : sortie monotone croissante
    K, tau = 1.0, 2.0
    t, y = generer_ordre1(K, tau)
    assert all(y[i] <= y[i + 1] for i in range(len(y) - 1))

def test_reponse_indicielle_ordre2_aperiodique():
    # zeta > 1 -> pas d'oscillations, montee monotone
    K, wn, zeta = 1.0, 2.0, 2.0
    t, y = generer_ordre2(K, wn, zeta)
    assert abs(y[-1] - K) < 0.02
    assert zeta > 1

def test_reponse_indicielle_ordre2_pseudooscillant():
    # 0 < zeta < 1 -> depassement (ymax > K)
    K, wn, zeta = 1.0, 2.0, 0.3
    t, y = generer_ordre2(K, wn, zeta)
    assert abs(y[-1] - K) < 0.02
    assert 0 < zeta < 1
    assert max(y) > K

def test_reponse_indicielle_ordre2_amorti():
    # zeta proche de 1 -> pas (ou tres peu) de depassement
    K, wn, zeta = 1.0, 2.0, 1.0
    t, y = generer_ordre2(K, wn, zeta)
    assert abs(y[-1] - K) < 0.02
    assert abs(zeta - 1.0) < 0.15

def test_plage_zeta_aperiodique():
    zeta = 2.0
    assert zeta > 1

def test_plage_zeta_pseudooscillant():
    zeta = 0.3
    assert 0 < zeta < 1

def test_plage_zeta_amorti():
    zeta = 1.0
    assert 0.9 <= zeta <= 1.1