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
    cities=['chicago', 'new york city' ,'washington']
    while True:
        city =input("Please enter a city 'chicago', 'new york city' ,'washington' :").lower()
        if city in cities:
            break
        else:
            print('Please enter a valid city')
            continue
  
    # TO DO: get user input for month (all, january, february, ... , june)]
    months=['january', 'february', 'march', 'april', 'may', 'june', 'july','all'] 
    
    while True:
        month=input("Please enter any one of the first 6 months or enter All to select all 6 months:").lower()
        if month in months:
            break
        else:
            print('Please enter a valid month')
            continue
    days=['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']
    
    while True:
        day =input("Please enter day's name or type all for all days:").lower()
        if day in days:
            break
        else:
            print('Please enter a valid day')
            continue
    

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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['month']= df['Start Time'].dt.month
    df['day_of_week']= df['Start Time'].dt.day_name()
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week']== day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months=['january', 'february', 'march', 'april', 'may', 'june', 'july','august', 'september', 'october', 'november', 'december']
    # TO DO: display the most common month
    most_month=df['month'].value_counts().idxmax()
    print('Most common month is : ', months[most_month-1])
    

    # TO DO: display the most common day of week
    most_day=df['day_of_week'].value_counts().idxmax()
    print('Most common day is : ',most_day)

    # TO DO: display the most common start hour
    most_start_hour=df['Start Time'].dt.hour.value_counts().idxmax()
    print('Most common hour is : ',most_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most common used start station is : ',df['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print('Most common used end station is : ',df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    print('Most frequent combination of start station and end station trip is : ',df.groupby('Start Station')['End Station'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['End Time']=pd.to_datetime(df['End Time'] )
    # TO DO: display total travel time
    df['Total Time'] = df['End Time'] - df['Start Time']
    
    print('Total travel time is : ',df['Total Time'].sum().round(freq='S'))
    # TO DO: display mean travel time
    print('Mean travel time is : ',df['Total Time'].mean().round(freq='S'))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    print('\nCounts of user types :\n',df['User Type'].value_counts()) 
    if city == 'washington': 
        print ('\nWashington has no Gender or Birth Year User Stats')
    else:         # bacause washington has no Gender or Birth Year Stats
        # TO DO: Display counts of gender
        print('\nCounts of gender :\n',df['Gender'].value_counts())

        # TO DO: Display earliest, most recent, and most common year of birth
        print('\nEarliest year of birth :',int(df['Birth Year'].min()))
        print('Most recent year of birth :',int(df['Birth Year'].max()))
        print('Most common year of birth :',int(df['Birth Year'].value_counts().idxmax()))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def view_raw(df):
    i=0
    while True:
        print(df.iloc[i*5:(i+1)*5])
        i=i+1
        while True:
            view=input('Would you like to view 5 more rows ? (yes,no)').lower()
            if view=='yes' or view =='no':
                break
            else:
                print('Please enter a valit input.')
                continue
        if view =='no':
            break
        else:
            continue
                
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        while True:
            view = input('Would you like to view raw data ? (yes,no):').lower()
            if view == 'yes' or view == 'no':
                break
            else:
                print('Please enter a valid input.')
                continue
          
        if view == 'yes':
            view_raw(df)
            
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        while True:
            restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
            if restart == 'yes' or restart == 'no':
                break
            else:
                print('Please enter a valid input (yes,no)')
                
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
