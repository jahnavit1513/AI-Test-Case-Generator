# 🧪 AI Test Case Generator

An AI-powered QA assistant built with Python that analyzes software requirements and automatically generates comprehensive test scenarios. The project uses the Groq API and GPT-OSS-20B to assist QA engineers in identifying functional, negative, boundary, UI/UX, accessibility, security, integration, and end-to-end test scenarios.

## 🚀 Features

* Generate functional and positive test cases
* Generate negative test scenarios
* Identify boundary value and edge cases
* Generate equivalence partitioning scenarios
* Generate UI/UX test scenarios
* Identify accessibility scenarios
* Identify security test scenarios
* Generate error-handling and data-validation scenarios
* Analyze integration scenarios
* Identify end-to-end user journeys
* Identify potential Playwright automation candidates
* AI-assisted requirement analysis

## 🛠️ Technology Stack

* **Python** – Core application logic
* **Streamlit** – Web-based user interface
* **Groq API** – AI/LLM integration
* **GPT-OSS-20B** – Requirement analysis and test case generation
* **Playwright** – UI automation candidates
* **JSON** – Test case data representation
* **python-dotenv** – Secure API key management

## 🏗️ Project Structure

```text
AI-Test-Case-Generator/
│
├── app.py
├── ai_test_generator.py
├── prompts.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── Test_cases/
    └── login_tetsts.json
```

## 🔄 How It Works

```text
Software Requirement
        ↓
Requirement Analysis
        ↓
AI Prompt Generation
        ↓
Groq API
        ↓
GPT-OSS-20B
        ↓
QA Test Scenario Generation
        ↓
Test Cases displayed in Streamlit
```

## 💡 Example

### Input

```text
User should be able to log in using a valid email address
and password. The password must contain at least 8 characters.
After successful login, the user should be redirected to the dashboard.
```

### AI Analysis

The application can identify scenarios such as:

* Valid login
* Invalid email
* Invalid password
* Empty email/password
* Invalid email format
* Password boundary conditions
* UI validation
* Error message validation
* Accessibility considerations
* Security scenarios
* Successful dashboard redirection
* End-to-end login journey

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/jahnavit1513/AI-Test-Case-Generator.git
```

Navigate to the project directory:

```bash
cd AI-Test-Case-Generator
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔐 API Configuration

Create a `.env` file in the project root:

```text
GROQ_API_KEY=your_groq_api_key
```

Replace `your_groq_api_key` with your own Groq API key.

**Never commit or publish your actual API key.**

The `.env` file is excluded from Git using `.gitignore`.

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

Enter a software requirement and click **Generate Test Cases**.

## 🎯 Future Enhancements

* Export generated test cases to Excel
* Generate structured test-case tables
* AI-based requirement ambiguity detection
* Automatic test-case prioritization
* Generate Playwright automation scripts
* Generate Robot Framework automation candidates
* AI-powered test failure analysis
* Automated API test generation
* Integration with CI/CD pipelines

## 👩‍💻 Project Goal

The goal of this project is to demonstrate how AI can assist QA engineers by reducing repetitive test-design activities while allowing human testers to focus on critical thinking, product quality, risk assessment, and user experience.


