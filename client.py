# import openai

# # Set your OpenAI API key
# openai.api_key = "sk-proj-BcxuUYoIILcY7Ika9O0mT3BlbkFJQdrSOyj7ed1JNXTlYHj4"

# # Create a chat completion request
# response = openai.ChatCompletion.create(
#     model="gpt-4",  # Replace with the correct model name
#     messages=[
#         {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud."},
#         {"role": "user", "content": "What is coding?"}
#     ]
# )

# # Print the response
# print(response['choices'][0]['message']['content'])