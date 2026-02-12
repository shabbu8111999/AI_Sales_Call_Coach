from agents.transcript_analyzer import load_transcript, analyze_transcript
from agents.sales_coach import sales_coach_analysis, load_rag_snapshot
from agents.objection_expert import objection_analysis


def generate_final_report():
    # Load transcript
    transcript_text = load_transcript()

    # Load lightweight RAG knowledge
    rag_context = load_rag_snapshot()

    # Agent 1: Transcript Analyzer
    transcript_analysis = analyze_transcript(transcript_text)

    # Agent 2: Sales Coach 
    sales_coach_output = sales_coach_analysis(
        transcript_text=transcript_text,
        rag_context=rag_context
    )

    # Agent 3: Objection Expert
    objection_output = objection_analysis(
        transcript_text=transcript_text,
        rag_context=rag_context
    )

    # Final Combined Report
    final_report = f"""
 FINAL SALES CALL ANALYSIS REPORT

---------------- CALL SUMMARY -----------------
{transcript_analysis}

---------------- SALES COACH FEEDBACK ----------------
{sales_coach_output}

---------------- OBJECTIONS & MISSED OPPORTUNITIES ----------------
{objection_output}
"""

    return final_report


if __name__ == "__main__":
    report = generate_final_report()
    print(report)
