#!/usr/bin/env python3
"""
System Health Dashboard
Monitors CPU, Memory, Disk and Network usage in real time.
Refreshes every few seconds in a colorful CLI dashboard.
"""

import psutil
import time
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich import box

console = Console()

REFRESH_INTERVAL = 2  # seconds

def get_metrics():
    """Collects system statistics using psutil."""
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    net = psutil.net_io_counters()
    return {
        "cpu": cpu,
        "mem_percent": mem.percent,
        "mem_used": mem.used / (1024 ** 3),
        "mem_total": mem.total / (1024 ** 3),
        "disk_percent": disk.percent,
        "disk_used": disk.used / (1024 ** 3),
        "disk_total": disk.total / (1024 ** 3),
        "bytes_sent": net.bytes_sent / (1024 ** 2),
        "bytes_recv": net.bytes_recv / (1024 ** 2)
    }

def make_table(metrics):
    """Formats data into a Rich table for live display."""
    table = Table(title=f"System Health Dashboard – {datetime.now():%H:%M:%S}", box=box.ROUNDED)
    table.add_column("Metric", justify="left", style="cyan", no_wrap=True)
    table.add_column("Value", justify="right", style="magenta")

    table.add_row("CPU Usage", f"{metrics['cpu']:.1f}%")
    table.add_row("Memory Usage", f"{metrics['mem_percent']:.1f}%  ({metrics['mem_used']:.1f} / {metrics['mem_total']:.1f} GB)")
    table.add_row("Disk Usage", f"{metrics['disk_percent']:.1f}%  ({metrics['disk_used']:.1f} / {metrics['disk_total']:.1f} GB)")
    table.add_row("Network Sent", f"{metrics['bytes_sent']:.1f} MB")
    table.add_row("Network Received", f"{metrics['bytes_recv']:.1f} MB")
    return table

def main():
    console.print("[bold green]Starting live system monitoring... (Ctrl+C to stop)[/bold green]")
    with Live(refresh_per_second=1, console=console) as live:
        try:
            while True:
                metrics = get_metrics()
                live.update(make_table(metrics))
                time.sleep(REFRESH_INTERVAL)
        except KeyboardInterrupt:
            console.print("\n[bold red]Monitoring stopped.[/bold red]")

if __name__ == "__main__":
    main()
