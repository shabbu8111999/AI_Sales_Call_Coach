from agents.transcript_analyzer import load_transcript, analyze_transcript
from agents.sales_coach import sales_coach_analysis
from agents.objection_expert import objection_analysis


def generate_final_report():
    # Load transcript
    transcript_text = load_transcript()

    # -------- Agent 1: Transcript Analyzer (Bedrock) --------
    transcript_analysis = analyze_transcript(transcript_text)

    # -------- Agent 2: Sales Coach (Bedrock + RAG Snapshot) --------
    sales_coach_output = sales_coach_analysis(
        transcript_text=transcript_text,
        rag_context=""
    )

    # -------- Agent 3: Objection Expert (Bedrock + RAG Snapshot) --------
    objection_output = objection_analysis(
        transcript_text=transcript_text,
        rag_context=""
    )

    # -------- Final Combined Report --------
    final_report = f"""
================ FINAL SALES CALL ANALYSIS REPORT ================

 CALL SUMMARY 
{transcript_analysis}

 SALES COACH FEEDBACK 
{sales_coach_output}

 OBJECTIONS & MISSED OPPORTUNITIES 
{objection_output}

 RECOMMENDED NEXT ACTIONS 
- Follow up with the customer addressing pricing concerns clearly.
- Ask deeper discovery questions to understand budget and timeline.
- End future calls with a clear next step or closing question.

===============================================================
"""

    return final_report


if __name__ == "__main__":
    report = generate_final_report()
    print(report)
