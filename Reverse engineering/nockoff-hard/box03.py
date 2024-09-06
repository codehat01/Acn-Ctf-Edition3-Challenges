import curses
import subprocess

# Display Go program 1
def display_go_program(stdscr):
    go_code = '''
package main

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
    "net/http"
    "os"
    "sync"
    "time"
)

type Data struct {
    Key   string `json:"key"`
    Value string `json:"value"`
}

func fetchData(url string, wg *sync.WaitGroup, ch chan<- Data) {
    defer wg.Done()
    resp, err := http.Get(url)
    if err != nil {
        fmt.Println("Failed to fetch data:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Failed to read response:", err)
        return
    }

    var data Data
    if err := json.Unmarshal(body, &data); err != nil {
        fmt.Println("Failed to parse JSON:", err)
        return
    }

    ch <- data
}

func main() {
    urls := []string{
        "https://example.com/api/data1",
        "https://example.com/api/data2",
        "https://example.com/api/data3",
    }

    var wg sync.WaitGroup
    dataChannel := make(chan Data, len(urls))

    for _, url := range urls {
        wg.Add(1)
        go fetchData(url, &wg, dataChannel)
    }

    wg.Wait()
    close(dataChannel)

    var collectedData []Data
    for data := range dataChannel {
        collectedData = append(collectedData, data)
    }

    file, err := os.Create("output.json")
    if err != nil {
        fmt.Println("Failed to create file:", err)
        return
    }
    defer file.Close()

    jsonData, err := json.Marshal(collectedData)
    if err != nil {
        fmt.Println("Failed to serialize data:", err)
        return
    }

    file.Write(jsonData)
    fmt.Println("Data saved to output.json")
}
'''

    stdscr.clear()
    lines = go_code.strip().splitlines()
    height, width = stdscr.getmaxyx()
    max_lines = height - 2  # Leave space for instructions at the bottom

    start_line = 0
    while True:
        stdscr.clear()
        for i in range(min(max_lines, len(lines) - start_line)):
            stdscr.addstr(i, 0, lines[start_line + i][:width])
        stdscr.addstr(height - 1, 0, "Use arrow keys to scroll, press 'p' to proceed")
        stdscr.refresh()

        key = stdscr.getch()
        if key == curses.KEY_UP and start_line > 0:
            start_line -= 1
        elif key == curses.KEY_DOWN and start_line + max_lines < len(lines):
            start_line += 1
        elif key == ord('p'):
            return

# Display Go program 2
def display_go_program1(stdscr):
    go_code = '''
package main

import (
    "fmt"
    "math"
)

func main() {
    numbers := []float64{16, 25, 36, 49, 64}

    var sum float64
    for _, num := range numbers {
        sum += num
    }

    mean := sum / float64(len(numbers))

    var varianceSum float64
    for _, num := range numbers {
        varianceSum += math.Pow(num - mean, 2)
    }
    variance := varianceSum / float64(len(numbers))
    stddev := math.Sqrt(variance)

    fmt.Printf("Sum: %.2f\\n", sum)
    fmt.Printf("Mean: %.2f\\n", mean)
    fmt.Printf("Variance: %.2f\\n", variance)
    fmt.Printf("Standard Deviation: %.2f\\n", stddev)
}
'''

    stdscr.clear()
    lines = go_code.strip().splitlines()
    height, width = stdscr.getmaxyx()
    max_lines = height - 2  # Leave space for instructions at the bottom

    start_line = 0
    while True:
        stdscr.clear()
        for i in range(min(max_lines, len(lines) - start_line)):
            stdscr.addstr(i, 0, lines[start_line + i][:width])
        stdscr.addstr(height - 1, 0, "Use arrow keys to scroll, press 'p' to proceed")
        stdscr.refresh()

        key = stdscr.getch()
        if key == curses.KEY_UP and start_line > 0:
            start_line -= 1
        elif key == curses.KEY_DOWN and start_line + max_lines < len(lines):
            start_line += 1
        elif key == ord('p'):
            return  # Proceed to the next step

# Challenge 1
def start_challenge1(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Enter the ARM1 key to proceed:")
    stdscr.refresh()

    # Get ARM key input
    curses.echo()  # Enable echoing of characters
    stdscr.addstr(1, 0, "i386 key: ")
    arm_key = stdscr.getstr(1, 9).decode('utf-8')  # Input starts at column 9
    curses.noecho()  # Disable echoing of characters

    # Check if the ARM key is correct
    if arm_key != "0xfffaa342344":
        stdscr.addstr(2, 0, "Incorrect ARM key. Exiting...")
        stdscr.refresh()
        stdscr.getch()  # Wait for user input to exit
        return False

    stdscr.addstr("Welcome to the Go Challenge!\n")
    stdscr.addstr("In this challenge, a Go program will be executed.\n")
    stdscr.addstr("You must analyze the Go code and answer the following questions:\n\n")
    stdscr.addstr("Press any key to continue...")
    stdscr.refresh()
    stdscr.getch()

    display_go_program(stdscr)
    stdscr.clear()

    stdscr.addstr(20, 0, "Go program executed successfully. Now, answer the following:")
    
    # Question 1
    stdscr.addstr(22, 0, "1. After the data is fetched, how many goroutines are still running?")
    stdscr.addstr(24, 0, "Answer: ")
    curses.echo()
    answer1 = stdscr.getstr(24, 8).decode('utf-8').strip()
    curses.noecho()

    # Question 2
    stdscr.addstr(26, 0, "2. What is the name of the output file generated by the Go program?")
    stdscr.addstr(27, 0, "Answer: ")
    curses.echo()
    answer2 = stdscr.getstr(27, 8).decode('utf-8').strip()
    curses.noecho()

    if answer1 == "0" and answer2 == "output.json":
        stdscr.addstr(29, 0, "Correct! You've successfully completed the challenge.")
        stdscr.addstr(30, 0, "Here is your key: 0xvexo1012")
        stdscr.addstr(31, 0, "Press any key to exit.")
        stdscr.refresh()
        stdscr.getch()
        return True
    else:
        stdscr.addstr(29, 0, "Incorrect answers. Try again.")
        stdscr.refresh()
        stdscr.getch()
        return False

# Challenge 2
def start_challenge2(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Enter the ARM1 key to proceed:")
    stdscr.refresh()

    # Get ARM key input
    curses.echo()
    stdscr.addstr(1, 0, "go_1 key: ")
    arm_key = stdscr.getstr(1, 9).decode('utf-8')
    curses.noecho()

    if arm_key != "0xvexo1012":
        stdscr.addstr(2, 0, "Incorrect ARM key. Exiting...")
        stdscr.refresh()
        stdscr.getch()
        return False

    stdscr.addstr("In this challenge, a Go program will be executed.\n")
    stdscr.addstr("You must analyze the Go code and answer the following questions:\n\n")
    stdscr.addstr("Press any key to continue...")
    stdscr.refresh()
    stdscr.getch()

    display_go_program(stdscr)
    stdscr.clear()

    stdscr.addstr(20, 0, "Go program executed successfully. Now, answer the following:")
    
    # Question 1
    stdscr.addstr(22, 0, "1. How many items are collected from the API?")
    stdscr.addstr(24, 0, "Answer: ")
    curses.echo()
    answer1 = stdscr.getstr(24, 8).decode('utf-8').strip()
    curses.noecho()

    # Question 2
    stdscr.addstr(26, 0, "2. What is the data type of the 'Price' field in the JSON structure?")
    stdscr.addstr(27, 0, "Answer: ")
    curses.echo()
    answer2 = stdscr.getstr(27, 8).decode('utf-8').strip()
    curses.noecho()

    if answer1 == "5" and answer2 == "float64":
        stdscr.addstr(29, 0, "Correct! You've successfully completed the challenge.")
        stdscr.addstr(30, 0, "Here is your key: 0xxddx1132.")
        stdscr.addstr(31, 0, "Press any key to exit.")
        stdscr.refresh()
        stdscr.getch()
        return True
    else:
        stdscr.addstr(29, 0, "Incorrect answers. Try again.")
        stdscr.refresh()
        stdscr.getch()
        return False
# Challenge 3
def start_challenge3(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Enter the key for Challenge 3 to proceed:")
    stdscr.refresh()

    # Get key input
    curses.echo()  # Enable echoing of characters
    stdscr.addstr(1, 0, "challenge_3 key: ")
    challenge_key = stdscr.getstr(1, 16).decode('utf-8')
    curses.noecho()  # Disable echoing of characters

    # Check if the key is correct
    if challenge_key != "0xxddx1132":
        stdscr.addstr(2, 0, "Incorrect key. Exiting...")
        stdscr.refresh()
        stdscr.getch()  # Wait for user input to exit
        return False

    stdscr.addstr(3, 0, "Welcome to Challenge 3!\n")
    stdscr.addstr(4, 0, "In this challenge, a new Go program will be executed.\n")
    stdscr.addstr(5, 0, "You must analyze the code and answer the following questions:\n\n")
    stdscr.addstr(6, 0, "Press any key to continue...")
    stdscr.refresh()
    stdscr.getch()

    # Display a new Go program for Challenge 3
    display_go_program1(stdscr)  # Assuming display_go_program1 contains the Go code for Challenge 3
    stdscr.clear()

    stdscr.addstr(20, 0, "Go program executed successfully. Now, answer the following:")
    
    # Question 1
    stdscr.addstr(22, 0, "1. What is the square root of the second number in the list?")
    stdscr.addstr(24, 0, "Answer: ")
    curses.echo()
    answer1 = stdscr.getstr(24, 8).decode('utf-8').strip()
    curses.noecho()

    # Question 2
    stdscr.addstr(26, 0, "2. What is the standard deviation of the numbers?")
    stdscr.addstr(27, 0, "Answer: ")
    curses.echo()
    answer2 = stdscr.getstr(27, 8).decode('utf-8').strip()
    curses.noecho()

    if answer1 == "5" and answer2 == "2.58":
        stdscr.addstr(29, 0, "Correct! You've successfully completed Challenge 3.")
        stdscr.addstr(33, 0, "You have found the flag= ACN_CTF{R3c0gn1z3_TH3 ")
        stdscr.addstr(34,0,"find the invisible final box to get the output")
        stdscr.addstr(35, 0, "Press any key to exit.")
        stdscr.refresh()
        stdscr.getch()
        return True
    else:
        stdscr.addstr(29, 0, "Incorrect answers. Try again.")
        stdscr.refresh()
        stdscr.getch()
        return False

# Main function to run the challenge sequence
def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Welcome to the Go CTF Challenge!")
        stdscr.addstr(2, 0, "1. Start Challenge 1")
        stdscr.addstr(3, 0, "2. Start Challenge 2")
        stdscr.addstr(4, 0, "Press 'q' to exit")
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('1'):
            if start_challenge1(stdscr):
                break
        elif key == ord('2'):
            if start_challenge2(stdscr):
                break
        elif key == ord('q'):
            break

if __name__ == "__main__":
    curses.wrapper(main)

