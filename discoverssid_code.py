import board
import busio
import time
import digitalio
from adafruit_esp32spi import adafruit_esp32spi

# Define the pins used by the BitsyExpander's ESP32 WiFi module
esp32_cs = digitalio.DigitalInOut(board.D9)
esp32_ready = digitalio.DigitalInOut(board.D11)
esp32_reset = digitalio.DigitalInOut(board.D12)
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)

# Initialize the ESP32 WiFi module
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

if esp.status == adafruit_esp32spi.WL_IDLE_STATUS:
    print("\nESP32 WiFi Module found.")
    print("Firmware version:", str(esp.firmware_version, "utf-8"))
    print("*" * 40)

while True:
    print("\nScanning for available networks...")
    # Add SSID of each Access Point (ap) in range to network_list
    network_list = [str(ap["ssid"], "utf-8") for ap in esp.scan_networks()]
    print(network_list)

    print("\nMAC Address:")
    # Format the MAC address (reverse byte order and format hex values)
    mac_addr = ":".join("{:02X}".format(byte) for byte in reversed(esp.MAC_address))
    print(mac_addr)

    print("\n" + "*" * 40)
    time.sleep(8)
