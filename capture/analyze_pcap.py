import subprocess
import pandas as pd

def analyze_pcap(file="capture/network_traffic.pcap"):
    print(f"Analyzing {file}...")

    # Run tshark command to extract packet summary
    command = f"tshark -r {file} -T fields -e ip.src -e ip.dst -e frame.len"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Process output
    data = [line.split() for line in result.stdout.split("\n") if line]

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=["Source_IP", "Destination_IP", "Packet_Size"])
    
    print("\nTop 5 Source IPs:")
    print(df["Source_IP"].value_counts().head())

if __name__ == "__main__":
    analyze_pcap()
