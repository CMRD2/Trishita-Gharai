import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source, duration=5)
	print('Speak')
	while True:#creating a loop
		audio=r.listen(source)#listening
		print('you said-' + r.recognize_google(audio))#print op