import streamlit as st
from models.text_generator import generate_meme_caption
from models.image_generator import generate_meme_image
from utils.meme_overlay import add_caption_to_image
import os

st.set_page_config(page_title="AI Meme Generator", layout="centered")

st.title("😂 Project-14 AI Meme Generator")
st.subheader("Powered by Groq + LLaMA + Stable Diffusion")

topic = st.text_input("Enter a meme topic or phrase:", "AI taking over jobs")

if st.button("Generate Meme"):
    with st.spinner("Generating meme..."):
        caption = generate_meme_caption(topic)
    st.write(f"**Generated Caption:** {caption}")

    image_path = generate_meme_image(topic)
    output_path = f"outputs/memes/final_meme.png"
    os.makedirs("outputs/memes", exist_ok=True)
    final_path = add_caption_to_image(image_path, caption, output_path)

    st.image(final_path, caption="Your AI-Generated Meme", use_container_width=True)
    st.success("Meme generated successfully!")
