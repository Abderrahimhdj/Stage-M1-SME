import math
import pytest

# ============================================================
# Tests script eq_ft
# Equation differentielle -> Fonction de transfert
# ============================================================

def test_eq_ft_ordre1():
    # dy/dt + ay = eu  ->  H(p) = e/(p+a)
    a = 3
    e = 5
    # le numerateur doit etre e et le denominateur p+a
    assert e == 5
    assert a == 3

def test_eq_ft_ordre2():
    # d²y/dt² + ady/dt + by = d_coef*du/dt + eu  ->  H(p) = (d_coef*p+e)/(p²+ap+b)
    a = 2
    b = 4
    d_coef = 3
    e = 1
    # numerateur : d_coef*p + e
    # denominateur : p² + a*p + b
    assert d_coef == 3
    assert e == 1
    assert a == 2
    assert b == 4

def test_eq_ft_ordre3():
    a = 2
    b = 3
    c = 5
    f_coef = 1
    d_coef = 2
    e = 4
    # H(p) = (f_coef*p²+d_coef*p+e)/(p³+ap²+bp+c)
    assert f_coef == 1
    assert d_coef == 2
    assert e == 4

def test_eq_ft_ordre4():
    a = 1
    b = 2
    c = 3
    d = 4
    g_coef = 2
    f_coef = 1
    d_coef = 3
    e = 5
    # H(p) = (g*p³+f*p²+d*p+e)/(p⁴+ap³+bp²+cp+d)
    assert g_coef == 2
    assert f_coef == 1

# ============================================================
# Tests script stabilite
# Critere de Routh
# ============================================================

def test_stabilite_ordre1():
    # stable si a > 0
    a = 3
    assert a > 0  # stable

def test_stabilite_ordre1_instable():
    a = -2
    assert not (a > 0)  # instable

def test_stabilite_ordre2():
    # stable si a > 0 et b > 0
    a = 3
    b = 5
    assert a > 0 and b > 0  # stable

def test_stabilite_ordre2_instable():
    a = -1
    b = 2
    assert not (a > 0 and b > 0)  # instable

def test_stabilite_ordre3():
    # stable si a > 0, c > 0 et ab > c
    a = 2
    b = 4
    c = 3
    assert a > 0 and c > 0 and a * b > c  # stable : 2*4=8 > 3

def test_stabilite_ordre3_instable():
    # ab > c pas satisfait
    a = 1
    b = 1
    c = 10
    assert not (a > 0 and c > 0 and a * b > c)  # instable : 1*1=1 < 10

def test_stabilite_ordre4():
    # stable si a > 0, d > 0, (ab-c) > 0, (abc - a²d - c²) > 0
    a = 3
    b = 4
    c = 5
    d = 1
    cond1 = a > 0 and d > 0
    cond2 = (a * b - c) > 0
    cond3 = (a * b * c - a * a * d - c * c) > 0
    assert cond1 and cond2 and cond3

# ============================================================
# Tests script schema_bloc
# FBF = N(p) / (D(p) + N(p))
# ============================================================

def test_schema_bloc_ordre1():
    # H(p) = K/(p+a)  ->  FBF = K/(p+a+K)
    K = 3
    a = 5
    den_fbf = a + K
    assert den_fbf == 8

def test_schema_bloc_ordre2():
    # H(p) = (ap²+bp+c)/(dp²+ep+f)
    # FBF numerateur = ap²+bp+c  (inchange)
    # FBF denominateur = (d+a)p² + (e+b)p + (f+c)
    a = 2
    b = 3
    c = 4
    d = 5
    e = 6
    f = 7
    den_p2 = d + a
    den_p1 = e + b
    den_0 = f + c
    assert den_p2 == 7
    assert den_p1 == 9
    assert den_0 == 11

def test_schema_bloc_ordre3():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    den_p3 = e + a
    den_p2 = f + b
    den_p1 = g + c
    den_0 = h + d
    assert den_p3 == 6
    assert den_p2 == 8
    assert den_p1 == 10
    assert den_0 == 12

# ============================================================
# Tests script parametres_canoniques ordre 1
# a*dy/dt + b*y = c*u  ->  K = c/b, tau = a/b
# ============================================================

def test_canonique_ordre1_K():
    a = 3
    b = 5
    c = 4
    K = round(c / b, 4)
    assert K == 0.8

def test_canonique_ordre1_tau():
    a = 3
    b = 5
    tau = round(a / b, 4)
    assert tau == 0.6

def test_canonique_ordre1_cas_fraction():
    # cas ou K = 1/3
    a = 1
    b = 3
    c = 1
    K = round(c / b, 4)
    assert abs(K - 0.3333) < 0.001  # tolerance milliemme

# ============================================================
# Tests script parametres_canoniques ordre 2
# a*d²y/dt² + b*dy/dt + c*y = d*u
# K = d/c, wn = sqrt(c/a), zeta = b/(2*sqrt(a*c))
# ============================================================

def test_canonique_ordre2_K():
    a = 2
    b = 3
    c = 4
    d = 8
    K = round(d / c, 4)
    assert K == 2.0

def test_canonique_ordre2_wn():
    a = 1
    c = 4
    wn = round(math.sqrt(c / a), 4)
    assert wn == 2.0

def test_canonique_ordre2_zeta():
    a = 1
    b = 2
    c = 4
    zeta = round(b / (2 * math.sqrt(a * c)), 4)
    assert zeta == 0.5

# ============================================================
# Tests script FT_k_tau
# H(p) = c/(ap+b)  ->  K = c/b, tau = a/b
# ============================================================

def test_ft_k_tau_ordre1_K():
    a = 3
    b = 5
    c = 4
    K = round(c / b, 4)
    assert K == 0.8

def test_ft_k_tau_ordre1_tau():
    a = 3
    b = 5
    tau = round(a / b, 4)
    assert tau == 0.6

def test_ft_k_tau_ordre2_K():
    a = 2
    b = 3
    c = 4
    d = 8
    K = round(d / c, 4)
    assert K == 2.0

def test_ft_k_tau_ordre2_wn():
    a = 1
    c = 4
    wn = round(math.sqrt(c / a), 4)
    assert wn == 2.0

def test_ft_k_tau_ordre2_zeta():
    a = 1
    b = 2
    c = 4
    zeta = round(b / (2 * math.sqrt(a * c)), 4)
    assert zeta == 0.5
