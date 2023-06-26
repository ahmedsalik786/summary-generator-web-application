
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest


text="""Once a Hare and tortoise lived in a forest. The hare was very proud of his fast speed. He made fun of the tortoise for his slow speed. The tortoise challenged the hare to have a race with him. The hare accepted the challenge.

The race started. The crow was the referee. The hare ran very fast. The tortoise was left far behind. The hare stopped to take rest under a tree. He fell asleep.

The tortoise passed him and reached the winning post. The hare woke up and ran as fast as he could. He saw that the tortoise was already at the winning post. He won the race
"""


# text="""Peter and Elizabeth took a taxi to attend the night party in the city. while in the party, Elizabeth collapsed and was rushed to the hospital. Since she was diagonised with a brain injury , the doctor told Peter to stay besides her until she gets well . Peter stayed with her at the hospital for 3 days without leaving.
# """
def summarizer(rowdocs):
    stop_words=list(STOP_WORDS)
    # print(stop_words)
    nlp=spacy.load('en_core_web_sm')
    doc=nlp(text)
    # print(doc)
    tokens=[token.text for token in doc]
    # print(tokens)

    word_freq={}
    for word in doc:
        if word.text.lower() not in stop_words and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text]=1
            else:
                word_freq[word.text]+=1
    # print(word_freq) 

    max_freq=max(word_freq.values())
    # print(max_freq)

    for word in word_freq.keys():
        word_freq[word]==word_freq[word]/max_freq
    # print(word_freq)

    sent_tokens=[sent for sent in doc.sents]
    # print(sent_tokens)

    sent_scores={}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent]=word_freq[word.text]
                else:
                    sent_scores[sent]+=word_freq[word.text]
    # print(sent_score)

    select_len=int(len(sent_tokens)*0.50)
    # print(select_len)
    summary=nlargest(select_len,sent_scores,key=sent_scores.get)
    # print(summary)
    final_summary=[word.text for word in summary]
    summary=' '.join(final_summary)
    # print(text)
    print(summary)
    # print("length of original text ",len(text.split(' ')))
    # print("length of summary text ",len(summary.split(' ')))

    # return summary,doc ,len(rowdocs.split(' ')),len(summary.split(' '))
summarizer(text)