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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nFish out one of [New York City- Chicago- Washington] To Filter by For Details:\n")
        city = city.lower()
        if city not in ['new york city', 'chicago', 'washington']:
            print("\nInvalid Choice! Try Again one of Mentioned below..\n")
            continue
        else:
            print("\nWell! Let's Start With {}.".format(city))
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nFish out one of ['january', 'february', 'march', 'april', 'may', 'june', 'all'] To Filter by For Details 'all' For No Filter: \n")
        month = month.lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("\nInvalid Choice! Try Again one of Mentioned below..\n")
            continue
        else:
            print("\nGreat! Let's Go For {}.".format(month))
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("\nFish out one of ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'all'] To Filter by For Details 'all' For No Filter: \n")
      day = day.lower()
      if day not in ['saturday','sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']:
        print("\nInvalid Choice! Try Again one of Mentioned below..\n")
        continue
      else:
        print("\n Good Job! Let's Go For {}.".format(day))        
        break

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
    # TO DO: load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # TO DO: convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # TO DO: filter by month if applicable
    if month != 'all':
        # TO DO: use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # TO DO: filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # TO DO: filter by day of week if applicable
    if day != 'all':
    # TO DO: filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: ", df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("The most common day of week  is: ", df['day_of_week'].mode()[0])
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour is: ", df['hour'].mode()[0])    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)    

    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    Start_End_Combination = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost frequent combination of start station and end station trip is: ', Start_Station, " & ", End_Station)    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is: ", (df['Trip Duration'].sum())/86400, "Days\n")

    # TO DO: display mean travel time
    print("The total mean time is", (df['Trip Duration'].mean())/60, "Minutes\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nUser Types:\n', user_types)
    
    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo Available Records For This Field!.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo Available Records For This Field!")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo Available Records For This Field!")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_raw_data(df):
    start_loc = 0
    while start_loc < len(df):
        response = input("\nWould you like to explore more row data? Enter 'yes' or 'no'.\n")
        if response.lower() == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
        else:
            break     
    else:
        print("/nIt's done! hopefully, you insightfully explore data you need..")
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()
