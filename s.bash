#!/bin/bash

# Run wsl --list --verbose command and store the output in a variable
output=$(wsl --list --verbose)

# Remove the first line of output, which contains the column headers
output=$(echo "$output" | sed '1d')

# Define a function to convert a single line of output to JSON format
function lineToJson {
    # Split the line into columns using whitespace as a delimiter
    IFS=' ' read -r -a columns <<< "$1"
    
    # Build a JSON object using the column values
    echo "{ \"name\": \"${columns[0]}\", \"state\": \"${columns[2]}\" }"
}

# Convert each line of output to JSON format and append to an array
json="["
while read -r line; do
    json="$json $(lineToJson "$line"),"
done <<< "$output"
# Remove the trailing comma and close the array
json="${json%?}]"

# Print the JSON output
echo "$json"
