from fastapi import FastAPI, UploadFile, Form
from api.model import score_match
from api.utils import extract_text_from_pdf, enrich_description
from monitoring.metric import REQUEST_TIME, MATCH_COUNT

app = FastAPI()


@REQUEST_TIME.time()
@app.post("/score/")
async def get_score(resume: UploadFile, job_description: str = Form(...)):
    MATCH_COUNT.inc()
    resume_text = extract_text_from_pdf(resume.file)
    enriched_jd = enrich_description(job_description)
    score = score_match(resume_text, enriched_jd)
    return {"match_score": round(score, 3)}
