import http.server
import socketserver
import webbrowser
import tkinter as tk
from tkinter import filedialog
import os
import sys
import threading

def main():
    
    root = tk.Tk()
    root.withdraw() 
    
    print("Please select an EPUB file from the dialog...")
    root.attributes("-topmost", True)
    file_path = filedialog.askopenfilename(
        title="Select an EPUB file to view",
        filetypes=[("EPUB files", "*.epub"), ("All files", "*.*")]
    )
    root.destroy()

    if not file_path:
        print("No file selected. Exiting.")
        sys.exit(0)

    print(f"Selected: {file_path}")
    
    class EpubWebHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            # Serve our custom viewer HTML for the root path
            if self.path == '/':
                self.path = '/viewer.html'
            
            # Intercept the request for the EPUB and serve the selected file directly
            if self.path == '/book.epub':
                try:
                    with open(file_path, 'rb') as f:
                        self.send_response(200)
                        self.send_header("Content-type", "application/epub+zip")
                        self.end_headers()
                        self.wfile.write(f.read())
                except Exception as e:
                    self.send_error(500, f"Error reading file: {e}")
                return

            if self.path == '/shutdown':
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Server shutting down...")
                
               
                def kill_server():
                    self.server.shutdown()
                threading.Thread(target=kill_server, daemon=True).start()
                return
            
            return super().do_GET()


    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    socketserver.TCPServer.allow_reuse_address = True

   
    try:
        with socketserver.TCPServer(("", 0), EpubWebHandler) as httpd:
            PORT = httpd.server_address[1]
            print(f"Serving at http://localhost:{PORT}")
            print("Opening browser...")
            webbrowser.open(f"http://localhost:{PORT}")
            httpd.serve_forever()
    except OSError as e:
        print(f"Error starting server: {e}")

if __name__ == "__main__":
    main()
