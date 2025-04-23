proc debug_error {error_msg} {
    puts "\n🔍 Debugging: $error_msg"

    if {[string match "*Timing violation*" $error_msg]} {
        puts "❌ Issue: Timing violation detected."
        puts "✅ Suggested Fixes:"
        puts "- Try adjusting the clock skew."
        puts "- Increase hold time or slack."
        puts "- Check the clock constraints in SDC file."
    } elseif {[string match "*Synthesis failed*" $error_msg]} {
        puts "❌ Issue: Synthesis failed."
        puts "✅ Suggested Fixes:"
        puts "- Ensure all modules are correctly instantiated."
        puts "- Check if all required libraries are included."
        puts "- Run 'check_design' in Design Compiler."
    } elseif {[string match "*Setup time violation*" $error_msg]} {
        puts "❌ Issue: Setup time violation detected."
        puts "✅ Suggested Fixes:"
        puts "- Optimize logic paths to reduce delay."
        puts "- Use higher drive strength cells."
        puts "- Reduce the number of combinational gates."
    } else {
        puts "⚠ No predefined fix found. Check documentation."
    }
}

# Read errors from errors.log
set log_file [open "errors.log" r]
while {[gets $log_file line] != -1} {
    debug_error $line
}
close $log_file

