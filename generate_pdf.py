import requests

# Your FastAPI endpoint
url = "http://localhost:8000/html-to-pdf"

# Payload with HTML content
data = {
    "html": "<h1>Hello PDFFF</h1>"
}

# Send POST request
response = requests.post(url, json=data)

# Save PDF if successful
if response.status_code == 200:
    with open("receipt4.pdf", "wb") as f:
        f.write(response.content)
    print("PDF saved as receipt4.pdf")
else:
    print("Error:", response.status_code, response.text)
