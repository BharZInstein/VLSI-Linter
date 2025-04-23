#!/bin/bash

echo "🚀 Running Log Parsing (Perl)..."
perl parse_logs.pl sample_log.txt

echo "✅ Errors extracted. Running Debugging (TCL)..."
tclsh debugging.tcl

#echo "💾 Storing errors into database..."
#python cli_debug.py

