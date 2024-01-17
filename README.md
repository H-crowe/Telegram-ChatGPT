# ChatGPT Telegram Bot

A simple powerful Telegram bot that engages users in interactive conversations using OpenAI's ChatGPT language model.

# Features

- **Interactive Conversations:** Engage in natural language conversations with the bot.
- **Menu Commands:**
  - `/start`: Display a welcome message and menu.
  - `/help`: Provide information about the bot.
  - `/restart`: Restart the conversation.
  - 
![لقطة الشاشة 2024-01-18 005413](https://github.com/H-crowe/Telegram-ChatGPT/assets/142697834/916b1639-e011-4c17-97b3-95238be72f15)


# Getting Started

1. **Telegram Bot Token:** Obtain a Telegram Bot Token from [BotFather](https://core.telegram.org/bots#botfather).

2. **OpenAI API Key:** Get an API key from the [OpenAI Platform](https://beta.openai.com/signup/).

# Configuration

1. `config.json` file in the project directory:

    ```json
    {
      "TELEGRAM_BOT_TOKEN": "your_telegram_bot_token_here",
      "OPENAI_API_KEY": "your_openai_api_key_here"
    }
    ```

    Replace placeholder values with your actual Telegram bot token and OpenAI API key.

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/H-crowe/Telegram-ChatGPT.git
    cd Telegram-ChatGPT
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

# Usage

1. **Run the bot:**

    ```bash
    python bot.py
    ```

2. **Interact with the bot on Telegram.**

## Additional Customization

Feel free to customize the bot by adding features, improving conversation handling, or enhancing error messages. The code is designed to be extensible and adaptable to your specific needs.

## Contributing

Contributions are welcome! If you have suggestions, feature requests, or bug reports, please create an issue or submit a pull request. Check the [CONTRIBUTING.md](CONTRIBUTING.md) file for more details.

---

Contact
If you have questions or need assistance, feel free to contact Telegram @cr0wel .
