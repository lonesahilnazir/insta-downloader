import requests

def download_instagram_reel(video_url):
    # API endpoint and parameters
    url = "https://social-media-video-downloader.p.rapidapi.com/smvd/get/all"
    params = {
        "url": video_url,
        "filename": "download"
    }

    # API headers
    headers = {
        "X-RapidAPI-Key": "824dddee65msh76dbe040b14bfe4p12ab6ajsnc6532155d4f8",
        "X-RapidAPI-Host": "social-media-video-downloader.p.rapidapi.com"
    }

    try:
        # Making GET request to the API
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Extracting download link from API response
        video_data = response.json()
        video_link = video_data["links"][0]["link"]  # Assuming first link is the download link

        # Downloading the video
        video_response = requests.get(video_link)
        with open("instagram_reel.mp4", "wb") as f:
            f.write(video_response.content)

        print("Instagram reel downloaded successfully.")
    except Exception as e:
        print(f"Error downloading Instagram reel: {e}")

# Example usage
video_urls = [
    "https://www.instagram.com/reel/C3O4O5-xVvF/?utm_source=ig_web_copy_link",
]

for video_url in video_urls:
    download_instagram_reel(video_url) 