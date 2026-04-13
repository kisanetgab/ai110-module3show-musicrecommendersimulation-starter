# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name
VibeFinder 1.0

---

## 2. Intended Use
Suggests the top 5 songs matching a user's taste profile (genre, mood, 
energy). Built for a CodePath AI course — not for real users or production.

---

## 3. How the Model Works
Each song gets a score based on how well it matches the user's preferences:
- Genre match = most points
- Mood match = moderate points  
- Energy closeness = partial points (closer = higher score)
- Acoustic preference = small bonus

Songs are sorted by score and the top 5 are returned.

---

## 4. Data
- 15 songs in CSV format
- Features: genre, mood, energy, tempo, valence, danceability, acousticness
- Manually created — no real listening history
- Missing genres: classical, R&B, hip-hop, country

---

## 5. Strengths
Works well when user preferences match the dataset. Chill Lofi and 
Intense Rock profiles both returned accurate, intuitive results. Energy 
similarity gives partial credit rather than a simple pass/fail, which 
makes scoring feel more natural.

---

## 6. Limitations and Bias
Genre weight (2.0) is so dominant that a weak genre match beats a 
perfect mood and energy match in a different genre. The Conflicted 
Listener profile (rock/sad) scored 0 mood points for every song 
because that combination doesn't exist in the dataset. The system 
also has no memory and cannot learn from feedback.

---

## 7. Evaluation

Tested four profiles: Intense Rock, High-Energy Pop, Chill Lofi, 
and Conflicted Listener. Also ran a weight-shift experiment (halved 
genre, doubled energy) which noticeably changed rankings and showed 
how sensitive the system is to small design choices.

![Terminal output - Intense Rock and High-Energy Pop profiles](image-2.png)
![Terminal output - Chill Lofi and Conflicted Listener profiles](image-1.png)

---

## 8. Future Work
1. Expand to 100+ songs covering more genres
2. Add collaborative filtering using simulated user data
3. Build a feedback loop so weights adjust based on user ratings

---

## 9. Personal Reflection
The Conflicted Listener result was the biggest surprise — the algorithm 
was doing exactly what the math said, but the output was useless because 
the data didn't support that preference combination. This changed how I 
think about apps like Spotify. The math is simple. The data is everything.