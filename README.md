# Stata-Python Bridge for VS Code

> **Developed with AI Assistance** 🤖✨
> This tool was co-created by a human researcher and an AI Agent to solve the challenge of seamless Stata integration in VS Code.

This tool enables a **Persistent Stata Session** directly inside VS Code (or similar ones like Antigravity), allowing you to run Stata code interactively without switching windows or blocking your editor. It works more like a  tool that you can rely on the AI to do Stata coding, run analysis, and have AI to read your results in one place. 

## What It Does
*   **Runs Stata in the Background**: Uses a Python script to launch Stata via COM Automation.
*   **Keeps Session Alive**: Unlike standard "batch mode," this keeps memory and variables active between commands.
*   **VS Code Integration**: Runs directly in the Integrated Terminal (`Ctrl+Shift+B`).

## Key Features
1.  **Speed**: No need to relaunch Stata for every snippet.
2.  **Focus**: Stay in your editor; output appears in the terminal.
3.  **Collaboration Ready**: Designed to work with AI coding assistants (via log files).

## Prerequisites
1.  **Stata (Version 17+)**: Must be installed and registered for COM Automation.
    *   *To register:* Open Command Prompt as Admin -> `cd "C:\Program Files\Stata17"` -> `StataSE.exe /Register`
2.  **Python 3.x**:
    *   Install dependencies: `pip install -r requirements.txt`
3.  **VS Code**:
    *   Extension: **Stata Run** or **Stata Improved** (Recommended for syntax highlighting).
    *   *Note:* The execution bridge works without any specific extension, but you need one to make `.do` files readable.

## Project Structure (Critical)
To ensure the automation works, your project folder **must** contain:

```text
My_Research_Project/           <-- You MUST open THIS folder in VS Code
├── .vscode/                   <-- Created automatically (hidden settings)
│     └── tasks.json           <-- The "Configuration" file
├── run_dynamic_stata.py       <-- The "Engine" script (MUST be at top level)
├── analysis.do                <-- Your Stata Code
└── data.dta                   <-- Your Data
```

### Important: Opening the Project
When you (or a colleague) start working, you must open the **entire project folder** in VS Code, not just a single file.
1.  Open VS Code.
2.  Go to **File > Open Folder...**
3.  Select `My_Research_Project`.

*Result:* VS Code will automatically detect the `.vscode` folder and enable the "Run Stata" task.

## Installation & Configuration

### Step 1: Place the Files
Copy the `run_dynamic_stata.py` file and the `.vscode` folder into the new user's project directory.

### Step 2: Configure Stata Path
Open `run_dynamic_stata.py` in a text editor.
Find line 5:
```python
STATA_PATH = r'C:\Program Files\StataNow19'
```
**Update this path** to match the location of Stata on the *new user's computer* (e.g., `C:\Program Files\Stata17`).

### Step 3: Configure Python Path (Optional)
The task assumes `python` is in the system PATH. If executing `python` in a terminal doesn't work, you may need to edit `.vscode/tasks.json`:
```json
"command": "python",  // Change to "C:\\Path\\To\\Python\\python.exe" if needed
```

## How to Use: Persistent Session
1.  **Start the Session:**
    *   Press **`Ctrl+Shift+B`**.
    *   The terminal will show: `STATA SESSION INITIALIZED`.
    *   *Leave this terminal open.*

2.  **Run Code:**
    *   Select Stata code in your editor.
    *   **Copy** it (`Ctrl+C`).
    *   Click in the Terminal window and press **`Enter`**.
    *   *Stata runs the code and keeps the session alive (memory is preserved).*

3.  **Repeat:**
    *   Copy next chunk -> Press Enter.

4.  **Stop:**
    *   Type `exit` or click the Trash icon to valid the session.

## Collaboration Workflow (User + AI)
Because AI assistants (like Gemini/ChatGPT) cannot see your terminal screen, we use the **Log File** as our shared "source of truth."

1.  **Enable Logging:**
    Add this to the top of your do-file:
    ```stata
    log using "analysis.log", replace
    ```
    *(Use `append` if you want to keep history)*

2.  **Teach the AI Your Data:**
    Before asking complex analysis questions, run these commands and ask the AI to read the log:
    ```stata
    describe
    codebook, problems
    ```
    *This gives the AI the "map" of your dataset (variable names, labels, types).*

3.  **Iterative Workflow:**
    *   **You Run Code:** Execute a block of code.
    *   **AI Reads Log:** Ask: *"Did it work?"* or *"What does the regression show?"*
    *   **AI Responds:** The AI reads `analysis.log` and interprets the exact Stata output for you.
