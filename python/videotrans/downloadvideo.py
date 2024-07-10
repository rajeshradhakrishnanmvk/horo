from pytube import YouTube

def download_video(url):
    YouTube(url).streams.first().download()

# Example usage
download_video('https://www.youtube.com/watch?v=<input>')