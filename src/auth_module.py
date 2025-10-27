import bcrypt
import pyotp

users = {}

def register_user(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    users[username] = {"password": hashed, "otp_secret": pyotp.random_base32()}
    print(f"User {username} registered successfully.")

def login_user(username, password):
    if username in users and bcrypt.checkpw(password.encode(), users[username]["password"]):
        print("Password correct. Proceeding to OTP...")
        return True
    else:
        print("Invalid username or password.")
        return False

def verify_otp(username, otp_input):
    totp = pyotp.TOTP(users[username]["otp_secret"])
    if totp.verify(otp_input):
        print("OTP verified. Login successful.")
        return True
    else:
        print("Invalid OTP.")
        return False

def get_current_otp(username):
    return pyotp.TOTP(users[username]["otp_secret"]).now()
