from menus.menus_show import MenusShow
from probability.operations import ProbabilityOperations
from utils.ui_worker import UIWorker
from probability.plot_probabilities import ProbabilityPlotter
class MenusProbability: 
    def probability_menu(self) -> int:
        _rtr = MenusShow.probability_menu()
        _switcher = {
            0: self.start_menu,
            1: self.plot_menu,
            2: self.calculate_probability,
            3: self.calculate_complement,
            4: self.calculate_union,
            5: self.calculate_intersection,
            6: self.calculate_conditional,
            7: self.calculateTotalFavorableOutcomes,
            8: self.calculateBinomialProbability,
            9: self.binomialProbabilityNormalApproximation
        }
        return _switcher.get(_rtr, self.probability_menu)()
    
    def plot_menu(self) -> int:
        _rtr = MenusShow.plot_menu()
        _switcher = {
            0: self.probability_menu,
            1: self.plot_binomial_probability
        }
        return _switcher.get(_rtr, self.plot_menu)()

    def calculate_probability(self) -> None:
        _event_outcomes = int(UIWorker.input('Enter the number of favorable outcomes: '))
        _sample_space = int(UIWorker.input('Enter the sample space size: '))
        UIWorker.print(f'The probability of the event is {ProbabilityOperations().calculate_probability(_event_outcomes, _sample_space)}', "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.probability_menu()
    
    def calculate_complement(self) -> None:
        _probability = float(UIWorker.input('Enter the probability: '))
        UIWorker.print(f'The complement of the probability is {ProbabilityOperations().complement(_probability)}', "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.probability_menu()
    
    def calculate_union(self) -> None:
        _probability_a = float(UIWorker.input('Enter the first probability: '))
        _probability_b = float(UIWorker.input('Enter the second probability: '))
        UIWorker.print(f'The union of the probabilities is {ProbabilityOperations().union(_probability_a, _probability_b)}', "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.probability_menu()
    
    def calculate_intersection(self) -> None:
        _probability_a = float(UIWorker.input('Enter the first probability: '))
        _probability_b = float(UIWorker.input('Enter the second probability: '))
        UIWorker.print(f'The intersection of the probabilities is {ProbabilityOperations().intersection(_probability_a, _probability_b)}', "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.probability_menu()
    
    def calculate_conditional(self) -> None:
        _probability_a = float(UIWorker.input('Enter the first probability: '))
        _probability_b = float(UIWorker.input('Enter the second probability: '))
        UIWorker.print(f'The conditional probability is {ProbabilityOperations().conditional(_probability_a, _probability_b)}', "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.probability_menu()
    
    def calculateTotalFavorableOutcomes(self) -> None:
        _sample_space = int(UIWorker.input('Enter the sample space size: '))
        _favorableOutcomes = int(UIWorker.input('Enter the number of favorable outcomes: '))
        UIWorker.print(f'The total number of favorable outcomes is {ProbabilityOperations().calculateTotalFavorableOutcomes(_sample_space, _favorableOutcomes)}', "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.probability_menu()
    
    def calculateBinomialProbability(self) -> None:
        _k = int(UIWorker.input('Enter the number of successes: '))
        _n = int(UIWorker.input('Enter the number of trials: '))
        _p = float(UIWorker.input('Enter the probability of success: '))
        UIWorker.print(f'The probability of k successes in n trials is {ProbabilityOperations().calculateBinomialProbability(_k, _n, _p)}', "Blue")
        _option = UIWorker.input('Do you want to plot the binomial probability distribution? (y/n): ')
        if _option == 'y':
            ProbabilityPlotter().plot_binomial_probability(_n, _p)
        UIWorker.input('Press Enter to continue...')
        return self.probability_menu()

    def plot_binomial_probability(self) -> None:
        _n = int(UIWorker.input('Enter the number of trials: '))
        _p = float(UIWorker.input('Enter the probability of success: '))
        ProbabilityPlotter().plot_binomial_probability(_n, _p)
        UIWorker.input('Press Enter to continue...')
        return self.plot_menu()
    
    def binomialProbabilityNormalApproximation(self) -> None:
        _n = int(UIWorker.input('Enter the number of trials: '))
        _p = float(UIWorker.input('Enter the probability of success: '))
        _k = int(UIWorker.input('Enter the number of successes: '))
        UIWorker.print(f'The normal approximation to the binomial distribution is {ProbabilityOperations().binomialProbabilityNormalApproximation(_k, _n, _p)}', "Blue")
        UIWorker.input('Press Enter to continue...')
        return self.probability_menu()

    def start_menu(self) -> int:
        pass
    
    
