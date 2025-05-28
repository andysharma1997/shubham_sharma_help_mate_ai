import os
from openai import OpenAI
from app.utilities.constants import Constants



def generate_prompt(query, top_chunks):
    context = "\n\n".join([f"Chunk {i+1}:\n{chunk}" for i, chunk in enumerate(top_chunks)])
    prompt = f"""
            You are an insurance policy assistant. Answer the following question using only the content from the provided chunks.
            If the answer is not found, respond with "Not specified in the document."

            Question: {query}

            Relevant Chunks:
            {context}

            Answer:
            """
    return prompt

def get_answer_from_openai(prompt, model=Constants.fetch_constant("generation_config")["model_name"], temperature=Constants.fetch_constant("generation_config")["temprature"]):
    client = OpenAI()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers based only on the insurance policy document."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature
    )
    return response.choices[0].message.content
