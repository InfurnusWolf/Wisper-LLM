# import os
# from dotenv import load_dotenv
# from transformers import pipeline
# import google.generativeai as genai

# # Load environment variables from .env file
# load_dotenv()

# # Step 1: Load Whisper model from Hugging Face
# print("Loading Whisper model...")
# whisper_model = pipeline("automatic-speech-recognition", model="openai/whisper-small")

# # Step 2: Gemini API setup
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# genai.configure(api_key=GEMINI_API_KEY)

# # Create the model
# generation_config = {
#   "temperature": 1,
#   "top_p": 0.95,
#   "top_k": 40,
#   "max_output_tokens": 8192,
#   "response_mime_type": "text/plain",
# }

# model = genai.GenerativeModel(
#   model_name="gemini-2.0-flash-exp",
#   generation_config=generation_config,
# )

# def categorize_transaction(transcription):
#     """Uses Gemini API to categorize the financial transaction."""
#     prompt = (
#         f"The following is a transcription of a financial transaction: '{transcription}'.\n"
#         "Categorize this transaction into one of the following categories: Food, Transportation, Utilities, Entertainment, Healthcare, Other, and provide a one-line reason for your choice."
#     )
#     print(f"Prompt: {prompt}")

#     chat_session = model.start_chat(
#         history=[]
#     )

#     response = chat_session.send_message(prompt)
#     category = response.text.strip()
#     return category

# # Step 3: Process audio input
# def process_audio(audio_path):
#     """Transcribe audio and categorize the transaction."""
#     print(f"Processing audio file: {audio_path}")
#     transcription = whisper_model(audio_path)["text"]
#     print(f"Transcription: {transcription}")

#     # Categorize the transcription
#     category = categorize_transaction(transcription)
#     print(f"Categorized as: {category}")

#     return {
#         "transcription": transcription,
#         "category": category
#     }

# # Example usage
# if __name__ == "__main__":
#     # Replace with the path to an audio file
#     audio_file_path = r"C:\Users\malat\Downloads\WhatsApp Audio 2025-06-12 at 20.47.20_b50b9253.wav"

#     # Process the audio file
#     result = process_audio(audio_file_path)
    
#     # Display results
#     print("\nFinal Result:")
#     print(f"Transcription: {result['transcription']}")
#     print(f"Category: {result['category']}")








import os
from dotenv import load_dotenv
from transformers import pipeline
import google.generativeai as genai
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Step 1: Load Whisper model from Hugging Face
print("Loading Whisper model...")
whisper_model = pipeline("automatic-speech-recognition", model="openai/whisper-small")

# Step 2: Gemini API setup
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# Create the Gemini model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
)

def categorize_transaction(transcription):
    """Uses Gemini API to categorize the financial transaction."""
    prompt = (
        f"The following is a transcription of a financial transaction: '{transcription}'.\n"
        "Categorize this transaction into one of the following categories: Food, Transportation, Utilities, Entertainment, Healthcare, Other, and provide a one-line reason for your choice."
    )
    
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt)
    category = response.text.strip()
    return category

def process_audio(audio_path):
    """Transcribe audio and categorize the transaction."""
    print(f"Processing audio file: {audio_path}")
    transcription = whisper_model(audio_path)["text"]
    print(f"Transcription: {transcription}")

    # Categorize the transcription
    category = categorize_transaction(transcription)
    print(f"Categorized as: {category}")

    return {
        "audio_file": audio_path,
        "transcription": transcription,
        "category": category
    }

def save_to_excel(data, excel_file='results.xlsx'):
    """Save or append data to an Excel file."""
    df_new = pd.DataFrame([data])

    if os.path.exists(excel_file):
        # If file exists, append without overwriting
        df_existing = pd.read_excel(excel_file)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        # If file doesn't exist, create a new one
        df_combined = df_new

    df_combined.to_excel(excel_file, index=False)
    print(f"Data saved to {excel_file}")

# Example usage
if __name__ == "__main__":
    # Replace with the path to your audio file
    audio_file_path = r"C:\Users\malat\Downloads\WhatsApp Audio 2025-06-12 at 20.47.20_b50b9253.wav"

    # Process the audio file
    result = process_audio(audio_file_path)

    # Save result to Excel file
    save_to_excel(result)
