TalentScout: Hiring Assistant Chatbot
🌟 Overview
TalentScout is a hiring assistant chatbot designed to streamline the hiring process. It guides candidates through the interview preparation journey by gathering essential details and generating personalized technical interview questions based on the candidate's experience, desired position, and tech stack. The tool uses AI to simulate interview scenarios, improving the recruitment process.
🛠️ Features
Candidate Details Collection: Collects essential details such as:
Full name
Email address
Phone number
Years of experience
Desired position(s)
Current location
Tech stack
Technical Interview Question Generation: Uses AI to generate relevant technical questions based on the candidate's experience and tech stack.
Anonymized Data Handling: Ensures all personal data is anonymized for privacy.
Real-Time Progress Tracking: Provides feedback and progress simulation to keep the user informed.
Fallback Mechanism: Offers meaningful responses for unexpected or unclear user inputs.
.
🚀 Setup & Installation
Follow these steps to set up the project locally:

Prerequisites
Python 3.x
Streamlit (for the front-end interface)
Groq (AI API for generating technical questions)
A GitHub account (for version control)
1. Clone the repository
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/venkat1004/talentscout.git
2. Set up the virtual environment
Create and activate a virtual environment:

bash
Copy code
# Create virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
3. Install dependencies
Install the required Python packages using the requirements.txt file:

bash
Copy code
pip install -r requirements.txt
4. Set up Groq API Key
Obtain your Groq API key and configure it in the backend.py file. Add the following line:

python
Copy code
client = Groq(api_key="YOUR_API_KEY_HERE")
Replace "YOUR_API_KEY_HERE" with your actual Groq API key.

🧑‍💻 Usage
Run the Application Locally
To run the application on your local machine, use:

bash
Copy code
streamlit run app.py
This will start a local web server. Open your browser and navigate to http://localhost:8501 to use the app.

🔧 Development
Adding New Features
Contributions are welcome! To add a new feature or fix a bug:

Fork the repository.
Create a new branch for your feature.
Write tests for new functionality.
Ensure that all tests pass.
Create a Pull Request (PR) with a detailed explanation of the changes.

👥 Contributing
Feel free to open issues, fork the repository, or submit pull requests to contribute to the project.

📄 License
This project is open-source and available under the MIT License.


