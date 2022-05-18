# Python 3, program to print a list of all pairs of players
# whose height in inches adds up to the integer input to the application. If no
# matches are found, the application will print "No matches found"

import requests
import json

menu_options = {
    1: 'Calculate pairs',
    2: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

"""
get_height: this function return srt value regading to its key 'h_in' 
"""
def get_height(player):
    return player.get('h_in')


"""
get_API: this function fetch the players from API
"""
def get_API():
    response_API = requests.get('https://mach-eight.uc.r.appspot.com')
    #print(response_API.status_code)
    response_json = response_API.json()
    players = response_json["values"]
    #print(players)
    # Sorting the list players by key 'h_in' ascending
    players.sort(key = get_height)
    #print(players)
    
    return players

"""
get_pairs: this function recieve as params the players sorted and the sum objective adds up.
"""
def get_pairs(players, sum):
     
    # Store the coincidences of every height in a dict
    mydict = dict()
    # Number of players
    number_players = len(players) - 1
    # Checking the total pairs
    pairs=0
 
    # Loop of players
    for i in range(number_players):

        h_in = int(players[i]['h_in'])
        # Looking for the next pair
        temp = sum - h_in

        # If the temp value exists in my dict I need to loop it
        if temp in mydict:
            # How many counts I have per height
            count = mydict[temp]
            for j in range(count):
                print("- ",players[j]['first_name'],players[j]['last_name'], 'Height:' , players[j]['h_in'],
                      '     '
                      ,players[i]['first_name'],players[i]['last_name'], 'Height:' , players[i]['h_in'],sep = " ", end = '\n')
                pairs +=1

        # If my height exists in my dict increment in 1 its value, else I add it.
        if h_in in mydict:
            mydict[h_in] += 1
        else:
            mydict[h_in] = 1
            
    # The dict with total appers for every height
    #print(mydict)
    # Total pairs you can build
    print('Total pairs found: ',pairs)
    if pairs == 0:
        print('No matches found')

def menu():
    return int(input("""Input a number: (Type exit to Exit)
    Selection: """))

# Main
if __name__ == '__main__':

    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           try:
               sum_pairs = int(input("Enter number to finds pairs please: "))
               get_pairs(get_API(), sum_pairs)
           except:
                print('Wrong input. Please enter a number ...')
        elif option == 2:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 2.')
