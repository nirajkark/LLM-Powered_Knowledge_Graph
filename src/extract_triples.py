from transformers import pipeline
import re


nlp = pipeline("ner", model="distilbert-base-uncased", tokenizer="distilbert-base-uncased")

def extract_triples(text):
    triples = []
    sentences = text.split('.')
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        
        entities = [ent["word"] for ent in nlp(sentence) if ent["entity"].startswith("B-")]
        if "capital is" in sentence:
            parts = sentence.split("capital is")
            subject = parts[0].strip()
            object_ = parts[1].strip().split(',')[0].strip()
            triples.append((subject, "capital", object_))
        elif "is a country" in sentence:
            subject = sentence.split("is a country")[0].strip()
            triples.append((subject, "type", "country"))
        elif "population of" in sentence:
            match = re.search(r"population of (.*?) is approximately ([\d.]+ billion)", sentence)
            if match:
                subject, pop = match.groups()
                triples.append((subject, "population", pop))
        
        if entities and "has a" in sentence:
            subject = entities[0]
            object_ = sentence.split("has a")[1].strip()
            triples.append((subject, "has", object_))
    return triples


with open("./data/input.txt", "r") as f:
    text = f.read()

triples = extract_triples(text)
with open("triples.txt", "w") as f:
    for s, p, o in triples:
        f.write(f"{s},{p},{o}\n")

print("Extracted triples:", triples)