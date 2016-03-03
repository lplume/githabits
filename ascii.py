class AsciiRenderer:

    def render(self, dataset):
        for r in range(12, -1, -1):
            if r > 2:
                print('| ', end='')
                for d in dataset:
                    if d[0] >= (r - 2):
                        print(' # ', end='')
                    else:
                        print('   ', end='')
                print('')
            else:
                if r == 2:
                    length = len(dataset) * 3 + 4
                    for c in range(length):
                        print('-', end='')
                    print('')
                elif r == 1:
                    print('   ', end='')
                    for d in dataset:
                        print(str(d[1]) + ' ', end='')
                    print('')