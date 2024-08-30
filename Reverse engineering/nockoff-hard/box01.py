import curses

# Define the correct results and answers for both challenges
correct_result_value_challenge1 = "8"  # Expected result in AL for challenge 1
correct_question_answer_challenge1 = "num"  # Correct answer for challenge 1

correct_result_value_challenge2 = "12"  # Expected result in AL for challenge 2
correct_question_answer_challenge2 = "5"  # Correct answer for challenge 2

correct_result_value_challenge3 = "8"  # Expected result in AL for challenge 3
correct_question_answer_challenge3 = "2"  # Correct answer for challenge 3


def start_challenge1(stdscr):
    stdscr.clear()

    # Define the text to be displayed with their positions
    text = [
        "Welcome to the Assembly Challenge!",
        "",
        "Analyze the following assembly code and provide the correct result:",
        "",
        "section .data",
        "    num db 5",
        "    result db 0",
        "",
        "section .text",
        "    global _start",
        "",
        "_start:",
        "    mov al, [num]",      
        "    mov bl, 3",          
        "    xor al, bl",        
        "    add al, 2",         
        "    mov [result], al",  
        "",
        "    cmp al, 4",
        "    jne not_equal",      
        "",
        "    mov ebx, 0",         
        "    mov eax, 1",         
        "    int 0x80",           
        "",
        "not_equal:",
        "    mov ebx, 1",         
        "    mov eax, 1",         
        "    int 0x80",           
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
    if user_input == correct_result_value_challenge1:
        stdscr.addstr(len(text) + 2, 0, "Correct result! Now answer the following question:")
        stdscr.addstr(len(text) + 3, 0, "Which data value was XORed with 3?")
        stdscr.refresh()

        # Get user answer to the follow-up question
        curses.echo()  # Enable echoing of characters
        stdscr.addstr(len(text) + 4, 0, "Answer: ")
        question_answer = stdscr.getstr(len(text) + 4, 8).decode('utf-8')  # Input starts at column 8
        curses.noecho()  # Disable echoing of characters

        if question_answer.lower() == correct_question_answer_challenge1.lower():
            stdscr.addstr(len(text) + 6, 0, "Correct answer!")
            stdscr.addstr(len(text)+7,0,"Key for the next challenge is = 0xfffff2f5L")
            stdscr.addstr(len(text) + 8, 0, "Press Enter to continue...")
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


def start_challenge2(stdscr):
    stdscr.clear()

    # Prompt for the ARM key
    stdscr.addstr(0, 0, "Enter the ARM1 key to proceed:")
    stdscr.refresh()

    # Get ARM key input
    curses.echo()  # Enable echoing of characters
    stdscr.addstr(1, 0, "ARM Key: ")
    arm_key = stdscr.getstr(1, 9).decode('utf-8')  # Input starts at column 9
    curses.noecho()  # Disable echoing of characters

    # Check if the ARM key is correct
    if arm_key != "0xfffff2f5L":  # Replace "ARM_SECRET" with the actual expected key
        stdscr.addstr(2, 0, "Incorrect ARM key. Exiting...")
        stdscr.refresh()
        stdscr.getch()  # Wait for user input to exit
        return False

    # Define the text to be displayed with their positions
    text = [
        "Welcome to the New Assembly Challenge!",
        "",
        "Analyze the following assembly code and provide the correct result:",
        "",
        "section .data",
        "    value db 10",
        "    result db 0",
        "",
        "section .text",
        "    global _start",
        "",
        "_start:",
        "    mov al, [value]",      
        "    mov bl, 5",          
        "    add al, bl",        
        "    sub al, 3",         
        "    mov [result], al",  
        "",
        "    cmp al, 7",
        "    jne not_equal",      
        "",
        "    mov ebx, 0",         
        "    mov eax, 1",         
        "    int 0x80",           
        "",
        "not_equal:",
        "    mov ebx, 1",         
        "    mov eax, 1",         
        "    int 0x80",           
        "",
        "Enter the result of the AL register after the operations:"
    ]

    # Display the text line by line
    for i, line in enumerate(text):
        stdscr.addstr(i + 2, 0, line)
    
    stdscr.refresh()
    
    # Prompt user for input at a specific position
    curses.echo()  # Enable echoing of characters
    stdscr.addstr(len(text) + 2, 0, "Result: ")
    user_input = stdscr.getstr(len(text) + 2, 8).decode('utf-8')  # Input starts at column 8
    curses.noecho()  # Disable echoing of characters

    # Check if the user input matches the correct result
    if user_input == correct_result_value_challenge2:
        stdscr.addstr(len(text) + 4, 0, "Correct result! Now answer the following question:")
        stdscr.addstr(len(text) + 5, 0, "What value was added to AL?")
        stdscr.refresh()

        # Get user answer to the follow-up question
        curses.echo()  # Enable echoing of characters
        stdscr.addstr(len(text) + 6, 0, "Answer: ")
        question_answer = stdscr.getstr(len(text) + 6, 8).decode('utf-8')  # Input starts at column 8
        curses.noecho()  # Disable echoing of characters

        if question_answer == correct_question_answer_challenge2:
            stdscr.addstr(len(text) + 8, 0, "Correct answer!")
            stdscr.addstr(len(text) + 9, 0, "Here is your key: 0xfff8945f")
            stdscr.refresh()
            stdscr.getch()  # Wait for user to press Enter
            return True  # Both conditions are true, returning True
        else:
            stdscr.addstr(len(text) + 8, 0, "Incorrect answer.")
    else:
        stdscr.addstr(len(text) + 4, 0, "Incorrect result.")

    stdscr.refresh()
    stdscr.getch()  # Wait for user input to proceed
    return False  # One or both conditions are false, returning False


def start_challenge3(stdscr):
    stdscr.clear()
    # Prompt for the ARM key
    stdscr.addstr(0, 0, "Enter the ARM2 key to proceed:")
    stdscr.refresh()

    # Get ARM key input
    curses.echo()  # Enable echoing of characters
    stdscr.addstr(1, 0, "ARM Key: ")
    arm_key = stdscr.getstr(1, 9).decode('utf-8')  # Input starts at column 9
    curses.noecho()  # Disable echoing of characters

    # Check if the ARM key is correct
    if arm_key != "0xfff8945f":  # Replace "ARM_SECRET" with the actual expected key
        stdscr.addstr(2, 0, "Incorrect ARM key. Exiting...")
        stdscr.refresh()
        stdscr.getch()  # Wait for user input to exit
        return False

    # Define the text to be displayed with their positions
    text = [
        "Welcome to the Next Assembly Challenge!",
        "",
        "Analyze the following assembly code and provide the correct result:",
        "",
        "section .data",
        "    value db 4",
        "    factor db 2",
        "    result db 0",
        "",
        "section .text",
        "    global _start",
        "",
        "_start:",
        "    mov al, [value]",    # Load value into AL
        "    mov bl, [factor]",   # Load factor into BL
        "    mul bl",             # Multiply AL by BL (AL = AL * BL)
        "    mov [result], al",  # Store result in 'result'
        "",
        "    cmp al, 6",
        "    jne not_equal",      # Jump if not equal to 'not_equal'
        "",
        "    mov ebx, 0",         # Exit code 0
        "    mov eax, 1",         # System call number for exit
        "    int 0x80",           # Interrupt to invoke system call
        "",
        "not_equal:",
        "    mov ebx, 1",         # Exit code 1
        "    mov eax, 1",         # System call number for exit
        "    int 0x80",           # Interrupt to invoke system call
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
    if user_input == correct_result_value_challenge3:
        stdscr.addstr(len(text) + 2, 0, "Correct result! Now answer the following question:")
        stdscr.addstr(len(text) + 3, 0, "What was the value used for multiplication?")
        stdscr.refresh()

        # Get user answer to the follow-up question
        curses.echo()  # Enable echoing of characters
        stdscr.addstr(len(text) + 4, 0, "Answer: ")
        question_answer = stdscr.getstr(len(text) + 4, 8).decode('utf-8')  # Input starts at column 8
        curses.noecho()  # Disable echoing of characters

        if question_answer == correct_question_answer_challenge3:
            stdscr.addstr(len(text) + 6, 0, "Correct answer!")
            stdscr.addstr(len(text) + 7, 0, "Here is your key: 0xeeff33ffaa")
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


def main():
    # Choose which challenge to test
    curses.wrapper(start_challenge1)  # or start_challenge2
