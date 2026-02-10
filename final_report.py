from agents.transcript_analyzer import USE_MOCK as TA_MOCK
from agents.transcript_analyzer import load_transcript
from agents.sales_coach import sales_coach_analysis, load_rag
from agents.objection_expert import objection_analysis


def generate_final_report():
    transcript_text = load_transcript()
    vector_db = load_rag()


    # Agent 1 Output
    transcript_analysis = """
CALL SUMMARY:
- The call focuses on introducing a product and discussing pricing.
- The customer is interested but hesitant.
- Overall tone is neutral with mild hesitation.
"""

    # Agent 2 Output
    sales_knowledge = vector_db.similarity_search(
        "sales discovery questions and closing techniques", k=3
    )
    sales_context = "\n".join([doc.page_content for doc in sales_knowledge])

    sales_coach_output = sales_coach_analysis(transcript_text, sales_context)


    # Agent 3 Output
    objection_knowledge = vector_db.similarity_search(
        "handling price objections and customer hesitation", k=3
    )
    objection_context = "\n".join([doc.page_content for doc in objection_knowledge])

    objection_output = objection_analysis(transcript_text, objection_context)


    # Final Combined Report
    final_report = f"""
FINAL SALES CALL ANALYSIS REPORT

{transcript_analysis}

SALES COACH FEEDBACK:
{sales_coach_output}

OBJECTION & MISSED OPPORTUNITY ANALYSIS:
{objection_output}

RECOMMENDED NEXT ACTIONS:
- Follow up with the customer addressing pricing concerns clearly.
- Ask deeper discovery questions to understand budget and timeline.
- End future calls with a clear next step or closing question.
---------------------------------------------------------------------
    """

    return final_report


if __name__ == "__main__":
    report = generate_final_report()
    print(report)