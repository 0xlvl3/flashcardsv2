def open_menu(menu_txt):
    with open(menu_txt, "r") as menu:
        menu_read = menu.read()
    print(menu_read)
