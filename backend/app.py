<<<<<<< HEAD
from flask import Flask, request, jsonify
from AgenticAutogen import tax_calculation_agent, user_context_agent, tax_optimization_agent, user_proxy

=======
import openai
from flask import Flask, jsonify
import random
from flask_cors import CORS
import os
>>>>>>> 76f18200639220069b1ac87e87890737a6073086

app = Flask(__name__)
CORS(app)

<<<<<<< HEAD
@app.route('/calculate_tax', methods=['POST'])
def calculate_tax():
    user_data = request.json
    # Initiate conversation with Tax Calculation Agent
    response = user_proxy.initiate_chat(
        tax_calculation_agent,
        message=f"Calculate tax for the following data: {user_data}"
    )
    return jsonify(response)

@app.route('/optimize_tax', methods=['POST'])
def optimize_tax():
    user_data = request.json
    # Initiate conversation with Tax Optimization Agent
    response = user_proxy.initiate_chat(
        tax_optimization_agent,
        message=f"Suggest tax-saving strategies for the following data: {user_data}"
    )
    return jsonify(response)

@app.route('/fill_form', methods=['POST'])
def fill_form():
    user_data = request.json
    # Initiate conversation with User Context Agent
    response = user_proxy.initiate_chat(
        user_context_agent,
        message=f"Assist in filling the tax return form with the following data: {user_data}"
    )
    return jsonify(response)
=======
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
>>>>>>> 76f18200639220069b1ac87e87890737a6073086

if __name__ == '__main__':
    app.run(debug=True)
