import openai
from gtts import gTTS
import os

# Set your OpenAI API key here
api_key = "YOUR_OPENAI_API_KEY"

# Initialize the OpenAI API client
openai.api_key = api_key

def chat_with_jarvis(input_text):
    try:
        # Send the user's input to GPT-3
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=input_text,
            max_tokens=50,  # Adjust as needed
            temperature=0.7,  # Adjust for creativity vs. coherence
        )

        # Get Jarvis's response from GPT-3
        jarvis_response = response.choices[0].text.strip()

        # Convert Jarvis's response to speech
        tts = gTTS(text=jarvis_response, lang='en')
        tts.save("jarvis_response.mp3")

        # Play the response
        os.system("mpg321 jarvis_response.mp3")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    print("Hello, I'm Jarvis. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        chat_with_jarvis(user_input)
