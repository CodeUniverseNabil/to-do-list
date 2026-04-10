📋 Routine Tracker CLI
A simple command-line app to manage your daily work routine and time tracking.
Features

Create a new routine list
Add tasks with time spent
Delete specific tasks
View your full routine
Clear everything and start fresh

Commands
CommandDescriptionnewStart a fresh routine (clears old data)addAdd more tasks to existing routineshowDisplay all current tasksdelRemove tasks one by oneclearDelete the entire routine
How to Run
bashpython your_file_name.py
Usage Example
Input your command: new
Enter the name of your work -> Study Python
Input your time -> 2.5
Enter the name of your work -> off
Data Storage
All tasks are saved in all_list.txt in the same directory, so your routine persists between sessions.
Requirements

Python 3.x
No external libraries needed