from sentence_transformers import SentenceTransformer, util
import torch

model = SentenceTransformer('all-MiniLM-L6-v2')

def encode_text(texts):
    if isinstance(texts, str):
        return model.encode(texts)
    return model.encode(texts, convert_to_tensor=True)

def get_best_match(query, corpus, threshold=0.5):
    query_vec = encode_text(query)
    corpus_vecs = encode_text(corpus)
    scores = util.pytorch_cos_sim(query_vec, corpus_vecs)
    max_score, idx = torch.max(scores, dim=1)
    if max_score.item() >= threshold:
        return corpus[idx[0]], max_score.item()
    return None, max_score.item()
