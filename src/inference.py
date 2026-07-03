import os
import joblib
import boto3
import pandas as pd
import botocore
import streamlit as st


class CreditScorePredictor:

    def __init__(self):

        self.bucket = "credit-score-md"
        self.key = "best_model.pkl"
        self.local_model = "best_model.pkl"

        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=st.secrets["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=st.secrets["AWS_SECRET_ACCESS_KEY"],
            region_name=st.secrets["AWS_DEFAULT_REGION"]
        )

        if not os.path.exists(self.local_model):
            self.download_model()

        self.model = joblib.load(self.local_model)

    def download_model(self):
        try:
            self.s3.download_file(
                self.bucket,
                self.key,
                self.local_model
            )
        except botocore.exceptions.ClientError as e:

            st.error(e.response["Error"])

            raise
    def predict(self, data):

        df = pd.DataFrame([data])

        return self.model.predict(df)[0]
