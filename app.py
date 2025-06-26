import streamlit as st

st.set_page_config(page_title="Argument Assist", layout="centered")

st.title("Argument Assist")
st.write("Improve your arguments with guided feedback and AI-style suggestions.")

user_input = st.text_area("Paste your claim or paragraph here:")

def generate_feedback(text):
    feedback = []

    if "because" not in text.lower():
        feedback.append("Can you explain *why* you believe this? Try using 'because'.")
    
    if "should" in text.lower():
        feedback.append("This sounds like a strong opinion. Could you give an example or data to support it?")
    
    if "but" not in text.lower() and "however" not in text.lower():
        feedback.append("Consider adding a counterargument — what might someone say in response?")
    
    if not feedback:
        feedback.append(" Solid reasoning! You could deepen it with a source or example.")

    return feedback

if user_input:
    st.subheader("📝 Suggestions:")
    for tip in generate_feedback(user_input):
        st.write(tip)
