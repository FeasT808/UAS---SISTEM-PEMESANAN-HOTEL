# 🚀 QUICK START GUIDE
## Sistem Pemesanan Hotel

---

## ⚡ START APLIKASI (3 Cara)

### 1. Cara Tercepat 🏃‍♂️
```bash
# Double-click file ini:
run.bat
```

### 2. Via Command Line 💻
```bash
python app.py
```

### 3. Via VS Code ▶️
```
Tekan F5 atau klik "Run Python File"
```

---

## 🌐 AKSES APLIKASI

Buka browser → **http://localhost:5000**

---

## 👤 LOGIN

### Admin (Full Access)
```
Username: admin
Password: admin123
```

### Tamu (Limited Access)
```
Username: tamu1
Password: tamu123
```

---

## 🎯 FITUR UTAMA

### Sebagai ADMIN 👨‍💼

#### 1️⃣ Kelola Kamar
- Klik **"Kamar"** di menu
- **Tambah**: Klik tombol "Tambah Kamar"
  - Pilih tipe: Standard/Deluxe/Suite
  - Masukkan nomor kamar
  - Klik "Simpan Kamar"
- **Edit**: Klik tombol "Edit" pada kamar
- **Hapus**: Klik tombol "Hapus" pada kamar

#### 2️⃣ Kelola Booking
- Klik **"Booking"** di menu
- Lihat semua booking dari semua tamu
- Edit status: Active/Completed/Cancelled
- Hapus booking

#### 3️⃣ Lihat Logs
- Klik **"Logs"** di menu
- Lihat semua aktivitas sistem

### Sebagai TAMU 🙋‍♂️

#### 1️⃣ Lihat Kamar Tersedia
- Klik **"Kamar"** di menu
- Lihat detail kamar, harga, fasilitas

#### 2️⃣ Buat Booking
- Klik **"Booking"** → "Buat Booking"
- Isi data:
  - Nama tamu
  - Nomor telepon
  - Pilih kamar
  - Tanggal check-in
  - Tanggal check-out
- Sistem akan hitung harga otomatis
- Klik "Buat Booking"

#### 3️⃣ Kelola Booking Sendiri
- Lihat booking yang sudah dibuat
- Edit status booking
- Hapus booking

---

## 💰 TIPE KAMAR & HARGA

### 🏠 Standard Room
- **Harga**: Rp 500,000/malam
- **Kapasitas**: 2 orang
- **Fasilitas**: 5 items

### 🏡 Deluxe Room
- **Harga**: Rp 800,000/malam
- **Kapasitas**: 3 orang
- **Diskon**: 10% untuk booking >3 malam
- **Fasilitas**: 7 items

### 🏰 Suite Room
- **Harga**: Rp 1,500,000/malam
- **Kapasitas**: 4 orang
- **Diskon**: 15% untuk booking >3 malam
- **Bonus**: Breakfast Included
- **Fasilitas**: 9 items

---

## 🎓 DEMO UNTUK UAS

### Skenario Demo Lengkap (5-10 menit)

#### 1. Login sebagai Admin
```
Username: admin
Password: admin123
```

#### 2. Demo Dashboard
- Tunjukkan statistik
- Total kamar, tersedia, booking

#### 3. Demo CRUD Kamar
- **CREATE**: Tambah kamar baru (Standard, nomor 103)
- **READ**: Lihat daftar kamar
- **UPDATE**: Edit status kamar (ubah jadi tidak tersedia)
- **DELETE**: Hapus kamar (yang baru ditambah)

#### 4. Logout & Login sebagai Tamu
```
Username: tamu1
Password: tamu123
```

#### 5. Demo Booking
- **CREATE**: Buat booking baru
  - Pilih Suite Room (untuk demo diskon)
  - Booking 5 malam (dapat diskon 15%)
  - Tunjukkan kalkulasi harga otomatis
- **READ**: Lihat detail booking
- **UPDATE**: Edit status booking
- **DELETE**: Hapus booking

#### 6. Login kembali sebagai Admin
```
Username: admin
Password: admin123
```

#### 7. Demo Logs
- Klik "Logs"
- Tunjukkan semua aktivitas tercatat:
  - Login success/failed
  - CRUD operations
  - User tracking

#### 8. Demo OOP Concepts
Buka file `models.py` dan tunjukkan:
- Abstract class `Room`
- Inheritance di `StandardRoom`, `DeluxeRoom`, `SuiteRoom`
- Polymorphism di method `calculate_price()`
- Encapsulation dengan `@property`

---

## 🧪 TEST OOP

Untuk verifikasi implementasi OOP:
```bash
python test_oop.py
```

Output akan menunjukkan:
- ✅ Abstract class test
- ✅ Inheritance test
- ✅ Polymorphism test
- ✅ Encapsulation test
- ✅ Abstraction test

---

## 📊 DATA AWAL

### Users (3 akun)
- 1 Admin: admin
- 2 Tamu: tamu1, tamu2

### Rooms (6 kamar)
- 2 Standard: 101, 102
- 2 Deluxe: 201, 202
- 2 Suite: 301, 302

### Bookings
- Kosong (siap untuk demo)

---

## 🐛 TROUBLESHOOTING

### Aplikasi tidak jalan?
```bash
# Install dependencies lagi
pip install -r requirements.txt

# Pastikan di folder yang benar
cd "d:\SEMS 3\PBO\UAS - SISTEM PEMESANAN HOTEL"

# Jalankan
python app.py
```

### Port 5000 sudah dipakai?
Edit `app.py` line terakhir:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Ganti port
```

### Login tidak bisa?
Cek file `data/users.json` ada dan tidak corrupt.

---

## 📚 FILE DOKUMENTASI

1. **README.md** → Overview proyek
2. **DOKUMENTASI_OOP.md** → Detail implementasi OOP
3. **PROJECT_SUMMARY.md** → Ringkasan lengkap
4. **QUICK_START.md** → File ini (panduan cepat)

---

## ✅ CHECKLIST SEBELUM DEMO

- [ ] Flask terinstall
- [ ] Aplikasi bisa jalan di http://localhost:5000
- [ ] Login admin berhasil
- [ ] Login tamu berhasil
- [ ] Dashboard tampil normal
- [ ] CRUD kamar berfungsi
- [ ] CRUD booking berfungsi
- [ ] Logs tercatat dengan benar
- [ ] UI tampil dengan baik (Bootstrap loaded)

---

## 🎉 SIAP DEMO!

**Aplikasi 100% lengkap dan memenuhi semua ketentuan UAS!**

---

## 🆘 NEED HELP?

1. Baca file README.md
2. Baca file DOKUMENTASI_OOP.md
3. Jalankan test_oop.py untuk verifikasi
4. Check app.log untuk error logs

---

**🏨 Good Luck dengan UAS! 🎊**
