from flask import Flask, render_template, request, redirect, url_for, flash
from auth_module import register_user, login_user, verify_otp, get_current_otp
from storage_module import encrypt_file, save_metadata
from detection_module import check_malware, check_buffer_overflow
from utils import log_event
from models import create_db
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

create_db()
logged_in_user = None

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        register_user(username, password)
        flash("User registered successfully! Please login.")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    global logged_in_user
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if login_user(username, password):
            otp = get_current_otp(username)
            flash(f"OTP for testing: {otp}")
            return render_template('login.html', otp_required=True, username=username)
        else:
            flash("Invalid credentials")
    return render_template('login.html', otp_required=False)

@app.route('/verify_otp', methods=['POST'])
def verify_otp_route():
    global logged_in_user
    username = request.form['username']
    otp_input = request.form['otp']
    if verify_otp(username, otp_input):
        logged_in_user = username
        return redirect(url_for('dashboard'))
    flash("Invalid OTP")
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if not logged_in_user:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=logged_in_user)

@app.route('/upload', methods=['GET','POST'])
def upload():
    if not logged_in_user:
        return redirect(url_for('login'))
    if request.method == 'POST':
        file = request.files['file']
        if file:
            os.makedirs("uploads", exist_ok=True)
            filepath = os.path.join("uploads", file.filename)
            file.save(filepath)

            enc_file = encrypt_file(filepath)
            save_metadata(enc_file, logged_in_user)

            check_malware(filepath)
            file.seek(0)
            check_buffer_overflow(file.read())

            log_event(f"{logged_in_user} uploaded {file.filename}")
            flash(f"File {file.filename} uploaded and encrypted successfully!")
            return redirect(url_for('dashboard'))
    return render_template('upload.html')

# ✅ Add this part to start the web app
if __name__ == "__main__":
    app.run(debug=True)
