# SaySo 🗳️
 
Is a web voting application built with Flask. SaySo lets a host set up a live voting session with custom candidates, register voters, collect votes, and view real-time results — all from the browser.

---
 
## Inspiration
 
This project takes Inspiration from Kahoot. We choose to add some of our own touches, such as an undo button, since we've all been there when clicking the wrong answer by mistake in Kahoot before.

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
 
## Project Structure
 
```
SaySo/
├── app.py          # Flask backend — routes and session logic
├── templates/
│   └── index.html  # Frontend UI
└── README.md
```
 
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
 
## How It Works
 
1. **Host setup** — POST to `/setup` with a PIN and a list of candidate names to initialize the session.
2. **Voter registration** — POST to `/register` with first name, last name, and the session PIN. Returns a unique voter ID.
3. **Voting** — POST to `/vote` with a voter ID and candidate ID. Validates against the hash table to prevent repeat votes.
4. **Undo** — POST to `/undo` to reverse the most recent vote (pops from the vote stack).
5. **Results** — GET `/results` returns candidates sorted by vote count descending.
6. **Reset** — POST to `/reset` clears all session data.
 
