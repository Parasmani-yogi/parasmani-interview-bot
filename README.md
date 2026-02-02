# Parasmani Interview Bot 🤖

A Streamlit-based AI chatbot that answers interview questions using my resume.  
It behaves like a real interview candidate by adapting answer length and tone based on the question.

---

## 🚀 Features

- Resume-aware responses  
- Smart answer length (short for basic, detailed for technical)  
- Clean Streamlit web UI  
- Interview-style tone  
- Powered by Groq LLM  

---

## 🛠 Tech Stack

- Python  
- Streamlit  
- Groq API  
- python-dotenv  

---

## 📂 Project Structure

parasmani-interview-bot/  
│── app.py  
│── .gitignore  
│── README.md  

---

# 1. Clone the repository
git clone https://github.com/Parasmani-yogi/parasmani-interview-bot.git
cd parasmani-interview-bot

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install streamlit groq python-dotenv

# 4. Create .env file
echo GROQ_API_KEY=your_api_key_here > .env

# 5. Run the app
python -m streamlit run app.py
