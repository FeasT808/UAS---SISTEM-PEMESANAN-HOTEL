# DOKUMENTASI IMPLEMENTASI OOP
# Sistem Pemesanan Hotel - UAS PBO

## ✅ CHECKLIST KETENTUAN TEKNIS

### 4.1 Pemrograman Berorientasi Objek

#### ✅ 1. Minimal 1 Class Abstrak
**File**: `models.py`
- Class: `Room` (abstract base class)
- Menggunakan `ABC` (Abstract Base Class) dari module `abc`
- Berisi 3 abstract methods yang wajib diimplementasikan oleh child classes

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

#### ✅ 2. Minimal 2 Class Turunan
**File**: `models.py`
- `StandardRoom` - extends Room
- `DeluxeRoom` - extends Room  
- `SuiteRoom` - extends Room

Setiap class turunan:
- Memanggil `super().__init__()` untuk inheritance
- Mengimplementasikan semua abstract methods
- Memiliki karakteristik unik sesuai tipe kamar

#### ✅ 3. Encapsulation
**Implementasi**:
- Semua attributes menggunakan underscore prefix (`_room_id`, `_room_number`, dll)
- Access melalui `@property` decorator (getter)
- Setter untuk attributes yang boleh diubah

```python
# Private attributes
def __init__(self, room_id: str, room_number: str, capacity: int, base_price: float):
    self._room_id = room_id
    self._room_number = room_number
    self._capacity = capacity
    self._base_price = base_price
    self._is_available = True

# Getter
@property
def room_id(self):
    return self._room_id

# Setter
@is_available.setter
def is_available(self, value: bool):
    self._is_available = value
```

#### ✅ 4. Inheritance
**Implementasi**:
- `StandardRoom`, `DeluxeRoom`, `SuiteRoom` inherit dari `Room`
- Memanggil constructor parent class dengan `super().__init__()`
- Mewarisi semua methods dan properties dari parent

```python
class StandardRoom(Room):
    def __init__(self, room_id: str, room_number: str):
        super().__init__(room_id, room_number, capacity=2, base_price=500000)
```

#### ✅ 5. Polymorphism
**Implementasi**:
Setiap child class mengimplementasikan abstract methods dengan behavior berbeda:

**a. `calculate_price()` - Different pricing logic**
```python
# StandardRoom
def calculate_price(self, nights: int) -> float:
    return self._base_price * nights

# DeluxeRoom - 10% discount untuk >3 malam
def calculate_price(self, nights: int) -> float:
    total = self._base_price * nights
    if nights > 3:
        total *= 0.9
    return total

# SuiteRoom - 15% discount untuk >3 malam
def calculate_price(self, nights: int) -> float:
    total = self._base_price * nights
    if nights > 3:
        total *= 0.85
    return total
```

**b. `get_room_type()` - Different room types**
```python
# StandardRoom
def get_room_type(self) -> str:
    return "Standard"

# DeluxeRoom
def get_room_type(self) -> str:
    return "Deluxe"

# SuiteRoom
def get_room_type(self) -> str:
    return "Suite"
```

**c. `get_amenities()` - Different amenities**
```python
# StandardRoom
def get_amenities(self) -> List[str]:
    return ["Single Bed", "WiFi", "TV", "AC", "Kamar Mandi"]

# DeluxeRoom
def get_amenities(self) -> List[str]:
    return ["Queen Bed", "WiFi Premium", "Smart TV", "AC", 
            "Kamar Mandi + Bathtub", "Mini Bar", "Balcony"]

# SuiteRoom  
def get_amenities(self) -> List[str]:
    return ["King Bed", "WiFi Premium", "Smart TV 55\"", "AC", 
            "Kamar Mandi Premium + Jacuzzi", "Mini Bar Premium", 
            "Living Room", "Balcony", "Breakfast Included"]
```

#### ✅ 6. Abstraction
**Implementasi**:
- Abstract class `Room` mendefinisikan interface
- Child classes wajib implement abstract methods
- Menyembunyikan kompleksitas implementasi

### 4.2 CRUD Berbasis OOP

#### ✅ CREATE
**File**: `utils.py`
- `create_room()` - Membuat kamar baru dengan OOP
- `create_booking()` - Membuat booking dengan memanggil method OOP `calculate_price()`

```python
def create_room(room_type: str, room_number: str, user: str) -> Optional[Room]:
    # Create room based on type (Polymorphism)
    if room_type == 'Standard':
        new_room = StandardRoom(room_id, room_number)
    elif room_type == 'Deluxe':
        new_room = DeluxeRoom(room_id, room_number)
    elif room_type == 'Suite':
        new_room = SuiteRoom(room_id, room_number)
```

#### ✅ READ
**File**: `utils.py`, `app.py`
- `load_rooms()` - Load dan create room objects
- `load_bookings()` - Load booking objects
- `get_room_by_id()` - Get specific room object
- Routes: `/rooms`, `/bookings`, `/dashboard`

#### ✅ UPDATE
**File**: `utils.py`
- `update_room_availability()` - Update room status menggunakan setter
- `update_booking_status()` - Update booking status

```python
def update_room_availability(room_id: str, is_available: bool, user: str):
    room.is_available = is_available  # Using setter from encapsulation
```

#### ✅ DELETE
**File**: `utils.py`
- `delete_room()` - Delete room
- `delete_booking()` - Delete booking

### 4.3 Penyimpanan Data

#### ✅ Menggunakan File JSON
**File**: `data/`
- `users.json` - User data
- `rooms.json` - Room data  
- `bookings.json` - Booking data

**TIDAK menggunakan database**

### 4.4 Aplikasi Web Flask

#### ✅ Routing Flask
**File**: `app.py`
- `/` - Index/redirect
- `/login` - Login page
- `/logout` - Logout
- `/dashboard` - Dashboard
- `/rooms` - Room list
- `/rooms/add` - Add room
- `/rooms/edit/<id>` - Edit room
- `/rooms/delete/<id>` - Delete room
- `/bookings` - Booking list
- `/bookings/add` - Add booking
- `/bookings/edit/<id>` - Edit booking
- `/bookings/delete/<id>` - Delete booking
- `/bookings/detail/<id>` - Booking detail
- `/logs` - System logs

#### ✅ Form Input HTML
**Templates**: `templates/`
- `login.html` - Login form
- `add_room.html` - Room form
- `edit_room.html` - Room edit form
- `add_booking.html` - Booking form with JavaScript calculation
- `edit_booking.html` - Booking edit form

#### ✅ Template Sederhana
- Base template dengan inheritance
- Reusable components
- Clean structure

#### ✅ UI Elegant
- Bootstrap 5.3.2
- Bootstrap Icons 1.11.2
- Custom CSS dengan gradient colors
- Responsive design
- Smooth animations
- Card-based layout
- Professional color scheme

### 4.5 Authentication & Session

#### ✅ Login dan Logout Pengguna
**File**: `app.py`
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    user = utils.authenticate_user(username, password)
    if user:
        session['user_id'] = user.user_id
        session['username'] = user.username
        session['role'] = user.role
```

#### ✅ Session Flask untuk Status Login
**Implementasi**:
- Flask session untuk menyimpan user data
- Decorators untuk protect routes:
  - `@login_required` - Butuh login
  - `@admin_required` - Butuh role admin

#### ✅ Role-based Access Control
**Roles**:
- **Admin**: Full access
  - CRUD kamar
  - Lihat semua booking
  - View logs
  
- **Tamu**: Limited access
  - View kamar
  - CRUD booking sendiri
  - Tidak bisa akses admin features

```python
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = utils.get_user_by_id(session['user_id'])
        if not user or not user.is_admin():
            flash('Akses ditolak. Hanya admin yang dapat mengakses halaman ini.', 'danger')
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated_function
```

### 4.6 Logging & Audit Trail

#### ✅ Aktivitas Dicatat ke File Log
**File**: `app.log`
**Function**: `log_activity()` in `utils.py`

```python
def log_activity(activity: str, user: str = "System", status: str = "INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{status}] [{user}] {activity}\n"
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(log_entry)
```

#### ✅ Login Berhasil/Gagal
```python
# Berhasil
log_activity(f"Login berhasil untuk user: {username}", user=username, status="SUCCESS")

# Gagal
log_activity(f"Login gagal untuk user: {username}", user=username, status="FAILED")
```

#### ✅ Transaksi Utama
```python
log_activity(f"Booking baru dibuat: {booking_id} untuk kamar {room.room_number}", 
            user=username, status="CREATE")
```

#### ✅ Update Data
```python
log_activity(f"Kamar {room.room_number} diupdate - Available: {is_available}", 
            user=user, status="UPDATE")

log_activity(f"Booking {booking_id} status diupdate: {old_status} -> {status}", 
            user=user, status="UPDATE")
```

#### ✅ Delete Data
```python
log_activity(f"Kamar {room_id} dihapus", user=user, status="DELETE")

log_activity(f"Booking {booking_id} dihapus", user=user, status="DELETE")
```

#### ✅ Error Sistem
```python
log_activity(f"Error loading users: {str(e)}", status="ERROR")

log_activity(f"Error saving rooms: {str(e)}", status="ERROR")
```

## SUMMARY IMPLEMENTASI OOP

### Classes Created:
1. **Room** (Abstract) - Base class untuk semua kamar
2. **StandardRoom** (Concrete) - Kamar standar
3. **DeluxeRoom** (Concrete) - Kamar deluxe
4. **SuiteRoom** (Concrete) - Kamar suite
5. **User** - User management
6. **Booking** - Booking management

### OOP Principles Demonstrated:

| Principle | Implementation | Location |
|-----------|---------------|----------|
| **Abstraction** | Abstract class `Room` dengan abstract methods | `models.py` lines 7-47 |
| **Encapsulation** | Private attributes dengan `@property` decorators | `models.py` throughout |
| **Inheritance** | 3 room classes inherit dari `Room` | `models.py` lines 50-125 |
| **Polymorphism** | Different implementations of abstract methods | `models.py` each child class |

### Benefits of OOP in This Project:
1. **Maintainability**: Easy to add new room types
2. **Reusability**: Common room logic in base class
3. **Extensibility**: Can add new features without breaking existing code
4. **Type Safety**: Strong typing with type hints
5. **Clean Code**: Separation of concerns

## CARA TESTING

### 1. Login sebagai Admin
```
Username: admin
Password: admin123
```

### 2. Test CRUD Kamar (Admin)
- Tambah kamar baru
- Edit status ketersediaan
- Lihat daftar kamar
- Hapus kamar

### 3. Login sebagai Tamu
```
Username: tamu1
Password: tamu123
```

### 4. Test CRUD Booking (Tamu)
- Buat booking baru (lihat polymorphism dalam perhitungan harga)
- Edit booking
- Lihat detail booking
- Hapus booking

### 5. Test Logging (Admin)
- Login sebagai admin
- Akses /logs
- Lihat semua aktivitas tercatat

### 6. Test Role-based Access
- Login sebagai tamu
- Coba akses /rooms/add (akan ditolak)
- Coba akses /logs (akan ditolak)

## KESIMPULAN

Aplikasi ini MEMENUHI SEMUA ketentuan UAS:
✅ Minimal 1 class abstrak
✅ Minimal 2 class turunan (ada 3)
✅ Encapsulation
✅ Inheritance
✅ Polymorphism
✅ Abstraction
✅ CRUD lengkap
✅ Penyimpanan JSON
✅ Flask web app dengan routing
✅ Form input HTML
✅ UI elegant
✅ Authentication & session
✅ Role-based access control
✅ Logging & audit trail lengkap

Aplikasi siap untuk didemonstrasikan dan dinilai!
