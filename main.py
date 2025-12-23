from image_stego import encode_image, decode_image
from audio_stego import encode_audio, decode_audio
from video_stego import encode_video, decode_video

key = "securepassworddd"
message = input("enter the message")

# Image
encode_image("cover.png", message, key, "cover.png")
print("Image Decoded:", decode_image("cover.png", key))


# Audio
encode_audio("cover.wav", message, key, "cover.wav")
print("Audio Decoded:", decode_audio("cover.wav", key))



# Video
encode_video("cover.avi", message, key, "cover1.mp4")
print("Video Decoded: ",message)