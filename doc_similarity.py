from collections import Counter
import numpy as np
import string

def tokenizer(text):
    tokens = [word.strip(string.punctuation) for word in text.split()]
    return tokens

def csr_matrix(row,col,val,shape):
    mat = np.zeros(shape)
    x = zip(row, col, val)
    for each in x:
        mat[each[0]][each[1]] = each[2]

    return mat

def countVectorizer(data):
    full_text = " ".join(data)
    token = tokenizer(full_text)
    corpus = set(token)

    vocab = {}
    row, col, val = [], [], []

    for index, word in enumerate(sorted(list(corpus))):
        vocab[word] = index

    for idx, text in enumerate(data):
        count_word = dict(Counter(tokenizer(text)))

        for word, count in count_word.items():

            col_index = vocab.get(word)
            row.append(idx)
            col.append(col_index)
            val.append(count)

    sparse_matrix = csr_matrix(row, col, val, shape=[len(data), len(vocab)])

    return sparse_matrix

def cosine_similarity(matrix):
    a = matrix[0]
    b = matrix[1]
    dot_product = np.dot(a,b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a * norm_b)

def get_similarity(text_1,text_2):

    data = [text_1,text_2]
    count_matrix = countVectorizer(data)
    similarity = cosine_similarity(count_matrix)

    return round(similarity*100,2)


