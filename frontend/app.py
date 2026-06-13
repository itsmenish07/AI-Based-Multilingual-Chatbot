import streamlit as st
import requests

st.set_page_config(
    page_title="AI Welfare Scheme Assistant",
    page_icon="🏛️",
    layout="wide"
)

st.title("🏛️ Bharat Welfare Assistant")

st.markdown(
    """
    Find government schemes you are eligible for and
    get AI-powered guidance in English and Hindi.
    """
)

language = st.selectbox(
    "Language",
    ["English", "Hindi"]
)

st.header("Check Your Eligibility")

age = st.number_input(
    "Age",
    min_value=0,
    max_value=100
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

occupation = st.selectbox(
    "Occupation",
    [
    "Farmer",
    "Worker",
    "Street Vendor",
    "Student",
    "Self Employed",
    "Unemployed"
]
)

income = st.number_input(
    "Annual Income",
    min_value=0
)

if st.button("Find Schemes"):

    payload = {
        "age": age,
        "gender": gender,
        "occupation": occupation,
        "income": income
    }

    response = requests.post(
        "http://127.0.0.1:8000/check-eligibility",
        json=payload
    )

    if response.status_code == 200:

        data = response.json()

        st.subheader("Recommended Schemes")

        for scheme in data["eligible_schemes"]:

            with st.expander(scheme["name"]):

                st.write("### Benefit")
                st.write(scheme["benefit"])

                st.write("### Description")
                st.write(scheme["description"])

                st.write("### Required Documents")

                for doc in scheme["documents"]:
                    st.write(f"✅ {doc}")

                st.write("### Application Process")

                for step in scheme["application_process"]:
                    st.write(f"➡️ {step}")

    else:
        st.error("Could not fetch scheme recommendations.")

st.divider()

st.header("🤖 AI Welfare Assistant")

question = st.text_input(
    "Ask a question about any welfare scheme"
)

if st.button("Ask AI"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={
                "question": question,
                "language": language
            }
        )

        if response.status_code == 200:

            data = response.json()

            st.subheader("AI Response")
            st.write(data["answer"])

        else:
            st.error("Failed to get response from AI.")

if "messages" not in st.session_state:
    st.session_state.messages = []