from menus.menus_show import MenusShow
from probability.operations import ProbabilityOperations
from utils.ui_worker import UIWorker
class MenusProbability: 
    def probability_menu(self) -> int:
        rtr = MenusShow.probability_menu()
        switcher = {
            1: self.calculate_probability,
            2: self.calculate_complement,
            3: self.calculate_union,
            4: self.calculate_intersection,
            5: self.calculate_conditional,
            6: self.start_menu
        }
        return switcher.get(rtr, self.probability_menu)()
    
    def calculate_probability(self) -> None:
        event_outcomes = int(UIWorker.input('Enter the number of favorable outcomes: '))
        sample_space = int(UIWorker.input('Enter the sample space size: '))
        UIWorker.print(f'The probability of the event is {ProbabilityOperations().calculate_probability(event_outcomes, sample_space)}', "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.probability_menu()
    
    def calculate_complement(self) -> None:
        probability = float(UIWorker.input('Enter the probability: '))
        UIWorker.print(f'The complement of the probability is {ProbabilityOperations().complement(probability)}', "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.probability_menu()
    
    def calculate_union(self) -> None:
        probability_a = float(UIWorker.input('Enter the first probability: '))
        probability_b = float(UIWorker.input('Enter the second probability: '))
        UIWorker.print(f'The union of the probabilities is {ProbabilityOperations().union(probability_a, probability_b)}', "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.probability_menu()
    
    def calculate_intersection(self) -> None:
        probability_a = float(UIWorker.input('Enter the first probability: '))
        probability_b = float(UIWorker.input('Enter the second probability: '))
        UIWorker.print(f'The intersection of the probabilities is {ProbabilityOperations().intersection(probability_a, probability_b)}', "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.probability_menu()
    
    def calculate_conditional(self) -> None:
        probability_a = float(UIWorker.input('Enter the first probability: '))
        probability_b = float(UIWorker.input('Enter the second probability: '))
        UIWorker.print(f'The conditional probability is {ProbabilityOperations().conditional(probability_a, probability_b)}', "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.probability_menu()
    
    def start_menu(self) -> int:
        pass
    
    
