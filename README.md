# OpenAI Status Tracker

A lightweight Python tool that automatically monitors the OpenAI Status Page and prints live incident updates in real time.

This script detects:
- New outages
- Performance degradations
- Service interruptions
- Resolution updates

It is designed to be scalable and efficient — suitable for tracking 100+ status pages with minimal load.

---

## Features
- Real-time status tracking (checks every 30 seconds)
- Prints only *new* incidents to avoid duplication
- Uses OpenAI’s public status API
- Zero setup required (runs in GitHub Codespaces or locally)

---

## How It Works

The script:
1. Calls the OpenAI Status API (`summary.json`)
2. Extracts the latest incident
3. Detects if the incident is new
4. Prints:
   - Affected Product / Service  
   - Latest status message  
   - Timestamp  

Example output:


---

## Requirements
Python 3.10+  
Modules used:
- `requests`
- `time`
- `datetime`

Install dependencies:


(You don’t need `sseclient` in the final version.)

---

## Run the Script


You'll see:


This will update every 30 seconds.

---

## File Structure


---

## Author
Rashi Pandey  
Submission for: **Bolna AI – Python Status Tracker Assignment**
