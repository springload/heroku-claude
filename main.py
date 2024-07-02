import anthropic

# Initialize the Anthropic client
client = anthropic.Anthropic()

try:
    # Create a message using the Anthropic API
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0,
        system="You are a world-class poet. Respond only with short poems.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Why is the ocean salty?"
                    }
                ]
            }
        ]
    )

    # Print the content of the message
    print(message.content)

except anthropic.BadRequestError as e:
    # Handle insufficient credits error
    print(f"Error: {e.message}")
    print("Error: Insufficient credits to access the Claude API. Please go to Plans & Billing to upgrade or purchase credits.")
