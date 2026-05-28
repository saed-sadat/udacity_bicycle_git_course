import os
import time
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'all':'all'}
DAY_DATA=['monday','tuesday','wednesday', 'thursday','friday','saturday','sunday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day 
        filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
   
# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a
    #while loop to handle invalid inputs
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    print('-'*40)
    def ask_user(prompt,valid_options):
        while True:
            try:
                user_input=input(prompt).strip().lower()
                if user_input in valid_options:
                    return user_input
                matches = [opt for opt in valid_options if opt.startswith(user_input)]
                if len(matches) == 1:
                    print(f"did you mean '{matches[0]}?(selected automatically)'")
                    return matches [0]
                print(f"invalid input! options:{join(list(valid_options))}\n")
            except(KeyboardInterrupt,EOFError):
                print("\n Keyboard Interrupt. Program exits!")
                exit()
    
    city = ask_user(
        "please enter the name of city(Chicago, New York, Washington):",CITY_DATA.keys()
    )
    month = ask_user("please enter the name of the month(Jan, Feb, Mar, Apr, May,Jun)  or 'all':" , MONTH_DATA.keys() )
                     
    day = ask_user("please enter the namethe day(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) or 'all':", DAY_DATA)
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
    filename = CITY_DATA[city]
    if not os.path.exists(filename):
        print(f"\ Error: File '{filename}' does not exist in the current folder!")
        return None
    
    try:
        df = pd.read_csv(filename)
    except Exception as e:
        print(f"\n error loading file '{filename}':{e}")
        return None             
            
    try:
        time_col = [c for c in df.columns if 'time' in c.lower() or 'date' in c.lower()]
        if len(time_col) > 0:
            chosen_time_col=time_col[0]
            df[chosen_time_col] = pd.to_datetime(df[chosen_time_col], errors='coerce')
            # alle_monate = df[chosen_time_col].dt.month
            # alle_tage   = df[chosen_time_col].dt.day_name().str.lower()
            df['hour'] = df[chosen_time_col].dt.hour
            df['month'] = df[chosen_time_col].dt.month
            df['day_of_week'] = df[chosen_time_col].dt.day_name().str.lower()
            if month != 'all':
                #ziel_monat_zahl = MONTH_DATA[month]
                df= df[df['month'] == MONTH_DATA[month]]
                if day != 'all':
                    df = df[df['day_of_week'] == day]
        return df
    except Exception as e:
        print(f"\n error during the data filtering {e}")
        return None
                

def time_stats(df):
    """
   Displays statistics on the most frequent times of travel.
   
   Args:
   
   (DataFrame) csv File of the city to be analyzed
   
   Returns:
   """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    if df.empty:
        return
    # TO DO: display the most common month
    try:
        month_names = {v: k for k, v in MONTH_DATA.items()}
        pop_month = df['month'].mode()[0]
        print(f"Most Common Month:{month_names[pop_month].title()}")
        # TO DO: display the most common day of week
        pop_day = df['day_of_week'].mode()[0]
        print(f"Most Common Day:{pop_day.title()}")
        # TO DO: display the most common start hour
        pop_hour = df['hour'].mode()[0]
        print(f" Most Common start time is:{int(pop_hour)}" )
    except Exception as e:
        print(f" Error during callucation of time_stats:{e}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):    
    """
     Displays statistics on the most popular stations and trip.
    Args:
        (DataFrame) csv File of the city to be analyzed                
    Returns:       
    """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    if df.empty:
        return
    try:
        start_col = [c for c in df.columns if 'start' in c.lower() and 'station' in \
                     c.lower()]
        end_col = [ c for c in df.columns if 'end' in c.lower() and 'station' in \
                   c.lower()]
        
        if start_col and end_col:
            pop_start = df[start_col[0]].mode()[0]
            print(f" Most commonly used start station:{pop_start}")
            # TO DO: display most commonly used end station
            pop_end = df[end_col[0]].mode()[0]
            print(f" Most commonly used end station:{pop_end}")
            df['trip_combination'] = df [start_col[0]] + " --> onto --> " + df[end_col[0]] 
            pop_trip = df['trip_combination'].mode()[0]
            print(f" \n Most frequent combination of start station and end station:\n  \n{pop_trip}"
            )
    except Exception as e:
            print(f" Error during calculation of station_stats:{e}")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    
    """
    Displays statistics on the total and average trip duration.
    Args:
        (DataFrame) csv File of the city to be analyzed                
    Returns:       
    """
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    if df.empty:
        return
    try:
        duration_col =[c for c in df.columns if 'dur' in c.lower()]
        
        if duration_col:
            total_duration = df[duration_col[0]].sum()
            mean_duration =  df[duration_col[0]].mean()
            if pd.notna(total_duration) and total_duration>0:
                total_mins, total_secs = divmod(total_duration,60)
                total_hours,total_mins = divmod(total_mins, 60)
                total_days, total_hours = divmod(total_hours, 24)
                # TO DO: display total travel time
                print(f" Total travel time: {int(total_days)} days, {int(total_hours) } hours, {int(total_mins)} Min.")
                # TO DO: display mean travel time
                print(f" mean travel time: {int(mean_duration// 60)} Min., \
{int(mean_duration % 60) } Sek.")
            else:
                print(" No columns for travel duration found.")
    except Exception as e:
        print(f" Error during der calculation of trip_duration_stats")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):    
    """
    Displays statistics on bikeshare users.
    Args:
        (DataFrame) csv File of the city to be analyzed                
    Returns:       
    """    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    if df.empty:
        return
    try:
        # Count First usertype (Subscriber vs Customer)
        user_col = [c for c in df.columns if 'user' in c.lower() or 'type' in c.lower()]
        if user_col:
            print(" Counts of user types:")
            #.value_counts() usagge to ount teh types
            for user_type, count in df[user_col[0]].value_counts().items():
                # TO DO: Display counts of user types
                print(f" -{user_type}: {count}")
    except Exception as e:
        print(f" Error during calculation of user_type")
    try:
        # Distribution by Gender Stats
        gender_col = [c for c in df.columns if 'gender' in c.lower()]
        if gender_col:
            # TO DO: Display counts of gender
            print("\n Distribution by gender:")
            for gender, count in df[gender_col[0]].value_counts().items():
                print(f" -{gender}:{count}")
        else:
            print("\n Gender statistics for chosen city is not available")
    except Exception as e:
        print(f" Error during calculation of gender statistics!")
                  
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        birth_col = [c for c in df.columns if 'birth' in c.lower() or 'year' in
                     c.lower()]
        if birth_col:
            valid_birth_years = df[birth_col[0]].dropna()
            if not valid_birth_years.empty:
                print("\n Distribution by year of birth:")
                print(f" - oldest class: {int(valid_birth_years.min())}")
                print(f" - Youngest class: {int(valid_birth_years.max())}")
                print(f" - Modal class: {int(valid_birth_years.mode()[0])}")
        else:
            print("\n For the  chosen city are the data about gnder/birth year not \
                  available")
    except Exception as e:
        print(f" Error during calculation of birth day.")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):    
    
    """
   This function prompts the user if they want to see 5 lines of raw data.
    Args:
        (DataFrame) csv File of the city to be analyzed                
    Returns:       
    """     
    if df is None or df.empty:
        print("\nNo data available to display")
        return
    
    start_row=0
    total_rows = len(df)
    
    while start_row < total_rows:
        try:
            user_input = input("\nDo you like to see 5 rows of the raw data? (yes/no): ").strip().lower()
            if user_input in ['yes','y']:
                end_row = min(start_row + 5, total_rows)
                print(df.iloc[start_row:end_row])
                start_row += 5
            elif user_input in ['no','n']:
                print("Presentation of raw data finished.")
                break
            else:
                print("Invalid input. Please enter 'yes or 'no.'")
        except (keyboardInterrupt,EOFError):
            print("\n Input is interrupted")
            break
    if start_row >= total_rows:
        print("\n No further raw data available to display.")
    
def main():
    """
    This function is the main entry points and coordinates the function calls as well
     as user input interfaces.
    
    Args:
                      
    Returns:       
    """
    while True:
        try:
            city, month, day = get_filters()
            df = load_data(city, month, day)
            
            if df is not None:
                if not df.empty:
                    time_stats(df)
                    station_stats(df)
                    trip_duration_stats(df)
                    user_stats(df)
                    display_raw_data(df)
                else:
                    print("\n Die Filterung ergab keine Treffer für diesen Zeitraum.")
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() not in ['yes','y']:
                print("\n\n user says no!. Ciao!")
                break
        except (KeyboardInterrupt,EOFError):
            print("\n\n Program was interrupetd by user. Ciao!")
            break
        except Exception as e:
            print(f"\n Error occured in main becaose of wrong input:{e}")
            restart = input('\nWould you like to restart? Enter yes or no:\n')
           # if restart.lower() != 'yes':
                #print("\n\n Program was interrupetd by user. Ciao!")  
                # break
            
            if restart.lower() not in ['yes','y']:
               
                print("\n\n Program was interrupetd by user. Ciao!") 
                break            
                 

if __name__ == "__main__":
	main()
