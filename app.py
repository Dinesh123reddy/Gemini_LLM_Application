!pip install google-generativeai
!pip install streamlit
!npm install localtunel

import google.generativeai as genai
import streamlit as st

api_key = "Gemini_api_key"
genai.configure(api_key=api_key)
model=genai.GenerativeModel("gemini-1.5-flash-latest")

chat=model.start_chat(history=[])
st.set_page_config(page_title="Q/A Demo")
st.header("Mini ChatBot")
if 'chat_history' not in st.session_state:
  st.session_state['chat_history']=[]

input=st.text_input("Input :", key="input")
submit=st.button("Submit")

if submit and input:
  response=chat.send_message(input,stream=True)
  st.session_state['chat_history'].append(("You",input))
  st.subheader("The response is :")
  
  for chunk in response:
    # st.write(chunk)
    st.session_state['chat_history'].append(("Bot",chunk.text))

st.subheader("Chat History")

for role, text in st.session_state['chat_history']:
  st.write(f"{role} : {text}")

!streamlit run /content/app.py & npx localtunnel --port 8501 & curl ipv4.icanhazip.com
