import pyttsx3
import wikipedia

abeba = pyttsx3.init()
voices=abeba.getProperty('voices')
abeba.setProperty('voice', voices[1].id)
abeba.setProperty('rate',175)

In=input("search wikipedia/google: ")
result = wikipedia.summary(In , sentences = 4)
abeba.say("according to wikipedia")
print(result)
abeba.say(result)
abeba.say("thanks for using buddy")
abeba.runAndWait()