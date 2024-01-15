import openai
import pyttsx3
import speech_recognition as sr

openai.api_key = "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"
engine = pyttsx3.init()
question = 'input_file.txt'
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening: ")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said: ", text)

            with open(question, 'a') as ques:
                ques.write(f'{text}\n')
        except sr.UnknownValueError:
            pass

def answer(prompt):
        
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "Your name is Sky. You are helpful home assistant. You are to answer to any instruction as yes boss and do what was said. You assist with home related issues only."},
            {"role": "user", "content": "I am your boss and you do as I say"},
            {"role": "system", "content": "Okay boss, I will do as you say."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

while True:
    listen()
    with open(question, 'r') as ques:
        lines = ques.readlines()
        ques = lines[-1]
    
    if ques:
        ans = answer(ques)
        print(f"Bot: {ans}")
        engine.say(ans)
        engine.runAndWait()
    else:
        pass