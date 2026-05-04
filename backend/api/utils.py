import os

def get_model_path(filename):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    return os.path.join(BASE_DIR, "backend", "models", filename)