from flask import Flask, render_template, request
from pysentimiento import create_analyzer

app = Flask(__name__)

sentiment_analyzer = create_analyzer(
    task='sentiment',
    lang='es',
    model_name='pysentimiento/robertuito-sentiment-analysis'
)

emotion_analyzer = create_analyzer(
    task='emotion',
    lang='es',
    model_name='pysentimiento/robertuito-emotion-analysis'
)

hate_analyzer = create_analyzer(
    task='hate_speech',
    lang='es',
    model_name='pysentimiento/robertuito-hate-speech'
)

irony_analyzer = create_analyzer(
    task='irony',
    lang='es',
    model_name='pysentimiento/robertuito-irony'
)


@app.route('/', methods=['GET', 'POST'])
def analyze_comment():
    sentiment_result = None
    emotion_result = None
    hate_result = None
    irony_result = None

    if request.method == 'POST':
        comment = request.form['comment']
        sentiment_result = sentiment_analyzer.predict(comment)
        emotion_result = emotion_analyzer.predict(comment)
        hate_result = hate_analyzer.predict(comment)
        irony_result = irony_analyzer.predict(comment)
        print(f"Comment: {comment}")
        print(f"Sentiment: {sentiment_result}")
        print(f"Emotion: {emotion_result}")
        print(f"Hate: {hate_result}")
        print(f"Irony: {irony_result}")

    return render_template('index.html', sentiment_result=sentiment_result, emotion_result=emotion_result,
                           hate_result=hate_result, irony_result=irony_result)


if __name__ == '__main__':
    app.run(debug=True)
