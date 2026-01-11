"""
This is the starting file of the server.
It serves API requests with appropriate response.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    Takes input text from user, sends it to emotion detector,
    then returns response on the web page.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Handle empty text case
    if not text_to_analyze:
        return render_template('index.html', error="Please enter a text to analyze.")

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return render_template('index.html', error="Invalid text! Please try again!")

    return render_template(
        'index.html',
        text=text_to_analyze,
        anger=response['anger'],
        disgust=response['disgust'],
        fear=response['fear'],
        joy=response['joy'],
        sadness=response['sadness'],
        dominant_emotion=response['dominant_emotion']
    )

@app.route("/")
def render_index_page():
    """
    Renders the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
