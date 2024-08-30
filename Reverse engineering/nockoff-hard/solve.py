import curses
import box01
import box02
import box03
import box04

# Define the grid state globally to access within callbacks
grid_state = {}

def check_all_box():
    j=0
    for i in range(grid_state):
      j=j+1
    if j==7:
        return True
    else:
        return False

def on_enter_secret_box(x,y,stdscr):
    ress=box04.final(stdscr)
    if ress:
        curser="😊"
    else:
        pass
def on_enter_box(x, y, stdscr):
    if x == 35 and y == 2:
        result = box01.start_challenge1(stdscr)
        if result:
            grid_state[(x, y)] = "ARM1"
        else:
            pass
    if x==18 and y==2:
        result2=box01.start_challenge2(stdscr)
        if result2:
            grid_state[(x,y)]="ARM2"
        else:
            pass
    if x==4 and y==2:
        result3 = box01.start_challenge3(stdscr)
        if result3:
            grid_state[(x, y)] = "ARM3"
        else:
            pass
    if x==4 and y==9:
        result4 = box02.start_challenge1(stdscr)
        if result4:
            grid_state[(x, y)] = "i386"
        else:
            pass
    if x==4 and y==16:
        result5=box03.start_challenge1(stdscr)
        if result5:
            grid_state[(x, y)] = "go1"
        else:
            pass
    if x==18 and y==16:
        result6=box03.start_challenge2(stdscr)
        if result6:
            grid_state[(x, y)] = "go2"
        else:
            pass
    if x==35 and y==16:
        result7=box03.start_challenge3(stdscr)
        if result7:
            grid_state[(x, y)] = "go3"
        else:
            pass


curser="😦"

def main(stdscr):
    global grid_state
    
    # Clear screen
    curses.curs_set(0)
    stdscr.clear()
    
    # Initial position of the "😦" character
    x, y = 8, 13
    
    # Coordinates of the boxes
    box_positions = [(4, 2), (18, 2), (35, 2), (4, 9), (4, 16), (18, 16), (35, 16)]
    
    # State of the grid (initially, all boxes contain "???")
    grid_state = {pos: "???" for pos in box_positions}

    # Display the grid
    def draw_grid():
        stdscr.addstr(0, 0, "----------------------------------------")
        stdscr.addstr(1, 0, "|       |      |       |       |       |")
        stdscr.addstr(2, 0, f"|  {grid_state[(4, 2)]}  |      |  {grid_state[(18, 2)]}  |       |  {grid_state[(35, 2)]}  |")
        stdscr.addstr(3, 0, "|       |      |       |       |       |")
        stdscr.addstr(4, 0, "|--   ---      ---   ---       ---   --|")
        stdscr.addstr(5, 0, "|                                      |")
        stdscr.addstr(6, 0, "|                                      |")
        stdscr.addstr(7, 0, "|--------                              |")
        stdscr.addstr(8, 0, "|       |                              |")
        stdscr.addstr(9, 0, f"|  {grid_state[(4, 9)]}                                 |")
        stdscr.addstr(10, 0, "|       |                              |")
        stdscr.addstr(11, 0, "|--------                              |")
        stdscr.addstr(12, 0, "|                                      |")
        stdscr.addstr(13, 0, "|                                      |")
        stdscr.addstr(14, 0, "|--   ---      ---   ---       ---   --|")
        stdscr.addstr(15, 0, "|       |      |       |       |       |")
        stdscr.addstr(16, 0, f"|  {grid_state[(4, 16)]}  |      |  {grid_state[(18, 16)]}  |       |  {grid_state[(35, 16)]}  |")
        stdscr.addstr(17, 0, "|       |      |       |       |       |")
        stdscr.addstr(18, 0, "----------------------------------------")

    while True:
        stdscr.clear()
        draw_grid()
        stdscr.addstr(y, x, curser)
        stdscr.refresh()

        # Check if the "😦" is inside a box
        if (x, y) in box_positions:
            stdscr.addstr(19, 0, "Enter the box?:")

        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == ord('\n') and (x, y) in box_positions:
            on_enter_box(x, y, stdscr)
        elif key == ord('w') and y > 1 and (y - 1, x) not in [(7, 0), (11, 0)]:  # Adjust if needed
            y -= 1
        elif key == ord('s') and y < 17 and (y + 1, x) not in [(7, 0), (11, 0)]:  # Adjust if needed
            y += 1
        elif key == ord('a') and x > 1 and (y, x - 1) not in [(0, 7), (0, 15), (0, 23), (0, 31)]:  # Adjust if needed
            x -= 1
        elif key == ord('d') and x < 38 and (y, x + 1) not in [(0, 7), (0, 15), (0, 23), (0, 31)]:  # Adjust if needed
            x += 1
        
        if x==4 and x==6 and check_all_box():
            stdscr.addstr(19, 0, "Enter the box?:")
        if key==ord('q'):
            break
        elif key == ord('\n') and x==4 and y==6:
            on_enter_secret_box(x,y,stdscr)

curses.wrapper(main)
