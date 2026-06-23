# CA4024/CSC1111 - Building Complex Computational Models
# Complete Exam Answers (2020/21 - 2024/25)

---

# EXAM 1: 2020/2021 (CA4024)

---

## QUESTION 1: Predator-Prey Population Dynamics [25 Marks]

### Q1(a) [4 Marks] - Determine coefficients a, b, c, d

**Given Information:**
- Owl population decays by 50% annually without rats
- Owls convert rat kills to population growth with 40% efficiency
- Rat population grows by 10% annually without owls
- Each owl reduces rat population by 0.1

**Solution:**

For the rat population equation: R_{n+1} = aR_n + bO_n
- In absence of owls: rats grow by 10%, so a = 1.1
- Each owl reduces rats by 0.1, so b = -0.1

For the owl population equation: O_{n+1} = cR_n + dO_n
- In absence of rats: owls decay by 50%, so d = 0.5
- Owls convert rat kills (0.1 rats per owl) with 40% efficiency: c = 0.1 x 0.4 = 0.04

**Answer:**
- **a = 1.1** (rat natural growth rate)
- **b = -0.1** (predation effect on rats)
- **c = 0.04** (owl population increase from predation)
- **d = 0.5** (owl survival without prey)

---

### Q1(b) [11 Marks] - Matrix System, Eigenvalues, Long-term Survival

**Matrix Form:**
```
[R_{n+1}]   [1.1   -0.1] [R_n]
[O_{n+1}] = [0.04   0.5] [O_n]

A = [1.1   -0.1]
    [0.04   0.5]
```

**Finding Eigenvalues:**
det(A - λI) = 0

```
|1.1-λ   -0.1 |
|0.04   0.5-λ | = 0

(1.1-λ)(0.5-λ) - (-0.1)(0.04) = 0
0.55 - 1.1λ - 0.5λ + λ² + 0.004 = 0
λ² - 1.6λ + 0.554 = 0
```

Using quadratic formula:
```
λ = (1.6 ± √(2.56 - 2.216))/2
λ = (1.6 ± √0.344)/2
λ = (1.6 ± 0.5867)/2

λ₁ = 1.093 (dominant eigenvalue)
λ₂ = 0.507
```

**Finding Eigenvector for λ₁ = 1.093:**
```
(A - λ₁I)v = 0
[1.1-1.093   -0.1  ] [v₁]   [0]
[0.04    0.5-1.093] [v₂] = [0]

[0.007   -0.1 ] [v₁]   [0]
[0.04   -0.593] [v₂] = [0]

0.007v₁ - 0.1v₂ = 0
v₁ = 14.3v₂

Eigenvector: [14.3, 1] or normalized [0.998, 0.070]
```

**Long-term Survival Analysis:**
- **λ_max = 1.093 > 1**
- Since the dominant eigenvalue exceeds 1, **both populations will grow continuously** over time
- The ratio of rats to owls will stabilize at approximately 14.3:1
- **Conclusion: The rat population survives and grows in the long term**

---

### Q1(c) [10 Marks] - 50% More Predation, Critical Rate

**New Scenario:** b changes from -0.1 to -0.15 (50% more rats killed per owl)

**New Matrix:**
```
A' = [1.1   -0.15]
     [0.06   0.5 ]
```
Note: c also changes to 0.06 (0.15 × 0.4 = 0.06)

**New Characteristic Equation:**
```
(1.1-λ)(0.5-λ) - (-0.15)(0.06) = 0
0.55 - 1.6λ + λ² + 0.009 = 0
λ² - 1.6λ + 0.559 = 0

λ = (1.6 ± √(2.56 - 2.236))/2
λ = (1.6 ± 0.569)/2

λ₁ = 1.085, λ₂ = 0.515
```

**Analysis:** λ_max = 1.085 > 1, so populations still grow (but slower than before).

**Critical Rate of Predation:**
Set λ_max = 1 for stability:
```
Let b = -k (predation rate) and c = 0.4k (efficiency)

det(A - I) = 0
(1.1-1)(0.5-1) - (-k)(0.4k) = 0
(0.1)(-0.5) + 0.4k² = 0
-0.05 + 0.4k² = 0
k² = 0.125
k = 0.354

Critical predation rate: |b| = 0.354
```

**Conclusion:** The critical rate of predation is approximately **0.354 rats per owl per year**. At this rate, the populations remain stable. Above this rate, both populations would decline.

---

## QUESTION 2: Time Series Decomposition [25 Marks]

### Q2(a) [4 Marks] - Two Decomposition Models

**1. Additive Model:**
```
Y_t = T_t + S_t + C_t + I_t
```
- **When to use:** When seasonal fluctuations are roughly constant regardless of the trend level
- **Example:** Monthly temperatures (variation stays ~10°C regardless of average)

**2. Multiplicative Model:**
```
Y_t = T_t × S_t × C_t × I_t
```
- **When to use:** When seasonal fluctuations scale proportionally with the trend level
- **Example:** Retail sales where holiday spikes grow as business grows

---

### Q2(b) [6 Marks] - Definitions

**Detrending:**
The process of removing the trend component from a time series to isolate other components. For a simple series without cyclical component:
- Calculate the trend using moving averages
- Subtract (additive) or divide (multiplicative) the trend from original data
- Result: Y_t - T_t or Y_t / T_t

**Seasonal Index:**
A numerical value representing the typical effect of a particular season/period relative to the average:
- Calculate detrended values for each period
- Average the detrended values for each season across years
- Normalize so indices sum to n (additive) or average to 1 (multiplicative)

**Seasonally Adjusted:**
Data with the seasonal component removed, revealing underlying trend and irregular movements:
- For additive: Y_t - S_t
- For multiplicative: Y_t / S_t
- Allows comparison of values across different seasons

---

### Q2(c) [15 Marks] - Quarterly Sales Analysis (1979-1982)

**Data Analysis:**

| Year | Q1 | Q2 | Q3 | Q4 |
|------|-----|-----|-----|-----|
| 1979 | 72 | 110 | 117 | 172 |
| 1980 | 76 | 112 | 130 | 194 |
| 1981 | 78 | 119 | 128 | 201 |
| 1982 | 81 | 134 | 141 | 216 |

**Model Selection:**
Looking at the data, Q4 consistently has highest sales with relatively constant seasonal amplitude. The difference between Q4 and Q1 remains around 100 throughout. This suggests an **ADDITIVE MODEL** is appropriate because the seasonal variation is roughly constant regardless of trend level.

**2×4-Point Moving Average Calculation:**

First, calculate 4-point MAs, then center them:

| Period | Sales | 4-pt MA | 2×4 MA (Trend) |
|--------|-------|---------|----------------|
| 1979 Q1 | 72 | - | - |
| 1979 Q2 | 110 | - | - |
| 1979 Q3 | 117 | 117.75 | 119.125 |
| 1979 Q4 | 172 | 120.50 | 123.625 |
| 1980 Q1 | 76 | 126.75 | 127.375 |
| 1980 Q2 | 112 | 128.00 | 128.500 |
| 1980 Q3 | 130 | 129.00 | 130.000 |
| 1980 Q4 | 194 | 131.00 | 131.625 |
| 1981 Q1 | 78 | 132.25 | 132.875 |
| 1981 Q2 | 119 | 133.50 | 134.500 |
| 1981 Q3 | 128 | 135.50 | 137.125 |
| 1981 Q4 | 201 | 138.75 | 140.750 |
| 1982 Q1 | 81 | 142.75 | - |
| 1982 Q2 | 134 | - | - |
| 1982 Q3 | 141 | - | - |
| 1982 Q4 | 216 | - | - |

**Seasonal Index Calculation (Additive):**

Detrended values (Sales - Trend):
| Quarter | 1979 | 1980 | 1981 | Average |
|---------|------|------|------|---------|
| Q1 | - | -51.375 | -54.875 | -53.125 |
| Q2 | - | -16.500 | -15.500 | -16.000 |
| Q3 | -2.125 | 0.000 | -9.125 | -3.750 |
| Q4 | 48.375 | 62.375 | 60.250 | 57.000 |

Adjustment: Sum = -53.125 - 16 - 3.75 + 57 = -15.875
Adjustment per quarter = -15.875/4 = -3.97

**Final Seasonal Indices:**
- Q1: -53.125 + 3.97 = **-49.16**
- Q2: -16.000 + 3.97 = **-12.03**
- Q3: -3.750 + 3.97 = **0.22**
- Q4: 57.000 + 3.97 = **60.97**

**Seasonally Adjusted Data:**

| Period | Sales | Seasonal Index | Seasonally Adjusted |
|--------|-------|----------------|---------------------|
| 1979 Q1 | 72 | -49.16 | 121.16 |
| 1979 Q2 | 110 | -12.03 | 122.03 |
| 1979 Q3 | 117 | 0.22 | 116.78 |
| 1979 Q4 | 172 | 60.97 | 111.03 |
| 1980 Q1 | 76 | -49.16 | 125.16 |
| ... | ... | ... | ... |

---

## QUESTION 3: Stationarity and ARIMA [25 Marks]

### Q3(a) [6 Marks] - Trend Stationary vs Difference Stationary

**Trend Stationary:**
- A time series that has a deterministic (predictable) trend that can be modeled and removed
- The underlying process is stationary once the trend is subtracted
- Example: Y_t = α + βt + ε_t where ε_t is stationary noise
- **How to render stationary:** Fit a regression line (linear or polynomial) to the data and subtract the predicted values: Z_t = Y_t - (α + βt)

**Difference Stationary:**
- A time series with a stochastic (random) trend, often called a unit root or random walk
- The series wanders unpredictably, but changes between periods are stationary
- Example: Y_t = Y_{t-1} + ε_t (random walk)
- **How to render stationary:** Take first differences: ΔY_t = Y_t - Y_{t-1}

**Key Distinction:**
- Trend stationary: shocks are temporary; series returns to trend
- Difference stationary: shocks are permanent; series never returns

---

### Q3(b) [11 Marks] - ACF, PACF, and Information Criteria

**Auto-Correlation Function (ACF):**
- Measures the correlation between a time series and its lagged values
- ACF(k) = Correlation(Y_t, Y_{t-k})
- Includes both direct and indirect effects through intermediate lags
- Useful for identifying MA(q) order: ACF cuts off after lag q

**Partial Auto-Correlation Function (PACF):**
- Measures the correlation between Y_t and Y_{t-k} after removing the linear effects of intermediate lags
- PACF(k) = Correlation(Y_t, Y_{t-k} | Y_{t-1}, ..., Y_{t-k+1})
- Useful for identifying AR(p) order: PACF cuts off after lag p

**Using ACF/PACF to determine p, q:**

| Model | ACF Pattern | PACF Pattern |
|-------|-------------|--------------|
| AR(p) | Tails off gradually | Cuts off after lag p |
| MA(q) | Cuts off after lag q | Tails off gradually |
| ARMA(p,q) | Tails off | Tails off |

**Information Criteria:**
When visual inspection is ambiguous, use:

- **AIC (Akaike Information Criterion):** AIC = -2ln(L) + 2k
- **BIC (Bayesian Information Criterion):** BIC = -2ln(L) + k·ln(n)

Where L is likelihood, k is number of parameters, n is sample size.

**Advantages:**
- Provides objective, quantitative model comparison
- Balances goodness of fit against model complexity
- BIC penalizes complexity more heavily (better for large samples)
- Select model with **lowest** AIC/BIC value

---

### Q3(c) [8 Marks] - Identifying Models from ACF/PACF

**Case (i): [4 Marks]**
- ACF: Single significant spike at lag 1, then cuts off to zero
- PACF: Tails off gradually (appears to decay)

**Model: MA(1)** or ARIMA(0,0,1)

**Justification:** The sharp cutoff in ACF after lag 1 is characteristic of an MA(1) process. The gradually declining PACF confirms this is not an AR process.

**Case (ii): [4 Marks]**
- ACF: Shows significant spikes at lags 1, 12, 24 with gradual decay
- PACF: Shows significant spikes at lags 1 and 12

**Model: SARIMA(1,0,0)(1,0,0)₁₂** or AR(1) with SAR(1)

**Justification:**
- The spike at lag 12 in both ACF and PACF indicates monthly seasonality (m=12)
- The significant PACF at lag 1 suggests AR(1) component
- The significant PACF at lag 12 suggests SAR(1) component
- The pattern is consistent with a seasonal autoregressive model

---

## QUESTION 4: Complex Systems [25 Marks]

### Q4(a) [3 Marks] - Define Complex System

A **Complex System** is a system composed of many interacting components (agents) where:

1. **Emergence:** The collective behavior of the system cannot be predicted or understood simply by analyzing individual components in isolation
2. **Non-linearity:** Small changes in initial conditions or parameters can lead to disproportionately large effects
3. **Adaptation:** Components may change their behavior based on interactions and feedback
4. **Self-organization:** Global patterns arise spontaneously from local interactions without central control

**Examples:** Ant colonies, financial markets, weather systems, the human brain, traffic flow

---

### Q4(b) [10 Marks] - Emergent Properties vs Self-Organization

**Emergent Properties:**
- **Definition:** Macro-level properties or behaviors that arise from micro-level interactions but cannot be predicted from studying individual components alone
- **Example 1:** Flocking behavior in birds - individual birds follow simple rules (separation, alignment, cohesion), but the flock exhibits complex, coordinated movement patterns
- **Example 2:** Consciousness emerging from neural interactions
- **Example 3:** Traffic jams emerging from individual driver behaviors

**Self-Organization:**
- **Definition:** The spontaneous formation of ordered structures or patterns from initially disordered states, without external direction or central control
- **Example 1:** Crystal formation - molecules arrange into regular lattice structures based on local energy minimization
- **Example 2:** Termite mound construction - no blueprint, just local rules
- **Example 3:** Bénard cells in heated fluid

**Key Differences:**
| Aspect | Emergence | Self-Organization |
|--------|-----------|-------------------|
| Focus | Properties/behaviors | Process/mechanism |
| What | The "what" (result) | The "how" (process) |
| Level | Macro-level outcomes | Pattern formation |

**Can self-organization exist without emergence?**
**Yes.** Crystallization is a classic example - molecules self-organize into a regular lattice structure through local energy minimization, but this ordered structure is predictable from molecular properties and doesn't constitute a truly emergent property in the strong sense. The pattern is more complex but fundamentally reducible to component properties.

---

### Q4(c) [12 Marks] - Steps in Modeling a Complex System

**Example: Traffic Flow Simulation**

**Step 1: Define Purpose and Boundaries**
- Purpose: Understand how traffic jams form and propagate
- Boundaries: Single highway segment, specific time period
- Questions: What causes congestion? How do accidents affect flow?

**Step 2: Identify Agents and Environment**
- Agents: Individual vehicles (cars, trucks)
- Environment: Road network with lanes, intersections, speed limits
- External factors: Weather, time of day

**Step 3: Define Agent Properties**
- Internal states: Speed, destination, driver patience
- Heterogeneity: Different vehicle sizes, driver behaviors
- Goals: Reach destination quickly and safely

**Step 4: Define Interaction Rules**
- Agent-Agent: Maintain safe following distance, lane changing decisions
- Agent-Environment: Obey speed limits, respond to signals
- Local rules: React to nearest vehicles only

**Step 5: Implement Computational Model**
- Choose appropriate framework (e.g., NetLogo, Mesa)
- Code agent behaviors and environment
- Set initial conditions and parameters

**Step 6: Validate and Calibrate**
- Compare model output to real traffic data
- Adjust parameters to match observed patterns
- Test with known scenarios (rush hour, accident)

**Step 7: Analyze Emergent Behaviors**
- Observe macro-level patterns (phantom jams, shockwaves)
- Run sensitivity analyses
- Draw conclusions about system dynamics

---

## QUESTION 5: Cellular Automata and ABM [25 Marks]

### Q5(a) [10 Marks] - Compare CA and ABM

| Aspect | Cellular Automata (CA) | Agent-Based Models (ABM) |
|--------|------------------------|--------------------------|
| **Space** | Discrete grid of cells | Continuous or discrete space |
| **Agents** | Cells are fixed/stationary | Agents are mobile |
| **Homogeneity** | All cells follow identical rules | Agents can be heterogeneous |
| **State** | Limited discrete states | Rich internal states, memory |
| **Updates** | Synchronous (all at once) | Often asynchronous |
| **Interactions** | Only with neighbors | Can interact at distance |

**What they are used for:**

**Cellular Automata:**
- Spatial diffusion processes (fire spread, epidemics)
- Pattern formation (crystal growth, vegetation)
- Theoretical computation (Rule 110 is Turing complete)
- Physical simulations (fluid dynamics, gas laws)

**Agent-Based Models:**
- Social systems (market dynamics, crowd behavior)
- Ecological systems (predator-prey, evolution)
- Traffic and transportation
- Organizational behavior and decision-making

**How they are constructed:**

**CA Construction:**
1. Define grid dimensions and boundary conditions
2. Define possible cell states (e.g., 0, 1, 2)
3. Define neighborhood (Von Neumann or Moore)
4. Define transition rules based on neighbor states
5. Apply rules synchronously each time step

**ABM Construction:**
1. Define environment and its properties
2. Create agent types with internal variables
3. Define agent behaviors and decision rules
4. Specify interaction protocols
5. Set up scheduling (random, sequential, etc.)

---

### Q5(b) [6 Marks] - Elements of Cellular Automata

**Core Elements:**

1. **Grid/Lattice:** A regular arrangement of cells in 1D, 2D, or 3D
2. **Cell States:** Finite set of possible values (e.g., 0=dead, 1=alive)
3. **Neighborhood:** Cells that influence the state of a central cell
4. **Transition Rules:** Function determining next state based on current neighborhood
5. **Boundary Conditions:** How edges are handled (periodic, fixed, absorbing)
6. **Time:** Discrete steps with synchronous updates

**Von Neumann Neighborhood (4 cells):**
```
      [N]
  [W] [C] [E]
      [S]
```
- Only orthogonally adjacent cells (North, South, East, West)
- Total of 4 neighbors + center = 5 cells considered

**Moore Neighborhood (8 cells):**
```
  [NW][N][NE]
  [W] [C] [E]
  [SW][S][SE]
```
- All surrounding cells including diagonals
- Total of 8 neighbors + center = 9 cells considered

---

### Q5(c) [9 Marks] - Conway's Game of Life and Emergence

**Conway's Game of Life Rules:**
Using Moore neighborhood, each cell follows:
1. **Birth:** Dead cell with exactly 3 live neighbors becomes alive
2. **Survival:** Live cell with 2-3 live neighbors survives
3. **Death by underpopulation:** Live cell with <2 neighbors dies
4. **Death by overpopulation:** Live cell with >3 neighbors dies

**Emergent Properties:**

1. **Static Patterns (Still Lifes):**
   - Block, Beehive, Loaf
   - Stable configurations that don't change

2. **Oscillators:**
   - Blinker (period 2), Toad, Beacon
   - Patterns that repeat after fixed cycles

3. **Spaceships (Gliders):**
   - Patterns that translate across the grid
   - Glider moves diagonally every 4 generations
   - Not in original rules - emerges from simple interactions

4. **Glider Guns:**
   - Patterns that periodically emit gliders
   - Can be used for computation

5. **Turing Completeness:**
   - The Game of Life can simulate any computer
   - Logic gates can be built from gliders

**Why This Demonstrates Emergence:**
- The four simple rules contain no concept of "movement" or "reproduction"
- Yet gliders move, guns reproduce patterns, and computation is possible
- These complex behaviors are not designed but emerge from local interactions
- Prediction of long-term behavior requires running the simulation

---

## QUESTION 6: Dynamical Systems and Chaos [25 Marks]

### Q6(a) [9 Marks] - Attractors, Strange Attractors, and Limit Cycles

**Attractor:**
- A set of states toward which a dynamical system tends to evolve
- Represents long-term behavior regardless of initial conditions (within basin of attraction)

**Point Attractor (Fixed Point):**
```
    x
    |    \
    |     \
    |      ●  ← Equilibrium point
    |     /
    |    /
    +--------→ t
```
- System converges to a single equilibrium value
- Example: Damped pendulum coming to rest
- All trajectories approach one point

**Limit Cycle:**
```
    y
    |   ╭──────╮
    |  │        │
    | │    ●    │  ← Closed orbit
    |  │        │
    |   ╰──────╯
    +------------→ x
```
- System settles into a periodic, repeating trajectory
- Closed loop in phase space
- Example: Heartbeat, predator-prey oscillations
- Trajectories approach from both inside and outside

**Strange Attractor:**
```
    z
    |     ∞∞
    |    ∞  ∞
    |   ∞    ∞   ← Lorenz butterfly
    |    ∞  ∞
    |     ∞∞
    +------------→ x
```
- Fractal structure with non-integer dimension
- Trajectories never repeat exactly (aperiodic)
- Sensitive dependence on initial conditions (chaos)
- Example: Lorenz attractor in weather systems
- Bounded but never repeating

---

### Q6(b) [8 Marks] - Logistic Map Bifurcation Diagram

**The Logistic Map:** x_{n+1} = r·x_n(1 - x_n)

**Point A (r ≈ 3.45):**
- **First Period-Doubling Bifurcation**
- Before this point (r < 3): single stable fixed point
- After: system oscillates between 2 values
- The fixed point becomes unstable and splits into period-2 cycle

**Point B (r ≈ 3.54):**
- **Second Period-Doubling (Period-4)**
- The period-2 cycle becomes unstable
- System now oscillates through 4 distinct values
- Each arm of the bifurcation splits again

**Point C (r ≈ 3.83):**
- **Window of Stability (Period-3)**
- Within the chaotic region, a clear window appears
- Period-3 cycle is stable
- Famous "period-3 implies chaos" theorem (Li-Yorke)
- Evidence that chaos contains infinite periodic windows

**Point D (r ≈ 3.9+):**
- **Fully Chaotic Region**
- Dense, apparently random scatter of points
- System visits essentially all values between 0 and 1
- Extremely sensitive to initial conditions
- Still deterministic but practically unpredictable

---

### Q6(c) [8 Marks] - Lotka-Volterra Limit Cycle

**The Lotka-Volterra Equations:**
```
dR/dt = αR - βRP    (Prey: growth minus predation)
dP/dt = δRP - γP    (Predator: gains from predation minus death)
```

**Phase Space Diagram:**
```
Predator (P)
    ^
    |     ╭────────╮
    |    ↑          ↓
    |   │            │
  P*|---│-----●------│----- (equilibrium)
    |   │            │
    |    ↑          ↓
    |     ╰────────╯
    +-------|--------→ Prey (R)
           R*
```

**Cycle Description:**

1. **Phase 1: Prey Abundant, Predators Increase**
   - Starting bottom-left: prey population is recovering
   - Abundant food → predator population grows rapidly
   - Arrow moves up and right

2. **Phase 2: Predators Peak, Prey Decline**
   - Top of cycle: maximum predator population
   - Heavy predation → prey population crashes
   - Arrow moves right and down

3. **Phase 3: Prey Scarce, Predators Decline**
   - Right side: prey nearly depleted
   - Insufficient food → predator population crashes
   - Arrow moves down and left

4. **Phase 4: Predators Scarce, Prey Recover**
   - Bottom: predator population at minimum
   - Reduced predation → prey recover
   - Arrow moves left and up, returning to Phase 1

**Key Features:**
- Closed orbit = perpetual oscillation
- Both populations never go extinct
- Phase relationship: predator peaks lag behind prey peaks
- Amplitude depends on initial conditions (not a true limit cycle in mathematical sense)

---

# EXAM 2: 2021/2022 (CA4024)

---

## QUESTION 1: Time Series Forecasting [25 Marks]

### Q1(a) [4 Marks] - Ex Post vs Ex Ante Forecasting

**Ex Post Forecasting:**
- Forecasts made for periods where actual values are already known
- Used for model validation, backtesting, and error calculation
- Example: Using 2000-2010 data to predict 2011-2015, then comparing to actual 2011-2015 values
- Considered the "gold standard" because accuracy can be objectively measured
- Purpose: Evaluate forecast model quality before deploying for real predictions

**Ex Ante Forecasting:**
- Forecasts predicting genuinely unknown future values
- True forecasting with no actual values for comparison (yet)
- Example: Using all available data to predict next year's sales
- Relies on assumption that historical patterns continue
- Higher risk: model errors only discovered after the fact

---

### Q1(b) [12 Marks] - Time Series Decomposition (2004-2007 Sales)

**Data:**

| Year | Q1 | Q2 | Q3 | Q4 |
|------|------|------|------|------|
| 2004 | 11 | 12.5 | 22 | 15 |
| 2005 | 12.5 | 13 | 23 | 15.5 |
| 2006 | 14 | 15.5 | 24.5 | 17.5 |
| 2007 | 15 | 17 | 27 | 21 |

**Model Selection:**
The data shows Q3 consistently highest with relatively stable seasonal amplitude. An **ADDITIVE MODEL** is appropriate since seasonal variations appear constant over time.

**2×4pt Moving Average (Trend):**

| Period | Sales | 4-pt MA | Trend (2×4) |
|--------|-------|---------|-------------|
| 2004 Q3 | 22 | 15.125 | 15.281 |
| 2004 Q4 | 15 | 15.438 | 15.594 |
| 2005 Q1 | 12.5 | 15.750 | 15.938 |
| 2005 Q2 | 13 | 16.125 | 16.250 |
| 2005 Q3 | 23 | 16.375 | 16.563 |
| 2005 Q4 | 15.5 | 16.750 | 17.000 |
| 2006 Q1 | 14 | 17.250 | 17.469 |
| 2006 Q2 | 15.5 | 17.688 | 17.906 |
| 2006 Q3 | 24.5 | 18.125 | 18.438 |
| 2006 Q4 | 17.5 | 18.750 | 19.063 |
| 2007 Q1 | 15 | 19.375 | 19.625 |
| 2007 Q2 | 17 | 19.875 | - |

**Seasonal Indices (Additive):**

| Quarter | Values (Sales - Trend) | Average |
|---------|------------------------|---------|
| Q1 | -3.438, -3.469, -4.625 | -3.84 |
| Q2 | -3.25, -2.406, -2.625 | -2.76 |
| Q3 | 6.719, 6.437, 6.062 | 6.41 |
| Q4 | -0.594, -1.5, -1.563 | -1.22 |

Adjustment factor = (-3.84 - 2.76 + 6.41 - 1.22)/4 = -0.35
**Final Seasonal Indices:** Q1: -3.49, Q2: -2.41, Q3: 6.76, Q4: -0.87

---

### Q1(c) [9 Marks] - 2008 Forecast

**Forecasting Procedure:**
1. Extrapolate trend line to 2008 quarters
2. Add seasonal indices

**Trend Extrapolation** (Linear trend ≈ +0.6 per quarter):
- Trend 2008 Q1 ≈ 20.8
- Trend 2008 Q2 ≈ 21.4
- Trend 2008 Q3 ≈ 22.0
- Trend 2008 Q4 ≈ 22.6

**2008 Forecasts:**
- Q1: 20.8 + (-3.49) = **17.3**
- Q2: 21.4 + (-2.41) = **19.0**
- Q3: 22.0 + 6.76 = **28.8**
- Q4: 22.6 + (-0.87) = **21.7**

**Classification:** This is an **Ex Ante** forecast because:
- We are predicting future values (2008) that are not in our dataset
- No actual values exist to compare against at the time of forecasting
- The model is applied to genuinely unknown future periods

---

## QUESTION 2: Stationarity [25 Marks]

### Q2(a) [16 Marks] - Trend vs Difference Stationarity

**(a) Trend Stationary:**
A series where non-stationarity is due to a deterministic trend:
- Y_t = α + βt + ε_t
- The trend is predictable and can be modeled
- Shocks (ε_t) are temporary; series returns to trend
- **Remedy:** Subtract the fitted trend

**(b) Difference Stationary:**
A series with stochastic (random walk) trend:
- Y_t = Y_{t-1} + ε_t
- No predictable trend; wanders randomly
- Shocks are permanent; series never returns to previous level
- **Remedy:** Take first differences: ΔY_t = Y_t - Y_{t-1}

**For Figure Q2(a):**
The series shows a clear upward trend with fluctuations around it. This appears to be **Trend Stationary** because:
- The trend appears deterministic (roughly linear)
- Fluctuations seem to return to the trend line
- Variance appears relatively constant

**Applying Detrending:**
1. Fit linear regression: Ŷ_t = a + bt
2. Subtract: Z_t = Y_t - Ŷ_t
3. Result: Stationary series fluctuating around zero

**Sketch of detrended result:**
```
     Z_t
      |    ∼∼∼∼∼∼∼∼∼∼∼∼
  0 ──|──∼∼∼∼∼∼∼∼∼∼∼∼∼∼── (mean = 0)
      |    ∼∼∼∼∼∼∼∼∼∼∼∼
      +-------------------→ t
```

**ACF Sketches:**

Original series (non-stationary):
```
ACF
 1 |████████████████████
   |███████████████████
   |██████████████████
   |█████████████████
   +--1--2--3--4--5--→ lag
```
- Slowly decaying ACF indicates non-stationarity

Detrended series (stationary):
```
ACF
 1 |██
   |█
   |
   |
   +--1--2--3--4--5--→ lag
```
- Rapid decay to zero indicates stationarity

---

### Q2(b) [9 Marks] - Identifying Stationary Series

**Stationary Series Criteria:**
- Constant mean over time
- Constant variance over time
- Autocovariance depends only on lag, not time

**Analysis of Figure Q2(b):**

**(a) - NOT Stationary:** Shows random walk behavior with changing mean
**(b) - STATIONARY:** Fluctuates around constant mean with constant variance
**(c) - NOT Stationary:** Clear upward/downward trend, changing mean
**(d) - NOT Stationary:** Increasing variance over time
**(e) - NOT Stationary:** Strong cyclical pattern with varying amplitude
**(f) - NOT Stationary:** Clear trend
**(g) - Possibly Stationary:** Appears cyclical but around constant mean
**(h) - NOT Stationary:** Strong periodic pattern (could be seasonality)
**(i) - NOT Stationary:** Clear upward trend

---

## QUESTION 3: Complex Systems & Bifurcation [25 Marks]

### Q3(a) [8 Marks] - Emergence and Self-Organization

**Emergent Behavior:**
- **Definition:** Complex patterns or behaviors at the macro-level arising from simple interactions at the micro-level
- **Example:** Murmuration of starlings - thousands of birds create stunning aerial patterns by each following simple rules about staying close to neighbors while avoiding collisions
- **Key characteristic:** The whole is greater than sum of parts; behavior cannot be predicted from individual components

**Self-Organization:**
- **Definition:** The spontaneous emergence of order from initial disorder without external control
- **Example:** Hurricane formation - warm moist air rises, creates low pressure, draws in surrounding air, rotation begins due to Coriolis effect, all without any external organizer
- **Key characteristic:** No central controller or blueprint; order emerges from local interactions

**Difference:**
- Self-organization is the PROCESS by which systems spontaneously form patterns
- Emergence is the RESULT - the properties that appear
- Self-organization → leads to → Emergent behavior
- One describes mechanism, other describes outcome

---

### Q3(b) [9 Marks] - Good Model Design

**Characteristics of a Good Model:**
1. **Parsimony:** Simple as possible while capturing essential dynamics
2. **Validity:** Produces results consistent with real-world observations
3. **Transparency:** Rules and assumptions are clear and justifiable
4. **Robustness:** Stable under reasonable parameter variations
5. **Predictive Power:** Can forecast or explain previously unobserved phenomena

**Example: Epidemic Spread Model (SIR)**

**Step 1: Define Purpose**
- Goal: Understand disease spread and evaluate intervention strategies
- Question: How does vaccination rate affect outbreak size?

**Step 2: Identify Components**
- Agents: Individuals in population
- States: Susceptible (S), Infected (I), Recovered (R)
- Environment: Contact network

**Step 3: Define Rules**
- Infection: S → I with probability β per contact with I
- Recovery: I → R with probability γ per time step
- Immunity: R individuals cannot be reinfected

**Step 4: Implement**
- Grid-based CA or network ABM
- Code transition rules
- Set initial conditions (Patient Zero)

**Step 5: Validate**
- Compare epidemic curves to historical data
- Check R₀ (basic reproduction number) matches real disease
- Verify herd immunity threshold

**Step 6: Experiment**
- Test vaccination scenarios
- Identify critical coverage levels

---

### Q3(c) [8 Marks] - Logistic Map Bifurcation

**Critical Points in the Bifurcation Diagram:**

**r < 1:**
- Population dies out regardless of initial condition
- Single stable point at x = 0

**1 < r < 3:**
- Single stable fixed point
- Population converges to x* = (r-1)/r
- Steady state equilibrium

**r ≈ 3 (First Bifurcation):**
- Fixed point becomes unstable
- Period-2 cycle emerges
- Population oscillates between two values

**r ≈ 3.449 (Period-4):**
- Period-2 becomes unstable
- Four-point cycle appears
- Further period doubling continues

**r ≈ 3.57 (Onset of Chaos):**
- Feigenbaum point
- Period-doubling cascade accumulates
- Chaos begins

**r > 3.57 (Chaotic Region):**
- Aperiodic, unpredictable behavior
- Sensitive dependence on initial conditions
- Dense bands in diagram

**r ≈ 3.83 (Period-3 Window):**
- Island of stability within chaos
- Clear period-3 cycle visible
- Period-3 implies chaos (Li-Yorke theorem)

---

## QUESTION 4: ABM and CA [25 Marks]

### Q4(a) [6 Marks] - ABM Agent Properties and Boids

**(i) Typical Properties of ABM Agents:**

1. **Autonomy:** Agents make independent decisions without central control
2. **Heterogeneity:** Agents can differ in attributes and behaviors
3. **Bounded Rationality:** Agents have limited information and cognitive capacity
4. **Adaptation:** Agents can learn and change behavior over time
5. **Mobility:** Agents can move through space
6. **Internal State:** Agents have memory and internal variables
7. **Goal-Directed:** Agents pursue objectives

**(ii) Boids Flocking Rules:**

```
Rule 1: SEPARATION
         ↖ ↑ ↗
          \|/
      ← ──●── →    Steer AWAY from nearby birds
          /|\      to avoid collision
         ↙ ↓ ↘

Rule 2: ALIGNMENT
         ↗ ↗ ↗
         → → →      Match direction and speed
         ↗ ↗ ↗      of neighboring birds

Rule 3: COHESION
         ↘   ↙
           ↓        Steer TOWARD average position
         ↗   ↖      of nearby birds (center of mass)
```

**Combined Effect:** These three simple rules produce realistic flocking behavior - a classic example of emergence from local interactions.

---

### Q4(b) [5 Marks] - Community Detection (Louvain Method)

**Louvain Method for Modularity Optimization:**

**Goal:** Maximize modularity Q, which measures quality of community division

**Modularity Formula:**
Q = (1/2m) Σ[A_ij - k_i·k_j/2m]δ(c_i, c_j)

Where:
- A_ij = adjacency matrix
- k_i = degree of node i
- m = total edges
- δ = 1 if i and j in same community

**Algorithm Steps:**

**Phase 1: Local Optimization**
1. Start with each node in its own community
2. For each node i, calculate modularity gain from moving i to neighbor j's community
3. Move i to community giving maximum positive gain
4. Repeat until no improvements possible

**Phase 2: Aggregation**
1. Build new network where nodes are communities from Phase 1
2. Edge weights = sum of edges between original communities
3. Apply Phase 1 again to aggregated network

**Repeat** Phases 1 and 2 until modularity no longer increases

**Advantages:**
- Fast: O(n log n) complexity
- Greedy but effective
- Handles large networks well
- Produces hierarchical community structure

---

### Q4(c) [6 Marks] - 2D CA Time Evolution

**Initial State (t=0):**
```
□ □ □ □ □ □
□ ■ ■ □ □ □
□ ■ ■ □ □ □
□ □ □ □ □ □
□ □ □ □ □ □
```

**Rules:**
- Von Neumann neighborhood (4 neighbors)
- Next state = round(S/5) where S = sum of neighborhood states

**t=1 Calculation:**
For each gray cell (1), its neighborhood sum S includes itself + 4 neighbors.
- Top-left gray: S = 1+1+1+0+0 = 3, round(3/5) = 1
- Pattern stabilizes as neighbors influence each other

```
t=1:
□ □ □ □ □ □
□ ■ ■ □ □ □
□ ■ ■ □ □ □
□ □ □ □ □ □
□ □ □ □ □ □
```

**t=2 and t=3:**
The pattern remains stable (still life) because each gray cell sees exactly 3 gray neighbors + itself = S ≈ 3-4, round(3-4/5) = 1.

---

### Q4(d) [8 Marks] - Forest Fire CA Model

**States:**
- **0 = Empty** (burned out or never forested)
- **1 = Tree** (alive, burnable)
- **2 = Burning** (currently on fire)

**State Transition Diagram:**
```
        Lightning/
         Neighbor
    ┌─────────────┐
    │             ↓
  [Tree] ────→ [Burning] ────→ [Empty]
    ↑              (1 step)        │
    │                              │
    └──────── Regrowth ────────────┘
               (probability p)
```

**Transition Rules:**
1. Empty → Tree: With probability p (regrowth)
2. Tree → Burning: If any Von Neumann neighbor is Burning, OR lightning strikes (probability f)
3. Burning → Empty: Always (fire consumes in one step)

**CA Properties Demonstrated:**
- **Discrete space:** Grid of cells
- **Discrete states:** 0, 1, 2
- **Local interaction:** Only neighbors affect state
- **Synchronous update:** All cells update simultaneously
- **Emergence:** Fire patterns, critical density thresholds

**Different Dimensions:**

**1-D Space:**
```
□ ■ ■ ■ □ ■ ■ □ ■ ■ ■ ■
```
- Fire can only spread left/right
- Any gap (empty cell) completely blocks fire
- Easy containment with firebreaks

**3-D Space:**
```
    Layer 3: ■ ■ ■
    Layer 2: ■ ● ■  (fire at ●)
    Layer 1: ■ ■ ■
```
- Fire spreads in 6 directions (up/down/left/right/front/back)
- Much harder to contain
- Exponentially more paths for propagation
- More realistic for actual forest fires (trees have height)

---

## QUESTION 5: Markov Processes and MCMC [25 Marks]

### Q5(a) [4 Marks] - Markov Process Definition

**A Markov Process** is a stochastic (random) process where the probability of the next state depends ONLY on the current state, not on the sequence of states that preceded it.

**Mathematically:** P(X_{t+1} | X_t, X_{t-1}, ..., X_0) = P(X_{t+1} | X_t)

**Main Assumptions:**
1. **Memorylessness (Markov Property):** Future depends only on present, not past
2. **Finite State Space:** Countable number of possible states
3. **Time Homogeneity:** Transition probabilities don't change over time
4. **Stationarity:** The process has well-defined limiting behavior

---

### Q5(b) [8 Marks] - Storm Category Markov Chain

**Given Transitions:**

| From/To | Cat 1 | Cat 2 | Cat 3 | Cat 4 |
|---------|-------|-------|-------|-------|
| Cat 1 | 0.05 | 0.75 | 0.20 | 0 |
| Cat 2 | 0.25 | 0.30 | 0.45 | 0 |
| Cat 3 | 0.10 | 0.40 | 0.30 | 0.20 |
| Cat 4 | 0 | 0.15 | 0.30 | 0.55 |

**(i) Transition Diagram:**
```
          0.75
    ┌──────────────┐
    │              ↓
  [C1]           [C2]
    ↑   0.25      ↓│  0.45
    │  ┌──────────┘│
0.05│  │    0.40   ↓  0.30
    │  │     ┌───[C3]───┐
    │  │     │     ↑    │ 0.20
    └──┴─────┘  0.30│   ↓
                    └──[C4]
                       ↺ 0.55
```

**Transition Matrix P:**
```
      C1    C2    C3    C4
P = [0.05  0.75  0.20  0.00]  C1
    [0.25  0.30  0.45  0.00]  C2
    [0.10  0.40  0.30  0.20]  C3
    [0.00  0.15  0.30  0.55]  C4
```

**(ii) Probability Cat 2 → Cat 1:**

**After 1 step:** P(C2→C1) = **0.25** (directly from matrix)

**After 2 steps:** P²[2,1]
```
P² = P × P

Row 2 of P² gives probabilities starting from C2:
P(C2→C1 in 2 steps) = P(C2→C1)×P(C1→C1) + P(C2→C2)×P(C2→C1) + P(C2→C3)×P(C3→C1) + P(C2→C4)×P(C4→C1)
= 0.25×0.05 + 0.30×0.25 + 0.45×0.10 + 0×0
= 0.0125 + 0.075 + 0.045 + 0
= **0.1325**
```

---

### Q5(c) [5 Marks] - MCMC Definition and Uses

**Markov Chain Monte Carlo (MCMC):**
A class of algorithms that sample from probability distributions by constructing a Markov chain whose equilibrium (stationary) distribution equals the target distribution.

**When to Use:**
1. **Bayesian Inference:** When computing posterior distributions directly is intractable
2. **High-dimensional integration:** When analytical solutions don't exist
3. **Complex probability models:** When normalization constants are unknown
4. **Sampling from non-standard distributions:** When direct sampling is impossible

**Core Concept:**
- Instead of calculating P(θ|data) directly
- Build a random walk that visits parameter values
- After "burn-in," samples represent draws from the target distribution
- More visits to a region = higher probability in that region

---

### Q5(d) [8 Marks] - MCMC Algorithm and Samplers

**Bayesian Framework:**
```
Posterior ∝ Prior × Likelihood
P(θ|D) ∝ P(θ) × P(D|θ)
```

**MCMC Workflow:**

1. **Initialize:** Start with initial parameter guess θ₀
2. **Propose:** Generate candidate θ' from proposal distribution
3. **Evaluate:** Calculate posterior probability ratio
4. **Accept/Reject:** Move to θ' or stay at θ based on ratio
5. **Repeat:** Build chain of samples
6. **Analyze:** After burn-in, samples approximate posterior

**Role of the Sampler:**
The sampler proposes new parameter values and decides whether to accept them. It determines HOW the Markov chain explores parameter space.

**Metropolis-Hastings Sampler:**

**Algorithm:**
1. Propose θ' from symmetric proposal distribution (e.g., θ' ~ Normal(θ_current, σ))
2. Calculate acceptance ratio:
   α = min(1, P(θ'|D) / P(θ_current|D))
3. Generate u ~ Uniform(0,1)
4. If u < α: accept θ', else stay at θ_current

**Advantages:**
- Simple to implement
- Works with any proposal distribution
- Only requires ratios (normalizing constants cancel)
- Proven convergence guarantees
- Flexible for various target distributions

**Intuition:**
- Always accept moves to higher probability regions
- Sometimes accept moves to lower probability (enables exploration)
- Resulting chain concentrates in high-probability areas while occasionally exploring elsewhere

---

# EXAM 3: 2022/2023 (CA4024)

---

## QUESTION 1: Time Series Types and ARIMA [25 Marks]

### Q1(a) [9 Marks] - Continuous vs Discrete Time Series

**Continuous Time Series:**
- Values can change at any point in time
- Time is measured on a continuous scale
- **Examples:**
  - Temperature readings from a sensor
  - Stock prices during trading hours
  - Blood pressure monitored continuously
  - Water level in a reservoir

```
Value
  |    ~~~~~
  |   ~     ~~~
  | ~~         ~~
  |~             ~
  +------------------→ Time
     (any instant)
```

**Discrete Time Series:**
- Values recorded only at specific, equally-spaced intervals
- Time moves in discrete steps
- **Examples:**
  - Daily closing stock prices
  - Monthly unemployment figures
  - Quarterly GDP
  - Annual rainfall totals

```
Value
  |  ●     ●
  |     ●     ●
  | ●           ●
  |       ●
  +--●--●--●--●--●--→ Time
     t  t+1 t+2 t+3
```

**How Discrete Series Arise:**

1. **Sampling:** Continuous phenomena measured at intervals
   - Temperature recorded hourly

2. **Aggregation:** Summing/averaging over periods
   - Daily sales totals from continuous transactions

3. **Inherently Discrete Events:**
   - Number of births per month
   - Annual elections

4. **Data Collection Constraints:**
   - Surveys conducted quarterly
   - Financial reporting periods

---

### Q1(b) [6 Marks] - ARIMA Model Identification

**Case 1 - Fig Q1(b)(i):**
- **ACF:** Tails off slowly, exponential decay
- **PACF:** Cuts off sharply after lag 2

**Model: AR(2)** or ARIMA(2,0,0)

**Justification:** The PACF cutoff after lag 2 indicates autoregressive order p=2. The slowly decaying ACF confirms this is an AR process rather than MA.

**Case 2 - Fig Q1(b)(ii):**
- **ACF:** Cuts off sharply after lag 2
- **PACF:** Tails off gradually

**Model: MA(2)** or ARIMA(0,0,2)

**Justification:** The ACF cutoff after lag 2 indicates moving average order q=2. The tailing PACF confirms this pattern.

---

### Q1(c) [10 Marks] - SARIMA Model Identification

**Case 1 - Fig Q1(c)(i):**
- **ACF:** Strong spikes at lags 1-3, then decay. Negative spike around lag 12.
- **PACF:** Significant spikes at lags 1, 2, and lag 12

**Model: SARIMA(2,0,0)(1,0,0)₁₂**

**Justification:**
- PACF cutoff at lag 2 → AR(2)
- Significant PACF at lag 12 → SAR(1)
- The seasonal period m = 12 (monthly data)
- No MA components suggested by ACF tailing off

**Case 2 - Fig Q1(c)(ii):**
- **ACF:** Decays but very slowly, significant through lag 12+
- **PACF:** Large spike at lag 1, significant spike at lag 12

**Model: SARIMA(1,1,0)(1,0,0)₁₂** or possibly needs differencing

**Justification:**
- Very slow ACF decay suggests non-stationarity → d=1
- PACF spike at lag 1 → AR(1)
- PACF spike at lag 12 → SAR(1)
- Seasonal period m = 12

---

## QUESTION 2: Decomposition [25 Marks]

### Q2(a) [4 Marks] - Two Decomposition Models

**1. Additive Model:**
Y_t = T_t + S_t + C_t + I_t

- Use when seasonal amplitude is CONSTANT regardless of trend level
- Seasonal effect is fixed absolute amount

**2. Multiplicative Model:**
Y_t = T_t × S_t × C_t × I_t

- Use when seasonal amplitude SCALES with trend level
- Seasonal effect is proportional percentage

---

### Q2(b) [6 Marks] - Component Definitions

**Detrending:**
Removing the long-term trend from data to reveal other components.
- Method: Fit trend line (moving average or regression) and subtract
- For additive: Detrended = Y_t - T_t

**Seasonal Index:**
A factor representing the typical deviation for each season.
- Method: Average the detrended values for each season across all years
- Represents "how much above/below average" that season typically is

**Seasonally Adjusted:**
Data with seasonal effects removed, showing underlying trend and irregularity.
- Method: Remove seasonal index from each observation
- For additive: SA_t = Y_t - S_i
- Allows fair comparison across different seasons

---

### Q2(c) [15 Marks] - School Leavers Data Analysis

**Data:**
| Year | Q1 | Q2 | Q3 | Q4 |
|------|-----|-----|------|-----|
| 1979 | 22 | 12 | 110 | 31 |
| 1980 | 21 | 26 | 150 | 70 |
| 1981 | 50 | 36 | 146 | 110 |

**Model Choice:** Strong seasonality with Q3 consistently high (school graduation season). Seasonal amplitude appears to increase with level → **MULTIPLICATIVE MODEL**

**2×4 Moving Average Calculations:**

| Period | Value | 4-pt MA | Trend |
|--------|-------|---------|-------|
| 1979 Q3 | 110 | 43.75 | 51.875 |
| 1979 Q4 | 31 | 60.00 | 65.125 |
| 1980 Q1 | 21 | 70.25 | 75.500 |
| 1980 Q2 | 26 | 80.75 | 82.750 |
| 1980 Q3 | 150 | 84.75 | 86.375 |
| 1980 Q4 | 70 | 88.00 | 90.000 |
| 1981 Q1 | 50 | 92.00 | 94.250 |
| 1981 Q2 | 36 | 96.50 | - |
| 1981 Q3 | 146 | - | - |

**Seasonal Index (Multiplicative):**

Ratio = Sales/Trend:
| Quarter | Ratios | Average |
|---------|--------|---------|
| Q1 | 0.278, 0.530 | 0.404 |
| Q2 | 0.314, 0.382 | 0.348 |
| Q3 | 2.122, 1.737 | 1.930 |
| Q4 | 0.476, 0.778 | 0.627 |

Normalize (should average to 1):
Sum = 3.309, Factor = 4/3.309 = 1.209
**Indices:** Q1: 0.489, Q2: 0.421, Q3: 2.333, Q4: 0.758

---

## QUESTION 3: Forecasting Methods [25 Marks]

### Q3(a) [6 Marks] - Qualitative vs Quantitative Forecasts

**Qualitative Forecasting:**
- Based on expert judgment, intuition, and subjective assessment
- Used when historical data is unavailable or unreliable
- **Examples:**
  - Delphi method (expert panel consensus)
  - Market research surveys for new product launch
  - Executive opinions for strategic planning
  - Sales force estimates

**Quantitative Forecasting:**
- Based on mathematical analysis of historical numerical data
- Assumes past patterns will continue
- **Examples:**
  - Time series models (ARIMA, Exponential Smoothing)
  - Regression analysis
  - Moving averages
  - Neural network predictions

**Key Difference:** Qualitative relies on human judgment; Quantitative relies on data and algorithms.

---

### Q3(b) [10 Marks] - Ex Post vs Ex Ante (Gold Standard)

**Ex Post Forecasting:**
- Making predictions for periods where actual values are already known
- Used for model validation and testing
- Can calculate actual forecast errors (MAE, RMSE, MAPE)
- **Example:** Use 2010-2018 data to predict 2019, compare to actual 2019

**Ex Ante Forecasting:**
- Predicting genuinely unknown future values
- True forecasting for decision-making
- Cannot verify accuracy until future arrives
- **Example:** Use all data through 2023 to predict 2024

**Gold Standard:** **Ex Post** forecasting is considered the gold standard because:
1. Provides objective accuracy measurement
2. Allows model comparison on same holdout set
3. Enables backtesting across multiple periods
4. Reveals model weaknesses before deployment
5. Statistical validation possible (not just "we'll see")

---

### Q3(c) [9 Marks] - Naïve Model and Exponential Smoothing

**Naïve Forecasting Model:**
```
ŷ_{t+1} = y_t
```
The forecast for the next period equals the most recent observation.

**Uses in Practice:**
1. **Baseline benchmark:** If sophisticated models can't beat Naïve, they're worthless
2. **Random walks:** Optimal for true random walk series
3. **Quick estimates:** Immediate forecast without computation
4. **Reference point:** Standard comparison for forecast accuracy

**Simple Exponential Smoothing:**
```
ŷ_{t+1} = αy_t + (1-α)ŷ_t
```
Where 0 < α ≤ 1 is the smoothing constant.

**Reduction to Naïve:**
When **α = 1**:
```
ŷ_{t+1} = 1·y_t + (1-1)·ŷ_t
ŷ_{t+1} = y_t + 0
ŷ_{t+1} = y_t
```

This is exactly the Naïve model. Therefore, Naïve forecasting is a special case of Exponential Smoothing where all weight is placed on the most recent observation and no weight on historical forecasts.

---

## QUESTION 4: Population Dynamics [25 Marks]

### Q4(a) [4 Marks] - Ant/Anteater Coefficients

**System:** Ants (R) and Anteaters (O)

From the description:
- Ant growth without anteaters: 10% → **a = 1.1**
- Each anteater reduces ants by 0.1 → **b = -0.1**
- Anteaters convert consumption with 40% efficiency: c = 0.1 × 0.4 = **c = 0.04**
- Anteaters decay 50% without ants → **d = 0.5**

**Coefficients:** a = 1.1, b = -0.1, c = 0.04, d = 0.5

(Same as owl/rat problem from 2021 exam)

---

### Q4(b) & Q4(c) - [21 Marks]

See Question 1 from 2020/21 exam - identical problem and solution.

---

## QUESTION 5: Complex Systems Summary [25 Marks]

### Q5(a) [3 Marks] - Complex System Definition

A **Complex System** is a system made up of many interacting components where:
- Global behavior emerges from local interactions
- The whole cannot be understood by analyzing parts in isolation
- Exhibits non-linear dynamics and feedback loops
- Often displays emergence, self-organization, and adaptation

---

### Q5(b) [8 Marks] - Modeling Steps

See Q4(c) from 2020/21 exam for detailed modeling steps example.

---

### Q5(c) [10 Marks] - CA vs ABM

See Q5(a) from 2020/21 exam for detailed comparison.

---

### Q5(d) [4 Marks] - Markov Process

See Q5(a) from 2021/22 exam for definition and assumptions.

---

## QUESTION 6: Network Analysis [25 Marks]

### Q6(a) [4 Marks] - Community Detection

**Community Detection:**
The process of identifying groups (communities/clusters) of nodes in a network that are more densely connected internally than with the rest of the network.

**Usefulness Example:**
In a social network, community detection can identify:
- Friend groups or cliques
- Interest-based communities
- Organizational departments
- Potential customer segments for marketing

---

### Q6(b) [6 Marks] - Adjacency Matrix and Initial Modularity

**Network from Figure Q6(b):** 8 nodes (Susan, Jim, James, Ben, John, Peter, Mary, Alice)

**Adjacency Matrix (unweighted):**
```
        Su Ji Ja Be Jo Pe Ma Al
Susan    0  1  1  0  0  0  0  0
Jim      1  0  1  0  1  0  0  1
James    1  1  0  1  0  0  0  0
Ben      0  0  1  0  1  0  0  0
John     0  1  0  1  0  1  1  1
Peter    0  0  0  0  1  0  1  0
Mary     0  0  0  0  1  1  0  0
Alice    0  1  0  0  1  0  0  0
```

**Modularity with each node as own community:**

When each node is its own community, no pairs are in the same community.
Modularity Q = 0 (or slightly negative) because:
- No edges contribute positively (no within-community edges)
- The expected term subtracts from zero

**Q = -Σ(k_i × k_j)/(2m) for all edges = negative value**

---

### Q6(c) [10 Marks] - Alice's Community Assignment

**Analysis using Louvain method logic:**

Alice's edges: Connected to Jim (1) and John (1)

**Option 1: Join (Susan, Jim, James)**
- Alice gains edges to Jim
- Internal edges increase by 1
- Modularity gain positive

**Option 2: Join (John, Ben, Mary, Peter)**
- Alice gains edges to John
- Internal edges increase by 1
- Must consider total edges in community

**Calculation:**
- Alice has degree 2 (Jim and John)
- Jim is in the "left" cluster
- John is in the "right" cluster
- Alice bridges both groups

**Conclusion:** Alice should join **(John, Ben, Mary, Peter)** because:
- More total connections to this group (stronger pull toward John's community)
- The modularity gain would be higher joining the larger community she connects to
- Staying alone provides no modularity benefit

---

### Q6(d) [5 Marks] - Forum Network Analysis

**Observations from Figure Q6(d):**

1. **Homophily by Area of Study:** Students tend to cluster with others from the same discipline (same node colors cluster together)

2. **Cross-disciplinary Communication:** Some communities span multiple colors, suggesting interdisciplinary interaction

3. **Bridge Nodes:** Certain students (like node 19) connect different communities, acting as information bridges

4. **Community Structure Reflects Study Groups:** Students who communicate frequently likely study together

5. **Potential Collaboration Networks:** Communities might represent project groups or study circles

---

# EXAM 4: 2023/2024 (CA4024)

---

## QUESTION 1: Time Series Analysis [25 Marks]

### Q1(a) [6 Marks] - Continuous vs Discrete

See Q1(a) from 2022/23 exam.

---

### Q1(b) [6 Marks] - Time Series Components

**Figure Q1(b) Analysis:**

**Top-Left (Marriages data 1820-1900):**
- Clear cyclical pattern with roughly 10-year cycles
- Moderate upward trend
- **Components:** Trend + Cyclical

**Top-Right (CO2 ppm 1965-1980):**
- Strong upward trend
- Regular seasonal fluctuations (annual CO2 cycle)
- **Components:** Trend + Seasonal

**Bottom-Left (debt 1950-1960):**
- Strong upward trend (exponential growth)
- No clear seasonality
- **Components:** Trend (possibly exponential)

**Bottom-Right (drowning cases 1987-1994):**
- Clear seasonal pattern (summer peaks)
- Relatively stable mean (no strong trend)
- **Components:** Seasonal + Irregular

---

### Q1(c) [6 Marks] - ARIMA Identification

**Case 1:**
- ACF: Decays exponentially
- PACF: Cuts off after lag 1
- **Model: AR(1)** or ARIMA(1,0,0)

**Case 2:**
- ACF: Cuts off after lag 2
- PACF: Tails off
- **Model: MA(2)** or ARIMA(0,0,2)

---

### Q1(d) [7 Marks] - SARIMA Components

**From Figure Q1(d):**

Looking at the ACF and PACF with "Indicates?" markers:

- **ACF spike at lag 1:** Indicates MA(1) or AR(1) depending on PACF
- **ACF spike at lag 12:** Indicates Seasonal MA(1) - SMA(1)
- **PACF spike at lag 1:** Indicates AR(1)
- **PACF spike at lag 12:** Indicates SAR(1)

**Model: SARIMA(1,0,0)(1,0,1)₁₂**

**Justification:**
- AR(1): PACF significant at lag 1
- SAR(1): PACF significant at lag 12 (seasonal period)
- SMA(1): ACF significant at lag 12 but decaying at seasonal lags

---

## QUESTION 2: Decomposition [25 Marks]

### Q2(a)-(c) - Online Orders Data

Similar methodology to previous decomposition questions. Apply 2×4 moving average to:

| Year | Q1 | Q2 | Q3 | Q4 |
|------|-----|-----|------|-----|
| 2015 | 32 | 22 | 105 | 32 |
| 2016 | 22 | 25 | 140 | 80 |
| 2017 | 52 | 38 | 144 | 114 |

**Model Selection:** Seasonal amplitude increases with level (Q3 peak grows from 105 to 144) → **MULTIPLICATIVE MODEL**

---

## QUESTION 3: Forecasting [25 Marks]

See corresponding questions from 2022/23 exam for Q3(a)-(c).

---

## QUESTION 4: Emergence and Bifurcation [25 Marks]

### Q4(a) [8 Marks] - Emergence vs Self-Organization

See Q3(a) from 2021/22 exam and Q4(b) from 2020/21 exam.

---

### Q4(b) [8 Marks] - Logistic Map Bifurcation

See Q3(c) from 2021/22 exam and Q6(b) from 2020/21 exam.

Key points for Figure Q4(b):
- r ≈ 3.4: Period-doubling cascade begins
- r ≈ 3.6: Period-4 cycle
- r ≈ 3.57: Onset of chaos
- r ≈ 3.83: Period-3 window
- r > 3.9: Fully chaotic with intermittent windows

---

### Q4(c) [7 Marks] - Complex System Modeling

See Q4(c) from 2020/21 exam.

---

## QUESTION 5: Networks [25 Marks]

### Q5(a) [4 Marks] - Community Structure

A network has community structure when nodes can be grouped such that:
- Nodes within a group are densely connected
- Connections between groups are sparse
- Groups represent meaningful functional units

**Example:** A company email network where departments form natural communities.

---

### Q5(b) [6 Marks] - Weighted Network Modularity

**From Figure Q5(b):**

Reading edge weights from diagram:
- Susan-James: 2
- Susan-Jim: 3
- Jim-James: 2
- Ben-James: 2
- Ben-John: 1 (implied)
- John-Jim: 1
- John-Alice: 4
- John-Peter: 3
- Peter-Mary: 4
- Mary-Alice: (no direct edge shown)

**Adjacency Matrix (weighted):**
```
        Su Ji Ja Be Jo Pe Ma Al
Susan    0  3  2  0  0  0  0  0
Jim      3  0  2  0  1  0  0  1
James    2  2  0  2  0  0  0  0
Ben      0  0  2  0  1  0  0  0
John     0  1  0  1  0  3  0  4
Peter    0  0  0  0  3  0  4  0
Mary     0  0  0  0  0  4  0  0
Alice    0  1  0  0  4  0  0  0
```

**Modularity Q with isolated communities:**
When each node is alone, Q = 0 or negative (no within-community edges).

---

### Q5(c) [10 Marks] - Alice Community Assignment

Alice connects to: Jim (weight 1), John (weight 4)

**Stronger connection to John** (weight 4 vs 1), so Alice should join **(John, Ben, Mary, Peter)**.

---

### Q5(d) [5 Marks] - Learning Behavior and Exam Performance

**Passed:** Ben, John, Mary, Alice, Jim, Peter
**Failed:** Susan, James

**Observation:** Students who passed are clustered together (stronger study group connections), while those who failed (Susan, James) form a separate weaker cluster.

**Conclusion:** Collaborative learning in well-connected groups correlates with better exam performance. The community structure reveals study partnerships that benefit academic outcomes.

---

## QUESTION 6: Population Dynamics [25 Marks]

### Q6(a) [4 Marks] - Rat/Owl Coefficients (Modified)

**Modified parameters:**
- Owl decay: 60% (d = 0.4)
- Conversion efficiency: 50% (c = 0.05)

**Coefficients:** a = 1.1, b = -0.1, c = 0.05, d = 0.4

---

### Q6(b)-(c) [21 Marks]

**Matrix:**
```
A = [1.1   -0.1]
    [0.05   0.4]
```

**Characteristic equation:**
```
(1.1-λ)(0.4-λ) - (-0.1)(0.05) = 0
0.44 - 1.5λ + λ² + 0.005 = 0
λ² - 1.5λ + 0.445 = 0

λ = (1.5 ± √(2.25 - 1.78))/2
λ = (1.5 ± 0.686)/2

λ₁ = 1.093, λ₂ = 0.407
```

**Since λ_max > 1, populations grow.**

**Q6(c): 30% less predation**
b changes from -0.1 to -0.07 (30% reduction)

This reduces predation pressure, likely leading to even faster population growth or potentially population explosion.

---

# EXAM 5: 2024/2025 (CSC1111)

---

## QUESTION 1: Stationarity and ACF/PACF [25 Marks]

### Q1(a) [13 Marks] - Stationarity Analysis

**(i) Trend vs Difference Stationary:** See Q2(a) from 2021/22 exam.

**(ii) For Figure Q1(a):**
- Shows upward trend with fluctuations
- Appears to be trend stationary (deterministic trend)
- Apply detrending: fit line, subtract
- Result: fluctuations around zero

**(iii) ACF Sketches:**
- Original: slow decay (non-stationary signature)
- Detrended: rapid decay to zero (stationary)

---

### Q1(b) [4 Marks] - ACF and PACF Definitions

See Q3(b) from 2020/21 exam.

---

### Q1(c) [8 Marks] - Model Identification

**Case (i):**
- ACF: Single large spike at lag 1, then zero
- PACF: Decays gradually
- **Model: MA(1)**

**Case (ii):**
- ACF: Spikes at lags 1, 12, 24 with decay
- PACF: Spike at lag 1, spike at lag 12
- **Model: SARIMA(1,0,0)(1,0,0)₁₂**

---

## QUESTION 2: Time Series Components [25 Marks]

### Q2(a) [4 Marks] - Four TS Components

1. **Trend (T):** Long-term movement (upward/downward)
2. **Seasonal (S):** Regular periodic fluctuations (yearly, quarterly)
3. **Cyclical (C):** Longer-term waves (business cycles)
4. **Irregular (I):** Random noise/residuals

---

### Q2(b) [6 Marks] - NSW Retail Sales Components

**Visible Components:**
1. **Trend:** Clear upward trend over 1982-2001
2. **Seasonality:** Strong recurring pattern (visible in enlarged section)

**Causes:**
- Trend: Population growth, economic development, inflation
- Seasonality: Holiday shopping (December peaks), seasonal sales

---

### Q2(c) [15 Marks] - Sales Data Decomposition

Same data as 2020/21 Q2(c). Apply identical methodology.

---

## QUESTION 3: Forecasting with EWMA [25 Marks]

### Q3(a) [7 Marks] - Ex Post vs Ex Ante

See Q3(b) from 2022/23 exam.

**Train/Test Split = Ex Post** because you're testing on data where true values are known.

---

### Q3(b) [12 Marks] - EWMA Calculations

**EWMA Formula:** ŷ_{t+1} = αy_t + (1-α)ŷ_t

**For Bison Population:**

| Year | Pop | EWMA(0.2) | EWMA(0.5) | EWMA(0.8) |
|------|------|-----------|-----------|-----------|
| 1920 | 1770 | 1770 | 1770 | 1770 |
| 1930 | 1704 | 1756.8 | 1737 | 1717.2 |
| 1940 | 1658 | 1737.0 | 1697.5 | 1664.8 |
| 1950 | 1852 | 1760.0 | 1774.8 | 1814.6 |
| 1960 | 1698 | 1747.6 | 1736.4 | 1721.3 |
| 1970 | 1954 | 1788.9 | 1845.2 | 1907.5 |
| 1980 | 1782 | 1787.5 | 1813.6 | 1807.1 |
| 1990 | 1660 | 1762.0 | 1736.8 | 1689.4 |
| 2000 | 1602 | 1730.0 | 1669.4 | 1619.5 |
| 2010 | 1650 | 1714.0 | 1659.7 | 1643.9 |
| **2020** | ? | **1701.2** | **1654.9** | **1648.8** |

---

### Q3(c) [6 Marks] - Which α to Use?

For conservation action on declining populations, **α = 0.8** (high smoothing) is recommended because:
1. Reacts quickly to recent declines
2. More responsive to actual current conditions
3. Less smoothing means earlier warning of population crashes
4. Conservative approach: better to act too early than too late

Lower α values might mask urgent trends by over-smoothing.

---

## QUESTION 4: Complex Systems [25 Marks]

### Q4(a)-(b) - Emergence, Self-Organization, Modeling

See Q3(a)-(b) from 2021/22 exam.

---

### Q4(c) [8 Marks] - Bifurcation Diagram Analysis

**Figure Q4(c) shows bifurcation for parameter θ:**

**θ ≈ 3.5:**
- System transitions from single stable point to period-2 oscillation
- First bifurcation point
- Indicates loss of stability of fixed point

**θ ≈ 14:**
- Region transitions between chaos and period-doubling
- May show window of stability within chaotic region
- OR marks onset of fully chaotic behavior

**General Pattern:**
- Low θ: Single stable equilibrium
- Increasing θ: Period-doubling cascade
- High θ: Chaotic dynamics with occasional stability windows

---

## QUESTION 5: ABM and CA [25 Marks]

### Q5(a)-(d) - Agent Properties, Louvain, CA Evolution, Forest Fire

See Q4(a)-(d) from 2021/22 exam for identical content.

---

## QUESTION 6: Markov Processes and MCMC [25 Marks]

### Q6(a) [4 Marks] - Markov Process

See Q5(a) from 2021/22 exam.

---

### Q6(b) [8 Marks] - Video Game Health Markov Chain

**Transition Matrix:**
```
       H     I     C     N
H  [ 0.05  0.75  0.20  0.00 ]
I  [ 0.25  0.30  0.45  0.00 ]
C  [ 0.10  0.40  0.30  0.20 ]
N  [ 0.00  0.15  0.30  0.55 ]
```

**(i) Transition Diagram:** (Same structure as storm categories in 2021/22)

**(ii) P(Injured → Healthy):**
- After 1 step: **0.25**
- After 2 steps: **0.25×0.05 + 0.30×0.25 + 0.45×0.10 = 0.1325**

---

### Q6(c)-(d) - MCMC

See Q5(c)-(d) from 2021/22 exam.

---

# KEY FORMULAS SUMMARY

## Population Dynamics
- **Eigenvalue:** det(A - λI) = 0
- **Stability:** λ_max > 1 (growth), λ_max < 1 (decay), λ_max = 1 (stable)

## Time Series
- **Additive:** Y = T + S + C + I
- **Multiplicative:** Y = T × S × C × I
- **Differencing:** Δy_t = y_t - y_{t-1}
- **EWMA:** ŷ_{t+1} = αy_t + (1-α)ŷ_t
- **Naïve:** ŷ_{t+1} = y_t

## ARIMA Identification
| Model | ACF | PACF |
|-------|-----|------|
| AR(p) | Tails off | Cuts off at p |
| MA(q) | Cuts off at q | Tails off |
| ARMA | Tails off | Tails off |

## Modularity
- Q = (1/2m) Σ[A_ij - k_i k_j/2m]δ(c_i, c_j)

## Logistic Map
- x_{n+1} = rx_n(1 - x_n)
- Chaos onset: r ≈ 3.57

---

*Document compiled from CA4024/CSC1111 Building Complex Computational Models examinations 2020/21 - 2024/25*
