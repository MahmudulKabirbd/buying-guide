import openai
import requests
import json

openai.api_key = "open ai key"

def generate_guide(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

keyword = input("Enter a keyword for which you want to generate a buying guide: ")

intro = generate_guide(f"Introduction to {keyword}:")
features = generate_guide(f"Features of {keyword}:")
why_buy = generate_guide(f"Why you should buy {keyword}:")
pros = generate_guide(f"Pros of {keyword}:")
cons = generate_guide(f"Cons of {keyword}:")
conclusion = generate_guide(f"Conclusion for {keyword}:")

buying_guide = f"Introduction:\n{intro}\n\nFeatures:\n{features}\n\nWhy you should buy this:\n{why_buy}\n\nPros:\n{pros}\n\nCons:\n{cons}\n\nConclusion:\n{conclusion}"
# Replace with your YouTube API Key
youtube_api_key = "YOUR_API_KEY"


### verify=False)
# Replace the URL with your WordPress site's URL
wp_url = "wordpress url"

# Replace the credentials with your WordPress site's credentials
wp_credentials = ('wordpress username', 'wordpress password')

headers = {
    'Content-Type': 'application/json'
}

# Prepare the data for the request
data = {
    'title': keyword + ' buying guide',
    'content': buying_guide,
    'status': 'publish'
}

# Make the POST request to the WordPress REST API
response = requests.post(wp_url, auth=wp_credentials, headers=headers, data=json.dumps(data), verify=False)

# Check the response status code
if response.status_code == 201:
    print("Post successfully created")
else:
    print("Post creation failed with status code:", response.status_code)