from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
import webbrowser,threading,os
PORT=8080
os.chdir(os.path.dirname(os.path.abspath(__file__)))
threading.Timer(.8,lambda:webbrowser.open(f"http://127.0.0.1:{PORT}")).start()
print(f"RSQ Plumbing website running at http://127.0.0.1:{PORT}")
ThreadingHTTPServer(("0.0.0.0",PORT),SimpleHTTPRequestHandler).serve_forever()
