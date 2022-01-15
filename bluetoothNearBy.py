import os
import threading
import time
import subprocess
import constants
from logs.log import log

pwd = constants.attributes['pwd']
mi_band_MAC = "C8:72:64:ED:20:B0"
mi_band_MAC_2 = "D8:6E:34:F2:37:19"

def near_by():
    global mi_band_MAC
    found = False
    bluetooth_scan_thread = threading.Thread(target=bluetooth_scan)
    bluetooth_scan_thread.start()
    time.sleep(5)
    os.system("killall bluetoothctl")
    time.sleep(1)
    os.system("cat " + pwd + "ImportantFiles/bluetoothctl.txt > " + pwd + "ImportantFiles/test.txt")
    scan_result = subprocess.run(['cat', pwd + 'ImportantFiles/test.txt'], stdout=subprocess.PIPE)
    found = mi_band_MAC in str(scan_result.stdout) or mi_band_MAC_2 in str(scan_result.stdout)
    # HACER UNA FUNCION DE ESTO
    if "C8:72:64:ED:20:B0 RSSI is nil" in str(scan_result.stdout) or "C8:72:64:ED:20:B0 RSSI: -8" in str(
            scan_result.stdout) or "C8:72:64:ED:20:B0 RSSI: -9" in str(scan_result.stdout):
        found = False
    print("Mi band cerca: " + str(found))
    log("BLUETOOTH_NEAR_BY", "NEAR_BY()", "La pulsera con la direccion MAC: " + mi_band_MAC + 'encontrada: '
        + str(found))
    return found


def empty_file():
    os.system("cat /dev/null > " + pwd + "ImportantFiles/bluetoothctl.txt && sleep 1")


def bluetooth_scan():
    empty_file()
    os.system("bluetoothctl scan on >> " + pwd + "ImportantFiles/bluetoothctl.txt")
