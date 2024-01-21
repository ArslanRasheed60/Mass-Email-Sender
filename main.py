from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

#internal imports
from email_service import send_email
from model import EmailModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create twilio sub account
@app.post("/send-emails/")
async def create_subaccount(emailModel: EmailModel):
    
    try:
        recipients_list = emailModel.recipient
        subject = emailModel.subject
        content = emailModel.content
        
        for recipient in recipients_list:
            send_email(subject, content, recipient)
        return JSONResponse(status_code=200, content={"details": "Emails Sent Successfully"})
    except Exception as e:
        print(f"Error while sending an emails: {e}")
        return JSONResponse(status_code=500, content={"details": "An error occurred while processing the request"})

if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI app with Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

