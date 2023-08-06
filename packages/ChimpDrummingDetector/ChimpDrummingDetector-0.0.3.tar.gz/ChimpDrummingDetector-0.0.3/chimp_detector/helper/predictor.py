from chimp_detector.helper.config import Hyperparams

import pkg_resources
from tensorflow import keras
import pandas as pd
import os

def predict_featuremap(featuremap):

    path_to_model = pkg_resources.resource_filename(__name__, os.path.join(Hyperparams.MODEL_FOLDER, Hyperparams.MODEL_NAME))

    model = keras.models.load_model(path_to_model)
    predictions_probs = model.predict(featuremap).flatten()
    prdicitions_binary = predictions_probs > 0.5

    return predictions_probs,prdicitions_binary

def produce_final_output_csv(predictions_probs,predictions_binary,timepoints_of_fmap_frames_in_s ):

    timepoints_of_fmap_frames_in_s = timepoints_of_fmap_frames_in_s.flatten()

    df =  pd.DataFrame({"timepoint_in_seconds": timepoints_of_fmap_frames_in_s, "drumming_probability": predictions_probs,
                                   "drumming_binarized": predictions_binary})
    df = df.drop_duplicates(subset="timepoint_in_seconds", ignore_index=True)
    df["drumming_probability"] = df["drumming_probability"].astype(float).round(3)

    return df