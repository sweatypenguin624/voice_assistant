# 🗣️ Voice Assistant

A Python-based AI voice assistant that listens to your speech, understands your command via OpenAI’s GPT models 🤖, and speaks the response back to you using text-to-speech 🔊. It’s like having your own mini Jarvis!

---

## ✨ Features

- 🎙️ **Speech Recognition** – Converts your voice into text using `speech_recognition` or OpenAI's Whisper.
- 🧠 **AI-Powered Replies** – Uses GPT-3.5/4 to process your input and generate human-like responses.
- 🔊 **Text-to-Speech** – Speaks the response aloud using `pyttsx3` or `gTTS`.
- 🛑 **Wake Word Activation** – Stays passive until a specific wake word is heard (e.g., “Hey Assistant”).
- ⚙️ **Customizable** – Choose voice engines, models, and more.

---

## 🛠️ Tech Stack

| Purpose            | Library / Tool         |
|--------------------|------------------------|
| Programming Language | Python 3.7+            |
| Speech Recognition  | `speech_recognition`, `whisper` (optional) |
| Text-to-Speech      | `pyttsx3`, `gTTS`, `playsound` |
| NLP Engine          | `openai` (GPT-3.5/4)   |
| Audio Playback      | `playsound`, `pyaudio` |
| Other Tools         | `asyncio`, `re`, etc.  |

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sweatypenguin624/voice_assistant.git
   cd voice_assistant
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install the required packages**
   ```bash
   pip install -r requirements.txt
   ```
   Or manually:
   ```bash
   pip install openai speechrecognition pyttsx3 gtts playsound
   ```

4. **Set your OpenAI API key**
   ```bash
   export OPENAI_API_KEY="your-api-key"      # macOS/Linux
   set OPENAI_API_KEY="your-api-key"         # Windows
   ```

---

## 🚀 Usage

Run the assistant from the terminal:
```bash
python voice_assistant.py
```

🧏 Speak the **wake word** (e.g., "ok chat") to activate the assistant.

💬 Ask a question or give a command.

🔁 The assistant listens, thinks, and replies… out loud!

---

## 🧩 Example Flow

> You: "Ok chat, what’s the capital of Japan?"  
>  
> 💡 Assistant: *"The capital of Japan is Tokyo."* 🔉

---

## 🤝 Contributing

Contributions are welcome! 🛠  
If you have ideas for improvements or spot any bugs, feel free to:

- Fork the repo 🍴
- Make your changes 💻
- Submit a pull request 🔁

Please make sure your code follows the existing style and is tested.

---

## 📄 License

❗ *No license file has been provided.*

If you want to use or share this project, please check with the author or consider adding a license such as MIT.

---

## 📬 Contact

For issues, suggestions, or collaboration:

- 🐧 GitHub: [@sweatypenguin624](https://github.com/sweatypenguin624)
- 📁 Open an [issue here](https://github.com/sweatypenguin624/voice_assistant/issues)

---

> Built with 💡 Python, 🤖 OpenAI, and 🎤 your voice.
