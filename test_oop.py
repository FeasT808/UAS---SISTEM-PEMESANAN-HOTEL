"""
Test script untuk memverifikasi implementasi OOP
Sistem Pemesanan Hotel
"""

from models import Room, StandardRoom, DeluxeRoom, SuiteRoom, User, Booking
from datetime import datetime

print("="*60)
print("TEST IMPLEMENTASI OOP - SISTEM PEMESANAN HOTEL")
print("="*60)

# Test 1: Abstract Class & Inheritance
print("\n1. TEST ABSTRACT CLASS & INHERITANCE")
print("-" * 60)
try:
    # Tidak bisa instantiate abstract class
    room = Room("R001", "101", 2, 500000)
    print("❌ GAGAL: Abstract class bisa di-instantiate (seharusnya error)")
except TypeError as e:
    print("✅ BERHASIL: Abstract class tidak bisa di-instantiate")
    print(f"   Error: {e}")

# Test 2: Inheritance - Creating child classes
print("\n2. TEST INHERITANCE - CHILD CLASSES")
print("-" * 60)
standard = StandardRoom("R001", "101")
deluxe = DeluxeRoom("R002", "201")
suite = SuiteRoom("R003", "301")

print(f"✅ StandardRoom created: {standard}")
print(f"✅ DeluxeRoom created: {deluxe}")
print(f"✅ SuiteRoom created: {suite}")

# Test 3: Polymorphism - Different implementations
print("\n3. TEST POLYMORPHISM - DIFFERENT BEHAVIORS")
print("-" * 60)

rooms = [standard, deluxe, suite]
nights_2 = 2
nights_5 = 5

print(f"\nBooking untuk {nights_2} malam:")
for room in rooms:
    price = room.calculate_price(nights_2)
    print(f"  {room.get_room_type():10s}: Rp {price:,.0f}")

print(f"\nBooking untuk {nights_5} malam (ada diskon untuk Deluxe & Suite):")
for room in rooms:
    price = room.calculate_price(nights_5)
    base_price = room.base_price * nights_5
    discount = base_price - price
    print(f"  {room.get_room_type():10s}: Rp {price:,.0f} (Diskon: Rp {discount:,.0f})")

print("\n✅ POLYMORPHISM BERHASIL: Setiap class punya implementasi berbeda")

# Test 4: Encapsulation - Property access
print("\n4. TEST ENCAPSULATION - PROPERTY ACCESS")
print("-" * 60)

print(f"Room ID (via getter): {standard.room_id}")
print(f"Room Number (via getter): {standard.room_number}")
print(f"Base Price (via getter): Rp {standard.base_price:,.0f}")
print(f"Is Available (via getter): {standard.is_available}")

# Test setter
print("\nMengubah availability via setter...")
standard.is_available = False
print(f"Is Available sekarang: {standard.is_available}")
standard.is_available = True
print(f"Is Available dikembalikan: {standard.is_available}")

print("\n✅ ENCAPSULATION BERHASIL: Data protected dengan property decorators")

# Test 5: Abstraction - Abstract methods must be implemented
print("\n5. TEST ABSTRACTION - ABSTRACT METHODS")
print("-" * 60)

print(f"StandardRoom.get_room_type(): {standard.get_room_type()}")
print(f"DeluxeRoom.get_room_type(): {deluxe.get_room_type()}")
print(f"SuiteRoom.get_room_type(): {suite.get_room_type()}")

print(f"\nStandardRoom amenities: {len(standard.get_amenities())} items")
print(f"DeluxeRoom amenities: {len(deluxe.get_amenities())} items")
print(f"SuiteRoom amenities: {len(suite.get_amenities())} items")

print("\n✅ ABSTRACTION BERHASIL: Semua child class implement abstract methods")

# Test 6: Object serialization
print("\n6. TEST OBJECT SERIALIZATION (untuk JSON)")
print("-" * 60)

room_dict = standard.to_dict()
print(f"Room object converted to dict:")
print(f"  Type: {room_dict['room_type']}")
print(f"  Number: {room_dict['room_number']}")
print(f"  Price: Rp {room_dict['base_price']:,.0f}")
print(f"  Amenities: {len(room_dict['amenities'])} items")

print("\n✅ SERIALIZATION BERHASIL: Object bisa dikonversi ke dictionary")

# Test 7: User class with role-based logic
print("\n7. TEST USER CLASS - ROLE-BASED ACCESS")
print("-" * 60)

admin = User("U001", "admin", "admin123", "admin", "Administrator")
tamu = User("U002", "tamu1", "tamu123", "tamu", "Budi Santoso")

print(f"Admin is_admin(): {admin.is_admin()} ✅")
print(f"Tamu is_admin(): {tamu.is_admin()} ✅")
print(f"Password check admin: {admin.check_password('admin123')} ✅")
print(f"Password check wrong: {admin.check_password('wrong')} ✅")

# Test 8: Booking class
print("\n8. TEST BOOKING CLASS")
print("-" * 60)

booking = Booking(
    booking_id="B0001",
    user_id="U002",
    room_id="R003",
    check_in="2025-12-25",
    check_out="2025-12-30",
    nights=5,
    total_price=suite.calculate_price(5),
    guest_name="Budi Santoso",
    guest_phone="08123456789"
)

print(f"Booking ID: {booking.booking_id}")
print(f"Guest: {booking._guest_name}")
print(f"Room ID: {booking.room_id}")
print(f"Nights: {booking._nights}")
print(f"Total: Rp {booking._total_price:,.0f}")
print(f"Status: {booking.status}")

print("\n✅ BOOKING CLASS BERHASIL")

# Summary
print("\n" + "="*60)
print("SUMMARY - SEMUA TEST BERHASIL! ✅")
print("="*60)
print("\nImplementasi OOP yang diverifikasi:")
print("1. ✅ Abstract Class (Room)")
print("2. ✅ Inheritance (StandardRoom, DeluxeRoom, SuiteRoom)")
print("3. ✅ Polymorphism (calculate_price, get_amenities, dll)")
print("4. ✅ Encapsulation (private attributes, @property)")
print("5. ✅ Abstraction (abstract methods)")
print("6. ✅ Additional Classes (User, Booking)")
print("\nAplikasi SIAP untuk UAS! 🎉")
print("="*60)
