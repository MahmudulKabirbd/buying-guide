import openai
import requests
import json
import os
import base64

openai.api_key = "openai API"

def generate_guide(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

def search_video(keyword):
    youtube_api_key = "AIzaSyCuCtYwg0AU97r64LtofI4WrKW49uJeVrQ"
    base_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": keyword,
        "type": "video",
        "key": youtube_api_key,
        "maxResults": 1,
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    video_id = data["items"][0]["id"]["videoId"]
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    return video_url

keyword = input("Enter a keyword for which you want to generate a buying guide: ")

intro = generate_guide(f"Introduction to {keyword}:")
features = generate_guide(f"Features of {keyword}:")
why_buy = generate_guide(f"Why you should buy {keyword}:")
pros = generate_guide(f"Pros of {keyword}:")
cons = generate_guide(f"Cons of {keyword}:")
conclusion = generate_guide(f"Conclusion for {keyword}:")
video_url = search_video(keyword)

# buying_guide = f"Introduction:\n{intro}\n\nFeatures:\n{features}\n\nWhy you should buy this:\n{why_buy}\n\nPros:\n{pros}\n\nCons:\n{cons}\n\nConclusion:\n{conclusion}\n\nVideo:\n{video_url}"
buying_guide = f"Introduction:\n{intro}\n\nFeatures:\n{features}\n\nWhy you should buy this:\n{why_buy}\n\nPros:\n{pros}\n\nCons:\n{cons}\n\nVideo:\n{video_url}\n\nConclusion:\n{conclusion}"
# Replace with your YouTube API Key
youtube_api_key = "AIzaSyDxaGwgsXBJqKt0qQJP8iXSIniWkeocs7M"
data = {
    "title": "Buying Guide for " + keyword,
    "content": buying_guide,### verify=False)
    "status": "publish"# Replace the URL with your WordPress site's URL
}


# Replace the credentials with your WordPress site's credentials



wp_url = "http://wp.local/wp-json/wp/v2/posts"
wp_credentials = ('admin', '6Bgz WHk9 ijPz Fanv JSWO Hu5f')
b64_credentials = base64.b64encode(bytes(':'.join(wp_credentials), 'utf-8')).decode('utf-8')
headers = {'Content-Type': 'application/json', 'Authorization': 'Basic ' + b64_credentials}


# Add the video URL to the data for the WordPress post
# data["content"] = f"{buying_guide}\n\nRelated Video:\n{video_url}"

# Make the POST request to the WordPress REST API
response = requests.post(wp_url, auth=wp_credentials, headers=headers, data=json.dumps(data), verify=False)

# Check the response status code
if response.status_code == 201:
    print("Post with video successfully created")
else:
    print("Post creation failed with status code:", response.status_code)



