import joblib
from pathlib import Path

# Load model
model_path = Path(__file__).parent.parent / "models" / "best_model.joblib"

model = joblib.load(model_path)

# Example flower
import pandas as pd

sample = pd.DataFrame({
    "sepal_length": [5.1],
    "sepal_width": [3.5],
    "petal_length": [1.4],
    "petal_width": [0.2]
})

prediction = model.predict(sample)

species = {
    0: "Iris-setosa",
    1: "Iris-versicolor",
    2: "Iris-virginica"
}

print("Prediction:", species[prediction[0]])