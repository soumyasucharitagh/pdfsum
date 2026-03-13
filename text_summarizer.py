from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

def summarize_text(text, max_length=120, min_length=30):

    summary = summarizer(
        text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False
    )

    return summary[0]["summary_text"]
