import pyshark
import signal
import threading
import time

class PacketListener: 

    def __init__(self, interface: str, filter: str):
        self.interface = interface
        self.filter = filter
        self.stop_sniffing = False
        self.packets = []
        self.lock = threading.Lock()
        self.listener_thread = None
        self.capture = pyshark.LiveCapture(interface=self.interface, bpf_filter=self.filter)

    def start(self):
        self.listener_thread = threading.Thread(target=self.listen_in_loop)
        self.stop_sniffing = False
        self.listener_thread.start()

    def stop(self):
        self.stop_listening()
        self.listener_thread.join()
    
    def stop_listening(self):
        with self.lock:
            self.stop_sniffing = True

    def listen_in_loop(self):
        for raw_packet in self.capture.sniff_continuously():
                with self.lock:
                    if self.stop_sniffing:
                        self.capture.close()
                        break
                    self.packets.append(raw_packet)

    def get_packet(self):
        with self.lock:
            if self.packets:
                return self.packets.pop(0)
        return None

    def wait_for_packet(self):
        while True:
            packet = self.get_packet()
            if packet:
                return packet


class RawUDPListener(PacketListener):
    
    def __init__(self, interface:str, filter = "udp"):
        super().__init__(interface, filter)

    def get_raw_packet(self):
        packet = super().get_packet()
        if packet is None or not hasattr(packet, 'data'):
            return None
        return bytes.fromhex(packet.data.data)
    
    def wait_for_raw_packet(self):
        packet = super().wait_for_packet()
        if hasattr(packet, 'data'):
            return bytes.fromhex(packet.data.data)
        else:
            return None

class UDPToBinaryFile(RawUDPListener):
    def __init__(self, filepath, duration, interface:str, filter="udp"):
        super().__init__(interface, filter)
        self.filepath = filepath
        self.duration = duration

    def save_to_file(self):
        self.start()
        start_time = time.time()
        buffered_packets = []
        try:
            while time.time() - start_time < self.duration:
                packet = self.get_raw_packet()
                if packet:
                    buffered_packets.append(packet)
        finally:
            self.stop()

        with open(self.filepath, 'ab') as f:
            for packet in buffered_packets:
                f.write(packet)
        
        print(f"Packets saved to {self.filepath}")
