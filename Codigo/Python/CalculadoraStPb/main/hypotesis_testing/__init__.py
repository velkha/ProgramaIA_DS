class GroupByValue:
    def __init__(self, data = {}):
        self.data = data

    def average_by_key(self, group_key: str, value_key: str):
        _grouped_data = {}
        for item in self.data:
            _group_value = item.get(group_key)
            _value = item.get(value_key)
            if _group_value in _grouped_data:
                _grouped_data[group_value].append(_value)
            else:
                _grouped_data[group_value] = [_value]

        _averages = {}
        for _group_value, _values in _grouped_data.items():
            _average = sum(_values) / len(_values)
            _averages[_group_value] = _average

        return _averages