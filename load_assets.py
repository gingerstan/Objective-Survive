import pygame as py

white = (255,255,255)

bg_img = py.image.load("assets/battlefield.png")
bg_img.set_colorkey(white)

nuke_img = py.image.load("assets/nuke.png")
nuke_img.set_colorkey(white)
nuke_img = py.transform.scale_by(nuke_img, 0.5)

aster_img = py.image.load("assets/Normal.png")
aster_img.set_colorkey(white)

rubble_img = py.image.load("assets/Rubble.png")
rubble_img.set_colorkey(white)

metal_img = py.image.load("assets/Metal.png")
metal_img.set_colorkey(white)