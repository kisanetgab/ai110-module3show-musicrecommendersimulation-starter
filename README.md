# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real-world recommenders like Spotify or YouTube learn from massive amounts of behavior data — what you skip, replay, or add to a playlist — and use that history to predict what you'll want next. This simulation takes a simpler, more transparent approach: instead of learning from behavior, it matches songs directly against an explicit user taste profile using a weighted scoring formula. The goal is to prioritize **interpretability** over accuracy — every recommendation can be explained by pointing to the exact features that drove the score.

### Song Features

Each `Song` object stores the following attributes from `data/songs.csv`:

- `genre` — categorical style label (e.g. pop, lofi, rock, jazz, synthwave)
- `mood` — emotional quality (e.g. happy, chill, intense, relaxed, focused, moody)
- `energy` — float from 0 to 1, how energetic the track feels
- `tempo_bpm` — beats per minute
- `valence` — float from 0 to 1, musical positiveness
- `danceability` — float from 0 to 1, how suitable the track is for dancing
- `acousticness` — float from 0 to 1, how acoustic (vs. electronic) the track sounds

### UserProfile Features

Each `UserProfile` captures four preference signals:

- `favorite_genre` — the genre the user most wants to hear
- `favorite_mood` — the mood the user is currently seeking
- `target_energy` — their preferred energy level, as a float from 0 to 1
- `likes_acoustic` — boolean flag for whether they prefer acoustic over electronic sounds

### Algorithm Recipe

Each song is scored by four rules, summed into a total (max 5.0), then ranked:

- **Genre match** — `+2.0` if genre matches, else `0`
- **Mood match** — `+1.0` if mood matches, else `0`
- **Energy proximity** — `1.5 × (1.0 − |song.energy − target_energy|)`
- **Acoustic bonus** — `+0.5` if `(acousticness >= 0.6) == likes_acoustic`, else `0`

The top `k` songs by total score are returned as recommendations.

### Potential Biases

- Genre carries 40% of the max score, so songs that miss on genre rarely surface even with strong mood and energy matches.
- Genre and mood are correlated in this catalog (e.g. every rock song is "intense"), so those two rules can double-count the same signal.
- No diversity control — the same artist can fill multiple top slots.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

## Terminal Output

![alt text](image.png)


### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

