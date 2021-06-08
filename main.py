import pygame

pygame.font.init()

# JANELA
WIDTH, HEIGHT = 800,600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WINDOW_NAME = pygame.display.set_caption('Pong Game')

# CORES
BLACK = (0,0,0)
WHITE = (255,255,255)

# PONTUAÇÃO
MAX_SCORE = 5
SCORE_1 = 0
SCORE_2 = 0

# FONTES DE TEXTO
FONTS = pygame.font.SysFont('comicsans', 40)

# LIMITE DE FPS
FPS = 60

# MEDIDAS DOS JOGADORES
PLAYER_WIDTH = 15
PLAYER_HEIGHT = 90

# POSIÇÃO DE JOGADORES
PLAYER_X = 30
PLAYER_Y = 250

PLAYER_2_X = 750
PLAYER_2_Y = 250

# POSIÇÃO DA BOLA
BALL_X = 400
BALL_Y = 300
BALL_VEL_X = 3
BALL_VEL_Y = 3

# VELOCIDADE
VEL = 10

# RELOGIO
clock = pygame.time.Clock()

# MAIN LOOP
run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.QUIT()

        # MOVIMENTOS DOS JOGADORES
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w] and PLAYER_Y > 0:
            PLAYER_Y -= VEL
        if key_pressed[pygame.K_s] and PLAYER_Y < HEIGHT - 80:
            PLAYER_Y += VEL

        if key_pressed[pygame.K_i] and PLAYER_2_Y > 0:
            PLAYER_2_Y -= VEL
        if key_pressed[pygame.K_k] and PLAYER_2_Y < HEIGHT - 80:
            PLAYER_2_Y += VEL

    # MOVIMENTOS DA BOLA
    if BALL_Y >= HEIGHT or BALL_Y <= 10:
        BALL_VEL_Y *= -1
    if BALL_X >= WIDTH:
        BALL_VEL_X *= -1
        SCORE_1 += 1
    if BALL_X <= 10:
        BALL_VEL_X *= -1
        SCORE_2 += 1

    BALL_X += BALL_VEL_X
    BALL_Y += BALL_VEL_Y

    WINDOW.fill(BLACK)
    PLAYER = pygame.draw.rect(WINDOW, WHITE, (PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT))
    PLAYER_2 = pygame.draw.rect(WINDOW, WHITE, (PLAYER_2_X, PLAYER_2_Y, PLAYER_WIDTH, PLAYER_HEIGHT))
    BALL = pygame.draw.circle(WINDOW, WHITE, (BALL_X, BALL_Y), 10)

    # TEXTOS DE PONTUAÇÃO
    SCORE_1_TEXT = FONTS.render(f'PUNTOS: {SCORE_1}', 1, WHITE)
    SCORE_2_TEXT = FONTS.render(f'PUNTOS: {SCORE_2}', 1, WHITE)

    # TEXTO DO GANHADOR
    WINNER_TEXT = ""
    if SCORE_1 == MAX_SCORE:
        WINNER_TEXT = "JUGADOR 1 GANA!"
    if SCORE_2 == MAX_SCORE:
        WINNER_TEXT = "JUGADOR 2 GANA!"

    if WINNER_TEXT != "":
        draw_text = FONTS.render(WINNER_TEXT, 1, WHITE)
        WINDOW.blit(draw_text, (WIDTH/3, HEIGHT/2))
        pygame.display.update()
        pygame.time.delay(3000)
        break


    WINDOW.blit(SCORE_1_TEXT, (10,10))
    WINDOW.blit(SCORE_2_TEXT, ((WIDTH - SCORE_2_TEXT.get_width() - 10) , 10))

    # COLISIONES
    if BALL.colliderect(PLAYER) or BALL.colliderect(PLAYER_2):
        BALL_VEL_X *= -1
    pygame.display.update()

pygame.QUIT()
