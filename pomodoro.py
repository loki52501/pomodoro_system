import pymsgbox
import time
res=pymsgbox.confirm("Do you want to start a new Pomodoro session?", "Pomodoro Timer")

if res == "OK":
    num_session=int(pymsgbox.prompt("Enter no of focus session:", "Pomodoro Timer"))
    focus_time=int(pymsgbox.prompt("Enter focus time in minutes:", "Pomodoro Timer"))
    break_time=int(pymsgbox.prompt("Enter break time in minutes:", "Pomodoro Timer"))
    long_break=int(pymsgbox.prompt("Enter long break time in minutes:", "Pomodoro Timer"))
    ress=pymsgbox.confirm(f"You have set {num_session} focus sessions with {break_time} minutes break and {long_break} minutes long break. Do you want to start?", "Pomodoro Timer")
    co=num_session
    while co>0:
        pymsgbox.alert("Focus session started. Stay focused!", "Pomodoro Timer")
        time.sleep(focus_time*60)  # Simulate focus time
        co-=1
        pymsgbox.alert("Focus session ended. Time for a break!", "Pomodoro Timer")
        time.sleep(break_time*60)  # Simulate break time
        if co % 4 == 0 and co != 0:
            pymsgbox.alert("Time for a long break!", "Pomodoro Timer")
            time.sleep(long_break*60)  # Simulate long break time
    pymsgbox.alert("All focus sessions completed. Great job!", "Pomodoro Timer")

print(ress)
 