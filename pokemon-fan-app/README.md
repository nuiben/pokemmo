# Pokémon Fan App

Welcome to the Pokémon Fan App! This application allows trainers to log in, catch Pokémon from a daily region, and build a roster and party to challenge other trainers for rewards.

## Features

- **User Authentication**: Trainers can log in and manage their sessions.
- **Catch Pokémon**: Trainers can catch Pokémon from a daily region using the PokeAPI.
- **Roster Management**: Trainers can build and manage their Pokémon roster.
- **Trainer Challenges**: Trainers can challenge others and earn rewards.

## Project Structure

```
pokemon-fan-app
├── src
│   ├── main.py                # Entry point of the application
│   ├── api
│   │   └── pokeapi_client.py  # Handles interactions with the PokeAPI
│   ├── auth
│   │   └── login.py           # Manages user authentication
│   ├── models
│   │   ├── trainer.py         # Represents a Pokémon trainer
│   │   ├── pokemon.py         # Represents a Pokémon
│   │   └── roster.py          # Manages a collection of Pokémon
│   ├── routes
│   │   ├── catch.py           # Allows trainers to catch Pokémon
│   │   ├── challenge.py       # Allows trainers to challenge others
│   │   └── region.py          # Retrieves the current daily region
│   └── utils
│       └── helpers.py         # Utility functions for the application
├── requirements.txt            # Lists project dependencies
└── README.md                   # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/pokemon-fan-app.git
   ```
2. Navigate to the project directory:
   ```
   cd pokemon-fan-app
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/main.py
   ```
2. Follow the on-screen instructions to log in, catch Pokémon, and challenge other trainers.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.