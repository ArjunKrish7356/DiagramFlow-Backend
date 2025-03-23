from openai import OpenAI
from fetchFromChromaDB import query_chromadb
import json

def generate_response(question):
    """
    Generate a response to a question using OpenAI API with context from ChromaDB and codebase information.
    
    Args:
        question (str): The question to answer
        
    Returns:
        str: The generated response from the AI model
    """
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
    )

    fetch_context = query_chromadb(question)

    with open("./formats/codebase.json","r") as f:
        data = json.load(f)

    with open("./formats/Charts.json", "r") as f:
        charts = json.load(f)

    prompt = f"""
    You are a coding assistant for a **specific project**. Answer the following question strictly based on the provided **codebase, architecture, and diagrams**.

    ### Question:
    {question}

    ### Relevant Code Snippets:
    {fetch_context}

    ### Codebase Overview:
    {json.dumps(data, indent=2)}

    ### Diagram Templates:
    {json.dumps(charts, indent=2)}

    Your answer must:
    1. **Strictly use the provided context** from the codebase, snippets, and diagrams. Do not generate information that is not supported by this context.
    2. Provide a clear and precise answer to the question, ensuring it aligns with the project's actual implementation.
    3. When the question involves system design, architecture, or workflows, include two or more **relevant** diagrams using Mermaid syntax:
       - Format the diagrams within triple backticks with 'mermaid.js' specified, for example:
         ```mermaid.js
         graph LR
           A --> B
         ```
       - Use the provided diagram templates as a guide. **Do not create random or unrelated images**.
    4.Ensure that there is no error in the diagrams.

    Stay strictly relevant to the project at all times.
    """



    completion = client.chat.completions.create(
        model="google/gemini-2.0-flash-exp:free",
        messages=[
            {
                "role": "user",
                "content": f"{prompt}"
            }
        ],
    )

    return completion.choices[0].message.content

    # for chunk in completion:
    #     if chunk.choices[0].delta.content:
    #         yield f"data: {chunk.choices[0].delta.content}\n\n"
    
    # yield "data: [DONE]\n\n"  # End of response signal


# Example usage
if __name__ == "__main__":
    example_question = "basic architecture?"
    generate_response(example_question)
    