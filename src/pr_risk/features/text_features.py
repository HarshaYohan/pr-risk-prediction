"""Text feature engineering helpers."""
from sklearn.feature_extraction.text import TfidfVectorizer


def create_text_features_tfidf(
    train_texts,
    val_texts,
    test_texts,
    max_features: int = 5000,
    ngram_range: tuple[int, int] = (1, 2),
):
    """Fit TF-IDF on train text and transform train, validation, and test text."""
    vectorizer = TfidfVectorizer(max_features=max_features, ngram_range=ngram_range)
    return (
        vectorizer.fit_transform(train_texts),
        vectorizer.transform(val_texts),
        vectorizer.transform(test_texts),
        vectorizer,
    )
