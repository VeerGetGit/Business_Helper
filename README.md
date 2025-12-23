AI-Based Automation Tool for Converting Business Requirements into Technical Specifications
1. Project Overview

This project presents an AI-based automation tool designed to convert high-level business requirements into detailed technical specifications. The system automatically generates system modules, database schemas, and pseudo code by analyzing natural language inputs.

The solution leverages Generative Artificial Intelligence using openai-gpt-oss120B via the Groq API to assist in early-stage software design. The primary objective is to reduce manual design effort, improve consistency, and accelerate the software development lifecycle.

2. Features

Automated transformation of business requirements into technical specifications

Generation of:

System modules

Database schema

Pseudo code

Identification of missing or ambiguous requirements

Structured output in JSON format

Backend API implemented using Flask

Frontend user interface developed with Streamlit

Simulation of multiple architectural perspectives:

Software Architect

Backend Architect

Database Architect

Security Architect

3. Technologies Used

Python

Flask (Backend API)

Streamlit (Frontend Interface)

Groq API

openai-gpt-oss120B

JSON

4. System Architecture
4.1 Frontend Layer (Streamlit)

The frontend provides a user interface where business requirements can be entered and the generated technical specifications can be reviewed.

4.2 Backend Layer (Flask)

The backend manages incoming requests, constructs architect-level prompts, communicates with the AI model, and returns structured responses.

4.3 AI Processing Layer

The AI layer, powered by Groq API and openai-gpt-oss120B, analyzes business requirements and produces system modules, database schemas, and pseudo code in a structured format.

5. Workflow

The user submits high-level business requirements through the frontend.

The backend generates an architect-level prompt.

The AI model processes the input and derives technical specifications.

The output is returned in structured JSON format.

The frontend displays the generated results
