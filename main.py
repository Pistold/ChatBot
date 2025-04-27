import openai

#import key
with open('GPTkey', 'r') as file:
    OpenAiKey = file.read().strip()

openai.api_key = OpenAiKey

#send and recieve from API
def chat_with_gpt(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=messages       #send full conversation history
    )
    
    #return reply
    return response['choices'][0]['message']['content'].strip()

if __name__ == "__main__":
    #start the conversation with a "system" message (sets chatbot behavior)
    messages = [{"role": "system", "content": "You are a helpful chatbot."}]
    
    #main loop for chatting
    while True:
        #get input
        user_input = input("You: ")
        
        #if exit clause
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        # Add the user's message to the conversation
        messages.append({"role": "user", "content": user_input})

        # Get the chatbot's response
        response = chat_with_gpt(messages)

        # Add the chatbot's reply to the conversation
        messages.append({"role": "assistant", "content": response})

        # Print the chatbot's reply
        print("Chatbot:", response)