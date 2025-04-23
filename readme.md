# VLSI-Linter

**VLSI-Linter** is a debugging and linting tool designed to assist in identifying and resolving errors in VLSI design flows. It parses log files, interacts with an error database, and provides both command-line and graphical interfaces for efficient debugging.

## Features

- **Log Parsing**: Extracts and analyzes error messages from log files.
- **Error Database Interaction**: Interfaces with an error database to provide detailed error information.
- **Command-Line Interface**: Offers a CLI for quick debugging tasks.
- **Graphical User Interface**: Provides a GUI built with Tcl for interactive debugging sessions.

## Repository Structure


      ├── cli_debug.py   - Command-line debugger script
      ├── debugger.py         #Core debugging logic
      ├── debugging.tcl       #GUI implementation using Tcl
      ├── errors.db           #SQLite database containing error information
      ├── errors.log          # Sample log file with errors
      ├── errors_db.py        # Script to interact with the error database
      ├── gui.tcl             # GUI script for the debugger
      ├── parse_logs.pl       # Perl script for parsing log files
      ├── run_debugger.sh     # Shell script to launch the debugger
      ├── sample_log.txt      # Sample input log file for testing

Usage
Run the Debugger

To launch the debugger (CLI or GUI), simply run:
./run_debugger.sh

Run Python Debugger directly

python debugger.py



Sample Input and Output
Input

The sample_log.txt file contains entries like:

ERROR: Net 'clk' has multiple drivers.
WARNING: Unconnected input port 'reset' on module 'counter'.

Output

Running the debugger will produce output similar to:

Identified Errors:
1. Net 'clk' has multiple drivers.
   - Suggested Fix: Ensure 'clk' is driven by only one source.
2. Unconnected input port 'reset' on module 'counter'.
   - Suggested Fix: Connect the 'reset' input to the appropriate signal.
