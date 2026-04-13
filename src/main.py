"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # User taste profile — drives all scoring in score_song()
    user_prefs = {
        "favorite_genre": "rock",
        "favorite_mood":  "intense",
        "target_energy":  0.88,
        "likes_acoustic": False,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"#{rank}  {song['title']} — {song['artist']}")
        print(f"    Score: {score:.2f}")
        print(f"    Why:   {explanation}")
        print("    " + "-" * 40)


if __name__ == "__main__":
    main()
