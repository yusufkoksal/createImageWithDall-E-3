import requests
import os
import openai
# OpenAI API key
openai.api_key = 'sk-proj-Konk3sqN9vRnQxXw9iTpT3BlbkFJDd1qfZGXfXiRnrbVdraG' #yusufkoksal ın openAI apisi kendi api keyinizi openAI üzerinden oluşturarak bu kodu kullanabilirsiniz

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

# Create and download 100 images with a phone number


# Create and download 900 images without a phone number
no_phone_number_prompt = (
    "I want to create a valid profile picture for a dating app. It must be realistic. The photo must contain one person."
)

for i in range(100,1000):
    image_url = create_image_with_prompt(no_phone_number_prompt)
    filename = os.path.join(output_dir, f"{i + 1}_false.jpg")
    download_image(image_url, filename)
    print(f"Downloaded {filename}")
