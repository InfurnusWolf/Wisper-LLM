# WhisperWallet - Voice-Powered Expense Tracker

A simple, AI-enabled expense tracking application that allows you to log transactions using your voice. It transcribes spoken input into text using OpenAI Whisper and intelligently categorizes expenses with Google Gemini AI. All transactions are automatically saved to an Excel file for easy record-keeping.

## ✨ Features

- 🎙️ **Voice-Enabled Expense Logging**  
  Converts your spoken transactions into text using Whisper for effortless expense tracking.

- 🧠 **AI-Based Categorization**  
  Uses Google Gemini AI to classify each transaction into common expense categories like Food, Transportation, and Utilities.

- 📊 **Persistent Excel Record Keeping**  
  All transactions and their categories are automatically saved and updated in an Excel file (`expenses.xlsx`) for future reference.

## 🚀 Technologies Used

- **Python 3.10+**
- [OpenAI Whisper (via Hugging Face Transformers)](https://huggingface.co/docs/transformers/index)
- [Google Gemini AI API](https://ai.google.dev/)
- **Pandas** (for data manipulation)
- **OpenPyXL** (for Excel file handling)
- **FFmpeg** (required for Whisper audio processing)

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/InfurnusWolf/Wisper-LLM.git
cd Wisper-LLM
````

### 2. Create Virtual Environment & Activate

```bash
python -m venv env
# Windows:
env\Scripts\activate
# Linux/Mac:
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg

* Download **FFmpeg** from: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
* Extract and copy the `bin` folder path (e.g., `C:\ffmpeg\bin`)
* Add the `bin` path to your system's **Environment Variables**:

  * **Windows**:
    Control Panel → System → Advanced system settings → Environment Variables → Path → Edit → New → paste the `bin` path
  * **Linux/Mac**:
    Add to `.bashrc` or `.zshrc`:

    ```bash
    export PATH="$PATH:/path_to_ffmpeg/bin"
    ```

### 5. Configure Environment Variables

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_google_gemini_api_key_here
```

Replace `your_google_gemini_api_key_here` with your actual Google Gemini API key.

## 🏃 Running the App

```bash
python main.py
```

Get a .wav file in the input say thing like :

```
"I spent 500 rupees on groceries"
```

The app will:

1. Convert your speech to text using Whisper.
2. Classify the expense using Gemini AI.
3. Save the transaction and its category to `expenses.xlsx`.

## 📂 Output

A file named **`expenses.xlsx`** will be created/updated with the following columns:

* **Date**
* **Transaction Text**
* **Amount**
* **Category**

## ✅ Requirements

See [`requirements.txt`](./requirements.txt) for all required Python packages.

## ⚠️ Notes

* Ensure FFmpeg is installed and properly configured.
* Internet connection is required for Gemini AI API.
* The `.env` file must contain a valid `GEMINI_API_KEY`.


