import curses
import subprocess

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
            return  # Proceed to the next step

def start_challenge3(stdscr):
    stdscr.clear()
    stdscr.addstr("In this challenge, a Go program will be executed.\n")
    stdscr.addstr("You must analyze the Go code and answer the following questions about the libraries used:\n\n")
    stdscr.addstr("Press any key to continue...")
    stdscr.refresh()
    stdscr.getch()

    display_go_program(stdscr)

    # Run the Go program
    try:
        subprocess.run(["go", "run", "GoProgram.go"], check=True)
    except subprocess.CalledProcessError as e:
        stdscr.addstr(20, 0, f"Error running Go program: {str(e)}")
        stdscr.refresh()
        stdscr.getch()
        return

    stdscr.addstr(20, 0, "Go program executed successfully. Now, answer the following:")
    
    # Advanced Question 1
    stdscr.addstr(22, 0, "1. What is the role of the 'sync' package in the Go program?")
    stdscr.addstr(23, 0, "Answer: ")
    curses.echo()
    answer1 = stdscr.getstr(23, 8).decode('utf-8').strip()
    curses.noecho()

    # Advanced Question 2
    stdscr.addstr(25, 0, "2. How does the 'net/http' package handle HTTP requests in the Go program?")
    stdscr.addstr(26, 0, "Answer: ")
    curses.echo()
    answer2 = stdscr.getstr(26, 8).decode('utf-8').strip()
    curses.noecho()

    # Advanced Question 3
    stdscr.addstr(28, 0, "3. What is the purpose of 'json.Unmarshal' in the Go program?")
    stdscr.addstr(29, 0, "Answer: ")
    curses.echo()
    answer3 = stdscr.getstr(29, 8).decode('utf-8').strip()
    curses.noecho()

    # Advanced Question 4
    stdscr.addstr(31, 0, "4. Explain how 'ioutil.ReadAll' contributes to reading the response body.")
    stdscr.addstr(32, 0, "Answer: ")
    curses.echo()
    answer4 = stdscr.getstr(32, 8).decode('utf-8').strip()
    curses.noecho()

    if (
        answer1.lower() == "to manage concurrent tasks and wait for their completion" and
        answer2.lower() == "it handles HTTP requests by providing methods like http.Get to send requests and receive responses" and
        answer3.lower() == "it converts JSON data from a byte slice into a Go data structure" and
        answer4.lower() == "it reads the entire response body into memory, returning it as a byte slice"
    ):
        stdscr.addstr(34, 0, "Correct! You've successfully completed the challenge.")
        stdscr.addstr(35, 0, "Here is the final flag = _1nV1s1b13_5678}")
    else:
        stdscr.addstr(34, 0, "Incorrect answers. Try again.")

