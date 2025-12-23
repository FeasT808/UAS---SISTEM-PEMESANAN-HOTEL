# Sistem Pemesanan Hotel
UAS Pemrograman Berorientasi Objek (PBO)

## Deskripsi Proyek
Aplikasi web berbasis Flask untuk sistem pemesanan hotel dengan implementasi konsep Pemrograman Berorientasi Objek (PBO).

## Fitur Utama

### 1. Pemrograman Berorientasi Objek
- **Abstract Class**: `Room` sebagai base class untuk semua jenis kamar
- **Inheritance**: `StandardRoom`, `DeluxeRoom`, `SuiteRoom` mewarisi dari `Room`
- **Encapsulation**: Properties dengan getter/setter untuk data protection
- **Polymorphism**: Method `calculate_price()`, `get_amenities()`, `get_room_type()` diimplementasikan berbeda di setiap child class
- **Abstraction**: Abstract methods yang wajib diimplementasikan oleh child classes

### 2. CRUD Operations
- **Create**: Tambah kamar baru, buat booking
- **Read**: Lihat daftar kamar, booking, detail booking
- **Update**: Edit status kamar, update status booking
- **Delete**: Hapus kamar, hapus booking

### 3. Penyimpanan Data
- Menggunakan file JSON (tidak menggunakan database)
- File data:
  - `data/users.json` - Data pengguna
  - `data/rooms.json` - Data kamar
  - `data/bookings.json` - Data booking

### 4. Authentication & Authorization
- Login/Logout dengan session management
- Role-based access control:
  - **Admin**: Akses penuh (CRUD kamar, lihat semua booking, lihat logs)
  - **Tamu**: Akses terbatas (lihat kamar, buat booking, lihat booking sendiri)

### 5. Logging & Audit Trail
- Semua aktivitas dicatat ke file `app.log`
- Log mencakup:
  - Login berhasil/gagal
  - CRUD operations
  - Update/Delete data
  - Error sistem

### 6. User Interface
- Design elegant menggunakan Bootstrap 5
- Responsive design
- Icon dari Bootstrap Icons
- Gradient colors dan smooth animations

## Struktur Proyek
```
UAS - SISTEM PEMESANAN HOTEL/
├── app.py              # Main Flask application
├── models.py           # OOP Models (Room classes, User, Booking)
├── utils.py            # Helper functions & data operations
├── requirements.txt    # Python dependencies
├── app.log            # Application logs
├── data/
│   ├── users.json     # User data
│   ├── rooms.json     # Room data
│   └── bookings.json  # Booking data
└── templates/
    ├── base.html           # Base template
    ├── login.html          # Login page
    ├── dashboard.html      # Dashboard
    ├── rooms.html          # Room list
    ├── add_room.html       # Add room form
    ├── edit_room.html      # Edit room form
    ├── bookings.html       # Booking list
    ├── add_booking.html    # Add booking form
    ├── edit_booking.html   # Edit booking form
    ├── booking_detail.html # Booking detail
    └── logs.html           # System logs (admin only)
```

## Instalasi dan Menjalankan

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Jalankan Aplikasi
```bash
python app.py
```

### 3. Akses Aplikasi
Buka browser dan akses: `http://localhost:5000`

## Akun Demo

### Admin
- Username: `admin`
- Password: `admin123`

### Tamu
- Username: `tamu1`
- Password: `tamu123`

atau

- Username: `tamu2`
- Password: `tamu123`

## Fitur per Role

### Admin
✅ Lihat semua kamar
✅ Tambah kamar baru
✅ Edit status ketersediaan kamar
✅ Hapus kamar
✅ Lihat semua booking
✅ Edit status booking
✅ Hapus booking
✅ Lihat system logs

### Tamu
✅ Lihat kamar tersedia
✅ Buat booking baru
✅ Lihat booking sendiri
✅ Edit booking sendiri
✅ Hapus booking sendiri
✅ Lihat detail booking

## Kategori Kamar

### 1. Standard Room
- Kapasitas: 2 orang
- Harga: Rp 500,000/malam
- Fasilitas: Single Bed, WiFi, TV, AC, Kamar Mandi

### 2. Deluxe Room
- Kapasitas: 3 orang
- Harga: Rp 800,000/malam
- Diskon: 10% untuk booking >3 malam
- Fasilitas: Queen Bed, WiFi Premium, Smart TV, AC, Bathtub, Mini Bar, Balcony

### 3. Suite Room
- Kapasitas: 4 orang
- Harga: Rp 1,500,000/malam
- Diskon: 15% untuk booking >3 malam
- Bonus: Breakfast Included
- Fasilitas: King Bed, WiFi Premium, Smart TV 55", AC, Jacuzzi, Mini Bar Premium, Living Room, Balcony

## Implementasi Konsep OOP

### 1. Abstract Class
```python
class Room(ABC):
    @abstractmethod
    def get_room_type(self) -> str:
        pass
    
    @abstractmethod
    def calculate_price(self, nights: int) -> float:
        pass
```

### 2. Inheritance
```python
class StandardRoom(Room):
    def __init__(self, room_id: str, room_number: str):
        super().__init__(room_id, room_number, capacity=2, base_price=500000)
```

### 3. Polymorphism
Setiap child class mengimplementasikan `calculate_price()` dengan logika berbeda:
- StandardRoom: Harga normal
- DeluxeRoom: Diskon 10% untuk >3 malam
- SuiteRoom: Diskon 15% untuk >3 malam

### 4. Encapsulation
```python
@property
def room_id(self):
    return self._room_id

@property
def is_available(self):
    return self._is_available

@is_available.setter
def is_available(self, value: bool):
    self._is_available = value
```

## Teknologi yang Digunakan
- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5.3.2
- **Icons**: Bootstrap Icons 1.11.2
- **Data Storage**: JSON files

## Catatan Penting
- Aplikasi ini untuk tujuan pembelajaran UAS PBO
- Password tidak di-hash (untuk demo purposes)
- Dalam production, gunakan proper password hashing dan database

## Author
UAS PBO - Sistem Pemesanan Hotel
© 2025
