def check_malware(file_path):
    if file_path.endswith(".exe"):
        print(f"Warning: {file_path} may be malware.")
        return True
    return False

def check_buffer_overflow(input_data):
    if len(input_data) > 1024:
        print("Buffer overflow attempt detected!")
        return True
    return False
