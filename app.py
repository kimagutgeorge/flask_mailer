# imports
from flask import Flask, jsonify, request
from flask_mail import Mail, Message
from flask_cors import CORS
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

# Initialize Flask app
app = Flask(__name__)

# Configure CORS
CORS(app, resources={r"/*": {"origins": ["http://localhost:8081", "http://127.0.0.1:8081"]}}, supports_credentials=True)

# Configure Flask-Mail
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME") 
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD") 
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_USERNAME")

# Initialize Flask-Mail
mail = Mail(app)

@app.route("/send-email", methods=["POST"])
def send_email():
    try:
        # Extract data from the request
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Validate required fields
        if not all([name, email, subject, message]):
            return jsonify({"error": "Missing required fields"}), 400

        # Create and send the email
        msg = Message(
            subject=f"New Message from {name}",
            recipients=[""]  # Replace with your recipient email
        )
        msg.body = f"""
        Name: {name}
        Email: {email}
        Subject: {subject}

        Message:
        {message}
        """

        mail.send(msg)
        return jsonify({"message": "1"}), 200

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)