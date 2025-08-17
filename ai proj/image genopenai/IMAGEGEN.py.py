import openai

# Read API key with strip() to remove any whitespace
openai.api_key = open("API_KEY", "r").read().strip()

response = openai.Image.create(
    prompt="a white cat with a red bow tie",  # Remove space around =
    n=1,                                      # Remove space around =
    size="1024x1024"                         # Remove space around =
)

image_url = response['data'][0]['url']

print(image_url)