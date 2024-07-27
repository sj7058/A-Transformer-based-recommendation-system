import pandas as pd
import matplotlib.pyplot as plt

# Example data
emotion_counts = df['emotion'].value_counts()
emotion_labels = [emotion for emotion, idx in emotion_mapping.items()]

plt.figure(figsize=(10, 6))
plt.bar(emotion_labels, emotion_counts)
plt.xlabel('Emotion')
plt.ylabel('Count')
plt.title('Distribution of Emotions in the Dataset')
plt.xticks(rotation=45)
plt.show()
