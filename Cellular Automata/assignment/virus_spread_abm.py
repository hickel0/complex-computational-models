"""
Virus Spread Agent-Based Model (ABM)
=====================================

This simulation models virus transmission among a population using an SIR
(Susceptible-Infected-Recovered) framework with spatial dynamics.

Features:
- 2D spatial simulation with random agent movement
- Configurable parameters via GUI
- Real-time visualization of agent states
- Time-series graphs of population dynamics
- Multiple simulation scenarios support

"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.patches import Patch
import matplotlib.animation as animation
from dataclasses import dataclass
from typing import List, Tuple
import argparse
import sys

# =============================================================================
# CONFIGURATION AND PARAMETERS
# =============================================================================

@dataclass
class SimulationConfig:
    """Configuration parameters for the virus spread simulation."""

    # Population parameters
    population_size: int = 200          # Total number of agents
    initial_infected: int = 5           # Number of initially infected agents

    # Spatial parameters
    world_size: float = 1.0             # Size of the 2D world (unit square)
    infection_radius: float = 0.03      # Distance for infection transmission

    # Movement parameters
    movement_speed: float = 0.01        # Base movement speed of agents
    social_distancing: float = 0.0      # Social distancing factor (0-1)

    # Disease parameters
    infection_probability: float = 0.3  # Probability of infection on contact
    recovery_time: int = 100            # Time steps until recovery
    mortality_rate: float = 0.0         # Probability of death (0-1)
    immunity_duration: int = 0          # Duration of immunity (0 = permanent)

    # Simulation parameters
    max_steps: int = 1000               # Maximum simulation steps


# =============================================================================
# AGENT CLASS
# =============================================================================

class Agent:
    """
    Represents an individual in the population.

    Each agent has:
    - Position (x, y) in 2D space
    - State: 'S' (Susceptible), 'I' (Infected), 'R' (Recovered), 'D' (Dead)
    - Infection timer tracking time since infection
    - Immunity timer tracking remaining immunity duration
    """

    # Class-level counter for unique IDs
    _id_counter = 0

    def __init__(self, x: float, y: float, state: str = 'S'):
        """
        Initialize an agent.

        Args:
            x: Initial x-coordinate (0 to world_size)
            y: Initial y-coordinate (0 to world_size)
            state: Initial state ('S', 'I', 'R', or 'D')
        """
        self.id = Agent._id_counter
        Agent._id_counter += 1

        self.x = x
        self.y = y
        self.state = state
        self.infection_timer = 0      # Time steps since infection
        self.immunity_timer = 0       # Remaining immunity duration

        # Random movement direction
        angle = np.random.uniform(0, 2 * np.pi)
        self.vx = np.cos(angle)
        self.vy = np.sin(angle)

    def move(self, speed: float, world_size: float, social_distancing: float = 0.0):
        """
        Move the agent randomly in 2D space.

        Args:
            speed: Movement speed
            world_size: Boundary of the world
            social_distancing: Factor reducing movement (0-1)
        """
        if self.state == 'D':  # Dead agents don't move
            return

        # Apply social distancing (reduces movement)
        effective_speed = speed * (1 - social_distancing * 0.8)

        # Add some randomness to direction
        angle_change = np.random.uniform(-0.5, 0.5)
        cos_a, sin_a = np.cos(angle_change), np.sin(angle_change)
        new_vx = self.vx * cos_a - self.vy * sin_a
        new_vy = self.vx * sin_a + self.vy * cos_a
        self.vx, self.vy = new_vx, new_vy

        # Normalize velocity
        magnitude = np.sqrt(self.vx**2 + self.vy**2)
        if magnitude > 0:
            self.vx /= magnitude
            self.vy /= magnitude

        # Update position
        self.x += self.vx * effective_speed
        self.y += self.vy * effective_speed

        # Boundary reflection (bounce off walls)
        if self.x < 0:
            self.x = 0
            self.vx = -self.vx
        elif self.x > world_size:
            self.x = world_size
            self.vx = -self.vx

        if self.y < 0:
            self.y = 0
            self.vy = -self.vy
        elif self.y > world_size:
            self.y = world_size
            self.vy = -self.vy

    def infect(self):
        """Change agent state to infected."""
        if self.state == 'S':
            self.state = 'I'
            self.infection_timer = 0

    def recover(self, immunity_duration: int):
        """
        Change agent state to recovered.

        Args:
            immunity_duration: Duration of immunity (0 = permanent)
        """
        self.state = 'R'
        self.immunity_timer = immunity_duration

    def die(self):
        """Change agent state to dead."""
        self.state = 'D'

    def lose_immunity(self):
        """Change agent state back to susceptible (when immunity wears off)."""
        self.state = 'S'
        self.immunity_timer = 0


# =============================================================================
# SIMULATION CLASS
# =============================================================================

class VirusSpreadSimulation:
    """
    Main simulation class for the virus spread ABM.

    Manages:
    - Agent population
    - Infection dynamics
    - Time progression
    - Data collection for analysis
    """

    def __init__(self, config: SimulationConfig):
        """
        Initialize the simulation.

        Args:
            config: SimulationConfig object with all parameters
        """
        self.config = config
        self.agents: List[Agent] = []
        self.time_step = 0

        # Data tracking for graphs
        self.history = {
            'susceptible': [],
            'infected': [],
            'recovered': [],
            'dead': []
        }

        # Reset agent ID counter
        Agent._id_counter = 0

        self._initialize_population()

    def _initialize_population(self):
        """Create the initial population of agents."""
        self.agents = []

        for i in range(self.config.population_size):
            # Random position within world bounds
            x = np.random.uniform(0, self.config.world_size)
            y = np.random.uniform(0, self.config.world_size)

            # First few agents are infected
            state = 'I' if i < self.config.initial_infected else 'S'

            agent = Agent(x, y, state)
            self.agents.append(agent)

        # Record initial state
        self._record_state()

    def reset(self):
        """Reset the simulation to initial state."""
        self.time_step = 0
        self.history = {
            'susceptible': [],
            'infected': [],
            'recovered': [],
            'dead': []
        }
        Agent._id_counter = 0
        self._initialize_population()

    def _get_neighbors(self, agent: Agent, radius: float) -> List[Agent]:
        """
        Find all agents within a given radius of the focal agent.

        Args:
            agent: The focal agent
            radius: Search radius

        Returns:
            List of neighboring agents (excluding the focal agent)
        """
        neighbors = []
        radius_sq = radius ** 2

        for other in self.agents:
            if other.id == agent.id:
                continue
            if other.state == 'D':
                continue

            dist_sq = (agent.x - other.x)**2 + (agent.y - other.y)**2
            if dist_sq < radius_sq:
                neighbors.append(other)

        return neighbors

    def _process_infections(self):
        """Process potential infections between agents."""
        for agent in self.agents:
            if agent.state != 'I':
                continue

            # Find susceptible neighbors
            neighbors = self._get_neighbors(agent, self.config.infection_radius)

            for neighbor in neighbors:
                if neighbor.state == 'S':
                    # Attempt infection
                    if np.random.random() < self.config.infection_probability:
                        neighbor.infect()

    def _process_recovery_and_death(self):
        """Process recovery and mortality for infected agents."""
        for agent in self.agents:
            if agent.state == 'I':
                agent.infection_timer += 1

                # Check for recovery
                if agent.infection_timer >= self.config.recovery_time:
                    # Check for death first
                    if np.random.random() < self.config.mortality_rate:
                        agent.die()
                    else:
                        agent.recover(self.config.immunity_duration)

            # Process immunity loss
            elif agent.state == 'R' and self.config.immunity_duration > 0:
                agent.immunity_timer -= 1
                if agent.immunity_timer <= 0:
                    agent.lose_immunity()

    def _record_state(self):
        """Record current population state for graphing."""
        counts = {'S': 0, 'I': 0, 'R': 0, 'D': 0}
        for agent in self.agents:
            counts[agent.state] += 1

        self.history['susceptible'].append(counts['S'])
        self.history['infected'].append(counts['I'])
        self.history['recovered'].append(counts['R'])
        self.history['dead'].append(counts['D'])

    def step(self):
        """Execute one simulation time step."""
        if self.time_step >= self.config.max_steps:
            return False

        # Move all agents
        for agent in self.agents:
            agent.move(
                self.config.movement_speed,
                self.config.world_size,
                self.config.social_distancing
            )

        # Process infections
        self._process_infections()

        # Process recovery and death
        self._process_recovery_and_death()

        # Record state
        self._record_state()

        self.time_step += 1

        # Check if epidemic is over (no more infected)
        infected_count = sum(1 for a in self.agents if a.state == 'I')
        return infected_count > 0 or self.time_step < 50  # Run at least 50 steps

    def get_state_counts(self) -> dict:
        """Get current counts of each state."""
        counts = {'S': 0, 'I': 0, 'R': 0, 'D': 0}
        for agent in self.agents:
            counts[agent.state] += 1
        return counts

    def get_agent_positions(self) -> dict:
        """Get positions of agents grouped by state."""
        positions = {
            'S': {'x': [], 'y': []},
            'I': {'x': [], 'y': []},
            'R': {'x': [], 'y': []},
            'D': {'x': [], 'y': []}
        }

        for agent in self.agents:
            positions[agent.state]['x'].append(agent.x)
            positions[agent.state]['y'].append(agent.y)

        return positions


# =============================================================================
# VISUALIZATION CLASS
# =============================================================================

class SimulationVisualizer:
    """
    Handles visualization of the simulation.

    Features:
    - Real-time 2D agent display
    - Time-series population graphs
    - Interactive parameter controls
    """

    # Color scheme for agent states
    COLORS = {
        'S': '#3498db',  # Blue - Susceptible
        'I': '#e74c3c',  # Red - Infected
        'R': '#2ecc71',  # Green - Recovered
        'D': '#7f8c8d'   # Gray - Dead
    }

    def __init__(self, simulation: VirusSpreadSimulation):
        """
        Initialize the visualizer.

        Args:
            simulation: VirusSpreadSimulation instance to visualize
        """
        self.sim = simulation
        self.running = False
        self.animation = None

        self._setup_figure()

    def _setup_figure(self):
        """Set up the matplotlib figure and subplots."""
        self.fig = plt.figure(figsize=(14, 8))
        self.fig.suptitle('Virus Spread Agent-Based Model', fontsize=14, fontweight='bold')

        # Create grid for subplots
        gs = self.fig.add_gridspec(3, 4, hspace=0.4, wspace=0.3)

        # Main agent display (left side)
        self.ax_agents = self.fig.add_subplot(gs[:2, :2])
        self.ax_agents.set_xlim(0, self.sim.config.world_size)
        self.ax_agents.set_ylim(0, self.sim.config.world_size)
        self.ax_agents.set_aspect('equal')
        self.ax_agents.set_title('Population View')
        self.ax_agents.set_xlabel('X Position')
        self.ax_agents.set_ylabel('Y Position')

        # Time series graph (right side)
        self.ax_graph = self.fig.add_subplot(gs[:2, 2:])
        self.ax_graph.set_title('Population Dynamics Over Time')
        self.ax_graph.set_xlabel('Time Step')
        self.ax_graph.set_ylabel('Number of Agents')
        self.ax_graph.set_xlim(0, self.sim.config.max_steps)
        self.ax_graph.set_ylim(0, self.sim.config.population_size)

        # Initialize scatter plots for agents
        self.scatters = {}
        for state in ['S', 'I', 'R', 'D']:
            self.scatters[state] = self.ax_agents.scatter(
                [], [], c=self.COLORS[state], s=20, alpha=0.7,
                label=self._get_state_label(state)
            )
        self.ax_agents.legend(loc='upper right', fontsize=8)

        # Initialize line plots for time series
        self.lines = {}
        self.lines['susceptible'], = self.ax_graph.plot(
            [], [], c=self.COLORS['S'], linewidth=2, label='Susceptible'
        )
        self.lines['infected'], = self.ax_graph.plot(
            [], [], c=self.COLORS['I'], linewidth=2, label='Infected'
        )
        self.lines['recovered'], = self.ax_graph.plot(
            [], [], c=self.COLORS['R'], linewidth=2, label='Recovered'
        )
        self.lines['dead'], = self.ax_graph.plot(
            [], [], c=self.COLORS['D'], linewidth=2, label='Dead'
        )
        self.ax_graph.legend(loc='upper right', fontsize=8)

        # Status text
        self.status_text = self.ax_agents.text(
            0.02, 0.98, '', transform=self.ax_agents.transAxes,
            verticalalignment='top', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        )

        # Control buttons
        self._setup_controls()

    def _get_state_label(self, state: str) -> str:
        """Get human-readable label for agent state."""
        labels = {
            'S': 'Susceptible',
            'I': 'Infected',
            'R': 'Recovered',
            'D': 'Dead'
        }
        return labels.get(state, state)

    def _setup_controls(self):
        """Set up interactive controls."""
        # Button axes
        ax_start = plt.axes([0.1, 0.05, 0.1, 0.04])
        ax_stop = plt.axes([0.22, 0.05, 0.1, 0.04])
        ax_reset = plt.axes([0.34, 0.05, 0.1, 0.04])

        self.btn_start = Button(ax_start, 'Start')
        self.btn_stop = Button(ax_stop, 'Stop')
        self.btn_reset = Button(ax_reset, 'Reset')

        self.btn_start.on_clicked(self._on_start)
        self.btn_stop.on_clicked(self._on_stop)
        self.btn_reset.on_clicked(self._on_reset)

        # Sliders for key parameters
        ax_inf_prob = plt.axes([0.55, 0.08, 0.35, 0.02])
        ax_inf_rad = plt.axes([0.55, 0.05, 0.35, 0.02])
        ax_social = plt.axes([0.55, 0.02, 0.35, 0.02])

        self.slider_inf_prob = Slider(
            ax_inf_prob, 'Infection Prob', 0.0, 1.0,
            valinit=self.sim.config.infection_probability
        )
        self.slider_inf_rad = Slider(
            ax_inf_rad, 'Infection Radius', 0.01, 0.1,
            valinit=self.sim.config.infection_radius
        )
        self.slider_social = Slider(
            ax_social, 'Social Distancing', 0.0, 1.0,
            valinit=self.sim.config.social_distancing
        )

        self.slider_inf_prob.on_changed(self._update_params)
        self.slider_inf_rad.on_changed(self._update_params)
        self.slider_social.on_changed(self._update_params)

    def _update_params(self, val):
        """Update simulation parameters from sliders."""
        self.sim.config.infection_probability = self.slider_inf_prob.val
        self.sim.config.infection_radius = self.slider_inf_rad.val
        self.sim.config.social_distancing = self.slider_social.val

    def _on_start(self, event):
        """Start the simulation."""
        if not self.running:
            self.running = True
            self.animation = animation.FuncAnimation(
                self.fig, self._update_frame,
                interval=50, blit=False, cache_frame_data=False
            )
            plt.draw()

    def _on_stop(self, event):
        """Stop the simulation."""
        self.running = False
        if self.animation:
            self.animation.event_source.stop()

    def _on_reset(self, event):
        """Reset the simulation."""
        self.running = False
        if self.animation:
            self.animation.event_source.stop()
        self.sim.reset()
        self._update_display()
        plt.draw()

    def _update_frame(self, frame):
        """Update function for animation."""
        if self.running:
            continue_sim = self.sim.step()
            self._update_display()
            if not continue_sim:
                self.running = False
                if self.animation:
                    self.animation.event_source.stop()
        return []

    def _update_display(self):
        """Update all visual elements."""
        # Update agent positions
        positions = self.sim.get_agent_positions()
        for state in ['S', 'I', 'R', 'D']:
            if positions[state]['x']:
                self.scatters[state].set_offsets(
                    np.c_[positions[state]['x'], positions[state]['y']]
                )
            else:
                self.scatters[state].set_offsets(np.empty((0, 2)))

        # Update time series
        time_points = list(range(len(self.sim.history['susceptible'])))
        for key in ['susceptible', 'infected', 'recovered', 'dead']:
            self.lines[key].set_data(time_points, self.sim.history[key])

        # Update graph limits if needed
        if time_points:
            self.ax_graph.set_xlim(0, max(len(time_points), 100))

        # Update status text
        counts = self.sim.get_state_counts()
        status = (
            f"Time: {self.sim.time_step}\n"
            f"S: {counts['S']} | I: {counts['I']} | R: {counts['R']} | D: {counts['D']}"
        )
        self.status_text.set_text(status)

    def show(self):
        """Display the visualization."""
        self._update_display()
        plt.show()


# =============================================================================
# COMMAND-LINE INTERFACE
# =============================================================================

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description='Virus Spread Agent-Based Model Simulation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python virus_spread_abm.py
  python virus_spread_abm.py --population 300 --infected 10
  python virus_spread_abm.py --infection-prob 0.5 --social-distancing 0.5
  python virus_spread_abm.py --mortality 0.02 --recovery-time 150
        """
    )

    parser.add_argument(
        '--population', '-p', type=int, default=200,
        help='Total population size (default: 200)'
    )
    parser.add_argument(
        '--infected', '-i', type=int, default=5,
        help='Initial number of infected agents (default: 5)'
    )
    parser.add_argument(
        '--infection-prob', type=float, default=0.3,
        help='Probability of infection on contact (default: 0.3)'
    )
    parser.add_argument(
        '--infection-radius', type=float, default=0.03,
        help='Radius for infection transmission (default: 0.03)'
    )
    parser.add_argument(
        '--recovery-time', type=int, default=100,
        help='Time steps until recovery (default: 100)'
    )
    parser.add_argument(
        '--mortality', type=float, default=0.0,
        help='Mortality rate (0-1, default: 0.0)'
    )
    parser.add_argument(
        '--social-distancing', type=float, default=0.0,
        help='Social distancing factor (0-1, default: 0.0)'
    )
    parser.add_argument(
        '--immunity-duration', type=int, default=0,
        help='Duration of immunity (0=permanent, default: 0)'
    )
    parser.add_argument(
        '--max-steps', type=int, default=1000,
        help='Maximum simulation steps (default: 1000)'
    )
    parser.add_argument(
        '--no-gui', action='store_true',
        help='Run without GUI (batch mode for data collection)'
    )

    return parser.parse_args()


def run_batch_simulation(config: SimulationConfig) -> dict:
    """
    Run simulation without GUI for data collection.

    Args:
        config: SimulationConfig with parameters

    Returns:
        Dictionary with simulation results
    """
    sim = VirusSpreadSimulation(config)

    while sim.step():
        pass

    # Calculate summary statistics
    peak_infected = max(sim.history['infected'])
    peak_time = sim.history['infected'].index(peak_infected)
    total_infected = config.population_size - min(sim.history['susceptible'])
    final_deaths = sim.history['dead'][-1] if sim.history['dead'] else 0

    return {
        'peak_infected': peak_infected,
        'peak_time': peak_time,
        'total_infected': total_infected,
        'final_deaths': final_deaths,
        'epidemic_duration': sim.time_step,
        'history': sim.history
    }


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

def main():
    """Main entry point for the simulation."""
    args = parse_arguments()

    # Create configuration from arguments
    config = SimulationConfig(
        population_size=args.population,
        initial_infected=args.infected,
        infection_probability=args.infection_prob,
        infection_radius=args.infection_radius,
        recovery_time=args.recovery_time,
        mortality_rate=args.mortality,
        social_distancing=args.social_distancing,
        immunity_duration=args.immunity_duration,
        max_steps=args.max_steps
    )

    if args.no_gui:
        # Batch mode
        print("Running simulation in batch mode...")
        print(f"Population: {config.population_size}")
        print(f"Initial infected: {config.initial_infected}")
        print(f"Infection probability: {config.infection_probability}")
        print(f"Infection radius: {config.infection_radius}")
        print("-" * 40)

        results = run_batch_simulation(config)

        print(f"Peak infected: {results['peak_infected']} (at time {results['peak_time']})")
        print(f"Total infected: {results['total_infected']}")
        print(f"Final deaths: {results['final_deaths']}")
        print(f"Epidemic duration: {results['epidemic_duration']} steps")

        # Save results plot
        plt.figure(figsize=(10, 6))
        time_points = range(len(results['history']['susceptible']))
        plt.plot(time_points, results['history']['susceptible'], 'b-', label='Susceptible')
        plt.plot(time_points, results['history']['infected'], 'r-', label='Infected')
        plt.plot(time_points, results['history']['recovered'], 'g-', label='Recovered')
        plt.plot(time_points, results['history']['dead'], 'gray', label='Dead')
        plt.xlabel('Time Step')
        plt.ylabel('Number of Agents')
        plt.title('Virus Spread Simulation Results')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig('simulation_results.png', dpi=150, bbox_inches='tight')
        print("\nResults saved to simulation_results.png")

    else:
        # GUI mode
        print("Starting Virus Spread ABM Simulation...")
        print("Controls:")
        print("  - Start: Begin simulation")
        print("  - Stop: Pause simulation")
        print("  - Reset: Reset to initial state")
        print("  - Sliders: Adjust parameters in real-time")
        print("-" * 40)

        sim = VirusSpreadSimulation(config)
        viz = SimulationVisualizer(sim)
        viz.show()


if __name__ == "__main__":
    main()
