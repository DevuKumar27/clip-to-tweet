import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="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")  # Replace with your key

st.title("🎙️ Clip-to-Tweet AI Assistant")

st.write("Paste your short podcast/video transcript and get a viral-style tweet thread.")

transcript = st.text_area("Paste Transcript (max 500 words)", height=200)

if st.button("Generate Tweet Thread"):
    with st.spinner("Writing tweets..."):
        prompt = f"Turn this clip into a 3–5 tweet thread in a viral, engaging Twitter style:\n\n{transcript}\n\nThread:"
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=500
        )

        thread = response.choices[0].message.content
        st.subheader("🧵 Tweet Thread")
        st.write(thread)