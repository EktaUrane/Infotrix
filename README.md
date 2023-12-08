
# Weather Checking App
**Description:**

This project is your quick and efficient solution for up-to-date weather information. Get instant access to real-time weather updates, forecasts, and conditions. Stay informed about the weather in multiple locations with ease. It is designed for simplicity, providing you with the essential information you need without any fuss.


## Installation

Install requests with pip

```powershell
  pip install requests
```
## Documentation
 After running the project you would be given 6 choices, which are as follows:
 ```powershell
**Please select an option from the given menu**
Menu:
1. Check Weather by City
2. Add to Favorite List
3. Remove from Favorite List
4. Display Favorite List
5. Auto Refresh Favorite List
6. Exit
Enter your choice (1-6):
```
### 1. Check Weather by City
By entering the city name of your choice you can view important weather details of the chosen city in real-time. for e.g.
```powershell
Enter your choice(1-6): 1
Enter the city name: mumbai
```
OUTPUT:
```powershell   
************ Weather information of mumbai City ************
        Temperature in mumbai: 31.99°C or 89.58°F
        Temperature in mumbai feels_like: 32.82°C or 91.08°F
        Humidity in mumbai: 43%
        Wind speed in mumbai: 4.12m/s
        General Weather in mumbai: smoke

        ************ ////////////////\\\\\\\\\ ************
```

### 2. Add to Favorite List
In this command, by entering the city name you can add the city to your favorite list. For e.g 
```powershell
Enter the city name to add to the favorite list: kolhapur
```
OUTPUT
```powershell
kolhapur added to the favorite list.
```
### 3. Remove From Favorite List 
By using this command, one can remove the city added to the favorite city list. For e.g
```powershell
Enter the city name to remove from the favorite list: kolhapur
```
OUTPUT
```powershell
kolhapur removed from the favorite list.
```
### 4. Display Favorite List
By using this command, one can retrieve the favorite list of cities.
```powershell
*******Favorite Cities******* 
Mumbai
```
### 5. Auto Refresh Favorite List
The Refresh command refreshes the cities added to the favorite list.
```powershell
Enter auto-refresh interval in seconds (15-30): 15
```
OUTPUT
```powershell
******** Weather information for pune ********

        ************ Weather information of pune City ************
        Temperature in pune: 24.85°C or 76.73°F
        Temperature in pune feels_like: 24.96°C or 76.93°F
        Humidity in pune: 60%
        Wind speed in pune: 3.07m/s
        General Weather in pune: overcast clouds

        ************ ////////////////\\\\\\\\\\\\\ ************
```
### 6. Exit
Using the exit command exits the program.
```powershell
You have chosen to exit the program. Goodbye!