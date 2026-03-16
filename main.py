from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def analyze(symptoms, lifestyle, history, age, gender):

    prompt_template = ChatPromptTemplate.from_template("""
You are a certified health educator providing ONLY general wellness guidance.
You MUST NOT provide diagnosis, treatment, prescriptions, or medical claims.

Analyze the following:
Symptoms: {symptoms}
Lifestyle: {lifestyle}
History: {history}
Age: {age}
Gender: {gender}

Return ONLY a JSON object in this EXACT structure:


{{ 
    "General Wellness Insights": "string",
    "Possible Non-Diagnostic Considerations": ["string"],
    "Risk Awareness": ["string"],
    "Lifestyle Suggestions": ["string"],
    "When to Seek Medical Care": ["string"],
    "Emergency Warning Signs": ["string"],
    "Overall Wellness Support Score": 0,
    "Summary": "string",
    "Safety Disclaimer": "string"
}}


Rules:
- DO NOT diagnose.
- DO NOT recommend medication.
- Avoid medical claims.
- Provide only general safety and wellness guidance.
- Output JSON ONLY.
""")

    llm = ChatOllama(
        model="llama3.2:3b",
        temperature=0.1
    )

    chain = prompt_template | llm | StrOutputParser()

    response = chain.invoke({
        "symptoms": symptoms,
        "lifestyle": lifestyle,
        "history": history,
        "age": age,
        "gender": gender
    })

    return response
