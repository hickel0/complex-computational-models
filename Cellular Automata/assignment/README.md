# Virus Spread Agent-Based Model (ABM)

**CSC1111 - Building Complex Computational Models**
2nd Continuous Assessment

## Overview

This project implements an Agent-Based Model (ABM) simulating virus transmission among a population using a SIRD (Susceptible-Infected-Recovered-Dead) framework with spatial dynamics. The simulation visualises epidemic spread in real-time and allows interactive parameter adjustment.

**Key Features:**
- Probabilistic infection and recovery mechanics
- Direct reinfection (R → I) modelling waning immunity
- Adjustable parameters via sliders and text boxes
- Real-time 2D spatial visualisation 

## Repo Structure

```
src/
 └──  virus_sim.py              # Python simulation

docs/
  ├──CSC1111 Project 2026.pdf  # Assignment brief
  └──CSC1111_ABM_Report.docx


outputs/                   # Scenario screenshots
    ├── scenario_1_baseline.png
    ├── scenario_2.png
    ├── scenario_3.png
    ├── scenario_3_w_reinfect.png
    ├── scenario_4_baseline.png
    ├── scenario_4_measels.png
    ├── scenario_5_baseline.png
    ├── scenario_5_measels.png
    ├── scenario_5_measels_reinfection.png
    └── scenario_5_measels_reinfection_socialdist.png

README.md
```

## Requirements

- Python 3.8+
- NumPy
- Matplotlib
- python-docx (for report generation only)

Install dependencies:
```bash
pip install numpy matplotlib python-docx
```

## Running the Simulation

```bash
python virus_sim.py
```

The GUI window will open with:
- Left panel: 2D visualisation of agent positions (colour-coded by state)
- Right panel: Real-time epidemic curve (S, I, R, D populations over time)
- Bottom: Control buttons, parameter sliders, and text boxes

## Parameters

All parameters can be adjusted in real-time using sliders or text boxes:

| Parameter | Default | Range | Description |
|-----------|---------|-------|-------------|
| Population | 200 | 50-500 | Number of agents in simulation |
| Initial Infected | 5 | - | Starting infected agents (set at initialisation) |
| Infection Prob | 0.3 | 0.0-1.0 | Chance of infection on contact (S → I) |
| Infection Radius | 0.03 | 0.01-0.15 | Distance for transmission |
| Min Recovery Time | 100 | 20-300 | Minimum time steps before recovery possible |
| Recovery Prob | 0.97 | 0.01-1.0 | Chance of recovery each step (after min time) |
| Mortality Rate | 0.0 | 0.0-1.0 | Chance of death upon recovery |
| Reinfection Rate | 0.0 | 0.0-1.0 | Chance recovered agent reinfects (R → I) on contact |
| Social Distancing | 0.0 | 0.0-1.0 | Reduces agent movement speed |
| Movement Speed | 0.01 | 0.001-0.03 | Base speed of agent movement |

## Model Definitions

| State | Colour | Description |
|-------|--------|-------------|
| **Susceptible (S)** | Blue | Agents who have NEVER been infected |
| **Infected (I)** | Red | Currently infectious agents |
| **Recovered (R)** | Green | Previously infected, now immune (can reinfect via reinfection_rate) |
| **Dead (D)** | Grey | Deceased agents (remain visible in simulation) |

**Important:** Susceptible is defined as agents who have never been infected. Reinfection occurs directly from R → I (not R → S), modelling real-world observations of COVID-19 reinfections.

## GUI Controls

| Control | Function |
|---------|----------|
| **Start/Stop** | Toggle simulation running/paused |
| **Reset** | Restart simulation with current parameter values |
| **Sliders** | Drag to adjust parameters in real-time |
| **Text Boxes** | Type exact values and press Enter |

**Note:** Population changes require clicking Reset to take effect.


## Output

The simulation provides:
- **2D Visualisation:** Agent positions colour-coded by health state
- **Epidemic Curve:** Time-series graph showing S, I, R, D populations
- **Status Display:** Current time step and population counts
- **Screenshots:** Save manually or via matplotlib's save button

## Authors

- Lee Hickey - Emma Reen -