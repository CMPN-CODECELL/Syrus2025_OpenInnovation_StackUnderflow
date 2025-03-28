import openai
from flask import Flask, jsonify
import random
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Set your OpenAI API key
openai.api_key = "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"  # Replace with your actual API key

def generate_tax_questions():
    prompt = """
    Generate 5 multiple-choice questions related to Indian income tax rules. 
    Each question should have a statement and a correct answer.
    Format:
    [
      {"question": "Your tax-related statement here.", "answer": "right/left"},
      ...
    ]
    "right" means it's a correct tax strategy.
    "left" means it's a tax mistake.
    """

    try:
        response = openai.chat.completions.create(
            model="gpt-4",  # Use "gpt-3.5-turbo" if needed
            messages=[{"role": "system", "content": "You are a tax expert."},
                      {"role": "user", "content": prompt}],
            temperature=0.7
        )

        # Extract text from response
        generated_text = response.choices[0].message.content.strip()
        
        # Convert response into a valid Python list
        tax_questions = eval(generated_text)  # ⚠️ Ensure OpenAI returns a valid format

        random.shuffle(tax_questions)
        return tax_questions

    except Exception as e:
        print(f"Error generating questions: {e}")
        return [
            {"question": "Error generating questions. Try again later.", "answer": "right"}
        ]

@app.route('/get_questions', methods=['GET'])
def get_questions():
    questions = generate_tax_questions()
    return jsonify(questions)

if __name__ == '__main__':
    app.run(debug=True)
