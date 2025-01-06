import streamlit as st
from backend import hash_data, query_llama, simulate_progress

# Apply custom CSS
st.markdown(
    """
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f5f5f5;
    }
    .main {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #4CAF50;
    }
    .btn-primary {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize Streamlit app
st.title("🌟 TalentScout: Hiring Assistant Chatbot")
st.markdown(
    "Welcome to **TalentScout's Hiring Assistant**! I’m here to guide you through the screening process with a few simple steps. Let’s get started! 😊"
)

# Show a progress bar for flow tracking
progress = st.progress(0)

# Initialize session state for tracking conversation
if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "step" not in st.session_state:
    st.session_state.step = 0

# Collect Candidate Details
if st.session_state.step == 0:
    st.subheader("Candidate Details")
    name = st.text_input("Full Name:").strip()
    email = st.text_input("Email Address:").strip()
    phone = st.text_input("Phone Number:").strip()
    experience = st.text_input("Years of Experience:").strip()
    position = st.text_input("Desired Position(s):").strip()
    location = st.text_input("Current Location:").strip()
    tech_stack = st.text_area("Tech Stack (programming languages, frameworks, tools):").strip()

    if st.button("Submit"):
        # Validate if any field is empty
        if not name or not email or not phone or not experience or not position or not location or not tech_stack:
            st.error("Please fill in all the fields before submitting!")
        else:
            anonymized_name = f"Candidate-{hash_data(name)}"
            anonymized_email = f"anon-{hash_data(email)}@example.com"
            anonymized_phone = f"+XXXXXXX-{phone[-4:]}"
            st.session_state.conversation.extend([
                {"role": "user", "content": f"My name is {anonymized_name}"},
                {"role": "user", "content": f"My anonymized email is {anonymized_email}, my anonymized phone is {anonymized_phone}"},
                {"role": "user", "content": f"I have {experience} years of experience."},
                {"role": "user", "content": f"I am applying for the position(s): {position}."},
                {"role": "user", "content": f"My current location is {location}."},
                {"role": "user", "content": f"My tech stack includes {tech_stack}."},
            ])

            st.write(f"Thank you for sharing your details, {anonymized_name}! 😊")
            st.write("Analyzing your expertise and generating questions...")

            # Simulate progress bar
            simulate_progress()

            # Proceed to the next step
            st.session_state.step = 1
            progress.progress(50)

# Generate technical questions after collecting details
if st.session_state.step == 1:
    response = query_llama(
        st.session_state.conversation
        + [{"role": "user", "content": f"Generate 3-5 technical questions for {tech_stack}, focusing on {experience} years of experience"}]
    )

    if response:
        if "Unexpected error occurred" in response or "issue processing your request" in response:
            st.warning("The chatbot could not generate questions based on the input. Please refine the details and try again.")
        else:
            st.subheader("Personalized Technical Questions")
            st.write(response)
            st.session_state.step = 2
            progress.progress(100)
    else:
        st.error("Failed to generate questions. Please try again.")
        st.session_state.step = 0

# Final step (e.g., End the conversation)
if st.session_state.step == 2:
    st.subheader("Final Steps")
    st.write("Thank you for providing all the required details! We’ll review your profile and get back to you soon. 😊")
    if st.button("End Conversation"):
        st.write("Conversation ended. Have a great day!")
        st.session_state.step = 0
        progress.progress(0)
