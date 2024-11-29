from pydub import AudioSegment
import librosa

def preprocess_audio(audio_path, target_sample_rate=22050):
    # Check if the input is MP3 or WAV
    if audio_path.endswith(".mp3"):
        # If it's an MP3, first convert it to WAV
        audio = AudioSegment.from_mp3(audio_path)
    else:
        # If it's already a WAV, just load it
        audio = AudioSegment.from_wav(audio_path)
    
    # Convert to mono (if stereo)
    if audio.channels > 1:
        audio = audio.set_channels(1)
    
    # Normalize audio
    audio = audio.normalize()

    # Export the processed audio as a WAV file
    processed_audio_path = audio_path.replace(".mp3", "_processed.wav").replace(".wav", "_processed.wav")
    audio.export(processed_audio_path, format="wav")
    
    return processed_audio_path

# Example usage
# Replace with the actual path of your MP3 or WAV file
processed_audio = preprocess_audio("C:/Users/Megas/Documents/GitHub/AudioTranscript/output.wav")
print(f"Processed audio saved at: {processed_audio}")
