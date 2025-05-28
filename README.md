# AI Tutor Project

AI Tutor is a multi-agent system designed for personalized learning, featuring a command-line interface and a web-based user interface.

## Current Features

*   **Decider Agent:** Keyword-based subject detection for Maths, Physics, Chemistry, Biology, History, Geography, Economics.
*   **Prototype Subject Tutors:**
    *   **Maths Tutor:** Provides placeholder responses for maths-related queries.
    *   **History Tutor:** Provides placeholder responses for history-related queries.
*   **Basic Student Interaction Logging:** Interactions are logged per student in JSON files.
*   **Command-Line Interface (CLI):** Allows users to interact with the AI Tutor.
*   **Web User Interface (Flask-based):** Provides a web page for interacting with the Decider Agent and Subject Tutors.

## Setup

1.  **Prerequisites:** Ensure you have Python 3.x installed.
2.  **Clone the repository (if you haven't already):**
    ```bash
    git clone <repository-url>
    cd <repository-folder-name> 
    ```
    Replace `<repository-url>` and `<repository-folder-name>` with the actual URL and folder name.
3.  **Install Dependencies:**
    This project uses Flask for the Web UI. Install it and other potential dependencies using `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

### 1. Command-Line Interface (CLI)

Navigate to the project directory that contains the `ai_tutor` package (e.g., the root of this project).
```bash
python ai_tutor/main_cli.py
```
Alternatively, if you are in the directory containing `ai_tutor` (e.g., `ai_tutor_project_root`), you can run it as a module:
```bash
python -m ai_tutor.main_cli
```

### 2. Web User Interface (Flask App)

Ensure you have completed the setup steps, especially installing requirements.

To run the Flask development server:
```bash
python ai_tutor/ui/app.py
```
After running the command, the application will typically be available at:
**`http://127.0.0.1:5000/`**
Open this URL in your web browser to use the AI Tutor.

## How to Run Tests

Navigate to the project's root directory and execute:
```bash
python -m unittest discover ai_tutor/tests
```

## Project Structure

*   `ai_tutor/`: Main package directory.
    *   `agents/`: Contains the different AI agent implementations (DeciderAgent, SubjectTutor, etc.).
    *   `data/`: Handles data storage, such as student interaction histories (e.g., `student_records/`).
    *   `tests/`: Contains unit tests for the project components.
    *   `utils/`: For utility functions and helper classes (currently placeholder).
    *   `ui/`: Contains the Flask Web UI application.
        *   `app.py`: The main Flask application file.
        *   `templates/`: HTML templates for the web interface.
    *   `main_cli.py`: The main entry point for the command-line interface.
*   `requirements.txt`: Lists project dependencies (e.g., Flask).
*   `README.md`: This file.