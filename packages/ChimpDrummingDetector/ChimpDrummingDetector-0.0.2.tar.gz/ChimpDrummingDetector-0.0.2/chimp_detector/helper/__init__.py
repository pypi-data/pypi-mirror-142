
from chimp_detector.helper import audio_processor, featuremap_processor, predictor


def detect_chimpz(path):

   signal = audio_processor.read_in_audio(path)
   featuremap, timepoints_of_fmap_frames_in_s = audio_processor.extract_spectrogram(signal)
   featuremap = featuremap_processor.denoise_featuremap(featuremap)
   featuremap = featuremap_processor.standartize_featuremap(featuremap)
   featuremap = featuremap_processor.segment_featuremap(featuremap)
   timepoints_of_fmap_frames_in_s = featuremap_processor.segment_featuremap(timepoints_of_fmap_frames_in_s)
   predictions_probs, predictions_binary = predictor.predict_featuremap(featuremap)

   output_dataframe = predictor.produce_final_output_csv(predictions_probs, predictions_binary, timepoints_of_fmap_frames_in_s)

   return (output_dataframe)
