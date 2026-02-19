*-------------------------------------------------------------------------------
* Example Stata Script for VS Code Integration
*-------------------------------------------------------------------------------
* INSTRUCTIONS:
* 1. Start Session: Press Ctrl+Shift+B (Terminal will say "STATA SESSION INITIALIZED").
* 2. Select a block of code (e.g., lines 15-20).
* 3. Copy (Ctrl+C).
* 4. Click in the Terminal window.
* 5. Press Enter to run.
* 
* AI WORKFLOW:
* - Ask your AI Assistant: "Read analysis.log and interpret the results."
*-------------------------------------------------------------------------------

* 1. Start Logging (Crucial for AI Collaboration)
capture log close
log using "analysis.log", replace text
display "Log Started - AI can now read output."

* 2. Load Example Data
sysuse auto, clear

* 3. Teach the AI Your Data (Run this first!)
*    Ask the AI: "Read the log and tell me about this dataset."
describe
codebook, problems

* 4. Run Analysis
*    Ask the AI: "What is the average price and mpg?"
summarize price mpg weight

* 5. Run a Regression
*    Ask the AI: "Interpret this regression. Is foreign status significant?"
regress price mpg weight foreign

* 6. Visualize (Optional - window will open in background)
scatter price mpg

* End of Test
display "Test Complete. Check analysis.log for results."
log close
