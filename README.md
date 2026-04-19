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
