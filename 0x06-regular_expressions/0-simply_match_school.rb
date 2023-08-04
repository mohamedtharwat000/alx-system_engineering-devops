#!/usr/bin/env ruby

# Retrieve the argument passed to the script
argument = ARGV[0]

# Define the regular expression pattern to match "School"
pattern = /School/

# Apply the regular expression to the argument
match = argument.match(pattern)

# Print the matched part or an empty string if there's no match
puts match ? match[0] : ''
