from chimp_detector.helper.config import Hyperparams

import librosa as lb
import numpy as np

def extract_spectrogram(signal):


    win_length_in_samples =  int(Hyperparams.SAMPLING_RATE * Hyperparams.WIN_LENGTH_MS * 0.001)
    hop_length_in_samples = int(win_length_in_samples * Hyperparams.STFT_WIN_OVERLAP_PERCENT)

    spec = lb.stft(y=signal, n_fft=Hyperparams.STFT_NFFT, win_length=win_length_in_samples,
                             hop_length=hop_length_in_samples, window="hanning",
                             center=True)
    spec = np.abs(spec)
    spec = lb.feature.melspectrogram(S=spec, sr=Hyperparams.SAMPLING_RATE, n_mels=Hyperparams.N_MELS,norm="slaney")
    spec = np.log(np.maximum(spec, Hyperparams.SPEC_CLIP_VALUE))
    spec = np.transpose(spec)

    hopsize_between_frames_in_s = Hyperparams.WIN_LENGTH_MS * 0.001 * Hyperparams.STFT_WIN_OVERLAP_PERCENT
    timepoints_of_fmap_frames_in_s = np.asarray([i * hopsize_between_frames_in_s for i in range(spec.shape[0])])


    return spec, timepoints_of_fmap_frames_in_s

def read_in_audio(path):
    y, sr = lb.load(path=path, sr=Hyperparams.SAMPLING_RATE, mono=True, duration=None)
    y = normalize_signal(y)
    y = limit_signal(y)
    return y

def normalize_signal(y):
    return y/np.max(abs(y))

def limit_signal(y, percentile = 99.9999):
    threshold = np.percentile(np.abs(y), percentile)
    y[y > threshold] = threshold
    y[y < -threshold] = -threshold
    y = normalize_signal(y)
    return y


