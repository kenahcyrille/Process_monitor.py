import psutil
import time

def monitor_core_processes(interval=1):
    while True:
        core_processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            core_processes.append({
                'pid': proc.info['pid'],
                'name': proc.info['name'],
                'cpu_percent': proc.info['cpu_percent']
            })
        print("Core Processes:")
        for process in core_processes:
            print(f"PID: {process['pid']}, Name: {process['name']}, CPU Percent: {process['cpu_percent']}")
        time.sleep(interval)

if __name__ == "__main__":
    monitor_core_processes()
