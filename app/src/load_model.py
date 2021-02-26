import mlflow
from pandas import DataFrame
import os
import json

"""
Load a model
"""

# set to your server URI
remote_server_uri = os.environ["MLFLOW_TRACKING_URI"]
mlflow.set_tracking_uri(remote_server_uri)

# Load model as a PyFuncModel
logged_model = os.environ['LOGGED_MODEL']
loaded_model = mlflow.pyfunc.load_model(logged_model)

def predict(data : dict) -> str:
    """
    Predict on incoming data

    @param data : dataframe as dictionary
    """
    
    # create a dataframe from the payload
    df : DataFrame = DataFrame(data)

    # predict on the datframe
    df_result : DataFrame = loaded_model.predict(df)

    # return result as a json string
    return df_result.to_json()