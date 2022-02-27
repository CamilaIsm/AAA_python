class CountVectorizer():
    def __init__(self):
        self.feature_names = []
        # self.fit_transform = []

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


corpus = ['Crock Pot Pasta Never boil pasta again', 'hot pomodoro pasta ']
vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)
print(count_matrix)
print(vectorizer.get_feature_names())
