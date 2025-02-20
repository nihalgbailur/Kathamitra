# Kathamitra 📚 - Your AI Storytelling Companion

Kathamitra (Sanskrit: "Story Friend") is an interactive AI-powered storytelling application that collaborates with you to create engaging narratives. Using state-of-the-art language models and an intuitive interface, it helps bring your stories to life.


## ✨ Features

- **Interactive Storytelling**: Co-create stories with AI assistance
- **Genre Selection**: Choose from Fantasy, Science Fiction, Mystery, Romance, and Horror
- **Writing Style Control**: Adjust between Concise, Balanced, and Descriptive styles
- **Story Management**: Save and restore story checkpoints
- **Chapter Organization**: Easily manage story chapters
- **Export Options**: Save your stories in various formats (TXT, PDF, DOCX - coming soon)

## 📸 Screenshot
![Kathamitra Interface]()![Screenshot 2025-02-20 at 10 49 02 PM](https://github.com/user-attachments/assets/b63c54a7-398c-4755-b8ad-14799db2b229)

*Kathamitra's intuitive user interface with story controls and writing options*

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Engine**: LangChain + DeepSeek LLM (via Ollama)
- **Language**: Python 3.9+

## 📋 Prerequisites

- Python 3.9 or higher
- [Ollama](https://ollama.ai/) installed with `deepseek-r1:7b` model
- Git (for cloning the repository)

## 🚀 Getting Started

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/kathamitra.git
   cd kathamitra
   ```

2. **Set Up Virtual Environment**
   ```bash
   python3 -m venv venv
   
   # For Windows
   venv\Scripts\activate
   
   # For macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Application**
   ```bash
   streamlit run main.py
   ```

## 📁 Project Structure

```
Kathamitra/
├── venv/                 # Virtual environment
├── .gitignore            # Git ignore file
├── README.md             # Project documentation (this file)
├── requirements.txt      # Python dependencies
├── main.py               # Streamlit application

```
---

## 🛠️ Dependencies
- Python 3.9+
- Streamlit
- LangChain
- DeepSeek LLM (via Ollama)

### 📋 requirements.txt
```plaintext
streamlit
langchain
```
---

## 🧑‍💻 How to Set Up and Run Kathamitra
### 1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/kathamitra.git
cd kathamitra
```

### 2. **Create a Virtual Environment**
```bash
python3 -m venv venv
```

### 3. **Activate the Virtual Environment**
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```
- On Windows:
  ```bash
  venv\Scripts\activate
  ```

### 4. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 5. **Ensure Ollama with DeepSeek is Installed**
- Install [Ollama](https://ollama.ai/)
- Ensure `deepseek-r1:7b` is downloaded and available.

### 6. **Run the Application**
```bash
streamlit run main.py
```
---

## 📝 Code Explanation
### **1. main.py (Streamlit App)**
- **DeepSeekLLM Class:** Custom LangChain-compatible LLM class that interacts with Ollama.
- **generate_story Function:** Builds a prompt using LangChain and generates story continuations.
- **Streamlit UI:** Displays the evolving story and takes user input to extend the narrative.

### **2. .gitignore**
```gitignore
venv/
__pycache__/
.streamlit/
.DS_Store
```
---

## ✅ Example Workflow
1. You enter a plot twist or character action.
2. Kathamitra generates a creative continuation.
3. The story evolves with every input.

---
## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first.

## 📜 License
[MIT](https://choosealicense.com/licenses/mit/)
