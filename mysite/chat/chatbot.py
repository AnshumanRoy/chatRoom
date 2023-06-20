from langchain import PromptTemplate
import openai

openai.api_key = "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"

template = """
Answer questions about the product only on basis of the information provided here.
==================================================================================
The name of the product is {name}.
It has been reviewed {n_reviews} times.
It has a rating of {rating}.
It costs {price} USD.
It has the following features : {desc}.
If its in stock or not : {status}.
Here's what customers have to say about the product : {reviews}.
==================================================================================

"""

starting_prompt = PromptTemplate(
        input_variables = ['name', 'n_reviews', 'rating', 'price', 'desc', 'status', 'reviews'],
        template = template,
        )


def reply(input, messages):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages, temperature = 0.5,
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

class Chatbot():

    def __init__(self):
        self.messages = [
            {
                "role" : "system", 
                "content" : "You are a kind and helpful assistant."
            }
        ]
    
    def reply(self, input):
        if input:
            self.messages.append({"role" : "user", "content" : "input"})
            chat = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo", messages = self.messages, temperature = 0.5,
                )
            reply = chat.choices[0].message.content
            self.messages.append({"role": "assistant", "content":reply})
            return reply
            
