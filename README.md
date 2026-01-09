## 🚀 AI-Powered LinkedIn Post Generator (GenAI Project)

This project is an AI-powered LinkedIn post generation tool built using Generative AI and LLMs.
It helps users create natural, professional LinkedIn posts by selecting a topic, length, and language (English or Hinglish).

The system leverages few-shot learning to guide the LLM toward a realistic LinkedIn writing style rather than generic AI text.

## ✨ Key Features

Generate LinkedIn posts with a natural, professional tone

Supports English and Hinglish

Control post length (Short / Medium / Long)

Uses few-shot examples to improve writing quality

Simple and clean Streamlit UI

Powered by Groq LLMs (Llama models)

## 🧠 How It Works (High-Level Flow)

Previously written LinkedIn posts are processed and structured.

Metadata such as topic, language, and length is extracted.

Relevant examples are selected for few-shot prompting.

A custom prompt is generated and sent to the LLM.

The LLM generates a LinkedIn-ready post matching the desired style.

## 🏗️ System Architecture
<img src="resources/architecture.jpg"/>

Stages:

Data Processing – Analyze and structure LinkedIn post data

Few-Shot Selection – Choose relevant examples based on user input

LLM Generation – Generate a post using prompt engineering

UI Layer – User interacts via Streamlit

## 🛠️ Tech Stack

Python

LangChain

Groq LLM (Llama)

Streamlit

Few-shot Prompting

Environment-based API key management

## ⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/Pa-rth518/linkedin-post-generator.git
cd linkedin-post-generator

2️⃣ Create Virtual Environment (Recommended)
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file:

GROQ_API_KEY=your_api_key_here


⚠️ Never push .env to GitHub.

5️⃣ Run the Application
streamlit run main.py

## 📌 Project Motivation

Most AI-generated LinkedIn posts feel robotic or unnatural.
This project focuses on human-like tone, context awareness, and real LinkedIn writing patterns, making the output suitable for real professional use.

📷 Demo / Screenshots
<img src="resources/tool.jpg"/>

## 📄 License

This project is built for learning and portfolio purposes.
Inspired by open-source GenAI workflows, but fully customized and implemented independently.

## 👤 Author

Parth Godage
GenAI | LLM | RAG | LangChain | Python
🔗 GitHub: https://github.com/Pa-rth518
