#!/usr/bin/perl
use strict;
use warnings;

my $logfile = $ARGV[0];

open(my $fh, '<', $logfile) or die "Could not open file '$logfile' $!";

open(my $out, '>', "errors.log") or die "Could not create errors.log $!";

while (my $line = <$fh>) {
    if ($line =~ /Timing violation at net (\w+)/) {
        print $out "Timing violation at net $1\n";
    }
    elsif ($line =~ /Synthesis failed due to (.+)/) {
        print $out "Synthesis failed due to $1\n";
    }
    elsif ($line =~ /Setup time violation detected/) {
        print $out "Setup time violation detected\n";
    }
}

close($fh);
close($out);
print "Parsed errors saved to errors.log\n";

