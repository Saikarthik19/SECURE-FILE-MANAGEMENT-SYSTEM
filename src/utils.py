def log_event(event):
    with open("activity_log.txt", 'a') as f:
        f.write(event + "\n")
