from app.backend.preprocessing.preprocessing_pipeline import (
    preprocess_text
)

result = preprocess_text(

    "Players cannot plant the spike outside designated areas."

)

print(result)