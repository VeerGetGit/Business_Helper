AI-Based Automation Tool for Converting Business Requirements into Technical Specifications
Project Overview

This project is an AI-powered automation tool that converts high-level business requirements into low-level technical specifications, including system modules, database schemas, and pseudo code. It leverages Generative AI (openai-gpt-oss120B via Groq API) to analyze natural language requirements and generate structured, developer-ready outputs.

The tool is designed to reduce manual effort, improve consistency, and support faster system design in real-world software development.

Features

Automated conversion of business requirements into technical specifications

Generates:

System modules

Database schema

Pseudo code

Detects missing or unclear requirements

Provides structured JSON output

Flask backend API with Streamlit frontend for user interaction

Simulates a panel of architects (Software, Backend, Database, Security)

Technologies Used

Python

Flask (Backend API)

Streamlit (Frontend UI)

Groq API

openai-gpt-oss120B

JSON

System Architecture

Frontend (Streamlit):
User interface to input business requirements and view generated specifications.

Backend (Flask):
Handles API requests, orchestrates AI prompts, and returns structured JSON responses.

AI Layer (Groq + openai-gpt-oss120B):
Processes high-level requirements and generates modules, database schemas, pseudo code, and architecture diagrams.

Workflow

User submits a high-level business requirement.

Backend constructs an architect-level prompt for the AI.

AI analyzes the requirement and generates technical specifications.

Results are returned in structured JSON format and displayed on the UI.

Setup Instructions

Clone the repository:

git clone https://github.com/your-username/business-gen-ai.git
cd business-gen-ai


Install dependencies:

pip install -r requirements.txt


Create a .env file and add your Groq API key:

GROQ_API_KEY=your_api_key_here


Run the Flask backend:

python app.py


Run the Streamlit frontend:

streamlit run frontend.py

