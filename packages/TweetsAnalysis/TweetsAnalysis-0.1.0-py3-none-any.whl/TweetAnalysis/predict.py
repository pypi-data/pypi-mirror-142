import pandas as pd

import joblib
from tensorflow.keras.models import load_model

from TweetAnalysis.config.core import config
from TweetAnalysis.processing import data_management as dm
from TweetAnalysis.processing import preprocessing as pp

print("pipeline loading...")
# pipe = dm.load_pipeline_keras()


tokenizer = joblib.load(config.app.MODELS_PATH + config.app.TOKENIZER_NAME)
model = load_model(config.app.MODELS_PATH + config.app.MODEL_NAME)

def get_label(proba):

    if proba <= config.model.NEUTRAL_MIN:
        return config.model.NEGATIVE_INDEX
    elif proba >= config.model.NEUTRAL_MAX:
        return config.model.POSITIVE_INDEX
    else:
        return config.model.NEUTRAL_INDEX


def make_bulk_prediction(X: pd.Series, clean=False) -> list:
    """Make multiple predictions using the saved model pipeline"""

    if clean:
        X = pp.CleanText().transform(X)

    print("predicting...")
    # predictions = pipe.predict(X)

    X = tokenizer.transform(X)
    X = pp.PaddingText().transform(X)
    predictions = model.predict(X)

    preds = [(config.model.CLASSES[int(get_label(p))], p[0]) for p in predictions]

    print('prediction done!!!')
    return preds


if __name__ == '__main__':
    x = dm.read_data()[:10]
    x = x['text']
    z = make_bulk_prediction(x, True)
    print(z)
