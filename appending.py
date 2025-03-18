# Get user input
data = input("Enter data to write to the file: ")

# Write data to output.txt
with open("output.txt", "w") as file:
    file.write(data + "\n")

# Append additional data
append_data = input("Enter additional data to append: ")
with open("output.txt", "a") as file:
    file.write(append_data + "\n")

# Read and display the final content
print("Final content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())
