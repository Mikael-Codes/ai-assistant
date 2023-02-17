# Import the AudioSegment class for processing audio and the 
# split_on_silence function for separating out silent chunks.
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os 

# Define a function to normalize a chunk to a target amplitude.
def match_target_amplitude(aChunk, target_dBFS):
    ''' Normalize given audio chunk '''
    change_in_dBFS = target_dBFS - aChunk.dBFS
    return aChunk.apply_gain(change_in_dBFS)

# Load your audio.
sourcepath = r"C:\Tut\ai-assistant\Homer"
audio_tracks = [os.path.join(dp, f) for dp, dn, filenames in os.walk(sourcepath) for f in filenames if os.path.splitext(f)[1] == '.mp3']

for track in audio_tracks:
    current_track = AudioSegment.from_mp3(track)
    output_folder = track.replace('.mp3', '').split('/')[-1]
    # Split track where the silence is 2 seconds or more and get chunks using 
    # the imported function.
    chunks = split_on_silence (
        # Use the loaded audio.
        current_track, 
        # Specify that a silent chunk must be at least 2 seconds or 2000 ms long.
        min_silence_len = 200,
        # Consider a chunk silent if it's quieter than -16 dBFS.
        # (You may want to adjust this parameter.)
        silence_thresh = -50
    )

    # Process each chunk with your parameters
    if not os.path.exists('/output'):
        os.makedirs('/output')

    for i, chunk in enumerate(chunks):
        # Create a silence chunk that's 0.5 seconds (or 500 ms) long for padding.
        silence_chunk = AudioSegment.silent(duration=500)

        # Add the padding chunk to beginning and end of the entire chunk.
        audio_chunk = silence_chunk + chunk + silence_chunk

        # Normalize the entire chunk.
        normalized_chunk = match_target_amplitude(audio_chunk, -20.0)

        # Export the audio chunk with new bitrate.
        print("{0}.wav.".format(i))
        normalized_chunk.export(
            "{0}/{1}.wav".format(output_folder, i),
            bitrate = "192k",
            format = "wav"
        )