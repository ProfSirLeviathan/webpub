# Smart EPUB Web Viewer

A lightweight, local, Python-based web app that allows you to read EPUB files in your favorite browser. Built with a focus on a clean UI, seamless Edge "Read Aloud" compatibility, and a frictionless experience.

## Features

- **Native File Picker:** Select any `.epub` from your file system using a native dialog.
- **Edge "Read Aloud" Support 🌐:** Bypasses standard iframe limitations so you can use Edge's high-quality natural voices.
- **Dark Mode 🌙:** Easy on the eyes, toggled on by default.
- **Custom Scrollbars & UI:** Minimal distracting elements, smooth vertical scrolling, and clean chapter navigation.
- **Custom TTS Fallback:** A built-in Web Speech API voice fallback for other browsers.
- **Text Alignment Settings:** Instantly switch between Left, Center, and Justify alignment.
- **Dynamic Server:** Safely finds an available port automatically to avoid "address in use" errors.

## How to Run

Ensure you have Python installed on your system.
No external pip dependencies are strictly required for the backend since it uses standard libraries! (The frontend uses a CDN to fetch `epub.js`).

1. Download or clone this repository.
2. Run the main script:
   ```bash
   python main.py
   ```
3. A file picker will prompt you to select an EPUB file.
4. Your default browser will automatically open and serve the book!

## Technologies used
- Python (http.server, tkinter)
- HTML/CSS/JavaScript
- [epub.js](https://github.com/futurepress/epub.js/)
