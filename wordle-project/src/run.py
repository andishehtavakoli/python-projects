from src.wordle import Wordle


if __name__ =='__main__':
    filep = 'src/data/unigram_freq.csv'
    obj = Wordle(filep)
    print(obj.words[:5])
    print(obj.run())


