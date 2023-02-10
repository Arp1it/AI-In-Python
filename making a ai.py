import openai

#get api from https://openai.com/api/
openai.api_key = "your_api_key"

while True:
    model_engine = "text-davinci-003"
    promptt = input("Enter: ")

    if promptt == 'exit' or promptt == 'quit':
        break

    completion = openai.Completion.create(engine=model_engine, prompt=promptt, max_tokens=1024, n=1, stop=None, temperature=0.5)

    responsee = completion.choices[0].text

    print(responsee)