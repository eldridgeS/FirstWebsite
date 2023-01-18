import random
import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    # Get a random image file from the "static" folder
    base_dir = os.path.abspath(os.path.dirname(__file__))
    img_file = random.choice(os.listdir(os.path.join(base_dir,'static')))
    print(base_dir)
    # Get a random audio file from the "audio" folder
    audio_file = random.choice(os.listdir(os.path.join(base_dir,'audio')))
    audio_file = random.choice(os.listdir(os.path.join(base_dir,'audio')))

    return render_template('index.html', img_file=img_file, audio_file=audio_file)

@app.route('/audio/<path:filename>')
def audio(filename):
    return send_from_directory('audio', filename)

