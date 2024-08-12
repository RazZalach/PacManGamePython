import pygame

def draw_welcome_message(win, font):
    text = font.render("Welcome to Pac-Man!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(win.get_width() // 2, win.get_height() // 2))
    win.blit(text, text_rect)
