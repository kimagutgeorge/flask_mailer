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
CORS(app, resources={r"/*": {"origins": ["http://localhost:8080", "http://127.0.0.1:8081"]}}, supports_credentials=True)

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
        msg.html = f"""
        <html>
            <head>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        color: #333;
                        padding: 20px;
                    }}
                    .email-container {{
                        background-color: #fff;
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        max-width: 600px;
                        margin: 0 auto;
                    }}
                    h1 {{
                        color: #303030;
                        font-size: 18px;
                        margin-bottom: 20px;
                        width:100%;
                        background-color: rgb(240, 240, 240);
                        padding: 10px 10px;
                    }}
                    p {{
                        font-size: 16px;
                        line-height: 1.6;
                        margin-bottom: 10px;
                        padding-left: 10px;
                    }}
                    .label {{
                        font-weight: bold;
                        color: #555;
                        padding-left: 10px;
                    }}
                    .sbjt{{
                        font-weight:bold;
                        font-size: 20px;
                        padding-left: 20px;
                    }}
                    .msg{{
                        padding-left: 20px;
                    }}
                </style>
            </head>
            <body>
                <div class="email-container">
                    <h1>New Message Received</h1>
                    <p><span class="label">Name:</span> {name}</p>
                    <p><span class="label">Email:</span> {email}</p>
                    <p class="sbjt">{subject}</p>
                    <p class="msg">{message}</p>
                </div>
            </body>
        </html>
        """

        mail.send(msg)
        return jsonify({"message": "1"}), 200

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    
# send enquirires
@app.route("/send-enquiry", methods = ['POST'])
def sendEnquiry():
    try:
        # Extract data from the request
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        service = request.form.get('service')

        # Validate required fields
        if not all([name, email, subject, message, service]):
            return jsonify({"error": "Missing required fields"}), 400

        # Create and send the email
        msg = Message(
            subject=f"New Enquiry from {name}",
            recipients=[""]  # Replace with your recipient email
        )
        # HTML content for the email
        msg.html = f"""
        <html>
            <head>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        color: #333;
                        padding: 20px;
                    }}
                    .email-container {{
                        background-color: #fff;
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        max-width: 600px;
                        margin: 0 auto;
                    }}
                    h1 {{
                        color: #303030;
                        font-size: 18px;
                        margin-bottom: 20px;
                        width:100%;
                        background-color: rgb(240, 240, 240);
                        padding: 10px 10px;
                    }}
                    p {{
                        font-size: 16px;
                        line-height: 1.6;
                        margin-bottom: 10px;
                    }}
                    .label {{
                        font-weight: bold;
                        color: #555;
                    }}
                    .sbjt{{
                        font-weight:bold;
                        font-size: 20px;
                    }}
                </style>
            </head>
            <body>
                <div class="email-container">
                    <h1>New Enquiry Received</h1>
                    <p><span class="label">Name:</span> {name}</p>
                    <p><span class="label">Email:</span> {email}</p>
                    <p><span class="label">Service:</span> {service}</p>
                    <p class="sbjt">{subject}</p>
                    <p>{message}</p>
                </div>
            </body>
        </html>
        """

        mail.send(msg)
        return jsonify({"message": "1"}), 200

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)