import openai
openai.api_key = "API-Key" 
# or use the method we defined earlier

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()


    
while True:
    chat = input("You : ")
    if chat == "bye" or chat == "Bye" or chat == "Exit" or chat == "goodbye":
        print("Ok..\nThank\'s.. ")
        break
    
    response = generate_response(chat)
    print("Bot: ",response)
        