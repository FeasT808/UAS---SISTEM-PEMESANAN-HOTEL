@echo off
echo ====================================
echo  Sistem Pemesanan Hotel
echo  UAS Pemrograman Berorientasi Objek
echo ====================================
echo.
echo Starting Flask application...
echo Application will be available at: http://localhost:5000
echo.
echo Login credentials:
echo Admin: admin / admin123
echo Tamu: tamu1 / tamu123
echo.
echo Press Ctrl+C to stop the server
echo.

".venv\Scripts\python.exe" app.py
