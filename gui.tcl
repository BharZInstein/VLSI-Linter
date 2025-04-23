#!/usr/bin/env wish

# Create the main window
wm title . "VLSI Error Debugger"
set log_file ""

# Label
label .lbl -text "Select Log File to Parse:" -font "Arial 12 bold"
pack .lbl -padx 10 -pady 5 -anchor w

# File selection
entry .entry -textvariable log_file -width 50
button .browse -text "Browse..." -command {
    set log_file [tk_getOpenFile -filetypes {{{Text Files} {.txt}} {{All Files} {*}}}]
    .entry configure -textvariable log_file
}
pack .entry .browse -side left -padx 5 -pady 5

# Run Button
button .run -text "Run Debugger" -command {
    if {$log_file eq ""} {
        tk_messageBox -message "Please select a log file first!" -icon warning
    } else {
        # Run the Perl script
        set cmd "perl parse_logs.pl \"$log_file\""
        catch {exec sh -c $cmd} result
        # Load and show errors
        if {[file exists "errors.log"]} {
            set f [open "errors.log" r]
            set content [read $f]
            close $f
            .text delete 1.0 end
            .text insert end $content
            .status configure -text "Parsed successfully!"
        } else {
            .status configure -text "Failed to generate errors.log"
        }
    }
}
pack .run -padx 10 -pady 5

# Text Display Box
text .text -height 20 -width 80 -wrap word -yscrollcommand ".scroll set"
scrollbar .scroll -command ".text yview"
pack .text .scroll -side left -fill both -expand 1

# Status Label
label .status -text "Waiting for input..." -font "Arial 10 italic"
pack .status -side bottom -fill x -padx 5 -pady 5

