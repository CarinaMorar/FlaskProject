import asyncio
from bleak import BleakScanner, BleakClient

# Funcția pentru scanarea dispozitivelor BLE
async def scan_devices():
    print("Căutare dispozitive Bluetooth...")
    devices = await BleakScanner.discover()
    for idx, device in enumerate(devices):
        print(f"{idx + 1}. Adresă: {device.address}, Nume: {device.name}")
    return devices

# Funcția pentru conectarea la un dispozitiv BLE și trimiterea unui mesaj
async def connect_and_send_message(device_address, characteristic_uuid, message):
    async with BleakClient(device_address) as client:
        print(f"Conectat la {device_address}")

        # Citirea unei caracteristici
        data = await client.read_gatt_char(characteristic_uuid)
        print(f"Date citite: {data}")

        # Scrierea unei caracteristici
        await client.write_gatt_char(characteristic_uuid, bytearray(message, "utf-8"))
        print(f"Mesaj trimis: {message}")

# Funcția principală care orchestrează scanarea și conectarea
async def main():
    devices = await scan_devices()
    if devices:
        # Selectează dispozitivul la care vrei să te conectezi
        numar_dispozitiv = int(input("Introdu numărul dispozitivului la care vrei să te conectezi: ")) - 1
        device_address = devices[numar_dispozitiv].address

        # UUID-ul caracteristicii (exemplu UUID; trebuie să-l înlocuiești cu unul valid pentru dispozitivul tău)
        characteristic_uuid = "00002a37-0000-1000-8000-00805f9b34fb"

        # Mesajul pe care vrei să-l trimiți
        message = "Salut de la calculator!"

        await connect_and_send_message(device_address, characteristic_uuid, message)
    else:
        print("Nu s-au găsit dispozitive.")

# Rulează funcția principală
if __name__ == "__main__":
    asyncio.run(main())
