import requests
import time
from datetime import datetime

STATUS_URL = "https://status.openai.com/api/v2/summary.json"

last_incident_id = None  # To track new incidents

def print_event(product, message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] Product: {product}")
    print(f"Status: {message}\n")

def check_status():
    global last_incident_id
    
    try:
        response = requests.get(STATUS_URL)
        data = response.json()

        incidents = data.get("incidents", [])

        if not incidents:
            print("No current incidents.\n")
            return

        latest_incident = incidents[0]  # Most recent incident

        incident_id = latest_incident.get("id")
        name = latest_incident.get("name", "Unknown Service")
        update_list = latest_incident.get("incident_updates", [])
        latest_update = update_list[0].get("body", "No details") if update_list else "No update message"

        # Only print if it's a NEW incident
        if incident_id != last_incident_id:
            print_event(name, latest_update)
            last_incident_id = incident_id

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print("🔍 Real-time OpenAI Status Monitoring Started...\n")

    while True:
        check_status()
        time.sleep(30)   # Check every 30 seconds
