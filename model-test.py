# Testing the hugginface summarizer model

from transformers import pipeline
classifier = pipeline("summarization")
res = classifier("Hello i am so happy to see you!")
print(res)
