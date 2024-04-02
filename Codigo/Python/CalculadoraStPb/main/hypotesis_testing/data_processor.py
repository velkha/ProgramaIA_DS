import re
class DataProcessor:
    def __init__(self, data = {}):
        self.data = data

    def check_data_consistency(self, group_key: str | list, value_key: str) -> bool:
        '''Checks if the data has the keys in the group_key and value_key, also check, in case the group_key is a multikey, if the keys are in the data'''
        if not self.data:
            return False
        if not group_key or not value_key or value_key not in self.data[0].keys():
            return False
        if not self.check_data_value(value_key):
            return False
        if ';' in group_key:
            _group_keys = group_key.split(';')
            return self.check_data_consistency_multi_key(_group_keys)
        elif group_key not in self.data[0].keys():
            return False
        return True
    
    def check_data_consistency_multi_key(self, group_key: list) -> bool:
        '''Checks if the data has the keys in the group_key, in case the group_key is a multikey'''
        for item in self.data:
            for key in group_key:
                if key not in item.keys():
                    return False
        return True
    def check_data_value(self, value_key: str) -> bool:
        '''Checks if the values in the data are numbers and converts them to float if they are not, in case they are strings that
        cannot be converted to float, it returns False'''
        for item in self.data:
            value = item.get(value_key)
            if not isinstance(value, (int, float)):
                value = re.sub(r'[€$]', '', value)
                value = re.sub(r',', '.', value)
                value = re.sub(r'\.', '', value, count=value.count('.')-1)
                try:
                    value = float(value)
                except ValueError:
                    return False
                item[value_key] = value
        return True
    def generategrouped_data (self, group_key: str, value_key: str, check_data=True) -> dict:
        '''Generates a dictionary with the data grouped by the group_key'''
        if check_data:
            if not self.check_data_consistency(group_key, value_key):
                return {}
        if ';' in group_key:
            _group_keys = group_key.split(';')
            return self.generategrouped_data_multi_key(_group_keys, value_key)
        else:
            return self.generategrouped_data_single_key(group_key, value_key)
        
    def generategrouped_data_single_key(self, group_key: str, value_key: str) -> dict:
        '''Generates a dictionary with the data grouped by the single group_key'''
        grouped_data = {}
        for item in self.data:
            _group_value = item.get(group_key)
            _value = item.get(value_key)
            if _group_value in grouped_data:
                grouped_data[_group_value].append(_value)
            else:
                grouped_data[_group_value] = [_value]

        return grouped_data
    
    def generategrouped_data_multi_key(self, group_key: list, value_key: str) -> dict:
        '''Generates a dictionary with the data grouped by the multi group_key'''
        grouped_data = {}
        for item in self.data:
            _group_value = tuple([item.get(key) for key in group_key])
            _value = item.get(value_key)
            if _group_value in grouped_data:
                grouped_data[_group_value].append(_value)
            else:
                grouped_data[_group_value] = [_value]
        return grouped_data
    
    def average_by_key(self, group_key: str, value_key: str) -> dict:
        '''Calculates the average of the values in the data grouped by the group_key'''
        if not self.check_data_consistency(group_key, value_key):
            return {}
        _grouped_data = self.generategrouped_data(group_key, value_key, False)
        _averages = {}
        for _group_value, _values in _grouped_data.items():
            _average = sum(_values) / len(_values)
            _averages[_group_value] = _average
        return _averages

    def variance_by_key(self, group_key: str, value_key: str) -> dict:
        '''Calculates the variance of the values in the data grouped by the group_key'''
        if not self.check_data_consistency(group_key, value_key):
            return {}
        _grouped_data = self.generategrouped_data(group_key, value_key, False)
        _variances = {}
        for _group_value, _values in _grouped_data.items():
            _average = sum(_values) / len(_values)
            _variance = sum([(_value - _average) ** 2 for _value in _values]) / len(_values)
            _variances[_group_value] = _variance
        return _variances

    def proportion_by_key(self, group_key: str, value_key: str) -> dict:
        '''Calculates the proportion of the values in the data grouped by the group_key'''
        if not self.check_data_consistency(group_key, value_key):
            return {}
        _grouped_data = self.generategrouped_data(group_key, value_key, False)
        _proportions = {}
        for _group_value, _values in _grouped_data.items():
            _total = len(_values)
            _proportion = sum([1 for _value in _values if _value == 1]) / _total
            _proportions[_group_value] = _proportion

        return _proportions