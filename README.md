# Parasmani Interview Bot 🤖

## Overview
This project is a resume-based AI interview chatbot built using **Streamlit** and the **Groq LLM API**.  
The bot answers questions as if it were the candidate, using information from the resume and adapting the response length based on the type of question.

The chatbot simulates real interview conversations by giving short answers for basic questions and more detailed responses for technical or project-based questions.

---

## Features
- Resume-aware responses.  
- Adaptive answer length (short for simple, detailed for technical).  
- Interview-style conversational tone.  
- Clean Streamlit web interface.  
- Powered by Groq LLM.  

---

## Tech Stack
- **Language:** Python  
- **Framework:** Streamlit  
- **API:** Groq LLM  
- **Libraries:** python-dotenv  

---

## How to Run

### Install Required Packages
Ensure you have Python 3.9 or higher installed. Then, install the necessary dependencies:
```bash
pip install streamlit groq python-dotenv
```

### Clone the Repository
Download the project from GitHub:
```bash
git clone https://github.com/Parasmani-yogi/parasmani-interview-bot.git
cd parasmani-interview-bot
```

### Create Environment File
Create a ```.env``` file in the project folder and add:
```bash
GROQ_API_KEY=your_api_key_here
```

### Run the Application
```bash
python -m streamlit run app.py

````

