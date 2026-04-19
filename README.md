# SaySo

Is a web voting application built with Flask. SaySo lets a host set up a live voting session with custom candidates, register voters, collect votes, and view real-time results — all from the browser.
 
---
 
## Features
 
- **Session setup** — Host configures a session PIN and adds candidates before voting begins
- **Voter registration** — Voters register with their name and session PIN; they receive a unique voter ID (e.g., `JD-001`)
- **One vote per person** — A hash table tracks voted status for O(1) double-vote prevention
- **Undo last vote** — A stack-based history allows the most recent vote to be reversed (LIFO)
- **Live results** — Candidates are returned sorted by vote count in real time
- **Session reset** — Host can wipe all session data and start fresh
---

## Tech Stack
 
- **Backend:** Python, Flask
- **Frontend:** HTML (Jinja2 templates)
- **Data structures used:** Array (candidates), Hash Table (voters), Stack (vote history), List (voter registry)
---
 
## Getting Started
 
### Prerequisites
 
- Python 3.x
- Flask
### Installation
 
```bash
git clone https://github.com/Havrt/SaySo.git
cd SaySo
pip install flask
```
 
### Running the App
 
```bash
python app.py
```
 
Then open your browser and go to `http://127.0.0.1:5000`.
 
---
 
