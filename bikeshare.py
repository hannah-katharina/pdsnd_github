import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all','january','february','march','april','may','june']

WEEKDAY_DATA = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
 
    try:
        city = input("Please choose a city (chicago, new york city or washington): ").lower()
        while city not in CITY_DATA:
            print("That is not a valid city.")
            city = input("Please choose a city (chicago, new york city or washington): ").lower()
    
        
    # TO DO: get user input for month (all, january, february, ... , june)
        month = input("Please choose a month (all, january, february,.., june): ").lower()
        while month not in MONTH_DATA:
            print("That is not a valid month.")
            month = input("Please choose a month (all, january, february,.., june): ").lower()
       
    


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input("Please choose a weekday (all, monday, tuesday,..,sunday): ").lower()
        while day not in WEEKDAY_DATA:
            print("That is not a valid weekday.")
            day = input("Please choose a weekday (all, monday, tuesday,..,sunday): ").lower()
        return city, month, day
    except:
        print("Please review your input.")


    print('-'*40)
   
    


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['weekday'] == day.title()]

    return df

 
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
   
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most common month:', popular_month)


    # TO DO: display the most common day of week
    df['weekday'] = df['Start Time'].dt.weekday
    popular_weekday = df['weekday'].mode()[0]
    print('Most common weekday:', popular_weekday)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most common hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most popular start station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most popular end station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + " and " + df['End Station']).mode()[0]
    print('Most frequent combination:', frequent_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
   
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        print(df['User Type'].value_counts())
    except Exception as e:
        print('Couldn\'t calculate the type of users because the following error occured: {}'.format(e))

    # TO DO: Display counts of gender
    try:
        print(df['Gender'].value_counts())
    except Exception as e:
        print('Couldn\'t provide any details on gender because the following data are missing: {}'.format(e))

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('Youngest biker (birth year): ' + str(int(df['Birth Year'].max())))
        print('Oldest biker (birth year): ' + str(int(df['Birth Year'].min())))
        print('Youngest biker (birth year): ' + str(int(df['Birth Year'].mode()[0])))
    except Exception as e:
        print('Couldn\'t provide any details about the age structure because the following data are missing: {}'.format(e))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    RESPONSE_LIST = ['yes','no']
    response = ''
    rows = 0
    
    while response not in RESPONSE_LIST:
        print('Do like to review the raw data? yes or no:')
        response = input().lower()
        if response == 'yes':
            print(df.head())
        elif response not in RESPONSE_LIST:
            print('Please write yes or no')
    
    while response == 'yes':
        print('Would you like to see more data?')
        rows +=5
        response = input().lower()
        if response == 'yes':
            print(df[rows:rows+5])
        elif response != 'yes':
            break
    
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
