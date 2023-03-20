def main():
    # Prompt the user to enter a speed of an object in miles per hour (mph). 
    # Convert this to meters per second using the formula 1mph = 0.447 m/s. 
    # Display the answer using a formatted print statement with labels and two decimal places – for example, '60.00 mph = 26.82 m/s'. 
    # Run this code to test it on 60 mph.
    mph = float(input('Enter a speed in mph: '))
    meters_per_second = mph * 0.447
    print('{:.2f} mph = {:.2f} m/s'.format(mph, meters_per_second))

    # Add code that prints the following messages: if the speed is at least 25 m/s, print 'Fast'; if it's less than 5 m/s, print 'Slow'; otherwise, print 'Meh'
    if meters_per_second >= 25:
        print('Fast')
    elif meters_per_second < 5:
        print('Slow')           
    else:
        print('Meh')

if __name__ == '__main__':
    main()  