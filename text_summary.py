from transformers import T5Tokenizer, TFT5ForConditionalGeneration

# def abstractive_summarization(text):
#     # Load pre-trained model and tokenizer
#     tokenizer = T5Tokenizer.from_pretrained('t5-base')
#     model = TFT5ForConditionalGeneration.from_pretrained('t5-base')

#     # Tokenize input text
#     inputs = tokenizer.encode("summarize: " + text, return_tensors='tf', max_length=512, truncation=True)

#     # Generate summary
#     summary_ids = model.generate(inputs, max_length=150, num_beams=4, length_penalty=2.0, early_stopping=True)
#     summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

#     return summary

# # Example usage
# input_text = "A hesitant writer, battling self-doubt, finally dared to submit their story. Rejections piled up, but determination fueled their pen. One day, an acceptance letter arrived, opening the door to a world of possibilities. With perseverance, they discovered that their words had the power to ignite hearts and change lives."
# summary = abstractive_summarization(input_text)
# print("Summary:", summary ,len(summary))



def summarizer(rowdocs):
    tokenizer = T5Tokenizer.from_pretrained('t5-base')
    model = TFT5ForConditionalGeneration.from_pretrained('t5-base')

    # Tokenize input text
    inputs = tokenizer.encode("summarize: " + rowdocs, return_tensors='tf', max_length=512, truncation=True)
    # Generate summary
    summary_ids = model.generate(inputs, max_length=150, num_beams=4, length_penalty=2.0, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary,rowdocs ,len(rowdocs.split(' ')),len(summary.split(' '))