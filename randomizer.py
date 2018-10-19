import random

class Randomizer(object):

    def __init__(self, file_name: str) -> None:
        """ put input file into the same directory """
        self.content = ''
        with open(file_name) as f:
            self.content = [line.rstrip('\n') for line in f.readlines()]
        self.content = [name for name in self.content if len(name) > 3]

    def randomize_list(self):
        random.shuffle(self.content)

    def prepare_output_list(self, file_name='randomized.txt'):
        with open(file_name, 'w+') as f:
            for i, name in enumerate(self.content):
                f.write('{0}. {1}'.format(i + 1, name) + '\n')
                if (i + 1) % 2 == 0:
                    f.write('\n')

if __name__ == '__main__':
    randomizer = Randomizer(file_name='names.txt')
    randomizer.randomize_list()
    randomizer.prepare_output_list()
