from scapy.all import sniff, wrpcap

def capture_packets(packet_count=500, output_file="capture/network_traffic.pcap"):
    print(f"Capturing {packet_count} packets using Scapy...")
    packets = sniff(count=packet_count)
    wrpcap(output_file, packets)
    print(f"Packets saved to {output_file}")

if __name__ == "__main__":
    capture_packets()
