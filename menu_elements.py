from menu import MenuSystem, StaticMenu, MenuButton, FuncButton, StatBar
from load_assets import *
from pygame import Surface
from animation import load_number_sequence

nums = load_number_sequence()


main_menu = MenuSystem()
start_menu = StaticMenu("Start",image=icon_img)
update_diff_button = FuncButton([700,700],"update_difficulty",nums[1])
update_diff_button.args = [update_diff_button,nums]
start_menu_elements = [
	FuncButton([700,850],"enter_game",play_img),
	update_diff_button
]
start_menu.add_elements(start_menu_elements)
main_menu.add_menu(start_menu)

t = Surface((0,0))
t.fill((0,0,0))
t.set_colorkey((0,0,0))

in_game_menu = MenuSystem()
bar_menu = StaticMenu("bar_gui",image=bar_img,pos=[0,800])
upgrade_menu = StaticMenu("upgrade_gui",image=t)
budget_menu = StaticMenu("budget_gui",image=basic_menu_img,pos=[100,0])
bar_menu_elements = [
	MenuButton([50,830],upgrade_menu,open_upgrade_menu_img),
	MenuButton([50,910],budget_menu,budget_img),
	StatBar([800,820],health_bar_img,None,200,(0,255,0),start_value=100,bg_color=(128,128,64))
]
upgrade_menu_elements = [
	FuncButton([200,200],"upgrade_speed",blank_ability_img),
	FuncButton([400,200],"upgrade_radius",blank_ability_img),
	MenuButton([800,800],bar_menu,back_img,keep_prev_menu=False)
]
budget_menu_elements = [
	MenuButton([800,675],bar_menu,back_img,keep_prev_menu=False)
]
bar_menu.add_elements(bar_menu_elements)
upgrade_menu.add_elements(upgrade_menu_elements)
budget_menu.add_elements(budget_menu_elements)
in_game_menu.add_menu(bar_menu)
in_game_menu.add_menu(upgrade_menu)
in_game_menu.add_menu(budget_menu)

