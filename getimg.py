import praw
import requests
import os

if os.path.isdir("cats") == False:
    os.mkdir("cats")
os.chdir("cats")

# Create a read-only Reddit instance
reddit = praw.Reddit(
    #insert youre client id
    client_id="YOURE CLIENT ID",
    #instert youre client secret
    client_secret="YOURE CLIENT SECRET",
    user_agent="redditbot"
)

# Function to download an image from a Reddit post
def download_image(submission_url, save_path):
    response = requests.get(submission_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded to {save_path}")
    else:
        print("Failed to download the image.")

# Function to extract images from a gallery post
def download_gallery_images(submission, count, limit):
    media_metadata = submission.media_metadata
    if media_metadata:
        for media_id, media_info in media_metadata.items():
            if count > limit:
                return count
            image_url = media_info['s']['u']
            download_image(image_url, f"cutecat{count}.jpg")
            count += 1
    return count

# Function to get image posts from the subreddit and download them
def get_titles_and_images(subreddit_name, limit):
    count = 1
    subreddit = reddit.subreddit(subreddit_name)
    
    for submission in subreddit.hot(limit=limit*2):  # Fetch more posts than needed to ensure enough images
        if count > limit:
            break
        
        if submission.url.endswith(('jpg', 'jpeg', 'png', 'gif')) or submission.url.startswith('https://i.redd.it/'):
            if count > limit:
                break
            download_image(submission.url, f"cutecat{count}.jpg")
            count += 1
        elif hasattr(submission, 'media_metadata') and submission.media_metadata:
            count = download_gallery_images(submission, count, limit)
        
        if count > limit:
            break


