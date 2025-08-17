import openai

openai.api_key = "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"  # Replace with your actual API key

try:
    models = openai.models.list()  # NEW way to list models in openai>=1.0.0
    print([model.id for model in models])
except openai.OpenAIError as e:  # Correct error handling for new OpenAI API
    print(f"Error: {e}")

