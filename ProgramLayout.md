Vex-AI-Project/
│
├── coach/                     # PC-side AI (training + strategy generation)
│   ├── data/                  # Logs pulled from SD card
│   ├── models/                # Saved coach models
│   ├── dictionary.json        # Token dictionary shared with player
│   ├── train_coach.py         # Learns strategies from logs
│   ├── generate_strategy.py   # Produces the strategy string
│   ├── simulate.py            # Simulation environment
│   └── utils.py               # Shared helper functions
│
├── player/                    # On-device AI (VEX V5)
│   ├── interpreter.cpp        # Reads strategy string + dictionary
│   ├── fallback_ai.cpp        # Improvisation logic
│   ├── sensors.cpp            # Sensor reading + situation encoding
│   ├── control.cpp            # Motor control logic
│   ├── dictionary.h           # Same dictionary as PC, but C++ version
│   └── main.cpp               # Entry point for VEX program
│
├── strategy_strings/          # Generated playbooks
│   ├── latest.txt
│   └── archive/
│
└── docs/                      # Documentation
    ├── architecture.md
    ├── workflow.md
    └── dictionary_spec.md
