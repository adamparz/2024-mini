"""
Response time - single-threaded
"""
import mip
mip.install("urequests")
import requests
# tried hard to implement into firebase - wrong approach:
    #import micropython-firebase-firestore
    #mip.install("github:WoolDoughnut310/micropython-firebase-firestore")
    #mip.install("firebase")
    #mip.install("firebase_firestore")
import network
from machine import Pin
import time
import random
import json

N: int = 10 #CHANGE
sample_ms = 10.0
on_ms = 500

def send_webhook_req(data):
    headers = {'Content-Type': 'application/xml'}
    url = "https://webhook.site/ed5374e1-bb47-4cb5-abf3-e69995d3a140"
    
    # webhook.site doesn't take jsons - use xml instead
    data_xml = """<?xml version="1.0" encoding="UTF-8"?>
    <data>
        <average_time>data['avg_time']</average_time>
        <minimum_time>data['min_time']</minimum_time>
        <maximum_time>data['max_time']</maximum_time>
    </data>
    """    
    try:
        response = requests.post(url, data=data_xml, headers=headers)
        print(f"Post request response: {response.status_code}")
        #print(f"Response text: {response.text}")
        response.close()
    except Exception as e:
        print(f"Failed to send data: {e}")

def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    
    wlan.active(True)
    ssid = "BU Guest (unencrypted)"
    #ssid = "Cameron"
    # scan for networks and check if the desired SSID is available
    available_networks = wlan.scan()
    for net in available_networks:
        if ssid in net[0].decode():
            print(f"Connecting to network: {ssid}")
            # connect to open network
            wlan.connect(ssid)

            timeout = 10  # in seconds
            while timeout > 0:
                if wlan.isconnected():
                    print(f"Connected to {ssid}")
                    print("Network config:", wlan.ifconfig())
                    return wlan
                time.sleep(1)
                timeout -= 1

            print(f"Failed to connect to {ssid} within timeout period.")
            return None

    print(f"Network {ssid} not found.")
    return None

def random_time_interval(tmin: float, tmax: float) -> float:
    """return a random time interval between max and min"""
    return random.uniform(tmin, tmax)


def blinker(N: int, led: Pin) -> None:
    # %% let user know game started / is over

    for _ in range(N):
        led.high()
        time.sleep(0.1)
        led.low()
        time.sleep(0.1)


def write_json(json_filename: str, data: dict) -> None:
    """Writes data to a JSON file.

    Parameters
    ----------

    json_filename: str
        The name of the file to write to. This will overwrite any existing file.

    data: dict
        Dictionary data to write to the file.
    """

    with open(json_filename, "w") as f:
        json.dump(data, f)


def scorer(t: list[int | None]) -> None:
    # %% collate results
    misses = t.count(None)
    print(f"You missed the light {misses} / {len(t)} times")

    t_good = [x for x in t if x is not None]

    print(t_good)

    # add key, value to this dict to store the minimum, maximum, average response time
    # and score (non-misses / total flashes) i.e. the score a floating point number
    # is in range [0..1]
    
    
    # START OF CODE
    if t_good:
        avg_time = sum(t_good) / len(t_good)
        min_time = min(t_good)
        max_time = max(t_good)
        
    if len(t) > 0:
        score = (len(t_good) / len(t))
    else: score = 0
    
    data = {
        "average_time": avg_time,
        "minimum_time": min_time,
        "maximum_time": max_time
        }
    
    print(data)
    
    # function to post data to web host
    send_webhook_req(data)
    
    # END OF CODE
    
    
    # %% make dynamic filename and write JSON

    now: tuple[int] = time.localtime()

    now_str = "-".join(map(str, now[:3])) + "T" + "_".join(map(str, now[3:6]))
    filename = f"score-{now_str}.json"

    print("write", filename)

    write_json(filename, data)


if __name__ == "__main__":
    # using "if __name__" allows us to reuse functions in other script files

    led = Pin("LED", Pin.OUT)
    button = Pin(16, Pin.IN, Pin.PULL_UP)
    
    connect_to_wifi()

    t: list[int | None] = []

    blinker(3, led)

    for i in range(N):
        time.sleep(random_time_interval(0.5, 5.0))

        led.high()

        tic = time.ticks_ms()
        t0 = None
        while time.ticks_diff(time.ticks_ms(), tic) < on_ms:
            if button.value() == 0:
                t0 = time.ticks_diff(time.ticks_ms(), tic)
                led.low()
                break
        t.append(t0)

        led.low()

    blinker(5, led)

    scorer(t)

