#!/usr/bin/env ruby

# Retrieve the argument passed to the script
argument = ARGV[0]

# Define the regular expression pattern"
pattern = /hbt+n/

# Use the scan method to find all occurrences of the pattern and join them
matched_string = argument.scan(pattern).join

# Print the matched part or an empty string if there's no match
puts matched_string
