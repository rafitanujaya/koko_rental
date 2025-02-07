# Rental Mobil Domain & Style Guide

## Domain Mobil

Atribut untuk domain rental mobil:

- `plat_nomor`: Nomor plat kendaraan
- `brand`: Merek mobil
- `model`: Model mobil
- `price_rental`: Harga sewa per hari
- `supir`: Informasi ketersediaan supir (ya/tidak)
- `phone_supir`: Nomor telepon supir

## Notulen

Dokumen ini berfungsi sebagai panduan pengembangan program rental mobil dengan fokus pada konvensi penulisan kode, prinsip clean code, dan pengujian yang memadai.

## Style Guide

### 1. Naming Convention

Gunakan format `snake_case` untuk penamaan variabel dan fungsi.

### 2. Format String

Gunakan tanda kutip tunggal (`'`) untuk string.

### 3. Prefix Function

- Gunakan prefix `lengkap_` untuk fungsi yang menyelesaikan proses lengkap.
- Gunakan prefix `subrutin_` untuk subrutin yang mendukung fungsi utama.

### 4. Menu Pilihan

Wajib menggunakan `switch-case` untuk implementasi menu pilihan dalam program.

### 5. Commenting Functions

Berikan komentar pada setiap fungsi yang menjelaskan apa yang akan dikembalikan (return value).

## 6. Prioritas Subrutin

- **Subrutin fungsi (helper functions)** ditulis paling atas.
- **Subrutin program (modul kecil)** ditulis di bagian tengah.
- **Program utama** diletakkan di dalam fungsi `main()` saat proses development.

## 6. Clean Code Principle

Setiap subrutin hanya menangani **satu logika** (Single Responsibility Principle).


## 8. DRY (Don't Repeat Yourself)
Hindari pengulangan kode dengan membuat fungsi yang dapat digunakan ulang.

## 9. Code Review

Ada proses code review oleh tim untuk memastikan kualitas kode tetap terjaga.

Proses code review meliputi:

- Pengecekan kesesuaian dengan style guide.
- Pengecekan penerapan prinsip clean code.
- Pengecekan fungsionalitas dan logika program.

## 10. Unit Test
Setiap subrutin wajib memiliki unit test untuk memastikan fungsionalitas berjalan sesuai harapan.