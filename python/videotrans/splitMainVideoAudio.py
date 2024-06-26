from moviepy.editor import VideoFileClip

def split_video(video_path, output_folder="split_videos"):
  """
  Splits a video into one-minute segments and saves them in a separate folder.

  Args:
    video_path: Path to the input video file.
    output_folder: Name of the folder to save the split videos (default: "split_videos").
  """

  # Load the video
  video = VideoFileClip(video_path)

  # Calculate the number of one-minute segments
  num_segments = int(video.duration) // 60 + (int(video.duration) % 60 != 0)

  # Split the video into segments
  for i in range(num_segments):
    start_time = i * 60
    end_time = min((i + 1) * 60, video.duration)
    segment = video.subclip(start_time, end_time)

    # Save each segment
    segment.write_videofile(f"{output_folder}/segment_{i+1}.mp4", codec="libx264", audio_codec="aac")

  print(f"Video split into {num_segments} segments.")

# Example usage:
split_video("LLM-AndreiKarpathy\Intro_to_Large_Language_Models.mp4","LLM-AndreiKarpathy\split_videos")


