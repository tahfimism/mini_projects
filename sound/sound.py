import pyttsx3
engine = pyttsx3.init()


engine.setProperty('rate', 200)  # speed of sound

engine.setProperty('volume',1.0) # (min=0 and max=1)


voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. o for male



engine.say(word)
engine.runAndWait()

 