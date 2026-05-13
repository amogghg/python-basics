# YouTube Playlist Analyzer

videos = [12, 4, 8, 15, 3, 20]

total = sum(videos)
longest = max(videos)
average = total / len(videos)

short_videos = []

for v in videos:
    if v < 5:
        short_videos.append(v)

print("Total Watch Time:", total, "minutes")
print("Longest Video:", longest, "minutes")
print("Average Duration:", average, "minutes")
print("Videos shorter than 5 minutes:", short_videos)

output
Total Watch Time: 62 minutes
Longest Video: 20 minutes
Average Duration: 10.333333333333334 minutes
Videos shorter than 5 minutes: [4, 3]