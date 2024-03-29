from menus.menu_worker import MenuWorker

while (True):
    _menu = MenuWorker()
    rtr = _menu.start_menu()
    if rtr == 3:
        break