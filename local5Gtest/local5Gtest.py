import logging
from speedtest import Speedtest

class MockEventingCSClient:
    def __init__(self, app_name):
        self.app_name = app_name
        self.data_store = {}

    def log(self, message):
        print(f"{self.app_name}: {message}")

    def get(self, key):
        return self.data_store.get(key, None)

    def put(self, key, value):
        self.data_store[key] = value
        print(f"Updated {key} to {value}")

def run_speedtest():
    print("Starting Speedtest...")
    s = Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    results = {
        'download': s.results.download / 1_000_000,  # Convert to Mbps
        'upload': s.results.upload / 1_000_000,  # Convert to Mbps
        'ping': s.results.ping
    }
    print("Speedtest Complete!")
    print(f"Download: {results['download']} Mbps")
    print(f"Upload: {results['upload']} Mbps")
    print(f"Ping: {results['ping']} ms")

def main():
    cp = MockEventingCSClient('LocalTest')
    cp.log('Simulated client starting...')
    run_speedtest()
    # You can add more simulated functionality if needed

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
