"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def display_profile(profile_name, user_prefs, songs):
    print(f"\n{'='*50}")
    print(f"Profile: {profile_name}")
    print(f"{'='*50}")
    recommendations = recommend_songs(user_prefs, songs, k=5)
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"#{rank}  {song['title']} — {song['artist']}")
        print(f"    Score: {score:.2f}")
        print(f"    Why:   {explanation}")
        print("    " + "-" * 40)


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Original profile
    display_profile("Intense Rock", {
        "favorite_genre": "rock",
        "favorite_mood":  "intense",
        "target_energy":  0.88,
        "likes_acoustic": False,
    }, songs)

    # Profile 1 — High Energy Pop
    display_profile("High-Energy Pop", {
        "favorite_genre": "pop",
        "favorite_mood":  "happy",
        "target_energy":  0.85,
        "likes_acoustic": False,
    }, songs)

    # Profile 2 — Chill Lofi
    display_profile("Chill Lofi", {
        "favorite_genre": "lofi",
        "favorite_mood":  "chill",
        "target_energy":  0.38,
        "likes_acoustic": True,
    }, songs)

    # Profile 3 — Edge Case (conflicting preferences)
    display_profile("Conflicted Listener", {
        "favorite_genre": "rock",
        "favorite_mood":  "sad",
        "target_energy":  0.90,
        "likes_acoustic": True,
    }, songs)


if __name__ == "__main__":
    main()