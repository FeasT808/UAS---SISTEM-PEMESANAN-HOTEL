# ROLE-BASED BOOKING TEMPLATES - UPDATE SUMMARY

## Perubahan Yang Dilakukan

### 1. Template Terpisah untuk Admin dan User

**Dibuat 3 template baru:**

#### a) `templates/bookings_admin.html` - Untuk Admin
- **Akses:** Admin dapat melihat SEMUA booking dari semua user
- **Aksi Tersedia:**
  - 👁️ **Detail** - Lihat detail booking
  - ✏️ **Edit** - Edit booking (termasuk status, tanggal, dll)
  - 🗑️ **Hapus** - Hapus booking
- **Informasi Tambahan:** Menampilkan User/Tamu di kolom terpisah
- **Pesan Info:** "Anda memiliki akses penuh untuk mengelola semua booking termasuk edit dan hapus"

#### b) `templates/bookings_user.html` - Untuk User/Tamu
- **Akses:** User hanya dapat melihat booking mereka sendiri
- **Aksi Tersedia (hanya untuk booking aktif):**
  - 👁️ **Detail** - Lihat detail booking
  - 📅 **Ubah** - Ubah tanggal check-in dan check-out
  - ❌ **Batalkan** - Batalkan booking
- **Informasi Tambahan:** Hanya menampilkan booking pribadi user
- **Pesan Info:** "Anda hanya bisa mengubah tanggal atau membatalkan booking yang masih aktif"

#### c) `templates/edit_booking_user.html` - Form Edit untuk User
- **Fungsi:** Memungkinkan user mengubah HANYA tanggal check-in, check-out, dan catatan
- **Disabled Fields (tidak bisa diubah):**
  - Booking ID
  - Nama Tamu
  - Kamar
  - Jumlah Malam (auto-calculate)
  - Total Harga (auto-calculate)
- **Pesan Info:** "Anda hanya dapat mengubah tanggal check-in dan check-out, serta menambah catatan"

### 2. Perubahan di `app.py`

#### a) Modifikasi Route `/bookings`
```python
@app.route('/bookings')
@login_required
def bookings():
    # ... existing code ...
    
    # Render different template based on user role
    if user.is_admin():
        return render_template('bookings_admin.html', bookings=bookings_with_rooms, user=user)
    else:
        return render_template('bookings_user.html', bookings=bookings_with_rooms, user=user)
```

#### b) Route Baru: `/bookings/edit-user/<booking_id>` (GET & POST)
- **Akses:** Hanya user pemilik booking
- **Fungsi:** Edit tanggal check-in dan check-out saja
- **Validasi:**
  - Check-out harus setelah check-in
  - Recalculate malam dan total harga otomatis
  - Hanya owner yang bisa edit

#### c) Route Baru: `/bookings/cancel/<booking_id>` (POST)
- **Akses:** Hanya user pemilik booking
- **Fungsi:** Mengubah status booking menjadi 'cancelled'
- **Pesan Konfirmasi:** "Yakin ingin membatalkan booking ini?"

### 3. Perubahan di `utils.py`

#### Fungsi Baru: `update_booking_dates()`
```python
def update_booking_dates(booking_id: str, check_in: str, check_out: str, notes: str, user: str) -> bool:
    """Update booking check-in and check-out dates - User self-edit"""
```

**Fitur:**
- Update tanggal check-in dan check-out
- Recalculate jumlah malam otomatis
- Recalculate total harga berdasarkan room price
- Simpan catatan (notes) user
- Log semua perubahan ke app.log

## Alur Akses

### Untuk ADMIN:
1. Login sebagai admin
2. Akses `/bookings` → Lihat `bookings_admin.html`
3. Admin melihat SEMUA booking dari SEMUA user
4. Admin dapat: **Lihat Detail** → **Edit** (apa saja) → **Hapus**

### Untuk USER/TAMU:
1. Login sebagai tamu (user)
2. Akses `/bookings` → Lihat `bookings_user.html`
3. User hanya melihat booking mereka sendiri
4. User dapat:
   - **Lihat Detail** booking
   - **Ubah Tanggal** (redirect ke `/bookings/edit-user/<id>`)
   - **Batalkan Booking** (status → 'cancelled')

## Keamanan

✅ **Permission Checks:**
- Route `edit_booking_user` hanya allow owner atau admin
- Route `cancel_booking` hanya allow owner
- User tidak bisa akses booking user lain
- User tidak bisa menggunakan route delete_booking

✅ **Data Validasi:**
- Check-out harus setelah check-in
- Hanya field check-in/check-out/notes yang bisa diubah user
- Total harga auto-recalculate (tidak bisa dimanipulasi)

✅ **Logging:**
- Semua perubahan di-log ke app.log dengan user yang melakukan perubahan

## Testing Checklist

- ✅ Flask app berjalan tanpa error
- ✅ Login page functional
- ✅ Admin login → lihat bookings_admin.html
- ✅ User login → lihat bookings_user.html
- ✅ User bisa klik "Ubah" → edit_booking_user.html
- ✅ User bisa klik "Batalkan" → status berubah ke cancelled
- ✅ Admin bisa Edit & Hapus tanpa batasan
- ✅ User tidak bisa akses route delete_booking
- ✅ Log file ter-update dengan semua aktivitas

## Catatan Penting

1. **Booking Status:** Untuk membatalkan, system mengubah status menjadi 'cancelled' (bukan delete)
2. **Auto-Calculate:** Malam dan total harga otomatis recalculate ketika tanggal berubah
3. **Room Availability:** Ketika booking dibatalkan, kamar otomatis tersedia kembali
4. **Restricted Edit:** User tidak bisa edit field selain tanggal dan catatan untuk menjaga data integrity
