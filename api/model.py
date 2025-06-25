from sentence_transformers import SentenceTransformer, util
import re 
import mlflow

model = SentenceTransformer('all-MiniLM-L6-v2')


def preprocess(text):
    text = re.sub(r'\S+@\S+', ' ', text)
    text = re.sub(r'http\S+', ' ', text)
    text = text.lower()
    text = re.sub(r"[^a-z0-9,.()\-\n ]", " ", text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def score_match(resume_text, jd_text):
    mlflow.set_experiment("smart_rank_experiment")
    with mlflow.start_run():
        resume_text = preprocess(resume_text)
        jd_text = preprocess(jd_text)
        emb_resume = model.encode(resume_text, convert_to_tensor=True)
        emb_jd = model.encode(jd_text, convert_to_tensor=True)
        score = util.pytorch_cos_sim(emb_resume, emb_jd).item()
        mlflow.log_param("model", "all-MiniLM-L6-v2")
        mlflow.log_metric("match_score", score)
        return (score*100)