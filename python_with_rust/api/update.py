import time
from rich.progress import track

def checkVersion(name):

    version = "1.0.0"
    getUpdate(f"Fetching current version for {name}...")

    print(f"\n[+] All Good! You're using the most recent of {name} --> {version}\n")


def getUpdate(description):
    for i in track(range(100), description=description):
        time.sleep(.1)  # Simulate work being done
