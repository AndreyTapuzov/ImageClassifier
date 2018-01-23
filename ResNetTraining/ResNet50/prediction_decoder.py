import json
import warnings
import keras
from keras import backend as K

CLASS_INDEX = None
CLASS_INDEX_PATH = 'ftp://..\\Model\\PredictionDecoderData\\class_indexes.json'
LABELS = {"0": ["acerolas"],
          "1": ["apples"],
          "2": ["apricots"],
          "3": ["avocados"],
          "4": ["bananas"],
          "5": ["blackberries"],
          "6": [ "blueberries"],
          "7": [ "cantaloupes"],
          "8": [ "cherries"],
          "9": [ "coconuts"],
          "10": ["figs"],
          "11": ["grapefruits"],
          "12": ["grapes"],
          "13": ["guava"],
          "14": ["kiwifruit"],
          "15": ["lemons"],
          "16": ["limes"],
          "17": ["mangos"],
          "18": ["olives"],
          "19": ["oranges"],
          "20": ["passionfruit"],
          "21": ["peaches"],
          "22": ["pears"],
          "23": ["pineapples"],
          "24": ["plums"],
          "25": ["pomegranates"],
          "26": ["raspberries"],
          "27": ["strawberries"],
          "28": ["tomatoes"],
          "29": ["watermelons"]}


def custom_decode_predictions(preds, top=5):
    """Decodes the prediction of an ImageNet model.

    # Arguments
        preds: Numpy tensor encoding a batch of predictions.
        top: integer, how many top-guesses to return.

    # Returns
        A list of lists of top class prediction tuples
        `(class_name, class_description, score)`.
        One list of tuples per sample in batch input.

    # Raises
        ValueError: in case of invalid shape of the `pred` array
            (must be 2D).
    """
    global CLASS_INDEX
    if len(preds.shape) != 2 or preds.shape[1] != 30:
        raise ValueError('`decode_predictions` expects '
                         'a batch of predictions '
                         '(i.e. a 2D array of shape (samples, 30)). '
                         'Found array with shape: ' + str(preds.shape))
    if CLASS_INDEX is None:
        #fpath = keras.utils.get_file('class_indexes.json',
        #                  CLASS_INDEX_PATH)
        CLASS_INDEX = LABELS#json.load(open(fpath))
    results = []
    for pred in preds:
        top_indices = pred.argsort()[-top:][::-1]
        result = [tuple(CLASS_INDEX[str(i)]) + (pred[i],) for i in top_indices]
        result.sort(key=lambda x: x[1], reverse=True)
        results.append(result)
    return results