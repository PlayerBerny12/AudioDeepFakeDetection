"""
DeepfakeDetectionFramework
--------------------------

if any required method is written in python
then import specific module and run the method
directlly otherwise import subprocess module
and run it as subprocess and parse the output

e.g.:
    from my_module import my_func1, my_func2
    my_func1(x, y)
    
    -------------------------
    
    import subprocess
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True) 
    
    print(result.stdout)
"""

from fastapi import FastAPI
from typing import Any

import subprocess

app = FastAPI()

NAME = "Method name"
DESCRIPTION = "Method description"

def check_request(file_path: str):
    """
    Check file type if it is processable
    """
    return True

def data_preparation(file_path: str):
    """
    Prepare data from request
    
    E.g.: convert to specific format (wav, mp3, ...) 
    or split data to frames, etc.
    """
    
    return file_path

def detection_method(file_path: str):
    """
    Run detection method on prepared data    
    """

    process = subprocess.run(
        ["python3", "train.py", "--feature_classname", "mfcc", "--model_classname", "ShallowCNN", "--restore", 
         "--in_distribution", "False", "--eval_one", "--test_file", file_path],
        text=True,
        capture_output=True
    )    
    
    return float(process.stdout.splitlines()[-2])

def results_normalization(results: Any):
    """
    Normalize data by converting to interval <0-1>
    """
    
    return results

@app.get("/detect")
def detect(id: int, checksum: str, filename: str, status: int, type: int):
    """
    Entry point for receiving requests
    """
    file_path = f"/mnt/processingdata/{filename}"
    
    if check_request(file_path):        
        # Prepare data from request (optional)
        file_path = data_preparation(file_path)
        
        # Run detection method
        results = detection_method(file_path)
        
        # Convert results to interval <0-1> (optional)
        results = results_normalization(results)

        return {"RequestID": id, "Value": results, "Name": NAME, "Description": DESCRIPTION}
    else:
        return {"RequestID": id, "Value": -1, "Name": NAME, "Description": DESCRIPTION}