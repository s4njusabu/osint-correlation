from datetime import datetime

def compare_dates(date1: str, date2: str):
    d1 = datetime.fromisoformat(date1.replace("Z", "+00:00"))
    d2 = datetime.fromisoformat(date2.replace("Z", "+00:00"))

    difference = abs((d1 - d2).total_seconds())

    max_difference = 86400 

    similarity = 1 - (difference / max_difference)

    return max(0, similarity)

def compare_texts(text1: str, text2: str):
    print("Never gonna let you down")

def compare_images(image1, image2):
    print("Never gonna run around and desert you")