import openai

#import key
with open('GPTkey', 'r') as file:
    OpenAiKey = file.read().strip()

openai.api_key = OpenAiKey

#send and recieve from API
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5",
        messages = [{"role": "user", "content": prompt}]
        )
    
    #return reply
    return response.choices[0].message.context.strip()

#
if __name__=="__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        
        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)