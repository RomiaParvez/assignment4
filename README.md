# assignment4
Problem Statement
# task1
Write a Python program that:
Opens and reads a text file named sample.txt.
Prints its content line by line.
Handles errors gracefully if the file does not exist.

 Code Implementation


Explanation

The try block attempts to open sample.txt.

with open("sample.txt", "r") ensures the file is properly handled.

The for loop reads each line, and line.strip() removes leading/trailing whitespaces and newline characters.

If the file does not exist, FileNotFoundError is caught and an error message is displayed.

Any other errors are caught and printed.

# task2
Problem Statement

Write a Python program that:

Takes user input and writes it to a file named output.txt.

Appends additional data to the same file.

Reads and displays the final content of the file.


Explanation

The program prompts the user for input and writes it to output.txt.
It then asks for more input and appends it to the same file.
Finally, it reads and prints the entire file content.
\n is added to ensure each input appears on a new line.
