import os
import boto3
import joblib

import streamlit as st

s3 = boto3.client(
    "s3",
    aws_access_key_id=st.secrets["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=st.secrets["AWS_SECRET_ACCESS_KEY"],
    region_name=st.secrets["AWS_DEFAULT_REGION"]
)
class CreditScorePredictor:

    def __init__(self):

        self.bucket = "credit-score-md"

        self.key = "best_model.pkl"

        self.local_model = "best_model.pkl"

        if not os.path.exists(self.local_model):

            self.download_model()

        self.model = joblib.load(self.local_model)

    def download_model(self):

        s3 = boto3.client("s3")

        s3.download_file(

            self.bucket,

            self.key,

            self.local_model

        )

    def predict(self, data):

        import pandas as pd

        df = pd.DataFrame([data])

        return self.model.predict(df)[0]
