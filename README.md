# Transparent Always-on-Top Pygame Animation

A fullscreen Pygame window with a transparent background, always-on-top behavior, and smooth sprite animation.

## Features

- Transparent background (color key: `#FF0080`)
- Always stays on top
- Fullscreen, borderless window
- Continuous sprite animation
- Press `Esc` to exit

## Setup

Install required libraries:

```bash
pip install pygame pywin32
```

## Place your sprite images in a sprites/ folder:
```bash
project/
├── main.py
└── sprites/
    ├── attack_1.png
    ├── attack_2.png
    ├── attack_3.png
    ├── ...
    └── attack_10.png

```

## Run
```bash
python main.py
```

## Notes
- The background color (255, 0, 128) is treated as transparent. Avoid using it in your sprite images.

- If you want a different background color for transparency, change both BG_COLOR in code and the SetLayeredWindowAttributes color.

- You can modify the scale_factor parameter when creating the Player to make the sprite bigger or smaller.
