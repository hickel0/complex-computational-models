"""
Virus Spread ABM 

A SIR (Susceptible-Infected-Recovered) epidemic model.

Run: python virus_sim.py
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, TextBox
from matplotlib.animation import FuncAnimation

# =============================================================================
# PARAMETER DEFAULTS
# =============================================================================
population = 200        # Number of agents
initial_infected = 5    # Starting infected
infection_prob = 0.3    # Chance of infection on contact
infection_radius = 0.03 # Distance for transmission
recovery_time = 100     # MINIMUM steps before recovery possible
recovery_prob = 1.0    # Chance of recovery each step (after min time)
mortality_rate = 0.0    # Chance of death (0-1)
reinfection_rate = 0.0  # Chance recovered agent reinfects (R -> I) on contact
social_distancing = 0.0 # Reduces movement (0-1)
movement_speed = 0.01   # How fast agents move

# =============================================================================
# GLOBAL VARIABLES
# =============================================================================
agents = []
history = {'S': [], 'I': [], 'R': [], 'D': []}
time_step = 0
running = False

# =============================================================================
# AGENT CLASS
# =============================================================================
class Agent:
    """Simple agent with position and health state."""
    def __init__(self, x, y, state='S', mortality_rate= mortality_rate):
        self.x = x
        self.y = y
        self.state = state  # S=Susceptible, I=Infected, R=Recovered, D=Dead
        self.timer = 0      # Tracks infection duration
        self.mortality_rate = mortality_rate

        # Random direction
        angle = np.random.uniform(0, 2*np.pi)
        self.vx = np.cos(angle)
        self.vy = np.sin(angle)

# =============================================================================
# SIMULATION FUNCTIONS
# =============================================================================
def initialize():
    """Create initial population."""
    global agents, history, time_step
    agents = []
    history = {'S': [], 'I': [], 'R': [], 'D': []}
    time_step = 0

    for i in range(population):
        x = np.random.random()
        y = np.random.random()
        state = 'I' if i < initial_infected else 'S'
        agents.append(Agent(x, y, state))

    record_counts()

def record_counts():
    """Record current population counts."""
    counts = {'S': 0, 'I': 0, 'R': 0, 'D': 0}
    for ag in agents:
        counts[ag.state] += 1
    for key in counts:
        history[key].append(counts[key])

def move_agent(ag):
    """Move an agent with random walk."""
    if ag.state == 'D':
        return

    # Reduce speed if social distancing
    speed = movement_speed * (1 - social_distancing * 0.8)

    # Add randomness to direction
    ag.vx += np.random.uniform(-0.1, 0.1)
    ag.vy += np.random.uniform(-0.1, 0.1)

    # Normalize
    mag = np.sqrt(ag.vx**2 + ag.vy**2)
    if mag > 0:
        ag.vx /= mag
        ag.vy /= mag

    # Update position
    ag.x += ag.vx * speed
    ag.y += ag.vy * speed

    # Bounce off walls
    if ag.x < 0 or ag.x > 1:
        ag.vx *= -1
        ag.x = max(0, min(1, ag.x))
    if ag.y < 0 or ag.y > 1:
        ag.vy *= -1
        ag.y = max(0, min(1, ag.y))

def update():
    """Run one simulation step."""
    global time_step, infection_prob

    # Move all agents
    for ag in agents:
        move_agent(ag)

    # Check infections (S -> I) and reinfections (R -> I)
    for ag in agents:
        if ag.state != 'I':
            continue
        # Find nearby agents that can be infected
        for other in agents:
            dist = np.sqrt((ag.x - other.x)**2 + (ag.y - other.y)**2)
            if dist < infection_radius:
                # Susceptible agents (never infected) - use infection_prob
                if other.state == 'S':
                    if np.random.random() < infection_prob:
                        other.state = 'I'
                        other.timer = 0
                # Recovered agents - use reinfection_rate (direct R -> I)
                elif other.state == 'R':
                    if np.random.random() < reinfection_rate:
                        other.state = 'I'
                        other.timer = 0

    # Check recovery/death (probabilistic after minimum time)
    for ag in agents:
        if ag.state == 'I':
            ag.timer += 1
            # After minimum recovery time, chance to recover each step
            if ag.timer >= recovery_time:
                if np.random.random() < recovery_prob:
                    # Recovered - now check if they die or survive
                    if np.random.random() < mortality_rate:
                        ag.state = 'D'
                    else:
                        ag.state = 'R'
                        ag.timer = 0  # Reset timer for tracking immunity
            else:
                # increment mortality rate every step past min recovery for which agent has not recvoered
                ag.mortality_rate += 1 

    time_step += 1
    record_counts()

    # Return True if epidemic ongoing
    infected = sum(1 for ag in agents if ag.state == 'I')
    return infected > 0

# =============================================================================
# MAIN PROGRAM
# =============================================================================
if __name__ == "__main__":
    print("Virus Spread ABM Simulation")
    print("---------------------------")
    print("Controls:")
    print("  Start/Stop - Run or pause simulation")
    print("  Reset      - Restart with current parameters")
    print("  Sliders/Text Boxes    - Adjust parameters in real-time")
    print("                         (Population change requires Reset)")
    print()

    # Initialize simulation
    initialize()

    # Colours for each state
    colours = {'S': '#3498db', 'I': '#e74c3c', 'R': '#2ecc71', 'D': '#7f8c8d'}

    # Create figure
    fig = plt.figure(figsize=(12, 5))
    fig.suptitle('Virus Spread Simulation (SIR Model)', fontsize=12, fontweight='bold')

    # Left plot: agents
    ax_sim = fig.add_subplot(121)
    ax_sim.set_xlim(0, 1)
    ax_sim.set_ylim(0, 1)
    ax_sim.set_aspect('equal')
    ax_sim.set_title('Population')
    ax_sim.set_xlabel('X')
    ax_sim.set_ylabel('Y')

    # Right plot: time series
    ax_graph = fig.add_subplot(122)
    ax_graph.set_title('Epidemic Curve')
    ax_graph.set_xlabel('Time')
    ax_graph.set_ylabel('Count')
    ax_graph.set_xlim(0, 500)
    ax_graph.set_ylim(0, population)

    # Create scatter plots for agents
    scatters = {}
    for state in ['S', 'I', 'R', 'D']:
        scatters[state] = ax_sim.scatter([], [], c=colours[state], s=15,
                                          label=state, alpha=0.7)
    ax_sim.legend(loc='upper right', fontsize=8)

    # Create lines for graph
    lines = {}
    lines['S'], = ax_graph.plot([], [], c=colours['S'], label='Susceptible', lw=2)
    lines['I'], = ax_graph.plot([], [], c=colours['I'], label='Infected', lw=2)
    lines['R'], = ax_graph.plot([], [], c=colours['R'], label='Recovered', lw=2)
    lines['D'], = ax_graph.plot([], [], c=colours['D'], label='Dead', lw=2)
    ax_graph.legend(loc='upper right', fontsize=8)
    ax_graph.grid(True, alpha=0.3)

    # Status text
    status_text = ax_sim.text(0.02, 0.98, '', transform=ax_sim.transAxes,
                               va='top', fontsize=9,
                               bbox=dict(boxstyle='round', facecolor='wheat'))

    # Adjust layout to make room for buttons and sliders
    plt.subplots_adjust(bottom=0.38)

    # =========================================================================
    # BUTTONS
    # =========================================================================
    ax_start = plt.axes([0.08, 0.24, 0.10, 0.04])
    ax_reset = plt.axes([0.20, 0.24, 0.10, 0.04])

    btn_start = Button(ax_start, 'Start/Stop')
    btn_reset = Button(ax_reset, 'Reset')

    # =========================================================================
    # SLIDERS AND TEXT BOXES - All adjustable parameters
    # =========================================================================
    # Left column: sliders + text boxes (4 rows)
    ax_s1 = plt.axes([0.1, 0.18, 0.17, 0.022])
    ax_s2 = plt.axes([0.1, 0.12, 0.17, 0.022])
    ax_s3 = plt.axes([0.1, 0.06, 0.17, 0.022])
    ax_s8 = plt.axes([0.1, 0.01, 0.17, 0.022])
    ax_t1 = plt.axes([0.32, 0.18, 0.06, 0.022])
    ax_t2 = plt.axes([0.32, 0.12, 0.06, 0.022])
    ax_t3 = plt.axes([0.32, 0.06, 0.06, 0.022])
    ax_t8 = plt.axes([0.32, 0.01, 0.06, 0.022])

    # Right column: sliders + text boxes (5 rows)
    ax_s4 = plt.axes([0.50, 0.24, 0.30, 0.022])
    ax_s5 = plt.axes([0.50, 0.18, 0.30, 0.022])
    ax_s6 = plt.axes([0.50, 0.12, 0.30, 0.022])
    ax_s7 = plt.axes([0.50, 0.06, 0.30, 0.022])
    ax_s9 = plt.axes([0.50, 0.01, 0.30, 0.022])
    ax_t4 = plt.axes([0.85, 0.24, 0.06, 0.022])
    ax_t5 = plt.axes([0.85, 0.18, 0.06, 0.022])
    ax_t6 = plt.axes([0.85, 0.12, 0.06, 0.022])
    ax_t7 = plt.axes([0.85, 0.06, 0.06, 0.022])
    ax_t9 = plt.axes([0.85, 0.01, 0.06, 0.022])

    # Create sliders
    slider_inf       = Slider(ax_s4, 'Infection Prob',   0.0,  1.0,  valinit=infection_prob)
    slider_radius    = Slider(ax_s5, 'Infection Radius', 0.01, 0.15, valinit=infection_radius)
    slider_social    = Slider(ax_s6, 'Social Distancing',0.0,  1.0,  valinit=social_distancing)
    slider_mort      = Slider(ax_s7, 'Mortality Prob',   0.0,  1.0,  valinit=mortality_rate)
    slider_reinfect  = Slider(ax_s9, 'Reinfection Prob', 0.0,  1.0,  valinit=reinfection_rate)
    slider_recovery  = Slider(ax_s1, 'Min Recovery Time',20,   300,  valinit=recovery_time, valstep=10)
    slider_recprob   = Slider(ax_s2, 'Recovery Prob',    0.01, 1.0,  valinit=recovery_prob)
    slider_speed     = Slider(ax_s3, 'Movement Speed',   0.001,0.03, valinit=movement_speed)
    slider_pop       = Slider(ax_s8, 'Population',       50,   500,  valinit=population, valstep=10)

    # Create text boxes (for typing exact values)
    text_inf      = TextBox(ax_t4, '', initial=str(infection_prob))
    text_radius   = TextBox(ax_t5, '', initial=str(infection_radius))
    text_social   = TextBox(ax_t6, '', initial=str(social_distancing))
    text_mort     = TextBox(ax_t7, '', initial=str(mortality_rate))
    text_reinfect = TextBox(ax_t9, '', initial=str(reinfection_rate))
    text_recovery = TextBox(ax_t1, '', initial=str(recovery_time))
    text_recprob  = TextBox(ax_t2, '', initial=str(recovery_prob))
    text_speed    = TextBox(ax_t3, '', initial=str(movement_speed))
    text_pop      = TextBox(ax_t8, '', initial=str(population))

    # =========================================================================
    # BUTTON CALLBACKS
    # =========================================================================
    def on_start_click(event):
        """Toggle simulation running state."""
        global running
        running = not running
        print(f"Running: {running}")

    def on_reset_click(event):
        """Reset the simulation."""
        global running
        running = False
        initialize()
        update_display()
        print("Reset complete")

    # --- Slider callbacks (update parameter + sync text box) ---
    def on_slider_inf_change(val):
        global infection_prob
        infection_prob = val
        text_inf.set_val(f"{val:.2f}")

    def on_slider_radius_change(val):
        global infection_radius
        infection_radius = val
        text_radius.set_val(f"{val:.3f}")

    def on_slider_social_change(val):
        global social_distancing
        social_distancing = val
        text_social.set_val(f"{val:.2f}")

    def on_slider_mort_change(val):
        global mortality_rate
        mortality_rate = val
        text_mort.set_val(f"{val:.2f}")

    def on_slider_recovery_change(val):
        global recovery_time
        recovery_time = int(val)
        text_recovery.set_val(str(int(val)))

    def on_slider_speed_change(val):
        global movement_speed
        movement_speed = val
        text_speed.set_val(f"{val:.3f}")

    def on_slider_pop_change(val):
        global population
        population = int(val)
        text_pop.set_val(str(int(val)))
        ax_graph.set_ylim(0, population)
        fig.canvas.draw_idle()

    def on_slider_recprob_change(val):
        global recovery_prob
        recovery_prob = val
        text_recprob.set_val(f"{val:.2f}")

    def on_slider_reinfect_change(val):
        global reinfection_rate
        reinfection_rate = val
        text_reinfect.set_val(f"{val:.3f}")

    # --- Text box callbacks (update parameter + sync slider) ---
    def on_text_inf(text):
        global infection_prob
        try:
            val = float(text)
            val = max(0.0, min(1.0, val))  # Clamp to valid range
            infection_prob = val
            slider_inf.set_val(val)
        except ValueError:
            pass

    def on_text_radius(text):
        global infection_radius
        try:
            val = float(text)
            val = max(0.01, min(0.15, val))
            infection_radius = val
            slider_radius.set_val(val)
        except ValueError:
            pass

    def on_text_social(text):
        global social_distancing
        try:
            val = float(text)
            val = max(0.0, min(1.0, val))
            social_distancing = val
            slider_social.set_val(val)
        except ValueError:
            pass

    def on_text_mort(text):
        global mortality_rate
        try:
            val = float(text)
            val = max(0.0, min(1.0, val))
            mortality_rate = val
            slider_mort.set_val(val)
        except ValueError:
            pass

    def on_text_recovery(text):
        global recovery_time
        try:
            val = int(float(text))
            val = max(20, min(300, val))
            recovery_time = val
            slider_recovery.set_val(val)
        except ValueError:
            pass

    def on_text_speed(text):
        global movement_speed
        try:
            val = float(text)
            val = max(0.001, min(0.03, val))
            movement_speed = val
            slider_speed.set_val(val)
        except ValueError:
            pass

    def on_text_pop(text):
        global population
        try:
            val = int(float(text))
            val = max(50, min(500, val))
            population = val
            slider_pop.set_val(val)
            ax_graph.set_ylim(0, population)
            fig.canvas.draw_idle()
        except ValueError:
            pass

    def on_text_recprob(text):
        global recovery_prob
        try:
            val = float(text)
            val = max(0.01, min(1.0, val))
            recovery_prob = val
            slider_recprob.set_val(val)
        except ValueError:
            pass

    def on_text_reinfect(text):
        global reinfection_rate
        try:
            val = float(text)
            val = max(0.0, min(1.0, val))
            reinfection_rate = val
            slider_reinfect.set_val(val)
        except ValueError:
            pass

    # Connect slider callbacks
    btn_start.on_clicked(on_start_click)
    btn_reset.on_clicked(on_reset_click)
    slider_inf.on_changed(on_slider_inf_change)
    slider_radius.on_changed(on_slider_radius_change)
    slider_social.on_changed(on_slider_social_change)
    slider_mort.on_changed(on_slider_mort_change)
    slider_recovery.on_changed(on_slider_recovery_change)
    slider_recprob.on_changed(on_slider_recprob_change)
    slider_reinfect.on_changed(on_slider_reinfect_change)
    slider_speed.on_changed(on_slider_speed_change)
    slider_pop.on_changed(on_slider_pop_change)

    # Connect text box callbacks
    text_inf.on_submit(on_text_inf)
    text_radius.on_submit(on_text_radius)
    text_social.on_submit(on_text_social)
    text_mort.on_submit(on_text_mort)
    text_recovery.on_submit(on_text_recovery)
    text_recprob.on_submit(on_text_recprob)
    text_reinfect.on_submit(on_text_reinfect)
    text_speed.on_submit(on_text_speed)
    text_pop.on_submit(on_text_pop)

    # =========================================================================
    # DISPLAY UPDATE
    # =========================================================================
    def update_display():
        """Update the visualization."""
        # Update agent positions
        for state in ['S', 'I', 'R', 'D']:
            xs = [ag.x for ag in agents if ag.state == state]
            ys = [ag.y for ag in agents if ag.state == state]
            if xs:
                scatters[state].set_offsets(np.c_[xs, ys])
            else:
                scatters[state].set_offsets(np.empty((0, 2)))

        # Update graph lines
        t = list(range(len(history['S'])))
        for state in ['S', 'I', 'R', 'D']:
            lines[state].set_data(t, history[state])

        # Update graph limits
        if len(t) > 10:
            ax_graph.set_xlim(0, max(len(t) + 50, 100))

        # Update status
        counts = {s: sum(1 for ag in agents if ag.state == s) for s in 'SIRD'}
        status_text.set_text(f"Time: {time_step}\nS:{counts['S']} I:{counts['I']} R:{counts['R']} D:{counts['D']}")

    # =========================================================================
    # ANIMATION
    # =========================================================================
    def animate(frame):
        """Animation function called each frame."""
        if running:
            update()
            update_display()
        return []

    # Initial display
    update_display()

    # Create animation 
    ani = FuncAnimation(fig, animate, interval=50, blit=False, cache_frame_data=False)

    # Show the plot
    plt.show()
