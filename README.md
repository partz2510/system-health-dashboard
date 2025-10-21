!# ⚙️ System Health Dashboard

A lightweight Python **command-line dashboard** that displays real-time system performance metrics using [`psutil`](https://pypi.org/project/psutil/) and [`rich`](https://pypi.org/project/rich/).

This project showcases **Python automation, system monitoring, and terminal UI design** — all in under 100 lines of code.

---

## 🎯 Features

- 🧠 Live monitoring of CPU, Memory, Disk, and Network statistics  
- 🎨 Color-coded, auto-refreshing terminal dashboard  
- 🔁 Updates every 2 seconds in real time  
- 🪶 Built with just two lightweight libraries: `psutil` + `rich`  
- ⚡ Cross-platform: runs on Windows, macOS, and Linux  

---

## ⚙️ Quick Start

```bash
# 1️⃣ Clone the repo
git clone https://github.com/<your-username>/system-health-dashboard.git
cd system-health-dashboard

# 2️⃣ Install dependencies
pip install psutil rich

# 3️⃣ Run the dashboard
python system_health_dashboard.py
Press Ctrl + C to stop monitoring at any time.

🖥️ Demo Output
![Demo Output](https://github.com/partz2510/system-health-dashboard/blob/main/demo_output.png?raw=true)

🧩 Output Explanation
Metric	Meaning
CPU Usage (%)	The percentage of CPU currently being used across all cores. A sudden spike may indicate heavy processing.
Memory Usage (%)	The amount of RAM currently used. Shows both used and total GB for clarity.
Disk Usage (%)	How much of your main disk drive is in use vs total capacity.
Network Sent / Received (MB)	Data uploaded and downloaded since system boot, updated every 2 seconds.

💡 How It Works
psutil collects live system metrics (CPU load, memory, disk, and network I/O).

rich renders the metrics into a visually styled table refreshed continuously in the terminal.

The script runs indefinitely until you stop it manually.

🚀 Ideas to Extend
Add GPU temperature or process list

Log metrics to a CSV file for later analysis

Integrate with a Flask or FastAPI web dashboard

Add threshold alerts when usage exceeds limits

🧠 Learning Takeaways
This project demonstrates:

Real-time data collection and visualization

Clean Python scripting practices

Basic system administration concepts

Automation mindset valuable for SOC and DevOps roles

📜 License
MIT — feel free to fork, modify, and share your version.

