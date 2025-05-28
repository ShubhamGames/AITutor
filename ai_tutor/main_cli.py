"""
Main command-line interface for the AI Tutor.
"""
import os
from agents.decider_agent import DeciderAgent
from agents.subject_tutor_agent import MathsTutor, HistoryTutor
from data.student_history import StudentHistory

def run_cli():
    """
    Runs the command-line interface for the AI Tutor.
    """
    print("Welcome to the AI Tutor!")

    # Initialize agents and history
    decider_agent = DeciderAgent()
    maths_tutor = MathsTutor()
    history_tutor = HistoryTutor()
    tutors = {
        "maths": maths_tutor,
        "history": history_tutor
        # Add other tutors here as they are implemented
        # "physics": PhysicsTutor(),
    }

    # Configure student history storage
    # Ensure the base data directory exists
    base_data_dir = "data"
    if not os.path.exists(base_data_dir):
        os.makedirs(base_data_dir)
    
    student_records_dir = os.path.join(base_data_dir, "student_records")
    # StudentHistory class creates the specific folder if it doesn't exist
    student_history_manager = StudentHistory(data_folder=student_records_dir)

    student_id = input("Enter your Student ID: ").strip()
    if not student_id:
        print("Student ID cannot be empty. Exiting.")
        return

    print(f"\nHello, Student {student_id}! Let's start learning.")
    # You can load and display past history if needed:
    # current_history = student_history_manager.get_history(student_id)
    # print(f"Loaded history: {current_history['interactions'][-3:]}") # Show last 3 interactions

    while True:
        user_input = input("\nAsk me anything or type 'exit' to quit: ").strip()

        if user_input.lower() == 'exit':
            print(f"Goodbye, Student {student_id}! Keep learning!")
            break

        if not user_input:
            print("Please enter a question.")
            continue

        # 1. Decide the subject
        subject = decider_agent.decide_subject(user_input)
        print(f"Decided subject: {subject}")

        # 2. Get the appropriate tutor
        selected_tutor = tutors.get(subject.lower())

        if selected_tutor:
            # 3. Get response from the tutor
            tutor_response = selected_tutor.get_response(user_input)
            print(f"\nTutor ({selected_tutor.subject_name}): {tutor_response}")

            # 4. Log the interaction
            student_history_manager.add_interaction(
                student_id=student_id,
                subject=selected_tutor.subject_name, # Use subject name from tutor
                prompt=user_input,
                response=tutor_response
            )
            print("Interaction logged.")
        else:
            print("Sorry, I can't determine the subject or I don't have a tutor for that yet.")
            # Optionally, log this "unknown" interaction as well
            student_history_manager.add_interaction(
                student_id=student_id,
                subject="unknown",
                prompt=user_input,
                response="No suitable tutor found or subject undetermined."
            )
            print("Interaction with 'unknown' subject logged.")

if __name__ == "__main__":
    # Adjust the path for imports if running main_cli.py directly from ai_tutor folder
    # This is a common Python pattern for scripts intended to be run as __main__
    import sys
    # Add the parent directory (root of the project) to sys.path
    # to allow absolute imports like 'from agents.decider_agent import DeciderAgent'
    # when this script is run directly.
    # This assumes main_cli.py is in 'ai_tutor/main_cli.py' and 'agents' is 'ai_tutor/agents/'
    project_root = os.path.dirname(os.path.abspath(__file__))
    if project_root not in sys.path: # Add parent dir if not already there
        sys.path.insert(0, project_root)

    # Now that sys.path is potentially updated, re-attempt imports if they failed initially
    # This is more of a safeguard; for a well-structured project, this might not be needed
    # if PYTHONPATH is set or the project is installed.
    from agents.decider_agent import DeciderAgent
    from agents.subject_tutor_agent import MathsTutor, HistoryTutor
    from data.student_history import StudentHistory
    
    run_cli()
