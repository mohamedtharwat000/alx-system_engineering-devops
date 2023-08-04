#!/usr/bin/env ruby

# Retrieve the argument passed to the script
argument = ARGV[0]

# Define the regular expression pattern to match "School"
pattern = /School/

# Apply the regular expression to the argument
match = argument.match(pattern)

# Join the matche and print the result
puts matche.join
