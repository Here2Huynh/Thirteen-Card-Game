#generate random data text files

import random
import string

mb = 1024 ** 2  # 1 Mb of text
#gb = 1073741824 # 1GB of text
chars = ''.join([random.choice(string.letters) for i in range(mb)])

def generate_fake_data(number_of_files):
    """Function takes in number_of_files and generate that many files that are 1MB big"""
    ran_gen = random.randint(0,number_of_files)
    for num in range(number_of_files):
        with open(str(num)+str(ran_gen)+'FakeData.txt', 'w+') as f:
            f.write(chars)

if __name__ == '__main__':
    number_of_files = input('How many files do you want to make? ')
    #size = input('How big do you want the file size to be? ')
    #print 'OKAY GENERATING...'
    print 'GENERATING...PLEASE WAIT....'
    generate_fake_data(number_of_files)
