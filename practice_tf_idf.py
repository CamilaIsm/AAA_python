from math import log


class CountVectorizer():
    def __init__(self):
        self.feature_names = []

    def get_feature_names(self):
        return self.feature_names

    def fit_transform(self, corpus):
        self._features(corpus)
        return self._count_matrix(corpus)

    def _features(self, corpus):
        feature_names = {word.lower() for text in corpus for word in text.split()}
        self.feature_names = list(feature_names)

    def _count_matrix(self, corpus):
        matrix = []
        for text in corpus:
            matrix.append([])
            for word in self.feature_names:
                text_words = [word.lower() for word in text.split()]
                matrix[-1].append(text_words.count(word))

        return matrix


def idf_transform(matrix):

    document_count = len(matrix)
    idf = []

    for idx, _ in enumerate(matrix[0]):
        a = sum([1 for i, _ in enumerate(matrix) if matrix[i][idx] > 0])
        idf.append(round(log((document_count + 1) / (a + 1)), 3) + 1)

    return idf


def tf_transform(matrix):

    tf = []
    for vector in matrix:
        tf.append([round(el/sum(vector), 3) for el in vector])

    return tf


def tf_idf_transformer(matrix):

    tf = tf_transform(matrix)
    idf = idf_transform(matrix)
    tf_idf = []
    for t in tf:
        tf_idf.append([round(a1*a2, 3) for a1, a2 in zip(t, idf)])

    return tf_idf


class TfIdfTransformer:
    pass


class TfIdfVectorizer(CountVectorizer):

    def __init__(self):
        super().__init__()
        self._tfidf_transformer = TfIdfTransformer()

    def fit_transform(self, matrix):
        count_matrix = super().fit_transform(matrix)
        return tf_idf_transformer(count_matrix)


if __name__ == '__main__':
    corpus = ['Crock Pot Pasta Never boil pasta again', 'hot pomodoro pasta ']
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(count_matrix)
    print(vectorizer.get_feature_names())

    print()
    print('TfIdfTransformer')
    vec = TfIdfTransformer()
    print('Tf')
    print(tf_transform(count_matrix))
    print('IDF')
    print(idf_transform(count_matrix))
    print('tf_idf_transformer')
    print(tf_idf_transformer(count_matrix))

    print()
    print('TfIdfVectorizer')
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfIdfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)
