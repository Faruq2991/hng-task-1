from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# Helper functions
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is perfect."""
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    num_digits = len(digits)
    return sum(d**num_digits for d in digits) == n

def digit_sum(n):
    """Calculate the sum of the digits of a number."""
    return sum(int(d) for d in str(n))

def get_fun_fact(n):
    """Fetch a fun fact about the number from numbersapi.com."""
    url = f"http://numbersapi.com/{n}/math"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

# API endpoint
@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    # Get the number from the query parameter
    number_input = request.args.get('number')

    # Validate input
    try:
        number = int(number_input)
    except (ValueError, TypeError):
        # Return the exact error response format
        return jsonify({
            "number": number_input if number_input else "alphabet",
            "error": True
        }), 400

    # Determine properties
    properties = []
    if is_prime(number):
        properties.append("prime")
    if is_perfect(number):
        properties.append("perfect")
    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 != 0:
        properties.append("odd")
    else:
        properties.append("even")

    # Fetch fun fact
    fun_fact = get_fun_fact(number)

    # Prepare response
    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": fun_fact
    }

    #return jsonify(response), 200
    # Ensure valid JSON
    return jsonify(response), 200

# Run the app
if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)
