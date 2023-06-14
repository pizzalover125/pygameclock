import pygame
import datetime

WIDTH, HEIGHT = 800, 200

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Digital Clock")
clock = pygame.time.Clock()

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def draw_text(number, size, color, position):
    font = pygame.font.Font('font.ttf', size)
    text = font.render(number, True, color)
    text_rect = text.get_rect(center=position)
    screen.blit(text, text_rect)

def main():
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        current_time = datetime.datetime.now()
        today = datetime.date.today()

        second = current_time.strftime('%S')
        minute = current_time.strftime('%M')
        hour = current_time.strftime('%I')
        am_pm = current_time.strftime('%p')
        weekday = current_time.strftime('%a')
        date = today.strftime("%B %d, %Y")

        if am_pm == "PM":
            theme = WHITE
            bg = BLACK
        else:
            theme = BLACK
            bg = WHITE

        screen.fill(bg)

        if int(second) % 2 == 0:
            draw_text(f"{hour}:{minute}", 200, theme, (WIDTH / 2 - 100, HEIGHT / 2))
        else:
            draw_text(f"{hour} {minute}", 200, theme, (WIDTH / 2 - 100, HEIGHT / 2))

        draw_text(second, 60, RED, (WIDTH / 2 + 175, HEIGHT / 2))
        draw_text(am_pm, 60, theme, (WIDTH / 2 + 260, HEIGHT / 2 - 45))
        draw_text(weekday, 60, theme, (WIDTH / 2 + 260, HEIGHT / 2 + 44))
        draw_text(date, 30, RED, (WIDTH / 2 + 175, HEIGHT / 2 + 85))
        draw_text("pizzalover125", 10, RED, (40, HEIGHT / 2 + 90))

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()


main()