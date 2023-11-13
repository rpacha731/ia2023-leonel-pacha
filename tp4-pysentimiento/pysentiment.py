from pysentimiento import create_analyzer
import pandas as pd

def main():

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

    dataset = pd.read_csv('dataset/reviews.csv')
    dataset_list = dataset.to_dict('records')

    # mostrar un progress bar
    for i, row in enumerate(dataset_list):
        resultSentiment = sentiment_analyzer.predict(row['comment'])
        resultEmotion = emotion_analyzer.predict(row['comment'])
        resultHate = hate_analyzer.predict(row['comment'])
        resultIrony = irony_analyzer.predict(row['comment'])
        for key in resultSentiment.probas:
            dataset_list[i]['sentiment_' + key] = resultSentiment.probas[key]
        for key in resultEmotion.probas:
            dataset_list[i]['emotion_' + key] = resultEmotion.probas[key]
        for key in resultHate.probas:
            dataset_list[i]['hate_' + key] = resultHate.probas[key]
        for key in resultIrony.probas:
            dataset_list[i]['irony_' + key] = resultIrony.probas[key]
        print(f"Processed {i+1} of {len(dataset_list)}")

    dataset = pd.DataFrame(dataset_list)
    dataset.to_csv('dataset/reviews_sentiment.csv')


if __name__ == "__main__":
    main()
