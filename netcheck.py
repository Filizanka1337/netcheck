from pythonping import ping
import speedtest
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def test_internet_speed():
    input("Kliknij Enter, aby sprawdzić prędkość internetu...")
    clear_console()
    print("Sprawdzanie...")
    
    st = speedtest.Speedtest()
    ping_result = ping('google.com', count=3)  # Pingowanie do google.com (możesz zmienić na inny adres)
    ping_time = round(ping_result.rtt_avg_ms, 2)  # Średni czas odpowiedzi ping w ms
    
    download_speed = st.download() / 10**6  # Prędkość pobierania w megabitach na sekundę (Mbps)
    upload_speed = st.upload() / 10**6  # Prędkość wysyłania w megabitach na sekundę (Mbps)
    
    clear_console()
    print("Oto jak prezentuje się twój internet:")
    print(f"Ping: {ping_time} ms")
    print(f"Wysyłanie: {upload_speed:.2f} Mbps")
    print(f"Pobieranie: {download_speed:.2f} Mbps")

test_internet_speed()
