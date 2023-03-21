from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import pyautogui
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Read the transcription from the file
with open('transcription.txt', 'r') as f:
    transcription = f.read()

# Capture the user's screen input
user_input = pyautogui.prompt('What do you want to do?')

# Generate the response using the ChatGPT model
input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
output = model.generate(input_ids, do_sample=True, max_length=1000, top_p=0.92, temperature=0.85)
response = tokenizer.decode(output[0], skip_special_tokens=True)

# Display the response to the user
pyautogui.alert(response)

# Print the response
print(response)
