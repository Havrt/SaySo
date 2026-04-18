from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- DATA STRUCTURES ---
# Array: Stores candidate objects (populated at session setup)
candidates = []

# Session PIN set by host at setup
session_pin = None

# Hash Table: Stores voter_id: bool (voted status)
# This provides O(1) lookup to prevent double-voting
voters = {}

# Stack: Stores history of (voter_id, candidate_id) for the Undo feature
vote_stack = []

# List: Stores registered voter objects
voter_list = []

# Counter: Used to generate zero-padded voter IDs
voter_id_counter = [0]

@app.route('/status')
def status():
    return jsonify({"configured": session_pin is not None, "pin": session_pin})

@app.route('/setup', methods=['POST'])
def setup():
    global session_pin, candidates
    pin = request.json.get('pin', '').strip()
    names = request.json.get('candidates', [])

    if not pin:
        return jsonify({"success": False, "message": "PIN is required."}), 400
    if not names:
        return jsonify({"success": False, "message": "Add at least one candidate."}), 400

    session_pin = pin
    candidates = [{"id": i + 1, "name": n.strip(), "votes": 0} for i, n in enumerate(names)]

    return jsonify({"success": True})

@app.route('/register', methods=['POST'])
def register():
    first = request.json.get('first', '').strip()
    last = request.json.get('last', '').strip()
    pin = request.json.get('pin', '')

    if session_pin is None:
        return jsonify({"success": False, "message": "Session not started yet."}), 403
    if pin != session_pin:
        return jsonify({"success": False, "message": "Invalid PIN."}), 403

    voter_id_counter[0] += 1
    voter_id = f"{first[0].upper()}{last[0].upper()}-{voter_id_counter[0]:03d}"

    voter_list.append({"id": voter_id, "first": first, "last": last})
    voters[voter_id] = False

    return jsonify({"success": True, "voter_id": voter_id})

@app.route('/')
def index():
    return render_template('index.html', candidates=candidates)

@app.route('/vote', methods=['POST'])
def vote():
    voter_id = request.json.get('voter_id')
    candidate_id = int(request.json.get('candidate_id'))

    # Validation: Check Hash Table
    if voters.get(voter_id):
        return jsonify({"success": False, "message": "You have already voted!"}), 400

    # Process Vote: Update Array
    for cand in candidates:
        if cand['id'] == candidate_id:
            cand['votes'] += 1
            voters[voter_id] = True # Mark as voted in Hash Table
            vote_stack.append((voter_id, candidate_id)) # Push to Stack
            return jsonify({"success": True})

    return jsonify({"success": False, "message": "Candidate not found"}), 404

@app.route('/undo', methods=['POST'])
def undo():
    if not vote_stack:
        return jsonify({"success": False, "message": "No votes to undo!"}), 400

    # Pop from Stack (LIFO)
    voter_id, candidate_id = vote_stack.pop()

    # Revert in Hash Table and Array
    voters[voter_id] = False
    for cand in candidates:
        if cand['id'] == candidate_id:
            cand['votes'] -= 1
            break

    return jsonify({"success": True, "message": f"Vote by {voter_id} undone."})

@app.route('/reset', methods=['POST'])
def reset():
    global session_pin, candidates
    session_pin = None
    candidates.clear()
    voters.clear()
    vote_stack.clear()
    voter_list.clear()
    voter_id_counter[0] = 0
    return jsonify({"success": True})

@app.route('/results')
def get_results():
    # Sort candidates by votes (highest first)
    sorted_results = sorted(candidates, key=lambda x: x['votes'], reverse=True)
    return jsonify(sorted_results)

if __name__ == '__main__':
    app.run(debug=True)
