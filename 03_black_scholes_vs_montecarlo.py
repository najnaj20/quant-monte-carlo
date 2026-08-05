"""
NAMA FILE: 03_black_scholes_vs_montecarlo.py
BAGIAN 3 - Bukti Monte Carlo = rumus (konvergensi).

Black-Scholes itu rumus 'pinter' buat harga opsi (ada sejak 1973).
Monte Carlo itu cara 'ngawur tapi bener' (coba jutaan kali).

Di file ini kita bandingkan:
  - Harga dari rumus Black-Scholes (analitik, pasti)
  - Harga dari Monte Carlo (acak, tapi makin banyak sampel -> makin dekat)

Kalau keduanya ketemu -> kamu tahu Monte Carlo kamu BENER.
Ini yang dihargai admission quant: 'two independent methods agree'.
"""

import numpy as np
from math import log, sqrt, exp, erf


def black_scholes_call(S0, K, T, r, sigma):
    """Rumus analitik harga call option (reference)."""
    d1 = (log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    # fungsi normal CDF pakai error function
    N = lambda x: 0.5 * (1 + erf(x / sqrt(2)))
    return S0 * N(d1) - K * exp(-r * T) * N(d2)


def monte_carlo_call(S0, K, T, r, sigma, N):
    Z = np.random.standard_normal(N)
    S_T = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * sqrt(T) * Z)
    payoff = np.maximum(S_T - K, 0)
    return np.exp(-r * T) * np.mean(payoff)


if __name__ == "__main__":
    print("=" * 55)
    print("MONTE CARLO vs BLACK-SCHOLES (bukti konvergen)")
    print("=" * 55)

    S0, K, T, r, sigma = 100, 100, 1.0, 0.05, 0.20
    bs = black_scholes_call(S0, K, T, r, sigma)
    print(f"Black-Scholes (pasti) = {bs:.4f}")
    print("-" * 55)

    for N in [1_000, 10_000, 100_000, 1_000_000]:
        mc = monte_carlo_call(S0, K, T, r, sigma, N)
        print(f"Monte Carlo N={N:>9} = {mc:.4f}  | selisih {abs(mc-bs):.4f}")
    print("-" * 55)
    print("Lihat: makin besar N, selisih makin kecil -> konvergen!")
