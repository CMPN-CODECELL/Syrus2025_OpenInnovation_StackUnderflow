from flask import Flask, request, jsonify
from AgenticAutogen import tax_calculation_agent, user_context_agent, tax_optimization_agent, user_proxy


app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
