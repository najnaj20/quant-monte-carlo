"""
NAMA FILE: 02_harga_opsi_sederhana.py
BAGIAN 2 - Monte Carlo buat harga opsi saham (level masih mudah).

CERITA SEDERHANA:
  Kamu punya hak (tapi bukan kewajiban) buat beli saham di harga 100
  setelah 1 tahun. Ini namanya 'Call Option'.
  - Kalau tahun depan saham naik jadi 120 -> kamu beli 100, jual 120 -> untung 20.
  - Kalau saham turun jadi 80 -> kamu nggak beli -> untung 0 (hak, bukan wajib).

Berapa 'hak' ini harganya SEKARANG?
Jawabannya tergantung: saham tahun depan harganya BERAPA?
Tapi harga saham masa depan itu GAK PASTI -> dia RANDOM VARIABLE.

Monte Carlo cara kerjanya:
  1. Kita 'andaikan' harga saham tahun depan dengan aturan acak (GBM).
  2. Ulangi jutaan kali -> dapat banyak kemungkinan harga.
  3. Untung di tiap kemungkinan = max(harga - 100, 0).
  4. Rata-rata untung -> itu ekspektasi -> diskon ke hari ini -> harga opsi.

Kita TIDAK pakai rumus stochastic calculus di sini.
Cukup tahu: saham gerak naik turun acak, kita simulasi aja.
"""

import numpy as np


def simulasi_harga_saham(S0, naik_tahun, volatilitas, T, N):
    """
    Simulasi harga saham akhir (setelah T tahun) sebanyak N kali.

    S0           = harga sekarang (misal 100)
    naik_tahun   = rata-rata pertumbuhan per tahun (misal 0.08 = 8%)
    volatilitas  = seberapa 'gila' naik turunnya (misal 0.2 = 20%)
    T            = waktu (tahun, misal 1)
    N            = jumlah simulasi

    RETURN: array N harga saham akhir (ini kumpulan random variable)
    """
    # Z = angka acak normal (lonjong tengah), ini 'kejutan' pasar
    Z = np.random.standard_normal(N)
    # Rumus gerak saham acak (GBM, penyederhanaan):
    # log(S_T) = log(S0) + (naik - 0.5*vol^2)*T + vol*sqrt(T)*Z
    S_T = S0 * np.exp((naik_tahun - 0.5 * volatilitas**2) * T
                       + volatilitas * np.sqrt(T) * Z)
    return S_T


def harga_call_option(S0, K, naik_tahun, volatilitas, T, r, N=200_000):
    """
    Hitung harga call option pakai Monte Carlo.

    K  = harga strike (hak beli di harga ini, misal 100)
    r  = suku bunga bebas risiko (misal 0.05 = 5%)
    """
    S_T = simulasi_harga_saham(S0, naik_tahun, volatilitas, T, N)
    payoff = np.maximum(S_T - K, 0)          # untung tiap skenario
    rata_rata_untung = np.mean(payoff)        # ekspektasi (Law of Large Numbers)
    harga_sekarang = np.exp(-r * T) * rata_rata_untung  # diskon ke hari ini
    return harga_sekarang, S_T


if __name__ == "__main__":
    print("=" * 55)
    print("MONTE CARLO LEVEL 2 - HARGA OPSI SAHAM")
    print("=" * 55)

    S0 = 100      # harga saham sekarang
    K = 100       # hak beli di 100
    naik = 0.08   # rata-rata naik 8%/thn
    vol = 0.20    # volatilitas 20%
    T = 1.0       # 1 tahun
    r = 0.05      # bunga 5%

    harga, sampel = harga_call_option(S0, K, naik, vol, T, r, N=200_000)
    print(f"Harga opsi (Monte Carlo) = Rp {harga:.2f} per lembar")
    print(f"Bandingkan: harga saham sekarang = {S0}")
    print()
    print("Coba ubah N jadi 1_000_000 -> hasil makin stabil.")
    print("Coba ubah vol jadi 0.40 -> opsi makin mahal (risiko tinggi).")
