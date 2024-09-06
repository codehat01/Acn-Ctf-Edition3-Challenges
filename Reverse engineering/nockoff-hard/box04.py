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
    stdscr.addstr("You must analyze the Go code and answer the following simple questions:\n\n")
    stdscr.addstr("Press any key to continue...")
    stdscr.refresh()
    stdscr.getch()

    display_go_program(stdscr)
    stdscr.clear()
    stdscr.addstr(20, 0, "Go program executed successfully. Now, answer the following:")

    # Simple Question 1
    stdscr.addstr(22, 0, "1. Which package is used for concurrency?")
    stdscr.addstr(23, 0, "Answer: ")
    curses.echo()
    answer1 = stdscr.getstr(23, 8).decode('utf-8').strip()
    curses.noecho()

    # Simple Question 2
    stdscr.addstr(25, 0, "2. Which package is used for making HTTP requests?")
    stdscr.addstr(26, 0, "Answer: ")
    curses.echo()
    answer2 = stdscr.getstr(26, 8).decode('utf-8').strip()
    curses.noecho()

    # Simple Question 3
    stdscr.addstr(28, 0, "3. Which package is used to parse JSON?")
    stdscr.addstr(29, 0, "Answer: ")
    curses.echo()
    answer3 = stdscr.getstr(29, 8).decode('utf-8').strip()
    curses.noecho()

    # Simple Question 4
    stdscr.addstr(31, 0, "4. Which function reads the entire response body?")
    stdscr.addstr(32, 0, "Answer: ")
    curses.echo()
    answer4 = stdscr.getstr(32, 8).decode('utf-8').strip()
    curses.noecho()

    if (
        answer1.lower() == "sync" and
        answer2.lower() == "http" and
        answer3.lower() == "json" and
        answer4.lower() == "readall"
    ):
        stdscr.addstr(34, 0, "Correct! You've successfully completed the challenge.")
        stdscr.addstr(35, 0, "Here is the final flag = _1nV1s1b13_5678}")
        stdscr.addstr(36, 0, "Press Enter to exit.")
        stdscr.refresh()
        while True:
            key = stdscr.getch()
            if key == ord('\n') or key == 10:  # Handling Enter key
                return True
    else:
        stdscr.addstr(34, 0, "Incorrect answers. Try again.")
        stdscr.addstr(35, 0, "Press Enter to exit.")
        stdscr.refresh()
        while True:
            key = stdscr.getch()
            if key == ord('\n') or key == 10:  # Handling Enter key
                return False

