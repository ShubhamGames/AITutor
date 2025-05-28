"""
Main Flask application for the AI Tutor Web UI.
"""
import sys
import os

# Add the project root to sys.path
# This assumes app.py is in ai_tutor/ui/
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from flask import Flask, render_template, request, jsonify
from ai_tutor.agents.decider_agent import DeciderAgent
from ai_tutor.agents.subject_tutor_agent import MathsTutor, HistoryTutor # SubjectTutor (if needed)
from ai_tutor.data.student_history import StudentHistory

# Initialize the Flask application
app = Flask(__name__)

# Initialize Agents and History
decider_agent = DeciderAgent()
tutors = {
    "maths": MathsTutor(),
    "history": HistoryTutor()
}

# Construct the path for student history data
# Ensures it points to ai_tutor/data/student_records from ai_tutor/ui/app.py
history_data_folder = os.path.join(os.path.dirname(__file__), '..', 'data', 'student_records')
student_history = StudentHistory(data_folder=history_data_folder)


@app.route('/')
def home():
    """
    Home route for the Flask application.
    Renders the main interaction page.
    """
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    """
    API endpoint to handle user questions.
    It determines the subject, gets a response from the relevant tutor,
    and logs the interaction.
    """
    data = request.get_json()
    prompt = data.get('prompt')
    student_id = data.get('studentId')

    if not prompt or not student_id:
        return jsonify({'error': 'Prompt and Student ID are required.'}), 400

    subject = decider_agent.decide_subject(prompt)
    tutor_response = "Sorry, I couldn't understand the subject or a tutor for it isn't available."
    response_subject = subject # Store the subject determined by decider agent

    if subject.lower() in tutors: # Ensure case-insensitivity for subject matching
        tutor = tutors[subject.lower()]
        tutor_response = tutor.get_response(prompt)
        student_history.add_interaction(student_id, tutor.subject_name, prompt, tutor_response)
        response_subject = tutor.subject_name # Use the official subject name from tutor
    else:
        # Log interaction even if no specific tutor is found
        student_history.add_interaction(student_id, "unknown", prompt, tutor_response)


    return jsonify({'response': tutor_response, 'subject': response_subject})


if __name__ == '__main__':
    # Runs the Flask development server
    # Debug mode is on for development, providing more detailed error messages.
    # In a production environment, debug mode should be turned off.
    app.run(debug=True)
