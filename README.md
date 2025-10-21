# ⚙️ System Health Dashboard

A lightweight Python **command-line dashboard** that displays real-time system performance metrics using [`psutil`](https://pypi.org/project/psutil/) and [`rich`](https://pypi.org/project/rich/).

This project showcases **Python automation, system monitoring, and terminal UI design**

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
```

Press Ctrl + C to stop monitoring at any time.

# 🖥️ Demo Output
![Demo Output](https://github.com/partz2510/system-health-dashboard/blob/main/screenshots/demo_output.png?raw=true)

# 🧩 Output Explanation
Metric Meaning
1. CPU Usage (%)	The percentage of CPU currently being used across all cores. A sudden spike may indicate heavy processing

2. Memory Usage (%)	The amount of RAM currently used. Shows both used and total GB for clarity.

3. Disk Usage (%)	How much of your main disk drive is in use vs total capacity.

4. Network Sent / Received (MB)	Data uploaded and downloaded since system boot, updated every 2 seconds.

# 💡 How It Works
1. 'psutil' collects live system metrics (CPU load, memory, disk, and network I/O).

2. 'rich' renders the metrics into a visually styled table refreshed continuously in the terminal.

The script runs indefinitely until you stop it manually.


# 🧠 Learning Takeaways
This project demonstrates:

1. Real-time data collection and visualization

2. Clean Python scripting practices

3. Basic system administration concepts

4. Automation mindset valuable for SOC and DevOps roles

# 📜 License
MIT — feel free to fork, modify, and share your version.

