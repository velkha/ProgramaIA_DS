from utils.ui_worker import UIWorker
class MenusShow:

    @staticmethod
    def start_menu() -> int:
        '''Start menu of the app.'''
        UIWorker.clear()
        UIWorker.print(['Start Menu', '1. Probability', '2. Statistics', '3. Exit'])
        rtr = UIWorker.input('Select an option: ')
        return int(rtr)
    
    @staticmethod
    def probability_menu() -> int:
        '''Probability menu of the app.'''
        UIWorker.clear()
        UIWorker.print(['Probability Menu', 
                        '1. Calculate probability', 
                        '2. Calculate complement', 
                        '3. Calculate union', 
                        '4. Calculate intersection', 
                        '5. Calculate conditional', 
                        '6. Back'])
        rtr = UIWorker.input('Select an option: ')
        return int(rtr)
    
    @staticmethod
    def statistics_menu() -> int:
        '''Statistics menu of the app.'''
        UIWorker.clear()
        UIWorker.print(['Statistics Menu', 
                        '1. Basic calculations', 
                        '2. Hypothesis testing', 
                        '3. Back'])
        rtr = UIWorker.input('Select an option: ')
        return int(rtr)
    
    @staticmethod
    def basic_calcs_menu() -> int:
        '''Basic calculations menu of the app.'''
        UIWorker.clear()
        UIWorker.print(['Basic Calculations Menu', 
                        '1. Calculate mean', 
                        '2. Calculate median', 
                        '3. Calculate mode', 
                        '4. Calculate variance', 
                        '5. Calculate standard deviation', 
                        '6. Calculate standard error', 
                        '7. Back'])
        rtr = UIWorker.input('Select an option: ')
        return int(rtr)
    
    @staticmethod
    def hypothesis_testing_menu() -> int:
        '''Hypothesis testing menu of the app.'''
        UIWorker.clear()
        UIWorker.print(['Hypothesis Testing Menu', '1. Z-test', '2. T-test', '3. Back'])
        rtr = UIWorker.input('Select an option: ')
        return int(rtr)
    
    