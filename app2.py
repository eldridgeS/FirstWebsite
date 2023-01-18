import random
import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    # Get a random image file from the "static" folder
    img_file = random.choice(os.listdir('static'))
    # Get a random audio file from the "audio" folder
    audio_file = random.choice(os.listdir('audio'))
    return render_template('index.html', img_file=img_file, audio_file=audio_file)

@app.route('/audio/<path:filename>')
def audio(filename):
    return send_from_directory('audio', filename)

if __name__ == '__main__':
    app.run()
