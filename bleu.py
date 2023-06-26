import nltk

# Tokenization function
def tokenize(text):
    return text.split()  # Change this to your preferred tokenization method

# Reference and candidate summaries
reference = "A hare challenged a tortoise to a race . The tortoise won the race the hare was sleeping."
candidate = "The tortoise challenged the hare to have a race with him. The hare was very proud of his fast speed. The tortoise passed him and reached the winning post. The hare woke up and ran as fast as he could. The hare ran very fast. He saw that the tortoise was already at the winning post. He made fun of the tortoise for his slow speed.."

# Tokenize the reference and candidate summaries
reference_tokens = tokenize(reference)
candidate_tokens = tokenize(candidate)

# Compute BLEU score
bleu_score = nltk.translate.bleu_score.sentence_bleu([reference_tokens], candidate_tokens)

# Print the BLEU score
print("BLEU score:", bleu_score)



# Once a Hare and tortoise lived in a forest. The hare was very proud of his fast speed. He made fun of the tortoise for his slow speed. The tortoise challenged the hare to have a race with him. The hare accepted the challenge.

# The race started. The crow was the referee. The hare ran very fast. The tortoise was left far behind. The hare stopped to take rest under a tree. He fell asleep.

# The tortoise passed him and reached the winning post. The hare woke up and ran as fast as he could. He saw that the tortoise was already at the winning post. He won the race