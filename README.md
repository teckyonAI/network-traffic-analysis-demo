# **Network Traffic Analysis Demo** 📡  

🚀 **Analyze and Visualize Network Traffic using Tcpdump, TShark & Scapy**  

This project captures and analyzes **network traffic** using **tcpdump, TShark, and Scapy**. It provides insights into packet flow, source-destination analysis, and protocol distribution through interactive visualizations.  

---

## **✨ Features**  

✅ **Packet Capture** – Capture live network traffic using **tcpdump** and **Scapy**.  
✅ **Traffic Analysis** – Extract useful insights using **TShark**.  
✅ **Data Visualization** – Generate **graphs, charts, and summary reports** for traffic analysis.  
✅ **Batch Processing** – Analyze large `.pcap` files efficiently.  
✅ **Automated Reporting** – Generate structured reports with **IP counts, packet size distribution, and protocol usage**.  

---

## **🛠 Tools & Technologies**  

This project is built using **Python** and popular **network analysis tools**:  

| Tool / Library  | Purpose  |
|----------------|----------|
| **tcpdump** | Packet capture in `.pcap` format |
| **Scapy** | Python-based packet sniffing and manipulation |
| **TShark** | Command-line packet analysis |
| **Pandas & NumPy** | Data manipulation & analysis |
| **Matplotlib & Seaborn** | Visualization of network traffic trends |

---

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/teckyonAI/network_traffic_analysis_demo.git

2. Navigate to the project directory:
   ```bash
   cd network_traffic_analysis_demo

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

---
## Usage

### 1. Capture Network Traffic  

- **Using tcpdump**:  `bash capture/capture_tcpdump.sh`
- **Using Scapy** (Python-based capture): `python capture/capture_scapy.py`

### 2. Analyze Captured Traffic 
Capture traffic can be analyzed by running `python capture/analyze_pcap.py`. 


---
## Contribution

Contributions are welcome! Here's how you can contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed explanation of the changes.


