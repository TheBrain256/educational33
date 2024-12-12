class WordsFinder:

    def __init__(self, file_name):
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        l = ''
        punk = [',', '.', '=', '!', '?', ';', ':', ' - ']
        with open(self.file_name, encoding= 'utf-8') as file:
            for line in file:
                line = line.lower()
                for i in line:
                    if i in punk:
                        line = line.replace(i, '')
                l = l + line
            all_words.update({self.file_name:l.split()})

        return all_words

    def find(self, txt):
        dist = {}
        world = self.get_all_words()[self.file_name]
        for i in range(len(world)):
            if txt.lower() == world[i]:
                dist.update({self.file_name: i + 1})
                return dist

    def count(self, txt):
        dist = {}
        n = 1
        world = self.get_all_words()[self.file_name]
        dist.update({self.file_name: world.count(txt.lower())})
        return dist


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))