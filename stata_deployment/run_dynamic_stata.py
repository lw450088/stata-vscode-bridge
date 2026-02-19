import sys
import os
import tkinter as tk

# 1. Configure Stata Path
STATA_PATH = r'C:\Program Files\StataNow19'
UTILITIES_PATH = os.path.join(STATA_PATH, 'utilities')
sys.path.append(UTILITIES_PATH)

try:
    import stata_setup
    stata_setup.config(STATA_PATH, 'se')
    from pystata import stata
    
    # 2. Hybrid Mode: Check for Arguments first
    if len(sys.argv) > 1:
        # Automated/Single-Run Mode
        arg = sys.argv[1]
        if os.path.exists(arg) and os.path.isfile(arg):
             print(f"Running code from file: {arg}")
             with open(arg, 'r') as f:
                 stata_code = f.read()
        else:
             print("Running provided code argument...")
             stata_code = arg
        
        stata.run(stata_code)
        print("\nAutomated Run Complete.")
        sys.exit(0)

    # 3. Interactive Loop (Persistent Session)
    print("\n" + "="*60)
    print("STATA SESSION INITIALIZED")
    print("Instructions:")
    print("1. Select code in VS Code.")
    print("2. Copy it (Ctrl+C).")
    print("3. Click here and press <Enter> to run.")
    print("   (Type 'exit' or 'q' to quit)")
    print("="*60 + "\n")

    root = tk.Tk()
    root.withdraw()

    while True:
        try:
            user_input = input("Ready > Press <Enter> to run clipboard code: ")
            if user_input.lower() in ['exit', 'q', 'quit']:
                break
            
            # Read from Clipboard
            stata_code = root.clipboard_get()
            
            if not stata_code.strip():
                print("Clipboard is empty.")
                continue

            print(f"\n--- Running {len(stata_code)} chars from clipboard ---")
            print(stata_code[:100] + "..." if len(stata_code) > 100 else stata_code)
            
            # Run in Stata
            stata.run(stata_code)
            print("--- Done ---\n")

        except tk.TclError:
            print("Error: Could not read clipboard.")
        except KeyboardInterrupt:
            print("\nSession closing...")
            break
        except Exception as e:
            print(f"Error: {e}")


except ImportError:
    print("Error: Could not import stata_setup.")
except Exception as e:
    print(f"An error occurred: {e}")
