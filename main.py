from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, JSONResponse
import pdfkit
import io

app = FastAPI()

@app.post("/html-to-pdf")
async def html_to_pdf(request: Request):
    try:
        data = await request.json()
        html_content = data.get("html")

        if not html_content:
            return JSONResponse(status_code=400, content={"error": "No HTML content provided"})

        config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")  # Path inside Docker image

        pdf_bytes = pdfkit.from_string(html_content, False, configuration=config)

        if not pdf_bytes:
            return JSONResponse(status_code=500, content={"error": "PDF generation failed: pdf_bytes is None"})

        return StreamingResponse(io.BytesIO(pdf_bytes), media_type="application/pdf", headers={
            "Content-Disposition": "attachment; filename=output.pdf"
        })

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
