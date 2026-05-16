## What is Stellatro?

Stellatro is a two-player, poker-meets-Balatro card game. Each round, both
players are dealt a 10-card hand and a shared pool of 15 randomly generated
**jokers** is rolled out between them.

A round runs in two phases:

1. **Draft phase** — players alternate picking jokers from the shared pool
   (Player 1 picks first). After each player has drafted 5 jokers, the draft
   ends.
2. **Play phase** — each player chooses 5 of their 10 cards to play as a
   poker hand. The hand is scored as `chips × mult`, where:
   - The hand type (High Card → Straight Flush) sets the base chips and mult.
   - Each scored card adds its rank value to chips.
   - Owned jokers can trigger in the pre-card, per-card, and post-card phases
     to add chips, mult, retrigger cards, or otherwise modify scoring.

Whoever has the higher score after both players play wins the round.



The project is split into three packages:

- `stellatro-common/` — shared Pydantic models and enums (`GameState`,
  `Phase`, `PlayerTurn`, `CardModel`, `JokerModel`).
- `stellatro-game/` — the game engine (`Game`, deck, jokers, hand checker,
  scoring). This is what bots and the GUI both drive.
- `starter-kit/gui/` — a pygame visualization that can run human-vs-human,
  human-vs-bot, or bot-vs-bot games.

## Installing requirements

Stellatro targets **Python 3.13**. Please install it [here](https://www.python.org/downloads/release/python-3130/) if you do not have it installed. 

### macOS / Linux

From the repo root:

```bash
# (optional, highly recommended) create and activate a virtual environment
python3.13 -m venv .venv
source .venv/bin/activate

# upgrade pip to the latest version
python -m pip install --upgrade pip
# python3 -m pip install --upgrade pip

# install the two local packages in editable mode
pip install -e ./stellatro-common
pip install -e ./stellatro-game

# install the GUI's runtime dependencies
pip install pygame numpy pydantic
```

### Windows

From the repo root, in PowerShell or Command Prompt:

```powershell
# (optional, highly recommended) create and activate a virtual environment
py -3.13 -m venv .venv
.venv\Scripts\activate

# upgrade pip to the latest version
python -m pip install --upgrade pip
# python3 -m pip install --upgrade pip

# install the two local packages in editable mode
pip install -e .\stellatro-common
pip install -e .\stellatro-game

# install the GUI's runtime dependencies
pip install pygame numpy pydantic
```

If `py -3.13` isn't available, install Python 3.13 from
[python.org](https://www.python.org/downloads/windows/) and make sure the
"Add Python to PATH" option is checked. On PowerShell, if activation is
blocked by the execution policy, run
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once and re-open the
shell.

`stellatro-common` and `stellatro-game` are installed editable so that any
edits you make to the engine are picked up immediately by the GUI.

## Running the GUI

From the repo root:

```bash
python starter-kit/gui/gui.py
# python3 starter-kit/gui/gui.py
```

By default both players are human-controlled. Useful flags:

| Flag | Description |
| --- | --- |
| `--game_speed <float>` | Multiplier on the simulation/animation speed (default `1.0`). |
| `--no_bg` | Disable the animated background (useful on slower machines). |

Examples:

```bash
# Faster game
python starter-kit/gui/gui.py --game_speed 2.0 --no_bg
# python3 starter-kit/gui/gui.py
```

## Notes

This is a demo of the competition, intended for users to become familiar with the game beforehand. 

You are NOT intended to begin coding a bot before the competition starts. The current jokers given is a small subset of the amount of jokers in the competition. All jokers and values given are subject to change before the competition.
