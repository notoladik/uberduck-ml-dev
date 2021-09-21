import sys
import os
import soundfile as sf 
import pandas as pd

workingdirectory = os.popen('git rev-parse --show-toplevel').read()[:-1]
sys.path.append(workingdirectory)
os.chdir(workingdirectory)

from src.utils import add_speakerid, parse_vctk, parse_libritts_mellotron, parse_lj7
import numpy as np

import soundfile as sf
import librosa

def load_filepaths_and_text(filename, split="|"):
    with open(filename, encoding='utf-8') as f:
        filepaths_and_text = [line.strip().split(split) for line in f]
    return filepaths_and_text

def synthesize_speakerids2(filelists, fix_indices_index = None):

    data_dict = {}
    data_dict_out = {}
    for f in range(len(filelists)):
            data = load_filepaths_and_text(filelists[f])
            data_dict[filelists[f]] = pd.DataFrame(data)    
        
    source_files = list(data_dict.keys())
    
    speaker_offset = {}
    nfilelist = len(filelists)
    reserved_speakers = np.unique(data_dict[filelists[fix_indices_index]].iloc[:,2])
    
    for s in range(nfilelist):
        source_file = filelists[s]
        data = data_dict[source_file]
        if s != fix_indices_index:
            speakers = np.unique(data.iloc[:,2])
            overlap = np.where(np.isin(speakers, reserved_speakers))[0]
            reserved_speakers_temp = np.union1d(speakers, reserved_speakers)
            newindices = np.setdiff1d(list(range(len(reserved_speakers) + len(speakers))), reserved_speakers_temp)[:len(overlap)]
            for o in range(len(overlap)):
                data.iloc[np.where(data.iloc[:,2] == overlap[o])[0] ,2] = newindices[o]

            data_dict_out[source_file] = data
            speakers = np.unique(data.iloc[:,2])
            reserved_speakers = np.union1d(speakers, reserved_speakers)
        else:
            data_dict_out[source_file] = data
    return(data_dict_out)  

def parse_vctk(folder):

    wav_dir = folder + 'wav48_silence_trimmed'
    txt_dir = folder + 'txt'
    speaker_wavs = os.listdir(wav_dir)
    speaker_txts = os.listdir(txt_dir)
    speakers = np.intersect1d(speaker_wavs, speaker_txts)
    
    output_dict = {}
    #wav_dict = {}
    #txt_dict = {}
    #speaker_dict = {}
    counter = 0
    for speaker in speakers:
        
        speaker_wav_dir = wav_dir + '/' + speaker
        speaker_txt_dir = txt_dir + '/' + speaker
        wav_files_speaker = np.asarray(os.listdir(speaker_wav_dir))
        txt_files_speaker = np.asarray(os.listdir(speaker_txt_dir))
        #data_dict[wav_dir] = pd.DataFrame()

        wav_files = np.asarray([])
        nwavfiles= len(wav_files_speaker)
        list1 = np.asarray([txt_files_speaker[i][:8] for i in range(len(txt_files_speaker))])
        list2 = np.asarray([wav_files_speaker[i][:8] for i in range(nwavfiles)])
        mic = np.asarray([wav_files_speaker[i][12]  for i in range(nwavfiles)])
        mic1_ind = mic == '1'
        wav_files_speaker = wav_files_speaker[mic1_ind]
        list2 = list2[mic1_ind]
        combined_files = np.intersect1d(list1, list2)
        matching_inds1 = np.where(np.isin(list1 , combined_files))[0]
        matching_inds2 = np.where(np.isin(list2 , combined_files))[0]
        inds1 = matching_inds1[list1[matching_inds1].argsort()]
        inds2 = matching_inds2[list2[matching_inds2].argsort()]
        txt_files_speaker = txt_files_speaker[inds1]
        wav_files_speaker = wav_files_speaker[inds2]
        texts = list()
        for g in range(len(txt_files_speaker)):
            text_file = speaker_txt_dir + '/' + txt_files_speaker[g]
            with open(text_file) as f:
                contents = f.read().splitlines() 
            #print(contents)
            texts = np.append(texts, contents)

            wav_file = speaker_wav_dir + '/' + wav_files_speaker[g]
            wav_files = np.append(wav_files, wav_file)

        if wav_files.shape[0]>0:
            output_dict[speaker] = pd.DataFrame([wav_files, texts,np.repeat(counter, wav_files.shape[0])]).transpose()
            counter = counter +1
            
    output = pd.concat(list(output_dict.values()))   
    return(output)

def parse_libritts_mellotron(source_folder, mellotron_filelist):

    data = pd.read_csv(mellotron_filelist, sep = "|",header=None, error_bad_lines=False)
    
    data[0] = data[0].str[17:]
    
    data[0] = source_folder + data[0].astype(str)
    return(data)

def load_filepaths_and_text(filename, split="|"):
    with open(filename, encoding='utf-8') as f:
        filepaths_and_text = [line.strip().split(split) for line in f]
    return filepaths_and_text

# export
def flac_to_wav(input_file):
    
    nsamp = input_file.shape[0]
    output_file = input_file.copy()
    for i in range(nsamp):
        filename = input_file.iloc[i,0]
        print(i,filename)
        filestart = filename[:-5]
        print(i,filestart)
        audio, sr = librosa.load(filename)#sf.read(filename)
        newfile = filestart + '.wav'
        print(i,newfile)
        sf.write(newfile,audio,sr)
        output_file.iloc[i,0] = newfile
        
    return(output_file)

def add_speakerid(data, speaker_key = 0):

    if data.shape[1] == 3:
        if type(data[2]) == int:
            pass
        else:
            speaker_ids = np.asarray(np.ones(data.shape[0], dtype = int) * speaker_key, dtype = int)
            data[2] = speaker_ids            
    if data.shape[1] == 2:
        speaker_ids = np.asarray(np.ones(data.shape[0], dtype = int) * speaker_key, dtype = int)
        data[2] = speaker_ids

    return(data)

# export 
def parse_libritts_mellotron(source_folder, mellotron_filelist):

    data = load_filepaths_and_text(mellotron_filelist)
    data = pd.DataFrame(data)    
    data[0] = data[0].str[17:]
    
    data[0] = source_folder + data[0].astype(str)
    return(data)

    
def parse_uberduck(source_folder):
    
    source_file = source_folder + '/all.txt'
    data = load_filepaths_and_text(source_file)
    data = pd.DataFrame(data)  
    
    nsamp = data.shape[0]
    data[0] =  source_folder + '/'+data[0].astype(str)
    output = add_speakerid(data, speaker_key = 0)
    
    for i in range(output.shape[0]):
        loaded = librosa.load(output.iloc[i,0])
        sf.write(output.iloc[i,0],loaded[0],loaded[1])
        
    return(output)

def parse_lj7(source_folder):
    
    source_file = source_folder + '/metadata.csv'
    data = load_filepaths_and_text(source_file)
    data = pd.DataFrame(data)  
    nsamp = data.shape[0]
    
    data[0] = source_folder + '/wavs/' + data[0].astype(str)
    output = add_speakerid(data, speaker_key = 0)
    for i in range(output.shape[0]):
        output.iloc[i,0] = output.iloc[i,0] + '.wav'
        
    return(output)