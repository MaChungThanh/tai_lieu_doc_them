import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm Listening...")
		audio = robot_ear.listen(mic,timeout=3,phrase_time_limit=3)

	print("Robot: ...")

	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = ""

	print("You: " + you)

	if you == "":
		robot_brain = "i can't hear you try again"
	elif "your name" in you:
		robot_brain = "my name is Alex"
	elif "how are you" in you:
		robot_brain = "i'm fine thank you"
	elif "favorite food" in you:
		robot_brain = "rice and egg"
	elif "i from" in you:
		robot_brain = "VietNam"
	elif "hello" in you:
	   robot_brain = "hello Thanh"
	elif "my lover" in you:
		robot_brain = "nobody"
	elif "football club" in you:
		robot_brain = "Arsenal" 
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "bye" in you:
		robot_brain = "Goodbye see you again"  
		print("Robot: " + robot_brain)   
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else:
		robot_brain = "i'm fine thank you and you"

	print("Robot: " + robot_brain)   
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()