from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
from datetime import datetime, timedelta
import utils
from models import User

app = Flask(__name__)
app.secret_key = 'hotel_booking_secret_key_2025'  # Change this in production

# Decorator untuk require login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Silakan login terlebih dahulu', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Decorator untuk require admin role
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Silakan login terlebih dahulu', 'warning')
            return redirect(url_for('login'))
        
        user = utils.get_user_by_id(session['user_id'])
        if not user or not user.is_admin():
            flash('Akses ditolak. Hanya admin yang dapat mengakses halaman ini.', 'danger')
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated_function

# ==================== AUTHENTICATION ROUTES ====================

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = utils.authenticate_user(username, password)
        if user:
            session['user_id'] = user.user_id
            session['username'] = user.username
            session['role'] = user.role
            session['full_name'] = user.full_name
            
            flash(f'Selamat datang, {user.full_name}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Username atau password salah', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    username = session.get('username', 'Unknown')
    utils.log_activity(f"User logout: {username}", user=username, status="INFO")
    
    session.clear()
    flash('Anda telah logout', 'info')
    return redirect(url_for('login'))

# ==================== DASHBOARD ====================

@app.route('/dashboard')
@login_required
def dashboard():
    user = utils.get_user_by_id(session['user_id'])
    rooms = utils.load_rooms()
    bookings = utils.load_bookings()
    
    # Statistics
    total_rooms = len(rooms)
    available_rooms = len([r for r in rooms if r.is_available])
    total_bookings = len(bookings)
    active_bookings = len([b for b in bookings if b.status == 'active'])
    
    # User-specific data
    if user.is_admin():
        user_bookings = bookings
    else:
        user_bookings = utils.get_user_bookings(user.user_id)
    
    return render_template('dashboard.html', 
                         user=user,
                         total_rooms=total_rooms,
                         available_rooms=available_rooms,
                         total_bookings=total_bookings,
                         active_bookings=active_bookings,
                         recent_bookings=user_bookings[-5:][::-1])

# ==================== ROOM MANAGEMENT (CRUD) ====================

@app.route('/rooms')
@login_required
def rooms():
    user = utils.get_user_by_id(session['user_id'])
    rooms = utils.load_rooms()
    return render_template('rooms.html', rooms=rooms, user=user)

@app.route('/rooms/add', methods=['GET', 'POST'])
@admin_required
def add_room():
    if request.method == 'POST':
        room_type = request.form.get('room_type')
        room_number = request.form.get('room_number')
        
        new_room = utils.create_room(room_type, room_number, session['username'])
        if new_room:
            flash(f'Kamar {room_number} berhasil ditambahkan', 'success')
            return redirect(url_for('rooms'))
        else:
            flash('Nomor kamar sudah ada atau tipe kamar tidak valid', 'danger')
    
    return render_template('add_room.html')

@app.route('/rooms/edit/<room_id>', methods=['GET', 'POST'])
@admin_required
def edit_room(room_id):
    room = utils.get_room_by_id(room_id)
    if not room:
        flash('Kamar tidak ditemukan', 'danger')
        return redirect(url_for('rooms'))
    
    if request.method == 'POST':
        is_available = request.form.get('is_available') == 'true'
        utils.update_room_availability(room_id, is_available, session['username'])
        flash(f'Kamar {room.room_number} berhasil diupdate', 'success')
        return redirect(url_for('rooms'))
    
    return render_template('edit_room.html', room=room)

@app.route('/rooms/delete/<room_id>', methods=['POST'])
@admin_required
def delete_room(room_id):
    if utils.delete_room(room_id, session['username']):
        flash('Kamar berhasil dihapus', 'success')
    else:
        flash('Gagal menghapus kamar', 'danger')
    return redirect(url_for('rooms'))

# ==================== BOOKING MANAGEMENT (CRUD) ====================

@app.route('/bookings')
@login_required
def bookings():
    user = utils.get_user_by_id(session['user_id'])
    
    if user.is_admin():
        all_bookings = utils.load_bookings()
    else:
        all_bookings = utils.get_user_bookings(user.user_id)
    
    # Get room info for each booking
    bookings_with_rooms = []
    for booking in all_bookings:
        room = utils.get_room_by_id(booking.room_id)
        bookings_with_rooms.append({
            'booking': booking,
            'room': room
        })
    
    # Render different template based on user role
    if user.is_admin():
        return render_template('bookings_admin.html', bookings=bookings_with_rooms, user=user)
    else:
        return render_template('bookings_user.html', bookings=bookings_with_rooms, user=user)

@app.route('/bookings/add', methods=['GET', 'POST'])
@login_required
def add_booking():
    if request.method == 'POST':
        room_id = request.form.get('room_id')
        check_in = request.form.get('check_in')
        check_out = request.form.get('check_out')
        guest_name = request.form.get('guest_name')
        guest_phone = request.form.get('guest_phone')
        
        # Calculate nights
        check_in_date = datetime.strptime(check_in, '%Y-%m-%d')
        check_out_date = datetime.strptime(check_out, '%Y-%m-%d')
        nights = (check_out_date - check_in_date).days
        
        if nights <= 0:
            flash('Tanggal check-out harus setelah check-in', 'danger')
            return redirect(url_for('add_booking'))
        
        new_booking = utils.create_booking(
            user_id=session['user_id'],
            room_id=room_id,
            check_in=check_in,
            check_out=check_out,
            nights=nights,
            guest_name=guest_name,
            guest_phone=guest_phone,
            username=session['username']
        )
        
        if new_booking:
            flash(f'Booking berhasil! Total: Rp {new_booking._total_price:,.0f}', 'success')
            return redirect(url_for('bookings'))
        else:
            flash('Kamar tidak tersedia', 'danger')
    
    # Get available rooms
    available_rooms = [r for r in utils.load_rooms() if r.is_available]
    
    # Set default dates
    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)
    
    return render_template('add_booking.html', 
                         rooms=available_rooms,
                         today=today,
                         tomorrow=tomorrow)

@app.route('/bookings/edit/<booking_id>', methods=['GET', 'POST'])
@login_required
def edit_booking(booking_id):
    booking = utils.get_booking_by_id(booking_id)
    if not booking:
        flash('Booking tidak ditemukan', 'danger')
        return redirect(url_for('bookings'))
    
    # Check permission
    user = utils.get_user_by_id(session['user_id'])
    if not user.is_admin() and booking.user_id != user.user_id:
        flash('Anda tidak memiliki akses untuk mengedit booking ini', 'danger')
        return redirect(url_for('bookings'))
    
    if request.method == 'POST':
        status = request.form.get('status')
        utils.update_booking_status(booking_id, status, session['username'])
        flash('Booking berhasil diupdate', 'success')
        return redirect(url_for('bookings'))
    
    room = utils.get_room_by_id(booking.room_id)
    return render_template('edit_booking.html', booking=booking, room=room)

@app.route('/bookings/edit-user/<booking_id>', methods=['GET', 'POST'])
@login_required
def edit_booking_user(booking_id):
    """Allow users to edit only check-in and check-out dates"""
    booking = utils.get_booking_by_id(booking_id)
    if not booking:
        flash('Booking tidak ditemukan', 'danger')
        return redirect(url_for('bookings'))
    
    # Check permission - only owner can edit
    user = utils.get_user_by_id(session['user_id'])
    if booking.user_id != user.user_id:
        flash('Anda tidak memiliki akses untuk mengedit booking ini', 'danger')
        return redirect(url_for('bookings'))
    
    if request.method == 'POST':
        check_in = request.form.get('check_in')
        check_out = request.form.get('check_out')
        notes = request.form.get('notes', '')
        
        # Validate dates
        check_in_date = datetime.strptime(check_in, '%Y-%m-%d')
        check_out_date = datetime.strptime(check_out, '%Y-%m-%d')
        nights = (check_out_date - check_in_date).days
        
        if nights <= 0:
            flash('Tanggal check-out harus setelah check-in', 'danger')
            return redirect(url_for('edit_booking_user', booking_id=booking_id))
        
        # Update booking dates
        if utils.update_booking_dates(booking_id, check_in, check_out, notes, session['username']):
            flash('Tanggal booking berhasil diubah', 'success')
            return redirect(url_for('bookings'))
        else:
            flash('Gagal mengubah tanggal booking', 'danger')
    
    room = utils.get_room_by_id(booking.room_id)
    return render_template('edit_booking_user.html', booking=booking, room=room)

@app.route('/bookings/cancel/<booking_id>', methods=['POST'])
@login_required
def cancel_booking(booking_id):
    """Allow users to cancel their own bookings"""
    booking = utils.get_booking_by_id(booking_id)
    if not booking:
        flash('Booking tidak ditemukan', 'danger')
        return redirect(url_for('bookings'))
    
    # Check permission - only owner can cancel
    user = utils.get_user_by_id(session['user_id'])
    if booking.user_id != user.user_id:
        flash('Anda tidak memiliki akses untuk membatalkan booking ini', 'danger')
        return redirect(url_for('bookings'))
    
    # Update status to cancelled
    if utils.update_booking_status(booking_id, 'cancelled', session['username']):
        flash('Booking berhasil dibatalkan', 'success')
    else:
        flash('Gagal membatalkan booking', 'danger')
    
    return redirect(url_for('bookings'))

@app.route('/bookings/delete/<booking_id>', methods=['POST'])
@login_required
def delete_booking(booking_id):
    booking = utils.get_booking_by_id(booking_id)
    if not booking:
        flash('Booking tidak ditemukan', 'danger')
        return redirect(url_for('bookings'))
    
    # Check permission
    user = utils.get_user_by_id(session['user_id'])
    if not user.is_admin() and booking.user_id != user.user_id:
        flash('Anda tidak memiliki akses untuk menghapus booking ini', 'danger')
        return redirect(url_for('bookings'))
    
    if utils.delete_booking(booking_id, session['username']):
        flash('Booking berhasil dihapus', 'success')
    else:
        flash('Gagal menghapus booking', 'danger')
    
    return redirect(url_for('bookings'))

@app.route('/bookings/detail/<booking_id>')
@login_required
def booking_detail(booking_id):
    booking = utils.get_booking_by_id(booking_id)
    if not booking:
        flash('Booking tidak ditemukan', 'danger')
        return redirect(url_for('bookings'))
    
    # Check permission
    user = utils.get_user_by_id(session['user_id'])
    if not user.is_admin() and booking.user_id != user.user_id:
        flash('Anda tidak memiliki akses untuk melihat booking ini', 'danger')
        return redirect(url_for('bookings'))
    
    room = utils.get_room_by_id(booking.room_id)
    return render_template('booking_detail.html', booking=booking, room=room, user=user)

# ==================== ADMIN LOGS ====================

@app.route('/logs')
@admin_required
def view_logs():
    try:
        with open(utils.LOG_FILE, 'r', encoding='utf-8') as f:
            logs = f.readlines()
            logs.reverse()  # Show latest first
            logs = logs[:100]  # Show last 100 entries
    except FileNotFoundError:
        logs = []
    
    return render_template('logs.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
