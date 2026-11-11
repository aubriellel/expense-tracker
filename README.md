Personal Expense Tracker
Project Description
This is a simple Python program that allows a user to enter expenses, view the expenses entered, calculate the total, and view additional expense statistics.

Initial Version
The initial version of the program included the following features:

Allowed the user to enter an expense amount
Stored expenses in a list
Displayed all expenses entered
Calculated and displayed the total expenses
Used a repeating menu
Allowed the user to exit the program
AI Tool Used
Microsoft Copilot

AI Assistance
I used Microsoft Copilot to help improve my existing Python program. I asked for help adding input validation and additional expense calculations without replacing the original purpose of the program.

New or Modified Features
The AI-assisted version added the following improvements:

Input validation so the program does not crash if the user enters text instead of a number
A message when a negative expense amount is entered
A new statistics option
Calculation of the average expense
Calculation of the highest expense
Clearer messages and comments in the program
Evaluation of AI Output
I reviewed the changes suggested by Microsoft Copilot and tested them before keeping them. I accepted the input validation and statistics features because they improved the original program and I understood how they worked. I tested the input validation by entering text instead of a number and confirmed that the program displayed an error message instead of crashing. I also tested the statistics using expenses of $25.50 and $10.00 and confirmed that the average was $17.75 and the highest expense was $25.50.

How to Run the Program
Make sure Python is installed.
Open the project folder in Visual Studio Code.
Open main.py.
Run the Python program.
Choose an option from the menu and follow the prompts.
Choose option 5 when you are ready to exit.

## Assignment 9: Dual-Approach Feature Development

### Manual Feature Specification

**Feature Name:** Remove Expense

**Purpose:**  
Allow the user to remove an expense that was entered by mistake.

**Expected Behavior:**  
The program will display the current expenses and allow the user to select an expense to remove. If there are no expenses, the program will display a message instead of trying to remove one.

**Test Cases:**
1. Add several expenses, remove one, and verify that the correct expense is removed.
2. Try to remove an expense when the list is empty and verify that the program displays a message without crashing.