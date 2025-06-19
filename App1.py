import streamlit as st
import openai  # ✅ Correct import

# Set your OpenAI API key
openai.api_key = "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"
# 🔐 Replace with your actual key or load from st.secrets

# Streamlit UI
st.set_page_config(page_title="Clip-to-Tweet AI", layout="centered")
st.title("🎙️ Clip-to-Tweet AI Assistant")

st.write("Paste a podcast or video transcript and get a viral-style Twitter thread.")

# Input
transcript = st.text_area("📄 Paste Transcript (max ~500 words)", height=200)

# Button click
if st.button("🚀 Generate Tweet Thread"):
    if not transcript.strip():
        st.warning("Please enter a transcript first.")
    else:
        with st.spinner("Generating tweet thread..."):
            try:
                prompt = (
                    f"Turn this into a 3–5 tweet thread in a viral, engaging Twitter style:\n\n{transcript}\n\nThread:"
                )

                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.8,
                    max_tokens=500
                )

                thread = response.choices[0].message.content
                st.subheader("🧵 Generated Tweet Thread")
                st.write(thread)
            except Exception as e:
                st.error(f"Error: {e}")

# Footer
st.markdown("---")
st.caption("Built with 🧠 OpenAI + Streamlit • Clip-to-Tweet AI")
