import streamlit as st
from ai_test_generator import generate_test_cases


st.set_page_config(
    page_title="AI UI QA Assistant",
    page_icon="🧪"
)


st.title("🧪 AI UI QA Assistant")

st.write(
    "Enter a UI requirement or user story "
    "and let AI generate comprehensive test scenarios."
)


user_story = st.text_area(
    "Enter UI User Story",
    placeholder="Example: User should be able to login using email and password."
)


if st.button("Generate Test Cases"):

    if not user_story.strip():

        st.warning("Please enter a user story.")

    else:

        with st.spinner("AI is analyzing the user journey..."):

            try:

                result = generate_test_cases(user_story)

                st.subheader("AI Generated QA Analysis")

                st.write(result)

            except Exception as e:

                st.error(f"Error: {e}")