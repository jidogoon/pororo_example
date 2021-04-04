import uvicorn as uvicorn
from pororo import Pororo
from fastapi import FastAPI

app = FastAPI()


@app.post("/api/text_summarization")
def read_item(input_text: str):
    return {
        "input_text": input_text,
        "summarized_text": get_text_summarization(input_text)
    }


def get_text_summarization(input_text: str) -> str:
    summarization = Pororo(task="text_summarization", lang="ko", model="abstractive")
    return summarization(input_text)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
