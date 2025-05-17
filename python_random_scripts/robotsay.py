import webbrowser
import tempfile
import os

def generate_robot_html(message: str) -> str:
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <title>Robot Says</title>
      <style>
        body {{
          font-family: 'Courier New', Courier, monospace;
          background: #121212;
          color: #eee;
          display: flex;
          justify-content: center;
          align-items: center;
          height: 100vh;
          margin: 0;
          flex-direction: column;
        }}
        .speech-bubble {{
          background: #00bcd4;
          border-radius: 15px;
          padding: 15px 25px;
          max-width: 400px;
          position: relative;
          font-size: 1.3rem;
          line-height: 1.4;
          margin-bottom: 40px;
          color: #121212;
          box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }}
        .speech-bubble::after {{
          content: '';
          position: absolute;
          bottom: -20px;
          left: 40px;
          width: 0;
          height: 0;
          border: 15px solid transparent;
          border-top-color: #00bcd4;
          border-bottom: 0;
          margin-left: -15px;
          margin-bottom: -15px;
        }}
        .robot {{
          font-size: 6rem;
          user-select: none;
          filter: drop-shadow(0 0 5px #00bcd4);
        }}
      </style>
    </head>
    <body>
      <div class="speech-bubble">{message}</div>
      <div class="robot">🤖</div>
    </body>
    </html>
    """
    return html_content

def open_robot_say(message: str):
    html = generate_robot_html(message)
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html', encoding='utf-8') as f:
        f.write(html)
        temp_file_path = f.name
    
    webbrowser.open_new('file://' + os.path.abspath(temp_file_path))

if __name__ == "__main__":
    msg = input("What should the robot say? ")
    open_robot_say(msg)
