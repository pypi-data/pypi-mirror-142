from hermessplitter.main import HermesSplitter
import unittest


class MainTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(MainTest, self).__init__(*args, **kwargs)
        self.hs = HermesSplitter('0.0.0.0', 2295, 'hermes', 'watchman', 'hect0r1337',
                            '192.168.100.109', 'wdb', 'watchman', 'hect0r1337',
                            '192.168.100.109', debug=False)

    def test_a(self):
        self.hs.activate(carnum='О083АН102')
        all_data = ['0', '-50', '10', '40', '100', '500', '1000', '6660']
        magic_data = []
        for data in all_data:
            response = self.hs.make_magic(data)
            magic_data.append(response)
        print("MAGIC DATA", dict(zip(all_data, magic_data)))
