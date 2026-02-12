# AI-Powered Sales Call Improvement Platform (AWS Native)
## Problem Statement

Sales managers often struggle to manually review sales call recordings to evaluate performance, identify missed opportunities, and provide structured feedback. This process is time-consuming and subjective.
The goal of this project is to build an AI-powered web platform that:

- Accepts a sales call audio recording
- Converts speech to text
- Uses AI with multi-agent orchestration
- Applies sales coaching knowledge via RAG
- Generates actionable feedback for improvement

This simulates a real SaaS product that helps organizations analyze and improve sales conversations using Generative AI.

---

## Project Overview

This project is a web-based AI system that analyzes uploaded sales call recordings and generates structured feedback.

End-to-End Flow:
- User uploads a sales call audio file
- Audio is uploaded to Amazon S3
- AWS Transcribe converts speech to text
- Transcript is analyzed by three AI agents
- Each agent focuses on a different aspect of sales performance
- A final combined report is generated
- Results are displayed in a clean web UI

The system uses modern LangChain orchestration and OpenAI LLM integration to produce structured and professional analysis.

---

## Project Structure
<pre>
AI_Sales_Call_Coach/
│
├── agents/
│   ├── objection_expert.py
│   ├── sales_coach.py
│   └── transcript_analyzer.py
│
├── backend/
│   ├── clean_transcript.txt
│   ├── rag_snapshot.txt
│   ├── transcribe_audio.py
│   └── upload_to_s3.py
│
├── knowledge_base/
│   ├── closing_techniques.txt
│   ├── discovery_questions.txt
│   ├── objection_handling.txt
│   └── tone_and_empathy.txt
│
├── static/
│   ├── css/style.css
│   └── js/main.js
│
├── templates/
│   └── index.html
│
├── uploads/
├── vector_db/
│
├── app.py
├── final_report.py
├── llm_config.py
├── requirements.txt
└── README.md
</pre>

---

## Technologies Used

- Speech to Text: AWS Transcribe
- LLM: OpenAI (gpt-3.5-turbo)
- AI Orchestration: LangChain (Python)
- Agents: LangChain multi-agent system
- RAG: FAISS vector store (local integration)
- Storage: Amazon S3
- Backend: Python (Flask)
- Frontend: Simple HTML, CSS, JavaScript
- Hosting: Render

---

## Multi-Agent System

### 1. Transcript Analyzer
**Role: Understand the full conversation.**

It reads the entire call and answers:

- What was the call about?
- What did the customer want?
- What was the customer concerned about?
- Was the tone positive, neutral, or negative?

This agent focuses only on understanding the conversation.

### 2. Sales Coach
**Role: Evaluate the salesperson’s performance.**

It checks:

- What the salesperson did well
- What could be improved
- Any missed selling opportunities
- Suggestions for better performance

This agent focuses only on improving sales skills.

### 3. Objection Expert
**Role: Handle customer objections properly.**

It detects:

- Did the customer raise objections?
- Were they handled correctly?
- If not, how should they have been handled?

This agent focuses only on objection handling.

---

## RAG (Retrieval-Augmented Generation)

The system includes a sales coaching knowledge base containing:

- Objection handling best practices
- Discovery questions
- Closing techniques
- Tone and empathy guidelines

FAISS is used locally for vector embedding.

---

## UI Workflow (Backend Explanation)

When a user uploads audio:

- Audio is saved locally.
- File is uploaded to Amazon S3.
- AWS Transcribe is triggered.
- System waits until transcription is completed.
- Transcript is stored in "clean_transcript.txt".
- Transcript is passed to three AI agents.
- Final report is generated.
- Transcript and report are returned as JSON.
- UI displays structured analysis.

The UI is simple but simulates a real SaaS dashboard.

---

## LLM Orchestration (Modern LangChain Style)

The project uses LangChain’s modern LCEL (LanChain Expression Language) chaining method:
LCEL is a simple and modern chaining syntax in LangChain.

```bash
prompt = PromptTemplate.from_template(template)
chain = prompt | llm
response = chain.invoke({"transcript": transcript})
```

Advantages:

- Clean modular design
- Easy LLM swapping
- Better maintainability
- Production-ready structure

---

## Challenges Faced

- AWS Bedrock quota limitations (model invocation quota set to zero)
- Render free-tier RAM limitations (512MB)
- FAISS and sentence-transformers causing memory issues in deployment
- Speech-to-text inaccuracies (e.g., name misinterpretation like "Daksh" → "Dax")
- Ensuring dynamic transcription instead of static transcript reuse

---

## Debugging & Troubleshooting

- Identified Bedrock throttling issue using AWS Service Quotas
- Raised AWS support ticket
- Switched LLM provider to OpenAI after approval
- Re-architected agents using modern LangChain LCEL
- Removed heavy embedding models from production environment
- Implemented dynamic Transcribe flow to avoid repeated outputs
- Validated Free Tier usage through AWS billing dashboard

---

## Key Learnings

- Proper cloud quota monitoring is essential
- Multi-agent architecture improves modular AI systems
- Lightweight production design matters in limited environments
- Separating LLM layer improves flexibility
- Real SaaS systems require proper asynchronous workflows

---

## Final Outcome

The system successfully:

- Accepts multiple different audio files
- Dynamically transcribes each file
- Produces unique AI-driven analysis
- Provides structured and actionable feedback
- Simulates a real-world AI SaaS sales coaching platform