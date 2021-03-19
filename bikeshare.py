import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    incorrect = "XXXXXXXXXXXXXXXXXXXXXXXX invalid input XXXXXXXXXXXXXXXXXXXXXXXX"
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        print('which the city you want to explore it\'s data? ')
        city = input().lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print(incorrect  ," \n Please choose a city from here: (Chicago, New York City or Washington) ")
    # get user input for month of first six months
    while True:
        print('which the month you want to explore it\'s data? ')
        month = input().lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print(incorrect  ," \n Please choose a month from here: (january, February, March, April, May, June or All) ")
    # get user input for day of week
    while True:
        print('which the day you want to explore it\'s data? ')
        day = input().lower()
        if day in ['sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']:
            break
        else:
            print(incorrect  ," \n Please choose a day from here: (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or All)")

    print('-'*40)
    return city, month, day


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month is: ", most_common_month, '\n')

    #display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week  is: ", most_common_day_of_week, '\n')

    #display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is: ", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #Display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: ", most_common_start_station, '\n')

    #display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: ", most_common_end_station, '\n')

    #display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + df['End Station']
    most_common_trip_station = df['combination'].mode()[0]
    print("The most frequent combination of start station and end station trip is: ", most_common_trip_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: ", total_travel_time)

    #Display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: ", average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    user_type = df['User Type'].value_counts()
    print("The counts of each user type:\n" ,user_type)

    #Display counts of gender
    try:
        counts_of_gender = df['Gender'].value_counts()
        print("\nThe counts of each gender:\n", counts_of_gender)
    except:
        print(" (@_@) !\nthis city dosen\'t have data of gender")

    #Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = int(df['Birth Year'].min())
        print('\nThe earliest year of birth is: ', earliest_year_of_birth)
        most_recent_year_of_birth = int(df['Birth Year'].max())
        print('\nThe most recent year of birth is: ', most_recent_year_of_birth)
        most_common_year_of_birth = int(df['Birth Year'].mode()[0])
        print('\nThe most common year of birth is: ', most_common_year_of_birth)
    except:
        print(" (@_@) !\nthis city dosen\'t have data of birth year")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    raw = 1
    while True:
        more_raw = input('\nDo you want to see more raw of data? (please enter YES or No)\n')
        if more_raw.lower() == 'yes':
            print(df.iloc[raw:raw+5])
            raw = raw+5
        elif more_raw.lower() == 'no':
            break
        else:
            print("Please Type Again!")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
