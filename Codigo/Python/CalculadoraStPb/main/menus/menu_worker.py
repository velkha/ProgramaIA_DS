from menus.menus_show import MenusShow
from menus.menus_probability import MenusProbability
from menus.menus_statistic import MenusStatistic
from menus.menus_hypotesis import MenusHypotesis

class MenuWorker:
    '''Class to handle the menus of the app.'''
    
    def start_menu(self) -> int:
        _rtr = MenusShow.start_menu()
        _menuProb = MenusProbability()
        _menuStat = MenusStatistic()
        _menuHyp = MenusHypotesis()
        switcher = {
            1: _menuProb.probability_menu,
            2: _menuStat.statistics_menu,
            3: _menuHyp.hypotesis_menu,
            0: exit
        }
        
        return switcher.get(_rtr, self.start_menu)()

    
    
    
    
