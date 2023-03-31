import pandas as pd
table = pd.read_csv('pop.csv')

#then reset pop by removing those values.
table = table.dropna()


def main():
    #print menu
    print(' 1. Display the entire table \n',
    '2. Display the total population of all the states. \n',
    '3. Prompt for the name of a state. Display its population. \n',
    '4. Display the table sorted by state name \n',
    '5. Display the table grouped by region \n',
    '6. Display the table sorted by population, largest to smallest \n',
    '0. Quit')
   
    #prompt user input
    state = input('Enter a option: ')
    if state == '1':
        # Display the entire table
        print(table)
    elif state == '2':
        # Display the total population of all the states.
        print('total population of all the states is: ', table['Population'].sum())
    elif state == '3':
        # Prompt for the name of a state. Display its population.
        s = input('Enter a state: ')
        print('the popuation of', s, 'is', table[table['State'] == s]['Population'].values[0])
    elif state == '4':
        #Display the table sorted by state name
        print(table.sort_values(by=['State']))
    elif state == '5':
        #Display the table grouped by region
        print(table.groupby('REGION').sum())
    elif state == '6':
        #Display the table sorted by population, largest to smallest
        print(table.sort_values(by=['Population'], ascending=False))
    elif state == '0':
        #Quit
        print('Program terminated.')

if __name__ == '__main__':
    main()