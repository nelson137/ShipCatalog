from collections import OrderedDict

testData = OrderedDict([('ship1', OrderedDict([('model', ''),
                                               ('production status', '')])),
                        ('ship2', OrderedDict([('model', ''),
                                               ('production status', '')])),
                        ('ship3', OrderedDict([('model', ''),
                                               ('production status', '')]))])

s = OrderedDict(sorted(testData.items(), key=lambda item: (item[1]['production status'], item[1]['model'])))
print(s.keys())
print(s.items())