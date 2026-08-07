from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
from io import BytesIO
from pypdf import PdfReader
from docx import Document
from fastapi.middleware.cors import CORSMiddleware

from Bot import ChatBot

app = FastAPI()

bots: dict[str, ChatBot] = {}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str
    session_id: str


@app.post("/chat")
async def chat(request: ChatRequest):

    if request.session_id not in bots:
        bots[request.session_id] = ChatBot()

    bot = bots[request.session_id]

    answer = bot.chat(request.message)

    return {
        "answer": answer
    }


@app.post("/upload")
async def upload(
    session_id: str = Form(...),
    file: UploadFile = File(...)
):

    text = await read_uploaded_document(file)

    if text is None:
        return {"error": "Unsupported file"}

    if session_id not in bots:
        bots[session_id] = ChatBot()

    bot = bots[session_id]

    bot.uploaded_text = text

    return {"message": "File uploaded successfully."}


async def read_uploaded_document(file: UploadFile):

    contents = await file.read()

    if file.filename.endswith(".txt"):

        text = contents.decode("utf-8")

        return text

    elif file.filename.endswith(".pdf"):

        pdf = PdfReader(BytesIO(contents))

        text = ""

        for page in pdf.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

        return text

    elif file.filename.endswith(".docx"):

        doc = Document(BytesIO(contents))

        text = ""

        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"

        return text

    return None