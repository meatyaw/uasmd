import os
import joblib
import gdown
import pandas as pd


class CreditScorePredictor:

    def __init__(self):

        self.file_id = "MASUKKAN_FILE_ID_DISINI"

        self.model_path = "best_model.pkl"

        if not os.path.exists(self.model_path):

            url = f"https://drive.google.com/uc?id={self.file_id}"

            gdown.download(
                url,
                self.model_path,
                quiet=False
            )

        self.model = joblib.load(self.model_path)

    def predict(self, data):

        df = pd.DataFrame([data])

        return self.model.predict(df)[0]
