from menus.menus_show import MenusShow
from menus.menus_probability import MenusProbability
from menus.menus_statistic import MenusStatistic

class MenuWorker:
    '''Class to handle the menus of the app.'''
    
    def start_menu(self) -> int:
        rtr = MenusShow.start_menu()
        _menuProb = MenusProbability()
        _menuStat = MenusStatistic()
        switcher = {
            1: _menuProb.probability_menu,
            2: _menuStat.statistics_menu,
            3: exit
        }
        
        return switcher.get(rtr, self.start_menu)()

    
    
    
    
