import pygame
import sys
import time

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

CELL_SIZE = 30

class GridVisualizer:
    def __init__(self, grid, sim_controller):
        pygame.init()

        self.grid = grid
        self.sim = sim_controller

        self.width = grid.width * CELL_SIZE
        self.height = grid.height * CELL_SIZE

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Real-Time Autonomous Navigation System")

        self.clock = pygame.time.Clock()

    def draw_grid(self):
        for x in range(self.grid.width):
            for y in range(self.grid.height):
                cell = self.grid.get_cell(x, y)

                rect = pygame.Rect(
                    x * CELL_SIZE,
                    y * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                )

                # Default color
                color = WHITE

                if cell.is_obstacle:
                    color = BLACK
                elif (x, y) == self.grid.start_pos:
                    color = GREEN
                elif (x, y) == self.grid.goal_pos:
                    color = RED
                elif cell.is_dynamic_obstacle:
                    color = PURPLE

                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, GRAY, rect, 1)

    def draw_agent(self):
        x, y = self.sim.agent.position
        rect = pygame.Rect(
            x * CELL_SIZE,
            y * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE
        )
        pygame.draw.rect(self.screen, BLUE, rect)

    def draw_path(self):
        for pos in self.sim.path:
            x, y = pos
            rect = pygame.Rect(
                x * CELL_SIZE,
                y * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )
            pygame.draw.rect(self.screen, YELLOW, rect.inflate(-10, -10))

    def run(self, delay=500):
        running = True

        # Plan initial path
        self.sim.plan_initial_path()

        while running:
            self.screen.fill(WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Draw everything
            self.draw_grid()
            self.draw_path()
            self.draw_agent()

            font = pygame.font.SysFont(None, 24)
            text = font.render(
                f"Cost: {self.sim.agent.current_cost} Time: {self.sim.agent.current_time}",
                True,
                (0, 0, 0)
                )
            self.screen.blit(text, (10, 10))    
            pygame.display.flip()
            # Run simulation step
            continue_sim = self.sim.run_step()

            pygame.time.delay(500)  # 500 ms = slower simulation

            if not continue_sim:
                print("Simulation ended.")
                time.sleep(2)
                running = False

            self.clock.tick(2)  # speed control