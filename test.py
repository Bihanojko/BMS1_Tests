import os

examples = os.listdir(os.curdir + '/Examples')

# if Makefile is present, make the source files
if 'Makefile' in os.listdir(os.curdir):
    os.system('make clean')
    os.system('make')

# if Makefile is missing and executables are not found, exit
elif 'bms1A' not in os.listdir(os.curdir) or 'bms1B' not in os.listdir(os.curdir):
    print('Executable files \'bms1A\' and/or \'bms1B\' not found!')
    exit()

txt_examples = sorted([x for x in examples if x[-3:] == 'txt'])
wav_examples = sorted([x for x in examples if x[-3:] == 'wav'])

# execute modulation and demodulation
for example in txt_examples:
    os.system('./bms1A Examples/' + example)
    os.system('./bms1B Examples/' + example[:-3] + 'wav')

for example in wav_examples:
    os.system('./bms1B Examples/' + example)

outputs = os.listdir(os.curdir + '/Examples')
txt_outputs = sorted([x for x in outputs if x[-3:] == 'txt'])

# compare txt files
print('\n\nComparing output files...')
for example in txt_outputs:
    print(example)
    os.system('diff ref.txt Examples/' + example)
