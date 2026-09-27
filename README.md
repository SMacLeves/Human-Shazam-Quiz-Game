# Human Shazam

A terminal-based music quiz game: the program plays a random song from a 100-track library of 2010s hits and challenges you to name the **song title** and its **artist** before time runs out. Faster, correct answers score more points; the top 10 all-time scores are kept on a persistent leaderboard.

Author: Levente Bódi (s1122062) — Programming 1, Radboud University

## How it works (`main.py`)

1. Loads song titles from `top100.txt` and artist names from `top100eloado.txt` (matched by line number).
2. For 10 rounds: picks a random remaining song, plays it with `winsound.PlaySound(...)`, times how long you take to type the song title, then the artist. Each correct, in-time answer scores up to 1000 points (title) / 500 points (artist), decayed by the number of seconds you took. A song is never repeated within a game.
3. At the end, your total score is compared against `top10.txt` (scores) / `top10names.txt` (names); if you beat an existing entry, the leaderboard is updated and rewritten to both files plus the combined `top10alltimes.txt`.

A longer walkthrough of the design (comparisons, loops, list operations, file I/O used) is in [`docs/Program description.docx`](docs/Program%20description.docx).

## Requirements

- **Windows**, because the game plays audio via the standard-library [`winsound`](https://docs.python.org/3/library/winsound.html) module, which only exists on Windows. (Porting to `playsound`/`simpleaudio`/`pydub` would be needed for macOS/Linux.)
- Python 3.11 (as used originally; should work on any Python 3.x on Windows)
- No third-party packages — see [`requirements.txt`](requirements.txt)

## The song library

This repo ships the game **code only**. The 100 `.wav` files it plays from are **not committed** (`songs/` is git-ignored) — the original dataset is ~3.8 GB of commercially released songs, which doesn't belong in a public git repo for size and copyright reasons.

To play:
1. Create a `songs/` folder next to `main.py` (or point the code at wherever you keep the songs).
2. Add 100 `.wav` files — 2010s-era pop songs — one per line of [`top100.txt`](top100.txt) (song title) and [`top100eloado.txt`](top100eloado.txt) (artist), in lowercase, in the same order. The value in `top100.txt` is passed directly to `winsound.PlaySound(...)`, so it must resolve to a playable file (e.g. adjust the entries to include the `.wav` extension/relative path for your own copy of the audio, or place the game script inside `songs/`).
3. `top10.txt` / `top10names.txt` / `top10alltimes.txt` seed the leaderboard (10 placeholder scores/names to start) and are overwritten as you play.

## Run

```bash
python main.py
```

## License

MIT — see [LICENSE](LICENSE). (Note: the MIT license covers the code in this repo; it does not grant any rights to third-party song audio you supply yourself.)
