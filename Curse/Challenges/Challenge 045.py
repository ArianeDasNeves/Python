#Write a program that displays a countdown on the screen for a fireworks display, ranging from 10 to 0, with a 1-second pause between each number.
import time
for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
time.sleep(1)
import emoji
print(emoji.emojize(':fireworks:'*10))
