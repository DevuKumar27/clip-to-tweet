import streamlit as st
import openai

# ✅ Securely load API key from Streamlit secrets
openai.api_key = st.secrets["openai_api_key"]

# UI Setup
st.set_page_config(page_title="Clip-to-Tweet AI", layout="centered")
st.title("🎙️ Clip-to-Tweet AI Assistant")
st.write("Paste a podcast or video transcript and get a viral-style Twitter thread.")

# Text input
transcript = st.text_area("📄 Paste Transcript", height=250)

# On click
if st.button("🚀 Generate Tweet Thread"):
    if not transcript.strip():
        st.warning("Please paste a transcript first.")
    else:
        with st.spinner("Generating tweet thread..."):
            try:
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "user",
                            "content": f"Turn this into a 3–5 tweet thread in a viral, engaging Twitter style:\n\n{transcript}"
                        }
                    ],
                    temperature=0.8,
                    max_tokens=500
                )

                thread = response.choices[0].message.content
                st.subheader("🧵 Generated Tweet Thread")
                st.write(thread)
            except Exception as e:
                st.error(f"Error: {e}")
