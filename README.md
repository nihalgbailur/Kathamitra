# Kathamitra: Collaborative Storytelling Companion

Kathamitra is an AI-powered collaborative storytelling companion that co-authors interactive stories. Built with **Streamlit**, **LangChain**, and **DeepSeek LLM (via Ollama)**, Kathamitra generates personalized story continuations based on your input.

---

## 🚀 Project Structure
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
git clone https://github.com/nihalgbailur/Kathamitra.git
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
