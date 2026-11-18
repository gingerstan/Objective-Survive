import pygame as py
py.init()
py.display.set_caption("Objective: Survive")
screen = py.display.set_mode((1000,1000), 0, 32)

white = (255,255,255)

bg_img = py.image.load("assets/battlefield.png")
bg_img.set_colorkey(white)
bg_img.convert()

icon_img = py.image.load("assets/IconV1.png")
icon_img.set_colorkey(white)
icon_img.convert()

loser_img = py.image.load("assets/loser.png")
loser_img.set_colorkey(white)
loser_img.convert()

bar_img = py.image.load("assets/upgrade_bar.png")
bar_img.set_colorkey(white)
bar_img.convert()

speed_upgrade_img = py.image.load("assets/upgrade_speed.png")
speed_upgrade_img.set_colorkey(white)
speed_upgrade_img.convert()

radius_upgrade_img = py.image.load("assets/upgrade_radius.png")
radius_upgrade_img.set_colorkey(white)
radius_upgrade_img.convert()

nuke_img = py.image.load("assets/nuke.png")
nuke_img.set_colorkey(white)
nuke_img = py.transform.scale_by(nuke_img, 0.5)
nuke_img.convert()

normal_img = py.image.load("assets/Normal.png")
normal_img.set_colorkey(white)
normal_img.convert()

rubble_img = py.image.load("assets/Rubble.png")
rubble_img.set_colorkey(white)
rubble_img.convert()

metal_img = py.image.load("assets/Metal.png")
metal_img.set_colorkey(white)
metal_img.convert()

comet_img = py.image.load("assets/comet.png")
comet_img.set_colorkey(white)
comet_img.convert()

diff_img = py.image.load("assets/diff.png")
diff_img.set_colorkey(white)
diff_img.convert()