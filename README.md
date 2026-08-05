# Quant Monte Carlo — Belajar dari Nol

Repo ini buat **belajar Monte Carlo dari yang paling gampang** sampai
bisa dipakai buat harga opsi saham (quant finance).

Setiap file bisa dijalankan langsung:
```bash
python3 01_dadu_dan_pi.py
python3 02_harga_opsi_sederhana.py
python3 03_black_scholes_vs_montecarlo.py
```

## Urutan Belajar (ikuti urut)

| File | Topik | Level |
|------|-------|-------|
| `01_dadu_dan_pi.py` | Lempar dadu & cari pi pakai titik acak | 🟢 Paling mudah |
| `02_harga_opsi_sederhana.py` | Harga opsi saham dengan simulasi acak | 🟡 Menengah |
| `03_black_scholes_vs_montecarlo.py` | Bukti MC = rumus (konvergensi) | 🔵 Lanjut |

## Konsep Inti (baca ini dulu!)

**Monte Carlo = ulangi hal acak berkali-kali, lalu ambil rata-rata.**

- Kamu sudah tahu **random variable** & **finite probability space**.
- Monte Carlo cuma pakai itu: ambil sampel random variable berkali-kali,
  rata-ratanya → ekspektasi (Law of Large Numbers).
- Di quant: harga saham masa depan = random variable. Kita simulasi jutaan
  skenario, hitung untung tiap skenario, rata-rata → harga opsi.

### Kenapa konvergen lambat?
Error Monte Carlo = $O(1/\sqrt{N})$.
Artinya: mau 10× lebih akurat → butuh **100× lebih banyak sampel**.
Makanya quant pakai *variance reduction* (lanjut nanti).

## Prasyarat
- Python 3 + numpy (`pip install numpy`)
- Sudah paham dasar probability (random variable, ekspektasi) — lihat FinMath YouTube.

## Next (stochastic calculus)
Setelah 3 file ini lancar, lanjut pelajari:
- Geometric Brownian Motion (GBM) secara formal
- Itô's lemma
- Variance reduction: antithetic variates, control variates

---
*Belajar quant*
