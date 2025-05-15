from datetime import datetime

name = input("What's your name? ")
hour = datetime.now().hour

if hour < 12:
    greeting = "Good morning"
elif hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

print(f"{greeting}, {name}! Let's dive into Python AI.")