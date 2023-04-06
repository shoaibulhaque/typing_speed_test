import curses
from curses import wrapper
import time
import sys

# intro_screen function
def start_game(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test !")
    stdscr.addstr("\nPress any key to continue.....")
    stdscr.refresh()
    stdscr.getkey()

def wpn_test(stdscr):
    target_text = "This is a sample test for this game!"
    current_text = []
    words_check = 0

    start_time = time.time()
    while True:
        stdscr.clear()
        display_text(stdscr, target_text, current_text, start_time, words_check)
        stdscr.refresh()


        key = stdscr.getkey()

        if ord(key) == 27:
            break


        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()

        elif len(current_text) < len(target_text):
            current_text.append(key)


def check_result(stdscr, words_check, target, start_time):
    if words_check == len(target):
        elapsed_time = time.time() - start_time
        stdscr.clear()
        stdscr.addstr(0, 0, f"Congratulations !, Time taken: {round(elapsed_time, 3)} sec", curses.color_pair(1))
        stdscr.addstr(2, 0, f"Do you want to play again ? Press 'P' or 'Q:'")
        key = stdscr.getkey()
        if key == 'P' or key == 'p':
            wpn_test(stdscr)
        else:
            sys.exit()

def display_text(stdscr, target, current,start_time,words_check = 0):
    stdscr.addstr(target)


    for i, char in enumerate(current):
        if char != target[i]:
            stdscr.addstr(0, i, char, curses.color_pair(2))
        else:
            stdscr.addstr(0, i, char, curses.color_pair(1))
            words_check += 1
            stdscr.addstr(1, 0, f"Correct Char: {words_check}")
            check_result(stdscr, words_check, target, start_time)



def main(stdscr): # stdscr --> screen name

    # Initializing colors
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)


    start_game(stdscr)
    wpn_test(stdscr)



wrapper(main)