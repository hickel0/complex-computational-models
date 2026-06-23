# Complex Computational Models

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![ABM](https://img.shields.io/badge/ABM-Agent%20Based%20Models-blue?style=flat-square)](.)
[![Time Series](https://img.shields.io/badge/Time%20Series-ARIMA%20%7C%20MA-orange?style=flat-square)](.)
[![Status](https://img.shields.io/badge/Status-Complete-success?style=flat-square)](.)

Comprehensive coursework covering agent-based modeling, cellular automata simulations, and time series analysis with practical implementations in Python and Excel.

## 📋 Project Overview

This repository contains projects and coursework from Complex Computational Models (CSC1111/CSC1139), focusing on simulation techniques, time series forecasting, and computational modeling of complex systems.

**Course Codes**: CSC1111, CSC1139
**Topics**: Cellular Automata, Agent-Based Models, Time Series Analysis
**Status**: ✅ Completed with Multiple Projects

## 🎯 Learning Objectives

- Understand and implement cellular automata and agent-based models
- Master time series analysis and forecasting techniques
- Apply computational modeling to real-world phenomena
- Develop simulation skills for complex adaptive systems
- Analyze and visualize emergent behaviors

## 📂 Repository Structure

```
Complex Comp Models/
├── Cellular Automata/
│   ├── Lab01.ipynb                          # Introduction to cellular automata
│   ├── agent_based_model.py                 # General ABM framework
│   ├── predator_prey_simulation.py          # Predator-prey dynamics
│   ├── segregation_model.py                 # Schelling's segregation model
│   ├── dla_simulation.py                    # Diffusion-limited aggregation
│   ├── network_visualization.py             # Network analysis and viz
│   └── assignment/
│       ├── virus_spread_simulation.py       # COVID-19 spread simulation
│       ├── report_generator.py              # Automated report creation
│       └── README.md                        # Assignment documentation
│
├── Time Series/
│   ├── W1/ - W6/                            # Weekly materials
│   ├── TSClassExercise_answers.xlsx         # Time series class exercises
│   ├── MA_Forecast_model_answers.xlsx       # Moving Average models
│   ├── School_leavers_additive_model.xlsx   # Additive decomposition
│   ├── JandJ_time_series_solutions.xlsx     # Johnson & Johnson analysis
│   └── VIX_daily_analysis.xlsx              # Volatility index analysis
│
├── Past Exams/
│   └── [Exam papers and solutions]
│
├── Lean_Business_Model_Canvas_GreenGrid_AI.pdf
├── Cheat_Sheet.pdf
└── revision_notes.md
```

## 🔬 Key Projects

### 1. Cellular Automata & Agent-Based Models

#### Virus Spread Simulation (Featured Assignment)
A sophisticated agent-based model simulating disease spread through a population.

**Features**:
- Configurable infection parameters (transmission rate, recovery time, mortality)
- Spatial movement and contact tracing
- Intervention strategies (lockdowns, social distancing, vaccination)
- Real-time visualization of spread dynamics
- Statistical analysis of outbreak patterns

**Skills**: Agent-based modeling, simulation, Python OOP, data visualization

**Files**: `Cellular Automata/assignment/virus_spread_simulation.py`

#### Predator-Prey Dynamics
Implementation of Lotka-Volterra equations and agent-based predator-prey models.

**Features**:
- Population dynamics simulation
- Emergent cyclical patterns
- Parameter sensitivity analysis
- Visualization of population trajectories

**Files**: `Cellular Automata/predator_prey_simulation.py`

#### Schelling's Segregation Model
Simulation demonstrating how individual preferences can lead to large-scale segregation.

**Features**:
- Agent preferences and movement rules
- Emergent segregation patterns
- Threshold analysis
- Spatial visualization

**Files**: `Cellular Automata/segregation_model.py`

#### Diffusion-Limited Aggregation (DLA)
Fractal growth simulation modeling particle aggregation.

**Features**:
- Random walk particle dynamics
- Fractal pattern formation
- Visualization of growth structures
- Dimension analysis

**Files**: `Cellular Automata/dla_simulation.py`

#### Network Visualization
Complex network analysis and visualization tools.

**Features**:
- Graph generation and analysis
- Network metrics (centrality, clustering)
- Community detection
- Interactive visualizations

**Files**: `Cellular Automata/network_visualization.py`

### 2. Time Series Analysis & Forecasting

#### Time Series Class Exercises
Comprehensive exercises covering fundamental time series concepts.

**Topics Covered**:
- Trend identification and removal
- Seasonal decomposition
- Stationarity testing
- Autocorrelation analysis

**Files**: `Time Series/TSClassExercise_answers.xlsx`

#### Moving Average Forecasting Models
Implementation and comparison of MA forecasting techniques.

**Models**:
- Simple Moving Average (SMA)
- Weighted Moving Average (WMA)
- Exponential Smoothing
- Model performance comparison

**Files**: `Time Series/MA_Forecast_model_answers.xlsx`

#### School Leavers Additive Model
Seasonal decomposition using additive model.

**Analysis**:
- Trend-cycle component extraction
- Seasonal pattern identification
- Irregular component analysis
- Forecasting with seasonal adjustment

**Files**: `Time Series/School_leavers_additive_model.xlsx`

#### Johnson & Johnson Time Series
Real-world financial time series analysis.

**Techniques**:
- Multiplicative decomposition
- Exponential growth trends
- Seasonal indices calculation
- Business forecasting

**Files**: `Time Series/JandJ_time_series_solutions.xlsx`

#### VIX Daily Analysis
Volatility Index (VIX) time series analysis.

**Focus**:
- Financial volatility modeling
- ARCH/GARCH concepts
- Market risk analysis
- Volatility forecasting

**Files**: `Time Series/VIX_daily_analysis.xlsx`

## 🛠️ Technologies Used

### Python Stack
```python
numpy==1.24.0           # Numerical computing
matplotlib==3.7.0       # Visualization
scipy==1.10.0           # Scientific computing
networkx==3.0           # Network analysis
pandas==2.0.0           # Time series data manipulation
```

### Simulation Libraries
- Custom agent-based modeling framework
- Cellular automata implementations
- Random walk simulations

### Analysis Tools
- Microsoft Excel (time series analysis)
- Jupyter Notebook (interactive development)
- Python statistical libraries

## 📊 Key Concepts Covered

### Cellular Automata
- Conway's Game of Life
- Elementary cellular automata (Rule 30, Rule 110)
- 2D grid-based simulations
- Emergence and self-organization
- Computational universality

### Agent-Based Modeling
- Individual agent behaviors
- Interaction rules
- Emergent collective phenomena
- Spatial dynamics
- Parameter sensitivity
- Model validation

### Time Series Analysis
- Components: Trend, Seasonal, Cyclical, Irregular
- Decomposition methods (additive/multiplicative)
- Smoothing techniques
- Forecasting methods:
  - Moving Averages
  - Exponential Smoothing
  - Holt-Winters
  - ARIMA concepts
- Model evaluation (MAE, RMSE, MAPE)

### Complex Systems
- Nonlinearity and feedback loops
- Self-organization
- Emergence
- Power laws and scale-free networks
- Tipping points and phase transitions

## 🎯 Assignment: Virus Spread Simulation

### Objectives
Develop an agent-based model to simulate disease spread and evaluate intervention strategies.

### Model Parameters
- Population size: Configurable
- Infection rate: Beta parameter
- Recovery time: Average days to recovery
- Mortality rate: Percentage of infected who die
- Movement: Random walk or directed
- Interventions: Lockdown, social distancing, vaccination

### Deliverables
- ✅ Python simulation code
- ✅ Visualization of spread dynamics
- ✅ Statistical analysis
- ✅ Report on intervention effectiveness
- ✅ Automated report generation

### Results
- Successfully modeled disease spread dynamics
- Demonstrated effectiveness of early interventions
- Analyzed parameter sensitivity
- Generated reproducible results

**Documentation**: See `Cellular Automata/assignment/README.md`

## 📈 Time Series Projects Summary

### Project 1: School Leavers Forecasting
**Objective**: Forecast number of school leavers using seasonal decomposition
**Method**: Additive model
**Result**: Accurate seasonal forecasts with trend analysis

### Project 2: Johnson & Johnson Stock Analysis
**Objective**: Analyze quarterly earnings and forecast future performance
**Method**: Multiplicative decomposition with exponential trend
**Result**: Successfully captured growth trend and seasonal patterns

### Project 3: VIX Volatility Analysis
**Objective**: Model and forecast market volatility
**Method**: Advanced time series techniques
**Result**: Insights into market risk patterns

### Project 4: Moving Average Comparison
**Objective**: Compare forecasting performance of different MA methods
**Method**: SMA, WMA, Exponential Smoothing
**Result**: Exponential smoothing performed best for trending data

## 🔧 Setup & Installation

### Prerequisites
```bash
Python 3.8 or higher
Microsoft Excel (for time series exercises)
Jupyter Notebook (optional)
```

### Installation

1. **Navigate to project directory**
```bash
cd "D:\Final Year\Complex Comp Models"
```

2. **Install Python dependencies**
```bash
pip install numpy matplotlib scipy pandas networkx
pip install jupyter notebook  # Optional
```

3. **Run simulations**
```bash
# Virus spread simulation
python "Cellular Automata/assignment/virus_spread_simulation.py"

# Predator-prey model
python "Cellular Automata/predator_prey_simulation.py"

# Segregation model
python "Cellular Automata/segregation_model.py"
```

4. **Open time series exercises**
- Open Excel files in `Time Series/` folder
- Follow worksheet instructions
- Review solutions and methodologies

## 📚 Learning Resources

### Textbooks & References
- Wolfram: "A New Kind of Science"
- Railsback & Grimm: "Agent-Based and Individual-Based Modeling"
- Box & Jenkins: "Time Series Analysis: Forecasting and Control"
- Hyndman & Athanasopoulos: "Forecasting: Principles and Practice"

### Course Materials
- Weekly lecture notes (W1-W6)
- Past exam papers with solutions
- Cheat sheet for quick reference
- Revision notes

## 🎓 Skills Demonstrated

### Computational Modeling
- Agent-Based Modeling
- Cellular Automata
- Discrete Event Simulation
- Monte Carlo Methods
- Stochastic Processes

### Time Series Analysis
- Decomposition Techniques
- Forecasting Methods
- Trend Analysis
- Seasonal Adjustment
- Model Selection and Evaluation

### Programming & Visualization
- Python OOP Design
- NumPy and SciPy
- Matplotlib Visualization
- Network Analysis (NetworkX)
- Excel Data Analysis

### Analytical Thinking
- Complex Systems Understanding
- Emergence Recognition
- Parameter Sensitivity Analysis
- Model Validation
- Critical Evaluation

## 🚀 Advanced Topics

### Explored Concepts
- Power law distributions
- Scale-free networks
- Self-organized criticality
- Chaos theory basics
- Adaptive complex systems

### Future Extensions
- Machine learning integration with ABM
- Real-time simulation visualization
- GPU-accelerated simulations
- Deep learning for time series (LSTM)
- Multi-agent reinforcement learning

## 📝 Business Application

### GreenGrid AI Lean Canvas
Application of complex models to sustainability startup:
- **Problem**: Energy grid inefficiency
- **Solution**: Agent-based modeling for smart grid optimization
- **Key Metrics**: Energy savings, grid stability
- **Competitive Advantage**: Predictive modeling using complex systems

**File**: `Lean_Business_Model_Canvas_GreenGrid_AI.pdf`

## 🎯 Assessment & Performance

### Assignments
- Virus Spread Simulation: [Grade]
- Time Series Forecasting: [Grade]
- Cellular Automata Implementation: [Grade]

### Exams
- Midterm: [Score]
- Final: [Score]

### Overall Performance
Demonstrated strong understanding of:
- Simulation methodology
- Time series techniques
- Complex systems theory
- Python implementation
- Analytical problem-solving

## 📄 License

Academic coursework - All rights reserved

## 🙏 Acknowledgments

- Course instructors for comprehensive teaching
- Open-source simulation communities
- Research papers on complex systems
- Textbook authors

---

**Course**: CSC1111/CSC1139 - Complex Computational Models
**Academic Year**: 2025-2026
**Topics**: Agent-Based Modeling, Cellular Automata, Time Series
**Last Updated**: June 2026
