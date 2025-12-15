# Serverless URL Shortener 🚀

A simple **serverless URL shortener** built on AWS using **API Gateway, Lambda, and DynamoDB**.  
This project demonstrates serverless architecture, routing, UUID generation, and DynamoDB integration.

---

## 🛠️ Technologies Used

- **AWS Lambda** (Python)
- **API Gateway**
- **DynamoDB**
- **IAM Roles**
- **Python 3.x**
- Optional: **CloudWatch** for logging

---

## 📌 Features

- Shorten URLs and store mapping in DynamoDB
- Redirect users from short URL to original URL
- Optional: Click analytics with timestamp and counter
- Fully serverless – no EC2 needed

---

## 📈 Architecture Diagram

<img width="375" height="467" alt="Screenshot 2025-12-02 at 13 49 20" src="https://github.com/user-attachments/assets/e1db78d1-7c41-45c1-a25e-3cb770b07e2f" />

---

## 🗂️ Project Structure

aws-serverless-url-shortener/
│
├─ infra/ # CloudFormation / SAM templates
├─ src/
│ ├─ createShortUrl/
│ │ └─ index.py # POST Lambda to create short URLs
│ └─ redirect/
│ └─ index.py # GET Lambda to redirect
├─ template.yaml # SAM template defining resources
└─ README.md

---

## ⚡ Deployment

1️⃣ Package & deploy with SAM CLI

sam build
sam deploy --guided

2️⃣ Environment variables

TABLE_NAME → Name of your DynamoDB table (e.g., UrlShortener)

3️⃣ IAM Permissions

Lambdas require access to DynamoDB:

{
  "Effect": "Allow",
  "Action": [
    'dynamodb:GetItem',
    "dynamodb:PutItem",
    "dynamodb:UpdateItem"
  ],
  "Resource": "arn:aws:dynamodb:<region>:<account-id>:table/UrlShortener"
}

* > Note: For simplicity, the Lambdas in this repo currently use DynamoDB FullAccess.  
> In production, you should restrict access to only the required table as shown above.


