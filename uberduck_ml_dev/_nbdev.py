# AUTOGENERATED BY NBDEV! DO NOT EDIT!

__all__ = ["index", "modules", "custom_doc_links", "git_url"]

index = {"insert_speaker": "data.cache.ipynb",
         "ensure_speaker_table": "data.cache.ipynb",
         "ensure_filelist_in_cache": "data.cache.ipynb",
         "CACHE_LOCATION": "exec.select_speakers.ipynb",
         "word_frequencies": "data.statistics.ipynb",
         "create_wordcloud": "data.statistics.ipynb",
         "count_frequency": "data.statistics.ipynb",
         "pace_character": "data.statistics.ipynb",
         "pace_phoneme": "data.statistics.ipynb",
         "get_sample_format": "data.statistics.ipynb",
         "AbsoluteMetrics": "data.statistics.ipynb",
         "TextMelDataset": "data_loader.ipynb",
         "TextMelCollate": "data_loader.ipynb",
         "TextAudioSpeakerLoader": "data_loader.ipynb",
         "TextAudioSpeakerCollate": "data_loader.ipynb",
         "DistributedBucketSampler": "data_loader.ipynb",
         "get_summary_statistics": "exec.dataset_statistics.ipynb",
         "calculate_statistics": "exec.dataset_statistics.ipynb",
         "generate_markdown": "exec.dataset_statistics.ipynb",
         "parse_args": "exec.train_vits.ipynb",
         "run": "exec.train_vits.ipynb",
         "STANDARD_MULTISPEAKER": "exec.generate_filelist.ipynb",
         "STANDARD_SINGLESPEAKER": "exec.generate_filelist.ipynb",
         "VCTK": "exec.generate_filelist.ipynb",
         "FORMATS": "exec.generate_filelist.ipynb",
         "Filelist": "exec.select_speakers.ipynb",
         "select_speakers": "exec.select_speakers.ipynb",
         "write_filenames": "exec.split_train_val.ipynb",
         "VITSEncoder": "models.attentions.ipynb",
         "Decoder": "models.mellotron.ipynb",
         "MultiHeadAttention": "models.common.ipynb",
         "FFN": "models.attentions.ipynb",
         "TTSModel": "models.base.ipynb",
         "Conv1d": "models.common.ipynb",
         "LinearNorm": "models.common.ipynb",
         "LocationLayer": "models.common.ipynb",
         "Attention": "models.common.ipynb",
         "STFT": "models.common.ipynb",
         "MelSTFT": "models.common.ipynb",
         "ReferenceEncoder": "models.common.ipynb",
         "STL": "models.common.ipynb",
         "GST": "models.common.ipynb",
         "LayerNorm": "models.common.ipynb",
         "Flip": "models.common.ipynb",
         "Log": "models.common.ipynb",
         "ElementwiseAffine": "models.common.ipynb",
         "DDSConv": "models.common.ipynb",
         "ConvFlow": "models.common.ipynb",
         "WN": "models.common.ipynb",
         "ResidualCouplingLayer": "models.common.ipynb",
         "ResBlock1": "models.common.ipynb",
         "ResBlock2": "models.common.ipynb",
         "LRELU_SLOPE": "models.common.ipynb",
         "DEFAULTS": "models.vits.ipynb",
         "Postnet": "models.mellotron.ipynb",
         "Prenet": "models.mellotron.ipynb",
         "Encoder": "models.mellotron.ipynb",
         "Tacotron2": "models.mellotron.ipynb",
         "piecewise_rational_quadratic_transform": "models.transforms.ipynb",
         "searchsorted": "models.transforms.ipynb",
         "unconstrained_rational_quadratic_spline": "models.transforms.ipynb",
         "rational_quadratic_spline": "models.transforms.ipynb",
         "DEFAULT_MIN_BIN_WIDTH": "models.transforms.ipynb",
         "DEFAULT_MIN_BIN_HEIGHT": "models.transforms.ipynb",
         "DEFAULT_MIN_DERIVATIVE": "models.transforms.ipynb",
         "StochasticDurationPredictor": "models.vits.ipynb",
         "DurationPredictor": "models.vits.ipynb",
         "TextEncoder": "models.vits.ipynb",
         "ResidualCouplingBlock": "models.vits.ipynb",
         "PosteriorEncoder": "models.vits.ipynb",
         "Generator": "models.vits.ipynb",
         "DiscriminatorP": "models.vits.ipynb",
         "DiscriminatorS": "models.vits.ipynb",
         "MultiPeriodDiscriminator": "models.vits.ipynb",
         "SynthesizerTrn": "models.vits.ipynb",
         "CMUDict": "text.cmudict.ipynb",
         "valid_symbols": "text.cmudict.ipynb",
         "symbols": "text.symbols.ipynb",
         "symbols_with_ipa": "text.symbols.ipynb",
         "DEFAULT_SYMBOLS": "text.symbols.ipynb",
         "IPA_SYMBOLS": "text.symbols.ipynb",
         "SYMBOL_SETS": "text.symbols.ipynb",
         "symbols_to_sequence": "text.symbols.ipynb",
         "arpabet_to_sequence": "text.symbols.ipynb",
         "should_keep_symbol": "text.symbols.ipynb",
         "symbol_to_id": "text.symbols.ipynb",
         "id_to_symbol": "text.symbols.ipynb",
         "curly_re": "text.symbols.ipynb",
         "words_re": "text.symbols.ipynb",
         "normalize_numbers": "text.util.ipynb",
         "expand_abbreviations": "text.util.ipynb",
         "expand_numbers": "text.util.ipynb",
         "lowercase": "text.util.ipynb",
         "collapse_whitespace": "text.util.ipynb",
         "convert_to_ascii": "text.util.ipynb",
         "convert_to_arpabet": "text.util.ipynb",
         "basic_cleaners": "text.util.ipynb",
         "transliteration_cleaners": "text.util.ipynb",
         "english_cleaners": "text.util.ipynb",
         "g2p": "text.util.ipynb",
         "clean_text": "text.util.ipynb",
         "english_to_arpabet": "text.util.ipynb",
         "cleaned_text_to_sequence": "text.util.ipynb",
         "text_to_sequence": "text.util.ipynb",
         "sequence_to_text": "text.util.ipynb",
         "CLEANERS": "text.util.ipynb",
         "random_utterance": "text.util.ipynb",
         "utterances": "text.util.ipynb",
         "TTSTrainer": "trainer.base.ipynb",
         "Tacotron2Loss": "trainer.base.ipynb",
         "MellotronTrainer": "trainer.base.ipynb",
         "dynamic_range_compression_torch": "trainer.vits.ipynb",
         "dynamic_range_decompression_torch": "trainer.vits.ipynb",
         "spectral_normalize_torch": "trainer.vits.ipynb",
         "spectral_de_normalize_torch": "trainer.vits.ipynb",
         "spectrogram_torch": "trainer.vits.ipynb",
         "spec_to_mel_torch": "trainer.vits.ipynb",
         "mel_spectrogram_torch": "trainer.vits.ipynb",
         "MAX_WAV_VALUE": "trainer.vits.ipynb",
         "mel_basis": "trainer.vits.ipynb",
         "hann_window": "trainer.vits.ipynb",
         "feature_loss": "trainer.vits.ipynb",
         "discriminator_loss": "trainer.vits.ipynb",
         "generator_loss": "trainer.vits.ipynb",
         "kl_loss": "trainer.vits.ipynb",
         "VITSTrainer": "trainer.vits.ipynb",
         "differenceFunction": "utils.audio.ipynb",
         "cumulativeMeanNormalizedDifferenceFunction": "utils.audio.ipynb",
         "getPitch": "utils.audio.ipynb",
         "compute_yin": "utils.audio.ipynb",
         "convert_to_wav": "utils.audio.ipynb",
         "match_target_amplitude": "utils.audio.ipynb",
         "modify_leading_silence": "utils.audio.ipynb",
         "normalize_audio_segment": "utils.audio.ipynb",
         "normalize_audio": "utils.audio.ipynb",
         "trim_audio": "utils.audio.ipynb",
         "MAX_WAV_INT16": "utils.audio.ipynb",
         "load_wav_to_torch": "utils.audio.ipynb",
         "save_figure_to_numpy": "utils.plot.ipynb",
         "plot_spectrogram": "utils.plot.ipynb",
         "plot_attention": "utils.plot.ipynb",
         "plot_gate_outputs": "utils.plot.ipynb",
         "load_filepaths_and_text": "utils.utils.ipynb",
         "synthesize_speakerids2": "utils.utils.ipynb",
         "parse_vctk": "utils.utils.ipynb",
         "parse_libritts_mellotron": "utils.utils.ipynb",
         "add_speakerid": "utils.utils.ipynb",
         "parse_uberduck": "utils.utils.ipynb",
         "parse_ljspeech": "utils.utils.ipynb",
         "get_alignment_metrics": "utils.utils.ipynb",
         "window_sumsquare": "utils.utils.ipynb",
         "griffin_lim": "utils.utils.ipynb",
         "dynamic_range_compression": "utils.utils.ipynb",
         "dynamic_range_decompression": "utils.utils.ipynb",
         "to_gpu": "utils.utils.ipynb",
         "get_mask_from_lengths": "utils.utils.ipynb",
         "reduce_tensor": "utils.utils.ipynb",
         "subsequent_mask": "utils.utils.ipynb",
         "convert_pad_shape": "utils.utils.ipynb",
         "sequence_mask": "utils.utils.ipynb",
         "generate_path": "utils.utils.ipynb",
         "slice_segments": "utils.utils.ipynb",
         "rand_slice_segments": "utils.utils.ipynb",
         "init_weights": "utils.utils.ipynb",
         "get_padding": "utils.utils.ipynb",
         "fused_add_tanh_sigmoid_multiply": "utils.utils.ipynb",
         "clip_grad_value_": "utils.utils.ipynb",
         "intersperse": "utils.utils.ipynb",
         "parse_values": "vendor.tfcompat.hparam.ipynb",
         "HParams": "vendor.tfcompat.hparam.ipynb",
         "PARAM_RE": "vendor.tfcompat.hparam.ipynb"}

modules = ["data/cache.py",
           "data/statistics.py",
           "data_loader.py",
           "exec/dataset_statistics.py",
           "exec/generate_filelist.py",
           "exec/normalize_audio.py",
           "exec/preprocess_vits.py",
           "exec/select_speakers.py",
           "exec/split_train_val.py",
           "exec/train_tacotron2.py",
           "exec/train_vits.py",
           "models/attentions.py",
           "models/base.py",
           "models/common.py",
           "models/mellotron.py",
           "models/transforms.py",
           "models/vits.py",
           "text/cmudict.py",
           "text/symbols.py",
           "text/util.py",
           "trainer/base.py",
           "trainer/vits.py",
           "utils/audio.py",
           "utils/plot.py",
           "utils/utils.py",
           "vendor/tfcompat/hparam.py"]

doc_url = "https://uberduck-ai.github.io/uberduck_ml_dev/"

git_url = "https://github.com/uberduck-ai/uberduck_ml_dev/tree/master/"

def custom_doc_links(name):
    return None
