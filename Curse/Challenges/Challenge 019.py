#Write a Python program that opens and plays the audio from an MP3 file.
import pygame
filename = "C:/Users/Ariane/Music/NEFFEX - Grateful [Copyright Free] No.54 - NEFFEX (youtube).mp3"
pygame.mixer.init()
pygame.mixer.music.load(filename)
pygame.mixer.music.play()
input("Press Enter to continue...")




