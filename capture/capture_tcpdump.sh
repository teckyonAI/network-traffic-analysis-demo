#!/bin/bash
echo "Starting packet capture with tcpdump..."
sudo tcpdump -i any -w capture/network_traffic.pcap -c 500
echo "Packet capture completed. Saved to capture/network_traffic.pcap"
