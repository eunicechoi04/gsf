from openai import OpenAI

client = OpenAI(api_key="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")
prompt = """
General Medical Relevance:
Assess the following prompt for relevance and comprehensibility in a general medical FAQ system:

Mouth, Surgery, or Symptoms of Cleft Lip Surgery:
For the same prompt, evaluate the relevance of the following prompt to a context involving the mouth, surgery, or symptoms of cleft lip surgery. Consider medical concerns related to baby, surgery, and mouth. Relevant symptoms may include:

Profuse bleeding or greater than 5 minutes
Pus at the surgery site
Profuse vomiting
Profuse diarrhea
Fever (temperature greater than 38.4 °C)
Lack of appetite
Significant bad breath
Changes in urine (amount or color)

Reply with “relevant” for the prompt if and only if it is relevant to either evaluations.
Reply with “irrelevant” for the prompt if and only if it is irrelevant to both evaluations.

Prompt: 
"""
prompt += input("Enter some words bro:  ")
chat_completion = client.chat.completions.create(
    messages=[{"role": "user", "content": prompt}], 
    model="gpt-4"
)
response_text = chat_completion.choices[0].message.content
print(response_text)
