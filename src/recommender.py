from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Score all songs against user and return the top k sorted by score descending."""
        user_dict = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood":  user.favorite_mood,
            "target_energy":  user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        ranked = sorted(self.songs, key=lambda s: score_song(user_dict, vars(s))[0], reverse=True)
        return ranked[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a human-readable string explaining why song was recommended for user."""
        user_dict = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood":  user.favorite_mood,
            "target_energy":  user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        _, reasons = score_song(user_dict, vars(song))
        return reasons

def load_songs(csv_path: str) -> List[Dict]:
    """Read csv_path with csv.DictReader and return a list of song dicts with numeric fields converted."""
    import csv

    float_fields = {"energy", "valence", "danceability", "acousticness"}
    int_fields   = {"tempo_bpm"}

    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if not row["id"].strip():
                continue
            for field in float_fields:
                row[field] = float(row[field])
            for field in int_fields:
                row[field] = int(row[field])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, str]:
    """Score one song against user_prefs using genre/mood/energy/acoustic rules; return (total_score, reasons_string)."""
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs["favorite_genre"]:
        score += 2.0
        reasons.append(f"genre match ({song['genre']})")

    if song["mood"] == user_prefs["favorite_mood"]:
        score += 1.0
        reasons.append(f"mood match ({song['mood']})")

    energy_sim = 1.0 - abs(song["energy"] - user_prefs["target_energy"])
    score += energy_sim
    reasons.append(f"energy similarity {energy_sim:.2f}")

    if not user_prefs["likes_acoustic"] and song["acousticness"] <= 0.2:
        score += 0.5
        reasons.append("non-acoustic match")

    return (score, ", ".join(reasons))

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song in songs against user_prefs and return the top k as (song, score, explanation) tuples."""
    scored = []
    for song in songs:
        score, explanation = score_song(user_prefs, song)
        scored.append((song, score, explanation))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
