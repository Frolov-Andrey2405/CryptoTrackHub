# CryptoTrackHub

CryptoTrackHub is a Python program that allows users to track cryptocurrency prices and set up alerts for specific price thresholds. It comes with a user-friendly web interface built using PyWebIO.

## Detailed description

CryptoTrackHub provides a simple way to monitor cryptocurrency prices and receive alerts when they reach certain levels. The program fetches real-time cryptocurrency prices from the Coinranking website and allows users to add coins to their watchlist. When the price of a tracked coin falls below the user-set threshold, the program triggers an alert and removes the coin from the watchlist.

The program consists of three main components:

- **main.py**: The entry point of the program, responsible for starting a thread to check coin balances and interacting with the user through a web interface.
- **menu.py**: Contains the TaskHandler class, which handles tasks such as adding, listing, and deleting coins from the watchlist. It also includes functions for reading and updating the task file.
- **parser.py**: Includes functions to fetch cryptocurrency prices from the Coinranking website and a loop to check for coin price alerts.

## Features

- **Real-time Price Tracking**: Utilizes web scraping to fetch real-time cryptocurrency prices.
- **User-friendly Interface**: Offers a simple and interactive web interface using PyWebIO.
- **Alert System**: Notifies users when a tracked cryptocurrency's price falls below the set threshold.
- **Task Management**: Allows users to add, list, and delete tasks (coins) from their watchlist.

## Preview

![Preview](/data/Preview.jpeg)
