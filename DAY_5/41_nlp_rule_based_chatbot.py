# 41 Simple NLP chatbot
import re
answers={"hello":"Hello!","name":"I am an AI lab chatbot.","help":"Ask me about AI or Python.","bye":"Goodbye!"}
while True:
 words=re.findall(r"[a-z]+",input("You: ").lower())
 key=next((w for w in words if w in answers),None)
 print("Bot:",answers.get(key,"Sorry, I did not understand."))
 if key=="bye":break