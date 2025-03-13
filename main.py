import subprocess
import time

if __name__ == "__main__": 
    # Function to run a script.
    def run_script(script_name, background=False):
        if background:
            return subprocess.Popen(["python", script_name])  # Run in the background
        else:
            subprocess.run(["python", script_name])  # Run in the foreground

    print("🛠️ Creating Kafka topics...")
    run_script("topics.py")

    print("🚨 Starting Weather Alert Consumer...")
    alert_consumer_process = run_script("consumer_alert.py", background=True)

    print("🚀 Running Producer for the first time...")

    try:
        while True:
            run_script("producer.py")
            print("⏳ Waiting for 5 minutes before next data fetch...")
            time.sleep(300)
    except KeyboardInterrupt:
        print("\n⚠️ Stopping all processes...")
        alert_consumer_process.terminate()