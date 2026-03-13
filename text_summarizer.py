from transformers import pipeline

# Use text2text-generation instead of summarization
summarizer = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

def summarize_text(text, max_length=150):

    prompt = "summarize: " + text

    summary = summarizer(
        prompt,
        max_length=max_length,
        do_sample=False
    )

    return summary[0]["generated_text"]
