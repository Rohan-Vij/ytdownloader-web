from flask import Flask, render_template, send_file
from pytube import YouTube, exceptions
import string
import random

app = Flask(__name__)

@app.route("/download/<id>")
def download(id):
    url = f'https://youtube.com/watch?v={id}'
    try:
        video_object = YouTube(url)  
    except exceptions.RegexMatchError:
        return "Invalid URL. After /download/, add the ID of the video. For example:\n roxenoz.xyz/download/ATOX9uMKtC4"

    if video_object.length > 1800:
        return "That video is too long! Your video can be up to 30 minutes long."   

    rand_name = ''.join(random.choice(string.ascii_letters) for i in range(15))
    video_object.streams.filter(progressive=True).order_by('resolution').desc().first().download(output_path="downloaded", filename=rand_name)
    return send_file(f"downloaded\\{rand_name}.mp4")
        

if __name__ == "__main__":
    app.run(debug=True)