import openai
import requests
import os

# OpenAI API key
openai.api_key = 'sk-proj-Konk3sqN9vRnQxXw9iTpT3BlbkFJDd1qfZGXfXiRnrbVdraG'

def create_image_with_prompt(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024",
        model="dall-e-3"    
    )
    return response['data'][0]['url']

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)

# Check and create the directory if it doesn't exist
output_dir = "images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create and download one image with a phone number
prompt = ("I want create profile picture for a dating app.But it should write exactly '545 323 1234'.Photo must contain one person .It must be realistic.")    
image_url = create_image_with_prompt(prompt)
filename = os.path.join(output_dir, "21_true.jpg")
download_image(image_url, filename)
print(f"Downloaded {filename}")

# Create and download one image without a phone number
prompt = "I want to create a valid profile picture for a dating app. It must be realistic.Photo must contain one person."
image_url = create_image_with_prompt(prompt)
filename = os.path.join(output_dir, "22_false.jpg")
download_image(image_url, filename)
print(f"Downloaded {filename}")
