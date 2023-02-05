import csv
import openai
import requests
import base64
import json

# Load OpenAI API key
openai.api_key = "openai API"

# Load the CSV file and extract keywords
with open('keywords.csv', 'r') as file:
    reader = csv.reader(file)
    keywords = []
    for row in reader:
        keywords.append(row[0])

# Use OpenAI to generate the buying guide
def generate_buying_guide(keywords):
    prompt = f"Please generate a buying guide for {keywords} with sections (Intro, Features, Why you should buy this, Pros, Cons, and Conclusion)"
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

buying_guide = generate_buying_guide(keywords)
# print(buying_guide)

# Retrieve the featured image from Pixabay API
def get_featured_image(keyword):
    API_KEY = "pixaba"
    URL = f"https://pixabay.com/api/?key={API_KEY}&q={keyword}&image_type=photo&pretty=true"
    response = requests.get(URL)
    data = response.json()
    if data['totalHits'] > 0:
        return data['hits'][0]['webformatURL']
    else:
        return None

featured_image = get_featured_image(keywords[0])

# print(featured_image)

# Retrieve a related video from YouTube API
youtube_api_key = "youtube API"

def find_video(keyword):
    video_response = requests.get(f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={keyword}&type=video&key={youtube_api_key}")

    if video_response.status_code != 200:
        print("Request failed with status code " + str(video_response.status_code))
    else:
        video_data = video_response.json()
        video_id = video_data['items'][0]['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        print("Video URL for " + keyword + ": " + video_url)

for keyword in keywords:
    find_video(keyword)



# Define the endpoint for the WordPress RestAPI

wordpress_url = "http://wp.local/wp-json/wp/v2"
user = "admin"
password = "6Bgz WHk9 ijPz Fanv JSWO Hu5f"

def post_to_wordpress(title, content, image_url, video_url):
    auth = base64.b64encode(f"{user}:{password}".encode()).decode()

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic " + auth
    }

    data = {
        "title": title,
        "content": content,
        "featured_media": image_url,
        "meta": {
            "video_url": video_url
        }
    }

    post_response = requests.post(wordpress_url, headers=headers, data=json.dumps(data), verify=False)
    print(post_response.json())

for keyword in keywords:
    featured_image(keyword)
    find_video(keyword)
    # print(buying_guide)
    # print(featured_image)
    # print(find_video)

    post_to_wordpress(title=keyword + " buying guide", content=buying_guide, image_url=featured_image, video_url=find_video)