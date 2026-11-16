import pygame as py

white = (255,255,255)

bg_img = py.image.load("assets/battlefield.png")
bg_img.set_colorkey(white)

icon_img = py.image.load("assets/IconV1.png")
icon_img.set_colorkey(white)

bar_img = py.image.load("assets/upgrade_bar.png")
bar_img.set_colorkey(white)

speed_upgrade_img = py.image.load("assets/upgrade_speed.png")
speed_upgrade_img.set_colorkey(white)

radius_upgrade_img = py.image.load("assets/upgrade_radius.png")
radius_upgrade_img.set_colorkey(white)

nuke_img = py.image.load("assets/nuke.png")
nuke_img.set_colorkey(white)
nuke_img = py.transform.scale_by(nuke_img, 0.5)

aster_img = py.image.load("assets/Normal.png")
aster_img.set_colorkey(white)

rubble_img = py.image.load("assets/Rubble.png")
rubble_img.set_colorkey(white)

metal_img = py.image.load("assets/Metal.png")
metal_img.set_colorkey(white)