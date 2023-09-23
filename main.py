import random
import pygame


class BarnslyFern:
    """КЛАСС ИНИЦИАЛИЗАЦИИ ТОЧЕК"""
    def __init__(self, width, height, scale, iterations):
        self.width = width
        self.height = height
        self.scale = scale
        self.iterations = iterations
        self.x, self.y = width // 2, height // 2

    def barnsley_fern(self):
        """Определение точек"""
        rand = random.random()

        if rand <= 0.01:
            x1, y1 = 0, 0.16 * self.y
        elif rand <= 0.85:
            x1, y1 = 0.85 * self.x + 0.04 * self.y, -0.04 * self.x + 0.85 * self.y + 1.6
        elif rand <= 0.93:
            x1, y1 = 0.2 * self.x - 0.26 * self.y, 0.23 * self.x + 0.22 * self.y + 1.6
        else:
            x1, y1 = -0.15 * self.x + 0.28 * self.y, 0.26 * self.x + 0.24 * self.y + 0.44
        self.x, self.y = x1, y1

    def generate_fern(self):
        """Генерация точек"""
        fern_points = []

        for _ in range(self.iterations):
            self.barnsley_fern()
            fern_points.append((int(self.width - self.x * self.scale), int(self.height - self.y * self.scale)))
        return fern_points


class FernRender:
    """КЛАСС ОТОБРАЖЕНИЯ"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, height))
        pygame.display.set_caption("Папоротник Барнсли")

    def run(self):
        """Запуск программы"""
        flag = True
        clock = pygame.time.Clock()

        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False

        clock.tick(30)



        pygame.quit()



if __name__ == "__main__":
    pygame.init()
    render = FernRender(800, 600)
    render.run()















