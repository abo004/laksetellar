
def laks():
    antall = int(input('Positivt heiltall: '))
    if antall < 1:
        print('Number too low')
    elif antall == 1:
        print(antall, 'laks')
    else:
        print(antall, 'laksar')

laks()
