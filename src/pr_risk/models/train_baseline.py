"""Baseline model training helpers."""
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


def train_logistic_regression(X_train, y_train, random_state: int = 42) -> LogisticRegression:
    """Train a Logistic Regression classifier."""
    return LogisticRegression(max_iter=1000, random_state=random_state).fit(X_train, y_train)

def train_random_forest(X_train, y_train, random_state: int = 42) -> RandomForestClassifier:
    """Train a Random Forest classifier."""
    model = RandomForestClassifier(n_estimators=200, random_state=random_state, n_jobs=-1)
    return model.fit(X_train, y_train)
