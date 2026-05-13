# Social Media Hashtag Tracker

hashtags = ["#fun", "#python", "#fun", "#code", "#python"]

frequency = {}

for tag in hashtags:
    if tag in frequency:
        frequency[tag] += 1
    else:
        frequency[tag] = 1

# Most repeated hashtag
max_count = max(frequency.values())

for tag in frequency:
    if frequency[tag] == max_count:
        most_repeated = tag

# Unique hashtags
unique_tags = list(set(hashtags))

# Remove duplicates
no_duplicates = []

for tag in hashtags:
    if tag not in no_duplicates:
        no_duplicates.append(tag)

print("Most Repeated Hashtag:", most_repeated)
print("Unique Hashtags:", unique_tags)
print("Frequency of Hashtags:", frequency)
print("Without Duplicates:", no_duplicates)