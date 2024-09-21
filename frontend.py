import streamlit as st
import engine

st.title("Recap Rephrasing")
# st.text("please input the text you want to recap ")
# st.chat_input()

user_input = st.text_area("Enter a phrase:", "")

# Button to trigger the rephrasing
if st.button("Rephrase"):
    if user_input:
        # Use the paraphrasing model to rephrase the input
        # rephrased_text = paraphrase_model(user_input, num_return_sequences=1)[0]['generated_text']
        st.subheader("Rephrased Text:")
        st.write(engine.functions(user_input))
    else:
        st.warning("Please enter a phrase.")