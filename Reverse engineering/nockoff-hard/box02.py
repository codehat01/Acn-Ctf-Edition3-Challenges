# Define the correct results and answers for both challenges
import curses

def start_challenge1(stdscr):
    stdscr.clear()
    # Prompt for the ARM key
    stdscr.addstr(0, 0, "Enter the ARM1 key to proceed:")
    stdscr.refresh()

    # Get ARM key input
    curses.echo()  # Enable echoing of characters
    stdscr.addstr(1, 0, "ARM3 Key: ")
    arm_key = stdscr.getstr(1, 9).decode('utf-8')  # Input starts at column 9
    curses.noecho()  # Disable echoing of characters

    # Check if the ARM key is correct
    if arm_key != "0xeeff33ffaa":  # Replace "ARM_SECRET" with the actual expected key
        stdscr.addstr(2, 0, "Incorrect ARM key. Exiting...")
        stdscr.refresh()
        stdscr.getch()  # Wait for user input to exit
        return False

    # Define the text to be displayed with their positions
    text = [
        "Welcome to the Assembly Challenge!",
        "",
        "Analyze the following assembly code and provide the correct result:",
        "",
        "section .data",
        "    value1 db 7",
        "    value2 db 3",
        "    result db 0",
        "",
        "section .text",
        "    global _start",
        "",
        "_start:",
        "    mov al, [value1]",      # Load value1 into AL
        "    sub al, [value2]",      # Subtract value2 from AL (AL = AL - value2)
        "    mov [result], al",     # Store result in 'result'
        "",
        "    cmp al, 4",
        "    jne not_equal",        # Jump if not equal to 'not_equal'
        "",
        "    mov ebx, 0",           # Exit code 0
        "    mov eax, 1",           # System call number for exit
        "    int 0x80",             # Interrupt to invoke system call
        "",
        "not_equal:",
        "    mov ebx, 1",           # Exit code 1
        "    mov eax, 1",           # System call number for exit
        "    int 0x80",             # Interrupt to invoke system call
        "",
        "Enter the result of the AL register after the operations:"
    ]

    # Display the text line by line
    for i, line in enumerate(text):
        stdscr.addstr(i, 0, line)
    
    stdscr.refresh()
    
    # Prompt user for input at a specific position
    curses.echo()  # Enable echoing of characters
    stdscr.addstr(len(text), 0, "Result: ")
    user_input = stdscr.getstr(len(text), 8).decode('utf-8')  # Input starts at column 8
    curses.noecho()  # Disable echoing of characters

    # Check if the user input matches the correct result
    if user_input == "4":  # Expected result in AL after operations
        stdscr.addstr(len(text) + 2, 0, "Correct result! Now answer the following question:")
        stdscr.addstr(len(text) + 3, 0, "What is the value that was subtracted from AL?")
        stdscr.refresh()

        # Get user answer to the follow-up question
        curses.echo()  # Enable echoing of characters
        stdscr.addstr(len(text) + 4, 0, "Answer: ")
        question_answer = stdscr.getstr(len(text) + 4, 8).decode('utf-8')  # Input starts at column 8
        curses.noecho()  # Disable echoing of characters

        if question_answer == "3":  # Expected value subtracted
            stdscr.addstr(len(text) + 6, 0, "Correct answer!")
            stdscr.addstr(len(text) + 7, 0, "Here is your key: 0xfffaa342344")
            stdscr.refresh()
            stdscr.getch()  # Wait for user to press Enter
            return True  # Both conditions are true, returning True
        else:
            stdscr.addstr(len(text) + 6, 0, "Incorrect answer.")
    else:
        stdscr.addstr(len(text) + 2, 0, "Incorrect result.")

    stdscr.refresh()
    stdscr.getch()  # Wait for user input to proceed
    return False  # One or both conditions are false, returning False
