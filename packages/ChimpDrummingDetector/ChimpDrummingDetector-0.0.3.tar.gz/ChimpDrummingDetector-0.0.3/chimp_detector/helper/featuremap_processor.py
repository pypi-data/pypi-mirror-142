from chimp_detector.helper.config import Hyperparams

import numpy as np

def denoise_featuremap(fmap):

    fmap = frequency_removal(fmap)
    fmap = spectral_subtraction(fmap)
    return fmap


def frequency_removal(fmap):
    mask = np.zeros((80,), dtype = bool)
    mask[0:5] = True
    fmap = fmap[:,mask]
    return fmap

def spectral_subtraction(fmap):

    segment_length_in_frames = seconds_to_length_in_frames(Hyperparams.SPEC_SUBTRACTION_SEGMENT_LENGTH_IN_S)

    fmap_length = fmap.shape[0]
    start_points = np.arange(0, fmap_length, segment_length_in_frames)
    end_points = np.arange(segment_length_in_frames, fmap_length, segment_length_in_frames)

    if end_points.size == 0:
        end_points = np.asarray([fmap_length])

    if start_points.size > end_points.size:
        start_points = start_points[:-1]
        end_points[-1] = fmap_length


    for start, end in zip(start_points,end_points):
        fmap[start : end] = fmap[start: end] - np.mean(fmap[start: end],axis=0)

    return fmap


def standartize_featuremap(fmap):
    return (fmap - Hyperparams.NORMALIZATION_MEAN ) / Hyperparams.NORMALIZATION_STD

def seconds_to_length_in_frames(seconds):
    return int(np.floor(seconds /
                 (0.001 * Hyperparams.WIN_LENGTH_MS * Hyperparams.STFT_WIN_OVERLAP_PERCENT)))


def segment_featuremap(m):

    m = np.expand_dims(m, -1) if m.ndim == 1 else m

    segment_length_in_frames = seconds_to_length_in_frames(Hyperparams.FMAP_SEGMENTATION_SEG_LENGTH_IN_S)




    amount_of_timeframes_in_map = m.shape[0]

    if amount_of_timeframes_in_map == segment_length_in_frames:
        m = np.expand_dims(m, 0) if m.ndim < 3 else m
        return m

    if amount_of_timeframes_in_map < segment_length_in_frames:
        n_missing_timeframes = segment_length_in_frames - amount_of_timeframes_in_map
        zero_element_to_append = np.zeros((m.shape[-1],))
        zero_map = np.tile(zero_element_to_append, (n_missing_timeframes, 1))
        return np.concatenate((m, zero_map), axis=0)

    if amount_of_timeframes_in_map > segment_length_in_frames:

        last_possible_segment_starting_position = amount_of_timeframes_in_map - segment_length_in_frames
        frames_to_shave_off = last_possible_segment_starting_position % segment_length_in_frames

        m_sub = m[:(amount_of_timeframes_in_map - frames_to_shave_off)]
        m_sub = np.reshape(m_sub, (-1, segment_length_in_frames, m.shape[-1]))

        if frames_to_shave_off != 0:
            m_sub = np.append(m_sub, np.expand_dims(m[last_possible_segment_starting_position:], axis=0),axis=0)

        return m_sub