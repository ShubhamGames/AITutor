# AI Tutor Project

AI Tutor - A multi-agent system for personalized learning.

## Current Features

*   **Decider Agent:** Keyword-based subject detection for Maths, Physics, Chemistry, Biology, History, Geography, Economics.
*   **Prototype Maths Tutor:** Provides placeholder responses for maths-related queries.
*   **Prototype History Tutor:** Provides placeholder responses for history-related queries.
*   **Basic Student Interaction Logging:** Interactions are logged per student in JSON files.
*   **Command-Line Interface (CLI):** Allows users to interact with the AI Tutor.

## How to Run

1.  **Prerequisites:** Ensure you have Python 3.x installed.
2.  **Navigate to the project directory:**
    ```bash
    cd path/to/your/ai_tutor_project_root
    ```
3.  **Run the CLI:**
    ```bash
    python ai_tutor/main_cli.py
    ```
    Alternatively, if you are in the directory containing `ai_tutor` (e.g., `ai_tutor_project_root`), you can run it as a module:
    ```bash
    python -m ai_tutor.main_cli
    ```

## How to Run Tests

Navigate to the project's root directory and execute:
```bash
python -m unittest discover ai_tutor/tests
```

## Project Structure

*   `ai_tutor/`: Main package directory.
    *   `agents/`: Contains the different AI agent implementations (DeciderAgent, SubjectTutor, etc.).
    *   `data/`: Handles data storage, such as student interaction histories.
    *   `tests/`: Contains unit tests for the project components.
    *   `utils/`: For utility functions and helper classes (currently placeholder).
    *   `ui/`: Intended for user interface components (currently contains `main_cli.py`).
    *   `main_cli.py`: The main entry point for the command-line interface.
