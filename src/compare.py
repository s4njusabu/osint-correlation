from datetime import datetime

def compare_dates(date1: str, date2: str):
    d1 = datetime.fromisoformat(date1.replace("Z", "+00:00"))
    d2 = datetime.fromisoformat(date2.replace("Z", "+00:00"))

    difference = abs((d1 - d2).total_seconds())

    max_difference = 86400 

    similarity = 1 - (difference / max_difference)

    return max(0, similarity)

def compare_texts(text1: str, text2: str):
    words1 = text1.lower().split()
    words2 = text2.lower().split()

    common = 0

    for word in words1:
        if word in words2:
            common += 1

    return common / max(len(words1), len(words2))


def compare_images(image1, image2):
    print("Never gonna run around and desert you")