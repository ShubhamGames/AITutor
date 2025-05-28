import json
import os
import datetime

class StudentHistory:
    """
    Manages student interaction history, storing and retrieving data from JSON files.
    """

    def __init__(self, data_folder: str):
        """
        Initializes the StudentHistory manager.

        Args:
            data_folder: The path to the folder where student history files are stored.
                         This folder will be created if it doesn't exist.
        """
        self.data_folder = data_folder
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)

    def _get_history_filepath(self, student_id: str) -> str:
        """
        Constructs the file path for a student's history JSON file.

        Args:
            student_id: The unique identifier for the student.

        Returns:
            The full path to the student's history file.
        """
        return os.path.join(self.data_folder, f"student_{student_id}_history.json")

    def get_history(self, student_id: str) -> dict:
        """
        Retrieves the interaction history for a given student.

        If a history file exists, it's loaded. Otherwise, a default
        history structure is returned.

        Args:
            student_id: The unique identifier for the student.

        Returns:
            A dictionary containing the student's history.
        """
        filepath = self._get_history_filepath(student_id)
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error loading history for student {student_id}: {e}")
                # Fall through to return default history if loading fails
        return {
            'student_id': student_id,
            'interactions': [],
            'weak_topics': {} # subject: [topic1, topic2]
        }

    def save_history(self, student_id: str, history_data: dict) -> bool:
        """
        Saves the student's interaction history to a JSON file.

        Args:
            student_id: The unique identifier for the student.
            history_data: The dictionary containing the student's history.

        Returns:
            True if saving was successful, False otherwise.
        """
        filepath = self._get_history_filepath(student_id)
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(history_data, f, indent=4)
            return True
        except IOError as e:
            print(f"Error saving history for student {student_id}: {e}")
            return False

    def add_interaction(self, student_id: str, subject: str, prompt: str, response: str):
        """
        Adds a new interaction record to the student's history.

        Args:
            student_id: The unique identifier for the student.
            subject: The subject of the interaction.
            prompt: The student's prompt or question.
            response: The AI tutor's response.
        """
        history_data = self.get_history(student_id)
        interaction = {
            'subject': subject,
            'prompt': prompt,
            'response': response,
            'timestamp': datetime.datetime.now().isoformat()
        }
        history_data['interactions'].append(interaction)
        self.save_history(student_id, history_data)
