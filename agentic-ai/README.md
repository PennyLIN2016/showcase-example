# Agentic Agent Project

## Overview
The Agentic Agent project is a web-based application that allows users to interact with a chatbot powered by a FastAPI backend and OpenAI's language model. The application connects to an external MCP server for additional functionalities and supports user prompts for enhanced interaction.

## Project Structure
```
agentic-agent
├── backend
│   ├── app
│   │   ├── main.py
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   ├── services
│   │   │   ├── mcp_client.py
│   │   │   ├── openai_client.py
│   │   │   └── prompt_manager.py
│   │   ├── models
│   │   │   └── agent_state.py
│   │   ├── schemas
│   │   │   └── request.py
│   │   ├── core
│   │   │   ├── config.py
│   │   │   └── logger.py
│   │   └── workers
│   │       └── agent_runner.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
├── web-ui
│   ├── package.json
│   ├── vite.config.js
│   ├── public
│   │   └── index.html
│   └── src
│       ├── main.js
│       ├── App.js
│       ├── components
│       │   ├── ChatWindow.js
│       │   ├── MessageList.js
│       │   └── MessageInput.js
│       ├── services
│       │   └── api.js
│       └── styles
│           └── main.css
├── docker-compose.yml
├── .gitignore
└── README.md
```

## Backend
The backend is built using FastAPI and serves as the main API for handling user requests and responses. It includes various services for interacting with the MCP server and OpenAI.

### Key Files
- `main.py`: Entry point for the FastAPI application.
- `routes.py`: Defines API endpoints for user interaction.
- `mcp_client.py`: Handles communication with the MCP server.
- `openai_client.py`: Interfaces with the OpenAI API.
- `prompt_manager.py`: Manages prompts for LLM thinking.

## Web UI
The web UI is built using JavaScript and provides an interface for users to interact with the chatbot. It allows users to input questions and view responses.

### Key Files
- `index.html`: Main HTML file for the web application.
- `App.js`: Main application component.
- `ChatWindow.js`: Displays the chat interface.
- `MessageInput.js`: Allows users to input their questions.

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd agentic-agent
   ```

2. Set up the backend:
   - Navigate to the `backend` directory.
   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Configure environment variables in `.env` based on `.env.example`.

3. Run the backend:
   ```
   uvicorn app.main:app --reload
   ```

4. Set up the web UI:
   - Navigate to the `web-ui` directory.
   - Install dependencies:
     ```
     npm install
     ```
   - Start the development server:
     ```
     npm run dev
     ```

5. Access the application at `http://localhost:3000`.

## Usage
Once the application is running, users can input their questions in the chat interface, and the chatbot will respond using the integrated LLM and MCP functionalities.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.