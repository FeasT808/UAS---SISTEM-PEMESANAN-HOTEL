# 🏨 SISTEM PEMESANAN HOTEL
## UAS Pemrograman Berorientasi Objek (PBO)

---

## 📋 RINGKASAN PROYEK

Aplikasi web **Hotel Booking System** yang mengimplementasikan seluruh konsep Pemrograman Berorientasi Objek (OOP) dengan lengkap, termasuk:

✅ **Abstract Class** (Room)
✅ **Inheritance** (3 child classes)  
✅ **Encapsulation** (Private attributes + @property)
✅ **Polymorphism** (Different implementations)
✅ **Abstraction** (Abstract methods)
✅ **CRUD Operations** (Create, Read, Update, Delete)
✅ **JSON Storage** (Tidak menggunakan database)
✅ **Flask Web Framework**
✅ **Elegant UI** (Bootstrap 5)
✅ **Authentication & Session Management**
✅ **Role-based Access Control** (Admin & Tamu)
✅ **Logging & Audit Trail**

---

## 🎯 FITUR UTAMA

### 1. Manajemen Kamar (Room Management)
- **3 Tipe Kamar** dengan karakteristik berbeda:
  - 🏠 **Standard**: Rp 500,000/malam (2 orang)
  - 🏡 **Deluxe**: Rp 800,000/malam (3 orang) + Diskon 10% >3 malam
  - 🏰 **Suite**: Rp 1,500,000/malam (4 orang) + Diskon 15% >3 malam + Breakfast

### 2. Sistem Booking
- Pemesanan kamar dengan perhitungan otomatis
- Validasi tanggal check-in/check-out
- Kalkulasi harga dengan diskon otomatis (polymorphism)
- Tracking status booking (Active, Completed, Cancelled)

### 3. User Management
- **Admin**: Full access ke semua fitur
- **Tamu**: Access terbatas untuk booking sendiri

### 4. Audit Trail
- Semua aktivitas tercatat di `app.log`
- Login success/failed
- CRUD operations
- System errors

---

## 📁 STRUKTUR PROYEK

```
UAS - SISTEM PEMESANAN HOTEL/
│
├── 📄 app.py                    # Main Flask application
├── 📄 models.py                 # OOP Classes (Abstract & Concrete)
├── 📄 utils.py                  # Helper functions & data operations
├── 📄 test_oop.py              # OOP verification test
├── 📄 run.bat                   # Quick start script
├── 📄 requirements.txt          # Dependencies
├── 📄 README.md                 # Project documentation
├── 📄 DOKUMENTASI_OOP.md       # Detailed OOP implementation
├── 📄 app.log                  # Application logs
│
├── 📁 data/
│   ├── users.json              # User accounts
│   ├── rooms.json              # Room data
│   └── bookings.json           # Booking records
│
└── 📁 templates/
    ├── base.html               # Base template (inheritance)
    ├── login.html              # Login page
    ├── dashboard.html          # Main dashboard
    ├── rooms.html              # Room list
    ├── add_room.html           # Add room form
    ├── edit_room.html          # Edit room form
    ├── bookings.html           # Booking list
    ├── add_booking.html        # Create booking form
    ├── edit_booking.html       # Edit booking form
    ├── booking_detail.html     # Booking details
    └── logs.html               # System logs (admin)
```

---

## 🚀 CARA MENJALANKAN

### Metode 1: Quick Start (Recommended)
```bash
# Double-click file run.bat
# atau jalankan di terminal:
run.bat
```

### Metode 2: Manual
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run application
python app.py
```

### 3. Akses Aplikasi
Buka browser: **http://localhost:5000**

---

## 👥 AKUN DEMO

### 🔑 Admin Account
```
Username: admin
Password: admin123
```
**Akses:**
- ✅ Tambah/Edit/Hapus Kamar
- ✅ Lihat Semua Booking
- ✅ System Logs
- ✅ Full CRUD Access

### 🔑 Tamu Account 1
```
Username: tamu1
Password: tamu123
```

### 🔑 Tamu Account 2
```
Username: tamu2
Password: tamu123
```
**Akses:**
- ✅ Lihat Kamar Tersedia
- ✅ Buat Booking
- ✅ Lihat/Edit/Hapus Booking Sendiri
- ❌ Tidak bisa kelola kamar
- ❌ Tidak bisa lihat logs

---

## 🎨 TEKNOLOGI

### Backend
- 🐍 **Python 3.x**
- 🌶️ **Flask 3.0.0** - Web Framework
- 📦 **JSON** - Data Storage

### Frontend
- 🎨 **Bootstrap 5.3.2** - UI Framework
- 🎭 **Bootstrap Icons 1.11.2** - Icon Library
- 📱 **Responsive Design**
- ✨ **Custom CSS** with Gradients

---

## 🏗️ IMPLEMENTASI OOP

### 1️⃣ Abstract Class
```python
from abc import ABC, abstractmethod

class Room(ABC):
    @abstractmethod
    def get_room_type(self) -> str:
        pass
    
    @abstractmethod
    def calculate_price(self, nights: int) -> float:
        pass
    
    @abstractmethod
    def get_amenities(self) -> List[str]:
        pass
```

### 2️⃣ Inheritance
```python
class StandardRoom(Room):
    def __init__(self, room_id: str, room_number: str):
        super().__init__(room_id, room_number, 
                        capacity=2, base_price=500000)

class DeluxeRoom(Room):
    def __init__(self, room_id: str, room_number: str):
        super().__init__(room_id, room_number, 
                        capacity=3, base_price=800000)

class SuiteRoom(Room):
    def __init__(self, room_id: str, room_number: str):
        super().__init__(room_id, room_number, 
                        capacity=4, base_price=1500000)
```

### 3️⃣ Polymorphism
Setiap tipe kamar punya logika pricing berbeda:

**Standard** → Harga normal
```python
def calculate_price(self, nights: int) -> float:
    return self._base_price * nights
```

**Deluxe** → Diskon 10% untuk >3 malam
```python
def calculate_price(self, nights: int) -> float:
    total = self._base_price * nights
    if nights > 3:
        total *= 0.9  # 10% off
    return total
```

**Suite** → Diskon 15% untuk >3 malam
```python
def calculate_price(self, nights: int) -> float:
    total = self._base_price * nights
    if nights > 3:
        total *= 0.85  # 15% off
    return total
```

### 4️⃣ Encapsulation
```python
# Private attributes
self._room_id = room_id
self._room_number = room_number
self._capacity = capacity
self._base_price = base_price

# Public getter
@property
def room_id(self):
    return self._room_id

# Public setter
@is_available.setter
def is_available(self, value: bool):
    self._is_available = value
```

---

## 📊 DIAGRAM KELAS

```
                    ┌─────────────┐
                    │   Room      │ (Abstract)
                    ├─────────────┤
                    │ - _room_id  │
                    │ - _room_number│
                    │ - _capacity │
                    │ - _base_price│
                    │ - _is_available│
                    ├─────────────┤
                    │ + get_room_type()│ (abstract)
                    │ + calculate_price()│ (abstract)
                    │ + get_amenities()│ (abstract)
                    └──────┬──────┘
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
    ┌────▼────┐      ┌────▼────┐      ┌────▼────┐
    │Standard │      │ Deluxe  │      │  Suite  │
    │  Room   │      │  Room   │      │  Room   │
    └─────────┘      └─────────┘      └─────────┘

┌──────────┐        ┌──────────┐
│   User   │        │ Booking  │
├──────────┤        ├──────────┤
│- user_id │        │- booking_id│
│- username│        │- user_id │
│- password│        │- room_id │
│- role    │        │- check_in│
│- full_name│       │- check_out│
└──────────┘        └──────────┘
```

---

## 📝 LOGGING FORMAT

```
[Timestamp] [Status] [User] Activity
```

**Contoh:**
```
[2025-12-23 20:35:34] [SUCCESS] [admin] Login berhasil untuk user: admin
[2025-12-23 20:36:15] [CREATE] [admin] Kamar baru dibuat: Standard - 103
[2025-12-23 20:37:22] [CREATE] [tamu1] Booking baru dibuat: B0001 untuk kamar 101
[2025-12-23 20:38:10] [UPDATE] [tamu1] Booking B0001 status diupdate: active -> completed
[2025-12-23 20:39:05] [DELETE] [admin] Kamar R007 dihapus
[2025-12-23 20:40:00] [ERROR] [System] Error loading rooms: File not found
```

---

## 🧪 TESTING

Jalankan test OOP verification:
```bash
python test_oop.py
```

Test akan memverifikasi:
- ✅ Abstract class tidak bisa di-instantiate
- ✅ Child classes berhasil dibuat
- ✅ Polymorphism dalam calculate_price()
- ✅ Encapsulation dengan property decorators
- ✅ Abstract methods implemented di semua child
- ✅ Object serialization ke dictionary
- ✅ User role-based logic
- ✅ Booking class functionality

---

## 📖 DOKUMENTASI TAMBAHAN

1. **README.md** - Overview dan instalasi
2. **DOKUMENTASI_OOP.md** - Detail implementasi OOP dengan checklist
3. **PROJECT_SUMMARY.md** - File ini (ringkasan lengkap)

---

## ✅ CHECKLIST KETENTUAN UAS

### 4.1 Pemrograman Berorientasi Objek
- ✅ Minimal 1 class abstrak → **Room**
- ✅ Minimal 2 class turunan → **StandardRoom, DeluxeRoom, SuiteRoom** (3 classes!)
- ✅ Encapsulation → Private attributes + @property
- ✅ Inheritance → super().__init__()
- ✅ Polymorphism → Different calculate_price()
- ✅ Abstraction → Abstract methods

### 4.2 CRUD Berbasis OOP
- ✅ Create → create_room(), create_booking()
- ✅ Read → load_rooms(), load_bookings(), get_room_by_id()
- ✅ Update → update_room_availability(), update_booking_status()
- ✅ Delete → delete_room(), delete_booking()

### 4.3 Penyimpanan Data
- ✅ Menggunakan file JSON
- ✅ Tidak menggunakan database

### 4.4 Aplikasi Web Flask
- ✅ Routing Flask → 12 routes
- ✅ Form input HTML → 5 forms
- ✅ Template sederhana → 11 templates
- ✅ UI elegant → Bootstrap 5 + custom CSS

### 4.5 Authentication & Session
- ✅ Login dan logout pengguna
- ✅ Session Flask untuk status login
- ✅ Role-based access control (Admin dan Tamu)

### 4.6 Logging & Audit Trail
- ✅ Login berhasil/gagal
- ✅ Transaksi utama (booking)
- ✅ Update data
- ✅ Delete data
- ✅ Error sistem

---

## 🎉 KESIMPULAN

Aplikasi **Sistem Pemesanan Hotel** ini:

1. ✅ **MEMENUHI 100% ketentuan UAS**
2. ✅ **Implementasi OOP yang solid dan clean**
3. ✅ **UI yang elegant dan user-friendly**
4. ✅ **Code yang well-documented**
5. ✅ **Siap untuk didemonstrasikan**

---

## 📞 SUPPORT

Untuk pertanyaan atau issue:
1. Baca **README.md** untuk instalasi
2. Baca **DOKUMENTASI_OOP.md** untuk detail OOP
3. Jalankan **test_oop.py** untuk verifikasi

---

## 📜 LICENSE

Proyek ini dibuat untuk tujuan **UAS Pemrograman Berorientasi Objek**.
© 2025 - Sistem Pemesanan Hotel

---

**🏨 Selamat Menggunakan Sistem Pemesanan Hotel! 🎊**
