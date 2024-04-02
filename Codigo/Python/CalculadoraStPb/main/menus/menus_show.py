from utils.ui_worker import UIWorker
class MenusShow:

    @staticmethod
    def start_menu() -> int:
        '''Start menu of the app.'''
        UIWorker.clear()
        UIWorker.print(['Start Menu', 
                        '1. Probability', 
                        '2. Statistics',
                        '3. Full Hypothesis testing',
                        '0. Exit'])
        _rtr = UIWorker.input('Select an option: ')
        return int(_rtr)
    
    @staticmethod
    def probability_menu() -> int:
        '''Probability menu of the app.'''
        UIWorker.clear()
        UIWorker.print(['Probability Menu',
                        '1. Plot Menu', 
                        '2. Calculate probability', 
                        '3. Calculate complement', 
                        '4. Calculate union', 
                        '5. Calculate intersection', 
                        '6. Calculate conditional', 
                        '7. Calculate total favorable outcomes',
                        '8. Calculate binomial probability',
                        '9. Normal approximation to binomial',
                        '10. Calculate probabilities for value',
                        '11. Calculate probability under a value',
                        '12. Calculate probability under a value with sample data',
                        '0. Back'])
        _rtr = UIWorker.input('Select an option: ')
        return int(_rtr)
    
    @staticmethod
    def plot_menu() -> int:
        '''Plot menu of the app.'''
        UIWorker.clear()
        UIWorker.print(['Plot Menu', 
                        '1. Binomial Probability Distribution', 
                        '2. Probability Distribution Histogram',
                        '0. Back'])
        _rtr = UIWorker.input('Select an option: ')
        return int(_rtr)

    @staticmethod
    def statistics_menu() -> int:
        '''Statistics menu of the app.'''
        UIWorker.clear()
        UIWorker.print(['Statistics Menu', 
                        '1. Basic calculations', 
                        '2. Hypothesis testing', 
                        '3. Sum operations',
                        '0. Back'])
        _rtr = UIWorker.input('Select an option: ')
        return int(_rtr)
    
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
                        '7. Calculate skewness',
                        '8. Calculate percentiles',
                        '9. Calculate quartiles',
                        '10. Calculate value for percentile',
                        '11. Calculate probability more than',
                        '0. Back'])
        _rtr = UIWorker.input('Select an option: ')
        return int(_rtr)
    
    @staticmethod
    def sum_operations_menu() -> int:
        '''Sum operations menu of the app.'''
        UIWorker.clear()
        UIWorker.print(['Sum Operations Menu', 
                        '1. Calculate sum', 
                        '2. Calculate sum standard error', 
                        '3. Calculate sum confidence interval', 
                        '4. Calculate sum expected value',
                        '5. Calculate probability sum more than',
                        '0. Back'])
        _rtr = UIWorker.input('Select an option: ')
        return int(_rtr)

    @staticmethod
    def hypothesis_testing_menu() -> int:
        '''Hypothesis testing menu of the app.'''
        UIWorker.clear()
        UIWorker.print(['Hypothesis Testing Menu', '1. Z-test', '2. T-test', '3. Back'])
        _rtr = UIWorker.input('Select an option: ')
        return int(_rtr)
    
    @staticmethod
    def hypotesis_menu() -> int:
        '''Hypotesis menu of the app.'''
        UIWorker.clear()
        UIWorker.print(['Hypotesis Menu',
                        '1. Hypotesis test simple',
                        '2. Hypotesis test full data',
                        '0. Back'])
        _rtr = UIWorker.input('Select an option: ')
        return int(_rtr)
    
    @staticmethod
    def hypotesis_test_simple_menu() -> int:
        '''Hypotesis test simple menu of the app.'''
        UIWorker.clear()
        UIWorker.print(['Hypotesis Test Simple Menu',
                        '1. Check average of sample data in groups',
                        '2. Check variance of sample data in groups',
                        '3. Check proportion of sample data in groups',
                        '0. Back'])
        _rtr = UIWorker.input('Select an option: ')
        return int(_rtr)
    
    @staticmethod
    def hypotesis_test_full_data_menu() -> int:
        '''Hypotesis test full data menu of the app.'''
        UIWorker.clear()
        UIWorker.print(['Hypotesis Test Full Data Menu',
                        '1. Compare the multiple values of given keys',
                        '0. Back'])
        _rtr = UIWorker.input('Select an option: ')
        return int(_rtr)
    