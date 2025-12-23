from abc import ABC, abstractmethod
from datetime import datetime
import json
from typing import List, Dict, Optional

class Room(ABC):
    """Abstract base class untuk semua jenis kamar hotel"""
    
    def __init__(self, room_id: str, room_number: str, capacity: int, base_price: float):
        self._room_id = room_id
        self._room_number = room_number
        self._capacity = capacity
        self._base_price = base_price
        self._is_available = True
    
    # Encapsulation - getters
    @property
    def room_id(self):
        return self._room_id
    
    @property
    def room_number(self):
        return self._room_number
    
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def base_price(self):
        return self._base_price
    
    @property
    def is_available(self):
        return self._is_available
    
    @is_available.setter
    def is_available(self, value: bool):
        self._is_available = value
    
    # Abstraction - method yang harus diimplementasikan oleh child class
    @abstractmethod
    def get_room_type(self) -> str:
        """Return tipe kamar"""
        pass
    
    @abstractmethod
    def calculate_price(self, nights: int) -> float:
        """Calculate total price dengan faktor khusus per tipe kamar"""
        pass
    
    @abstractmethod
    def get_amenities(self) -> List[str]:
        """Return daftar fasilitas kamar"""
        pass
    
    def to_dict(self) -> Dict:
        """Convert object ke dictionary untuk JSON storage"""
        return {
            'room_id': self._room_id,
            'room_number': self._room_number,
            'room_type': self.get_room_type(),
            'capacity': self._capacity,
            'base_price': self._base_price,
            'is_available': self._is_available,
            'amenities': self.get_amenities()
        }
    
    def __str__(self):
        return f"{self.get_room_type()} - Room {self._room_number} (Capacity: {self._capacity})"


class StandardRoom(Room):
    """Class untuk kamar tipe Standard - Inheritance dari Room"""
    
    def __init__(self, room_id: str, room_number: str):
        super().__init__(room_id, room_number, capacity=2, base_price=500000)
    
    # Polymorphism - implementasi method abstrak dari parent class
    def get_room_type(self) -> str:
        return "Standard"
    
    def calculate_price(self, nights: int) -> float:
        """Standard room - harga normal"""
        return self._base_price * nights
    
    def get_amenities(self) -> List[str]:
        return ["Single Bed", "WiFi", "TV", "AC", "Kamar Mandi"]


class DeluxeRoom(Room):
    """Class untuk kamar tipe Deluxe - Inheritance dari Room"""
    
    def __init__(self, room_id: str, room_number: str):
        super().__init__(room_id, room_number, capacity=3, base_price=800000)
    
    # Polymorphism - implementasi method abstrak dari parent class
    def get_room_type(self) -> str:
        return "Deluxe"
    
    def calculate_price(self, nights: int) -> float:
        """Deluxe room - 10% discount untuk booking >3 malam"""
        total = self._base_price * nights
        if nights > 3:
            total *= 0.9  # 10% discount
        return total
    
    def get_amenities(self) -> List[str]:
        return ["Queen Bed", "WiFi Premium", "Smart TV", "AC", 
                "Kamar Mandi + Bathtub", "Mini Bar", "Balcony"]


class SuiteRoom(Room):
    """Class untuk kamar tipe Suite - Inheritance dari Room"""
    
    def __init__(self, room_id: str, room_number: str):
        super().__init__(room_id, room_number, capacity=4, base_price=1500000)
    
    # Polymorphism - implementasi method abstrak dari parent class
    def get_room_type(self) -> str:
        return "Suite"
    
    def calculate_price(self, nights: int) -> float:
        """Suite room - 15% discount untuk booking >3 malam, gratis sarapan"""
        total = self._base_price * nights
        if nights > 3:
            total *= 0.85  # 15% discount
        return total
    
    def get_amenities(self) -> List[str]:
        return ["King Bed", "WiFi Premium", "Smart TV 55\"", "AC", 
                "Kamar Mandi Premium + Jacuzzi", "Mini Bar Premium", 
                "Living Room", "Balcony", "Breakfast Included"]


class User:
    """Class untuk user management"""
    
    def __init__(self, user_id: str, username: str, password: str, role: str, full_name: str):
        self._user_id = user_id
        self._username = username
        self._password = password  # In production, hash this!
        self._role = role  # 'admin' or 'tamu'
        self._full_name = full_name
    
    @property
    def user_id(self):
        return self._user_id
    
    @property
    def username(self):
        return self._username
    
    @property
    def password(self):
        return self._password
    
    @property
    def role(self):
        return self._role
    
    @property
    def full_name(self):
        return self._full_name
    
    def to_dict(self) -> Dict:
        return {
            'user_id': self._user_id,
            'username': self._username,
            'password': self._password,
            'role': self._role,
            'full_name': self._full_name
        }
    
    def check_password(self, password: str) -> bool:
        return self._password == password
    
    def is_admin(self) -> bool:
        return self._role == 'admin'


class Booking:
    """Class untuk booking/reservation management"""
    
    def __init__(self, booking_id: str, user_id: str, room_id: str, 
                 check_in: str, check_out: str, nights: int, total_price: float,
                 guest_name: str, guest_phone: str, status: str = 'active',
                 created_at: Optional[str] = None):
        # created_at dibuat optional supaya loading dari JSON yang sudah ada tidak error
        self._booking_id = booking_id
        self._user_id = user_id
        self._room_id = room_id
        self._check_in = check_in
        self._check_out = check_out
        self._nights = nights
        self._total_price = total_price
        self._guest_name = guest_name
        self._guest_phone = guest_phone
        self._status = status
        self._created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @property
    def booking_id(self):
        return self._booking_id
    
    @property
    def user_id(self):
        return self._user_id
    
    @property
    def room_id(self):
        return self._room_id
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value: str):
        self._status = value
    
    def to_dict(self) -> Dict:
        return {
            'booking_id': self._booking_id,
            'user_id': self._user_id,
            'room_id': self._room_id,
            'check_in': self._check_in,
            'check_out': self._check_out,
            'nights': self._nights,
            'total_price': self._total_price,
            'guest_name': self._guest_name,
            'guest_phone': self._guest_phone,
            'status': self._status,
            'created_at': self._created_at
        }
