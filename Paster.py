import time
import keyboard
import clipboard
import random

def human_like_typing(text, wpm=200):
    words = text.split()
    words_per_minute = wpm
    average_delay = 60.0 / words_per_minute

    for word in words:
        keyboard.write(word)
        # After typing the word, add space
        keyboard.write(' ')
        # Now, we introduce a delay. We subtract the time taken to type the word (which is negligible) 
        # and then add a random delay ranging between 1 to 2 seconds.
        delay = average_delay + random.uniform(0.1, 0.3)
        time.sleep(delay)

if __name__ == "__main__":
    text = clipboard.paste()
    human_like_typing(text)
