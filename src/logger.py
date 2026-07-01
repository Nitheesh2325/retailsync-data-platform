from datetime import datetime

LOG_FILE = "logs/pipeline.log"

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output = f"[{timestamp}] {message}"

    print(output)

    with open(LOG_FILE, "a") as file:
        file.write(output + "\n")