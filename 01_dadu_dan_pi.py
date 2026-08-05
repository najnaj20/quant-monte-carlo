"""
NAMA FILE: 01_dadu_dan_pi.py
BAGIAN 1 dari belajar Monte Carlo - level paling mudah.

Monte Carlo itu cuma satu ide:
  "Kalau kita coba sesuatu berkali-kali secara acak,
   rata-rata hasilnya bakal mendekati nilai yang 'sebenarnya'."

Ini persis seperti Law of Large Numbers yang kamu sudah pelajari:
lempar dadu banyak kali -> rata-ratanya mendekati 3.5 (ekspektasi).

Di file ini kita buktikan 2 hal sederhana PAKE KODE:
  1. Lempar dadu -> rata-rata mendekati 3.5
  2. Titik acak di kotak -> kita bisa "nemuin" nilai pi
"""

import random
import math


def bukti_dadu(jumlah_lempar=100_000):
    """
    Lempar dadu (1-6) berkali-kali.
    Ekspektasi teoritis = (1+2+3+4+5+6)/6 = 3.5
    """
    total = 0
    for _ in range(jumlah_lempar):
        mata = random.randint(1, 6)   # random variable: nilai 1..6 sama mungkin
        total += mata
    rata_rata = total / jumlah_lempar
    print(f"[DADU] setelah {jumlah_lempar} lempar, rata-rata = {rata_rata:.4f}")
    print(f"[DADU] ekspektasi teoritis         = 3.5000")
    print(f"[DADU] selisih                      = {abs(rata_rata - 3.5):.4f}")
    return rata_rata


def bukti_pi(jumlah_titik=1_000_000):
    """
    Bayangin kotak 2x2 (dari -1 sampai 1) dengan lingkaran radius 1 di tengah.
    Luas kotak  = 4
    Luas lingkaran = pi * r^2 = pi
    Jadi proporsi titik yang jatuh DI DALAM lingkaran = pi / 4.

    Kita sebar titik acak, hitung berapa yang masuk lingkaran,
    lalu:  pi ~ 4 * (jumlah_masuk / jumlah_total)
    """
    masuk = 0
    for _ in range(jumlah_titik):
        x = random.uniform(-1, 1)   # random variable uniform di [-1,1]
        y = random.uniform(-1, 1)
        if x*x + y*y <= 1:          # di dalam lingkaran?
            masuk += 1
    pi_est = 4 * masuk / jumlah_titik
    print(f"[PI]   setelah {jumlah_titik} titik, pi ~ {pi_est:.5f}")
    print(f"[PI]   pi sebenarnya            = {math.pi:.5f}")
    print(f"[PI]   selisih                  = {abs(pi_est - math.pi):.5f}")
    return pi_est


if __name__ == "__main__":
    print("=" * 55)
    print("MONTE CARLO LEVEL 1 - DADU & PI")
    print("=" * 55)
    bukti_dadu()
    print()
    bukti_pi()
    print()
    print("Kesimpulan: makin banyak sampel, makin dekat ke nilai bener.")
    print("Itu inti Monte Carlo. Di file berikutnya kita pakai")
    print("cara ini buat menghitung harga opsi saham.")
