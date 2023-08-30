import openai

# Your OpenAI API key and subject variable
api_key = "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"
subject = "Similarities between ancient mythology stories and stories of aliens"

# Initialize the OpenAI API client
openai.api_key = api_key

# Define your prompt and other parameters
prompt = f"Create a 1-minute documentary script about {subject}."
max_tokens = 500  # You may need to adjust this based on how long you want the script to be

# Make an API call to generate the script
response = openai.Completion.create(
    engine="text-davinci-002",  # You can use other engines too
    prompt=prompt,
    max_tokens=max_tokens
)

# Extract and print the generated script
script = response.choices[0].text.strip()
print("Generated Script:")
print(script)
