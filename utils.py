import json
import os
from datetime import datetime
from typing import List, Dict, Optional
from models import Room, StandardRoom, DeluxeRoom, SuiteRoom, User, Booking

# File paths
DATA_DIR = 'data'
USERS_FILE = os.path.join(DATA_DIR, 'users.json')
ROOMS_FILE = os.path.join(DATA_DIR, 'rooms.json')
BOOKINGS_FILE = os.path.join(DATA_DIR, 'bookings.json')
LOG_FILE = 'app.log'

def ensure_data_dir():
    """Ensure data directory exists"""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def log_activity(activity: str, user: str = "System", status: str = "INFO"):
    """Log activities to file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{status}] [{user}] {activity}\n"
    
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(log_entry)

# ==================== USER MANAGEMENT ====================

def load_users() -> List[User]:
    """Load users from JSON file"""
    ensure_data_dir()
    if not os.path.exists(USERS_FILE):
        return []
    
    try:
        with open(USERS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [User(**user_data) for user_data in data]
    except Exception as e:
        log_activity(f"Error loading users: {str(e)}", status="ERROR")
        return []

def save_users(users: List[User]):
    """Save users to JSON file"""
    ensure_data_dir()
    try:
        with open(USERS_FILE, 'w', encoding='utf-8') as f:
            json.dump([user.to_dict() for user in users], f, indent=4, ensure_ascii=False)
    except Exception as e:
        log_activity(f"Error saving users: {str(e)}", status="ERROR")

def authenticate_user(username: str, password: str) -> Optional[User]:
    """Authenticate user"""
    users = load_users()
    for user in users:
        if user.username == username and user.check_password(password):
            log_activity(f"Login berhasil untuk user: {username}", user=username, status="SUCCESS")
            return user
    
    log_activity(f"Login gagal untuk user: {username}", user=username, status="FAILED")
    return None

def get_user_by_id(user_id: str) -> Optional[User]:
    """Get user by ID"""
    users = load_users()
    for user in users:
        if user.user_id == user_id:
            return user
    return None

# ==================== ROOM MANAGEMENT ====================

def load_rooms() -> List[Room]:
    """Load rooms from JSON file and create appropriate Room objects"""
    ensure_data_dir()
    if not os.path.exists(ROOMS_FILE):
        return []
    
    try:
        with open(ROOMS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            rooms = []
            for room_data in data:
                room_type = room_data['room_type']
                room_id = room_data['room_id']
                room_number = room_data['room_number']
                
                # Polymorphism - create appropriate room type
                if room_type == 'Standard':
                    room = StandardRoom(room_id, room_number)
                elif room_type == 'Deluxe':
                    room = DeluxeRoom(room_id, room_number)
                elif room_type == 'Suite':
                    room = SuiteRoom(room_id, room_number)
                else:
                    continue
                
                room.is_available = room_data['is_available']
                rooms.append(room)
            
            return rooms
    except Exception as e:
        log_activity(f"Error loading rooms: {str(e)}", status="ERROR")
        return []

def save_rooms(rooms: List[Room]):
    """Save rooms to JSON file"""
    ensure_data_dir()
    try:
        with open(ROOMS_FILE, 'w', encoding='utf-8') as f:
            json.dump([room.to_dict() for room in rooms], f, indent=4, ensure_ascii=False)
    except Exception as e:
        log_activity(f"Error saving rooms: {str(e)}", status="ERROR")

def get_room_by_id(room_id: str) -> Optional[Room]:
    """Get room by ID"""
    rooms = load_rooms()
    for room in rooms:
        if room.room_id == room_id:
            return room
    return None

def create_room(room_type: str, room_number: str, user: str) -> Optional[Room]:
    """Create new room - CRUD: Create"""
    rooms = load_rooms()
    
    # Check if room number already exists
    for room in rooms:
        if room.room_number == room_number:
            return None
    
    # Generate room ID
    room_id = f"R{len(rooms) + 1:03d}"
    
    # Create room based on type
    if room_type == 'Standard':
        new_room = StandardRoom(room_id, room_number)
    elif room_type == 'Deluxe':
        new_room = DeluxeRoom(room_id, room_number)
    elif room_type == 'Suite':
        new_room = SuiteRoom(room_id, room_number)
    else:
        return None
    
    rooms.append(new_room)
    save_rooms(rooms)
    
    log_activity(f"Kamar baru dibuat: {room_type} - {room_number}", user=user, status="CREATE")
    return new_room

def update_room_availability(room_id: str, is_available: bool, user: str):
    """Update room availability - CRUD: Update"""
    rooms = load_rooms()
    for room in rooms:
        if room.room_id == room_id:
            room.is_available = is_available
            save_rooms(rooms)
            log_activity(f"Kamar {room.room_number} diupdate - Available: {is_available}", 
                        user=user, status="UPDATE")
            return True
    return False

def delete_room(room_id: str, user: str) -> bool:
    """Delete room - CRUD: Delete"""
    rooms = load_rooms()
    initial_count = len(rooms)
    rooms = [room for room in rooms if room.room_id != room_id]
    
    if len(rooms) < initial_count:
        save_rooms(rooms)
        log_activity(f"Kamar {room_id} dihapus", user=user, status="DELETE")
        return True
    return False

# ==================== BOOKING MANAGEMENT ====================

def load_bookings() -> List[Booking]:
    """Load bookings from JSON file"""
    ensure_data_dir()
    if not os.path.exists(BOOKINGS_FILE):
        return []
    
    try:
        with open(BOOKINGS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Booking(**booking_data) for booking_data in data]
    except Exception as e:
        log_activity(f"Error loading bookings: {str(e)}", status="ERROR")
        return []

def save_bookings(bookings: List[Booking]):
    """Save bookings to JSON file"""
    ensure_data_dir()
    try:
        with open(BOOKINGS_FILE, 'w', encoding='utf-8') as f:
            json.dump([booking.to_dict() for booking in bookings], f, indent=4, ensure_ascii=False)
    except Exception as e:
        log_activity(f"Error saving bookings: {str(e)}", status="ERROR")

def create_booking(user_id: str, room_id: str, check_in: str, check_out: str, 
                  nights: int, guest_name: str, guest_phone: str, username: str) -> Optional[Booking]:
    """Create new booking - CRUD: Create"""
    room = get_room_by_id(room_id)
    if not room or not room.is_available:
        return None
    
    # Calculate price
    total_price = room.calculate_price(nights)
    
    # Generate booking ID
    bookings = load_bookings()
    booking_id = f"B{len(bookings) + 1:04d}"
    
    # Create booking
    new_booking = Booking(
        booking_id=booking_id,
        user_id=user_id,
        room_id=room_id,
        check_in=check_in,
        check_out=check_out,
        nights=nights,
        total_price=total_price,
        guest_name=guest_name,
        guest_phone=guest_phone
    )
    
    # Update room availability
    update_room_availability(room_id, False, username)
    
    # Save booking
    bookings.append(new_booking)
    save_bookings(bookings)
    
    log_activity(f"Booking baru dibuat: {booking_id} untuk kamar {room.room_number}", 
                user=username, status="CREATE")
    
    return new_booking

def get_booking_by_id(booking_id: str) -> Optional[Booking]:
    """Get booking by ID"""
    bookings = load_bookings()
    for booking in bookings:
        if booking.booking_id == booking_id:
            return booking
    return None

def update_booking_status(booking_id: str, status: str, user: str) -> bool:
    """Update booking status - CRUD: Update"""
    bookings = load_bookings()
    for booking in bookings:
        if booking.booking_id == booking_id:
            old_status = booking.status
            booking.status = status
            
            # If cancelled or completed, make room available again
            if status in ['cancelled', 'completed']:
                update_room_availability(booking.room_id, True, user)
            
            save_bookings(bookings)
            log_activity(f"Booking {booking_id} status diupdate: {old_status} -> {status}", 
                        user=user, status="UPDATE")
            return True
    return False

def update_booking_dates(booking_id: str, check_in: str, check_out: str, notes: str, user: str) -> bool:
    """Update booking check-in and check-out dates - User self-edit"""
    bookings = load_bookings()
    for booking in bookings:
        if booking.booking_id == booking_id:
            old_check_in = booking._check_in
            old_check_out = booking._check_out
            
            # Update dates
            booking._check_in = check_in
            booking._check_out = check_out
            booking.notes = notes
            
            # Recalculate nights and total price
            from datetime import datetime
            check_in_date = datetime.strptime(check_in, '%Y-%m-%d')
            check_out_date = datetime.strptime(check_out, '%Y-%m-%d')
            booking._nights = (check_out_date - check_in_date).days
            
            # Recalculate total price based on new nights
            room = get_room_by_id(booking.room_id)
            if room:
                booking._total_price = room.calculate_price(booking._nights)
            
            save_bookings(bookings)
            log_activity(f"Booking {booking_id} tanggal diupdate: {old_check_in} - {old_check_out} -> {check_in} - {check_out}", 
                        user=user, status="UPDATE")
            return True
    return False

def delete_booking(booking_id: str, user: str) -> bool:
    """Delete booking - CRUD: Delete"""
    bookings = load_bookings()
    booking = get_booking_by_id(booking_id)
    
    if booking:
        # Make room available again
        update_room_availability(booking.room_id, True, user)
    
    initial_count = len(bookings)
    bookings = [b for b in bookings if b.booking_id != booking_id]
    
    if len(bookings) < initial_count:
        save_bookings(bookings)
        log_activity(f"Booking {booking_id} dihapus", user=user, status="DELETE")
        return True
    return False

def get_user_bookings(user_id: str) -> List[Booking]:
    """Get all bookings for a specific user"""
    bookings = load_bookings()
    return [b for b in bookings if b.user_id == user_id]
