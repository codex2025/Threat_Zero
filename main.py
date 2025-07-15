import pyttsx3

# Initialize the Text-to-Speech engine
engine = pyttsx3.init()

# Set speaking rate (default: 200)
engine.setProperty('rate', 150)

# Set voice (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Try [1] for female on some systems

# Get user input
text = input("Enter text to speech: ")

# Convert text to speech
engine.say(text)
engine.runAndWait()
