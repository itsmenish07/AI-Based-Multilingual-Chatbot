import streamlit as st
import requests

# ---------------------------
# Page Configuration
# ---------------------------

st.set_page_config(
    page_title="Bharat Welfare Assistant",
    page_icon="🏛️",
    layout="wide"
)

# ---------------------------
# Session State
# ---------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------
# Header
# ---------------------------

st.title("🏛️ Bharat Welfare Assistant")

st.markdown("""
Find government welfare schemes you are eligible for and get AI-powered guidance in multiple Indian languages.
""")

# ---------------------------
# Language Selection
# ---------------------------

language = st.selectbox(
    "Language",
    [
        "English",
        "Hindi",
        "Tamil"
    ]
)

st.divider()

# ---------------------------
# Eligibility Checker
# ---------------------------

st.header("📋 Check Your Eligibility")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=0,
        max_value=100
    )

    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female"
        ]
    )

    state = st.selectbox(
        "State",
        [
            "Uttar Pradesh",
            "Maharashtra",
            "Delhi",
            "Tamil Nadu",
            "Karnataka",
            "West Bengal",
            "Other"
        ]
    )

with col2:

    occupation = st.selectbox(
        "Occupation",
        [
            "Farmer",
            "Worker",
            "Vendor",
            "Student",
            "Self Employed",
            "Unemployed"
        ]
    )

    income = st.number_input(
        "Annual Income",
        min_value=0
    )

    category = st.selectbox(
        "Category",
        [
            "General",
            "OBC",
            "SC",
            "ST"
        ]
    )

area = st.selectbox(
    "Area",
    [
        "Urban",
        "Rural"
    ]
)

# ---------------------------
# Find Schemes
# ---------------------------

if st.button("🔍 Find Schemes"):

    payload = {
        "age": age,
        "gender": gender,
        "occupation": occupation,
        "income": income,
        "state": state,
        "category": category,
        "area": area
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/check-eligibility",
            json=payload
        )

        if response.status_code == 200:

            data = response.json()

            st.subheader("🎯 Recommended Schemes")

            if len(data["eligible_schemes"]) == 0:
                st.warning(
                    "No matching schemes found."
                )

            for scheme in data["eligible_schemes"]:

                with st.expander(
                    scheme["name"]
                ):

                    if "match_score" in scheme:

                        st.progress(
                            scheme["match_score"] / 100
                        )

                        st.write(
                            f"Match Score: {scheme['match_score']}%"
                        )

                    st.write("### 💰 Benefit")
                    st.write(
                        scheme.get(
                            "benefit",
                            "Not Available"
                        )
                    )

                    st.write("### 📖 Description")
                    st.write(
                        scheme.get(
                            "description",
                            "Not Available"
                        )
                    )

                    st.write("### 📄 Required Documents")

                    for doc in scheme.get(
                        "documents",
                        []
                    ):
                        st.write(
                            f"✅ {doc}"
                        )

                    st.write(
                        "### 🚀 Application Process"
                    )

                    for step in scheme.get(
                        "application_process",
                        []
                    ):
                        st.write(
                            f"➡️ {step}"
                        )

        else:
            st.error(
                f"Backend Error: {response.status_code}"
            )

    except Exception as e:
        st.error(
            f"Error connecting to backend: {e}"
        )

st.divider()

# ---------------------------
# AI Assistant
# ---------------------------

st.header("🤖 AI Welfare Assistant")

question = st.text_input(
    "Ask a question about any welfare scheme"
)

if st.button("Ask AI"):

    if question.strip() == "":
        st.warning(
            "Please enter a question."
        )

    else:

        try:

            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={
                    "question": question,
                    "language": language
                }
            )

            if response.status_code == 200:

                data = response.json()

                st.session_state.messages.append(
                    ("You", question)
                )

                st.session_state.messages.append(
                    (
                        "Assistant",
                        data["answer"]
                    )
                )

                st.subheader(
                    "🤖 AI Response"
                )

                st.write(
                    data["answer"]
                )

            else:
                st.error(
                    f"Backend Error: {response.status_code}"
                )

        except Exception as e:
            st.error(
                f"Error connecting to backend: {e}"
            )

st.divider()

# ---------------------------
# Chat History
# ---------------------------

if len(st.session_state.messages) > 0:

    st.header("💬 Chat History")

    for role, message in st.session_state.messages:

        if role == "You":

            st.info(
                f"You: {message}"
            )

        else:

            st.success(
                f"Assistant: {message}"
            )