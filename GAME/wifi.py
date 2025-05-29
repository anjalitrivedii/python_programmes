import subprocess


def scan_wifi():
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'network'], capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error scanning Wi-Fi networks: {e}")
        return None

def connect_to_wifi(ssid, password=None):
    try:
        if password:
            result = subprocess.run(
                ['netsh', 'wlan', 'connect', 'name', f'"{ssid}"', 'ssid', f'"{ssid}"', 'key', f'"{password}"'],
                capture_output=True, text=True)
        else:
            result = subprocess.run(['netsh', 'wlan', 'connect', 'name', f'"{ssid}"', 'ssid', f'"{ssid}"'],
                                    capture_output=True, text=True)

        if result.returncode == 0:
            print(f"Successfully connected to Wi-Fi network: {ssid}")
        else:
            print(f"Failed to connect to Wi-Fi network: {ssid}")
            print("Error details:", result.stderr)  # Print stderr for more details+p
    except subprocess.CalledProcessError as e:
        print(f"Error connecting to Wi-Fi network: {e}")


def main():
    networks = scan_wifi()

    if networks is None:
        print("Failed to retrieve Wi-Fi networks.")
        return

    print("Available Wi-Fi networks:")
    print(networks)

    ssid = input("Enter the SSID of the Wi-Fi network to connect to: ").strip()
    password = input("Enter the password (leave empty for open networks): ").strip()

    if ssid:
        connect_to_wifi(ssid, password)
    else:
        print("SSID cannot be empty. Please enter a valid SSID.")


main()
