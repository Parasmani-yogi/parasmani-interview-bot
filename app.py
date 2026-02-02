import streamlit as st
from groq import Groq
import os
# Load API key
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="Parasmani chatbot", page_icon="🤖")

# ===== Resume Context =====
RESUME_CONTEXT = """
Name: Parasmani Yogi
Degree: M.Sc in Mathematics and Computing
Institute: IIT (ISM) Dhanbad

Education:
- M.Sc Mathematics and Computing, IIT (ISM) Dhanbad (2026)
- B.Sc Mathematics, University of Rajasthan (2023)
- 12th, Board of Secondary Education Rajasthan (2020)

Projects:
1. Interactive Summer Olympics Analysis (Python, Streamlit, Pandas, Plotly, AWS EC2)
   - Built an interactive Streamlit web app for EDA on Summer Olympics dataset.
   - Preprocessed data and deployed on AWS EC2.

2. Emotion Detection using Facial Expressions (Python, TensorFlow, Keras, CNN, ResNet50)
   - Built CNN & ResNet50 models for 7-class emotion classification.
   - Used transfer learning, achieved 65% validation accuracy and 0.65 F1-score.

3. Duplicate Question Detection App (Python, NLP, Streamlit, ML)
   - Built Streamlit app to detect semantically similar questions.
   - Achieved 80% accuracy.

Technical Skills:
- Languages: Python, C++, SQL
- ML/DL: TensorFlow, Keras, Scikit-learn, CNN, ResNet50
- NLP: NLTK, SpaCy, TF-IDF, FuzzyWuzzy
- Data: Pandas, NumPy, Matplotlib, Seaborn
- Tools: Streamlit, VS Code, MySQL, PowerBI
- Cloud: AWS EC2

Achievements:
- IIT JAM 2024 AIR 647
- INSPIRE Scholarship
"""

# ===== Adaptive Interview Prompt =====
SYSTEM_PROMPT = f"""
You are Parasmani Yogi, an M.Sc student in Mathematics and Computing at IIT (ISM) Dhanbad.

Here is your resume:
{RESUME_CONTEXT}

ADAPTIVE INTERVIEW MODE:
- If the question is personal/basic → answer in 1 short sentence.
- If the question is descriptive (background, motivation) → answer in 2–3 sentences.
- If the question is technical or project-based → answer in 3 concise bullet-style sentences.
- Never write long paragraphs.
- Keep language simple, professional, and confident.
- Avoid listing the full resume.

Always answer like a real interview candidate.
"""

st.title("🤖 Parasmani AI ")
st.write("Ask me anything about myself.")

# ===== Memory =====
if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("You:")

if st.button("Send") and user_input:
    st.session_state.chat.append(("You", user_input))

    # Build context
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for speaker, msg in st.session_state.chat:
        role = "user" if speaker == "You" else "assistant"
        messages.append({"role": role, "content": msg})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    reply = response.choices[0].message.content
    st.session_state.chat.append(("Paras", reply))

# ===== Show only latest =====
if len(st.session_state.chat) >= 2:
    u = st.session_state.chat[-2]
    b = st.session_state.chat[-1]
    st.markdown(f"**{u[0]}:** {u[1]}")
    st.markdown(f"**{b[0]}:** {b[1]}")
