# hng-task-1 Number Classification API

A simple Flask API that classifies a given number based on its properties (prime, perfect, armstrong, even/odd) and fetches a fun fact about it.

## Features
- Checks if a number is **prime, perfect, or an Armstrong number**.
- Determines if the number is **even or odd**.
- Calculates the **sum of its digits**.
- Fetches a **fun fact** about the number from [NumbersAPI](http://numbersapi.com/).

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo.git
cd your-repo
```

### 2. Install Dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run the API
```bash
python app.py
```
The API runs on `http://127.0.0.1:5000` by default.

## Usage

### Endpoint: `/api/classify-number`
#### **Request:**
Send a **GET** request with a query parameter:
```bash
http://18.171.137.193:5000/api/classify-number?number=28
```

#### **Response Example:**
```json
{
    "number": 28,
    "is_prime": false,
    "is_perfect": true,
    "properties": ["perfect", "even"],
    "digit_sum": 10,
    "fun_fact": "28 is a perfect number, equal to the sum of its divisors."
}
```

## Testing
- During testing, **Postman** was used to send API requests and inspect responses.
- You can also test with **cURL**:
  ```bash
  curl "http://127.0.0.1:5000/api/classify-number?number=7"
  ```

## Deployment
This API was deployed on **AWS EC2** by:
1. Launching an EC2 instance.
2. Installing Python and Flask.
3. Running the API with `gunicorn`.
4. (Optional) Using Nginx as a reverse proxy.


## License
MIT License

---
Built with ❤️ using Flask.

