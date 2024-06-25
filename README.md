# Web Server Project

## Overview
This project is a simple web server implemented using Python's socket programming. The server handles one HTTP request at a time and demonstrates the basics of TCP connections and HTTP packet handling.

## Features
- Accepts and parses HTTP requests.
- Retrieves the requested file from the server’s file system.
- Creates and sends an HTTP response message with the requested file preceded by header lines.
- Sends a "404 Not Found" message if the requested file is not found.

## Setup and Running the Server
1. **Place an HTML file** in the same directory as the server script.
2. **Run the server program**:
   ```sh
   python web_server.py
