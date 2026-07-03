import joblib
import pandas as pd


class CreditScorePredictor:

    def __init__(self, model_path):

        self.model = joblib.load(model_path)

    def predict(self, data: dict):

        df = pd.DataFrame([data])

        prediction = self.model.predict(df)[0]

        return prediction