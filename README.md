🤖 AI-Based Automation Tool for Converting Business Requirements into Technical Specifications
📌 Project Overview

This project is an AI-powered automation tool that converts high-level business requirements into low-level technical specifications, including:

System modules

Database schemas

Pseudo code

It leverages Generative AI using openai-gpt-oss120B via the Groq API to analyze natural language requirements and generate structured, developer-ready outputs.

✨ The tool is designed to:

Reduce manual effort

Improve consistency

Accelerate system design in real-world software development projects

🚀 Features

Automated conversion of business requirements into technical specifications

Generates:

System modules

Database schema

Pseudo code

Detects missing or unclear requirements

Provides structured JSON output

Flask backend API with Streamlit frontend

Simulates a panel of architects:

Software Architect

Backend Architect

Database Architect

Security Architect

🛠️ Technologies Used

Python

Flask – Backend API

Streamlit – Frontend UI

Groq API

openai-gpt-oss120B

JSON

🏗️ System Architecture
🔹 Frontend (Streamlit)

User interface to input business requirements

Displays generated technical specifications

🔹 Backend (Flask)

Handles API requests

Constructs architect-level AI prompts

Returns structured JSON responses

🔹 AI Layer (Groq + openai-gpt-oss120B)

Analyzes high-level requirements

Generates:

System modules

Database schemas

Pseudo code

Architecture insights

🔄 Workflow

User submits a high-level business requirement

Backend constructs an architect-level prompt

AI analyzes the requirement

Technical specifications are generated

Results are returned in structured JSON

Output is displayed on the Streamlit UI

⚙️ Setup Instructions
🔹 Clone the Repository
git clone https://github.com/your-username/business-gen-ai.git
cd business-gen-ai

🔹 Install Dependencies
pip install -r requirements.txt

🔹 Configure Environment Variables

Create a .env file and add your Groq API key:

GROQ_API_KEY=your_api_key_here


⚠️ Important: Keep your API key private.

🔹 Run the Flask Backend
python app.py

🔹 Run the Streamlit Frontend
streamlit run frontend.py
