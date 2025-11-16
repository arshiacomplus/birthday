from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)
OWNER = "Arshia"

MESSAGES = {
    "fatemeh": {
        "name": "Fatemeh",
        "message": """Happy Birthday, Fatemeh 🥳
        
It's been so great getting to know you in our class. You're a wonderful friend. 
I hope you have an amazing day and a fantastic year ahead, full of happiness, health, and success!
        
Best wishes,
— Arshia"""
    },
    "mohammad_hassan": {
        "name": "Mohammad Hassan",
        "message": """Happy Birthday, Mohammad Hassan 🎉
        
Man, it's been fun having you in class all this time. You're a great guy! 
Wishing you a very happy birthday and an awesome year. Hope it's filled with good times and new achievements.
        
Cheers,
— Arshia"""
    }
}

LOGIN_HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>A Message For You</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Poppins', sans-serif;
      display: flex;
      min-height: 100vh;
      align-items: center;
      justify-content: center;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%);
      background-size: 400% 400%;
      animation: gradientShift 15s ease infinite;
      color: #fff;
      position: relative;
      overflow: hidden;
    }
    @keyframes gradientShift {
      0%, 100% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
    }
    .confetti { position: absolute; width: 10px; height: 10px; background: #f0f; opacity: 0.7; animation: fall linear infinite; }
    @keyframes fall { to { transform: translateY(100vh) rotate(360deg); } }
    .card {
      width: 92%;
      max-width: 480px;
      background: rgba(255, 255, 255, 0.95);
      padding: 40px 32px;
      border-radius: 24px;
      box-shadow: 0 20px 60px rgba(0,0,0,0.3);
      animation: fadeInUp 0.8s ease-out;
      backdrop-filter: blur(20px);
      border: 2px solid rgba(255,255,255,0.3);
    }
    @keyframes fadeInUp { 
      from { opacity: 0; transform: translateY(40px) scale(0.95); } 
      to { opacity: 1; transform: translateY(0) scale(1); } 
    }
    h1 {
      margin: 0 0 12px;
      font-size: 32px;
      font-weight: 700;
      background: linear-gradient(135deg, #667eea, #764ba2);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      text-align: center;
    }
    p {
      margin: 6px 0 24px;
      line-height: 1.6;
      color: #555;
      text-align: center;
      font-size: 15px;
    }
    label {
      display: block;
      margin-top: 12px;
      font-size: 14px;
      color: #666;
      font-weight: 600;
    }
    input[type=text] {
      width: 100%;
      padding: 14px 16px;
      border-radius: 12px;
      border: 2px solid #e0e0e0;
      background: #fff;
      color: #333;
      font-size: 15px;
      font-family: 'Poppins', sans-serif;
      transition: all 0.3s;
    }
    input[type=text]:focus {
      outline: none;
      border-color: #667eea;
      box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
    }
    .btn {
      display: block;
      width: 100%;
      margin-top: 20px;
      padding: 14px;
      border-radius: 12px;
      border: 0;
      background: linear-gradient(135deg, #667eea, #764ba2);
      color: white;
      cursor: pointer;
      font-size: 16px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.3s;
      font-family: 'Poppins', sans-serif;
      box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    .btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    .btn:active {
      transform: translateY(0);
    }
    .error {
      color: #e74c3c;
      margin-top: 16px;
      font-size: 14px;
      text-align: center;
      font-weight: 500;
    }
    .emoji { font-size: 48px; text-align: center; margin-bottom: 16px; animation: bounce 2s infinite; }
    @keyframes bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
  </style>
</head>
<body>
  <div class="card">
    <div class="emoji">🎁</div>
    <h1>Hello 👋</h1>
    <p>This is a small birthday surprise prepared by {{ owner }}. Please enter your first-name to continue.</p>
    <form method="post" action="/greet">
      <label for="name">Your name:</label>
      <input id="name" name="name" type="text" autocomplete="off" required>
      <button class="btn" type="submit">Open Your Gift 🎉</button>
    </form>
    {% if error %}
      <div class="error">{{ error }}</div>
    {% endif %}
  </div>
  <script>
    for(let i=0;i<30;i++){
      const c=document.createElement('div');
      c.className='confetti';
      c.style.left=Math.random()*100+'%';
      c.style.background=['#ff6b6b','#4ecdc4','#ffe66d','#a8e6cf','#ffd3b6'][Math.floor(Math.random()*5)];
      c.style.animationDuration=(Math.random()*3+2)+'s';
      c.style.animationDelay=Math.random()*5+'s';
      document.body.appendChild(c);
    }
  </script>
</body>
</html>
"""

GREET_HTML = """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Happy Birthday</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    padding: 20px;
    position: relative;
    overflow-x: hidden;
  }
  @keyframes gradientShift {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
  }
  .balloon { position: absolute; font-size: 3rem; animation: float 6s ease-in-out infinite; }
  @keyframes float { 0%, 100% { transform: translateY(0) rotate(0deg); } 50% { transform: translateY(-30px) rotate(10deg); } }
  .box {
    width: 94%;
    max-width: 720px;
    padding: 40px;
    border-radius: 24px;
    background: rgba(255, 255, 255, 0.95);
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    animation: fadeInUp 0.8s ease-out;
    backdrop-filter: blur(20px);
    border: 2px solid rgba(255,255,255,0.3);
  }
  @keyframes fadeInUp { 
    from { opacity: 0; transform: translateY(40px) scale(0.95); } 
    to { opacity: 1; transform: translateY(0) scale(1); } 
  }
  h2 {
    margin: 0 0 12px;
    font-size: 32px;
    font-weight: 700;
    background: linear-gradient(135deg, #667eea, #764ba2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
  }
  p {
    margin: 6px 0 20px;
    line-height: 1.6;
    color: #555;
    text-align: center;
    font-size: 15px;
  }
  .message-block {
    white-space: pre-wrap;
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(118,75,162,0.1));
    padding: 24px;
    border-radius: 16px;
    font-size: 15px;
    line-height: 1.8;
    color: #333;
    border: 2px solid rgba(102,126,234,0.2);
    min-height: 150px;
  }
  .cake-area {
    text-align: center;
    margin: 30px 0 20px;
  }
  .cake { font-size: 7rem; animation: cakeBounce 2s infinite; }
  @keyframes cakeBounce { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }
  .candles {
    font-size: 3.5rem;
    letter-spacing: 8px;
    margin-top: -25px;
    animation: flicker 1.5s infinite alternate;
  }
  @keyframes flicker { 0% { opacity: 1; } 100% { opacity: 0.8; } }
  .action {
    margin-top: 30px;
    text-align: center;
  }
  .btn {
    display: inline-block;
    padding: 16px 32px;
    border-radius: 16px;
    border: 0;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    cursor: pointer;
    font-size: 16px;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.3s;
    font-family: 'Poppins', sans-serif;
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
  }
  .btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
  }
  .btn:active {
    transform: translateY(0);
  }
</style>
</head>
<body>
  <div class="balloon" style="top:10%;left:5%;animation-delay:0s;">🎈</div>
  <div class="balloon" style="top:20%;right:8%;animation-delay:1s;">🎈</div>
  <div class="balloon" style="bottom:15%;left:10%;animation-delay:2s;">🎈</div>
  <div class="balloon" style="bottom:25%;right:5%;animation-delay:1.5s;">🎈</div>
  
  <div class="box">
    <h2>Happy Birthday, {{ name }} 🎊</h2>
    <p>A special message from {{ owner }}:</p>
    <div id="message-block" class="message-block"></div>
    
    <div class="cake-area">
      <div class="candles">🕯️🕯️🕯️</div>
      <div class="cake">🎂</div>
    </div>
    
    <div class="action">
      <a href="{{ url_for('finale', name=name) }}" class="btn">Make a wish and blow out the candles! 🎉</a>
    </div>
  </div>
  
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const message = `{{ message }}`;
      const messageBlock = document.getElementById('message-block');
      let i = 0;
      function typeWriter() {
        if (i < message.length) {
          messageBlock.innerHTML += message.charAt(i);
          i++;
          setTimeout(typeWriter, 40);
        }
      }
      typeWriter();
    });
  </script>
</body>
</html>
"""

FINAL_HTML = """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Wishes</title>
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    text-align: center;
    padding: 20px;
  }
  @keyframes gradientShift {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
  }
  .wrap {
    width: 94%;
    max-width: 720px;
    padding: 50px 40px;
    border-radius: 24px;
    background: rgba(255, 255, 255, 0.95);
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    animation: fadeInScale 1s ease-out;
    backdrop-filter: blur(20px);
    border: 2px solid rgba(255,255,255,0.3);
  }
  @keyframes fadeInScale { 
    from { opacity: 0; transform: scale(0.8) rotate(-5deg); } 
    to { opacity: 1; transform: scale(1) rotate(0deg); } 
  }
  h1 {
    margin: 0 0 12px;
    font-size: 38px;
    font-weight: 700;
    background: linear-gradient(135deg, #667eea, #764ba2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: titlePulse 2s infinite;
  }
  @keyframes titlePulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }
  p {
    margin: 6px 0 20px;
    font-size: 20px;
    color: #555;
    font-weight: 500;
  }
  .cake {
    font-size: 8rem;
    margin-top: 20px;
    animation: cakeSpin 3s ease-in-out infinite;
  }
  @keyframes cakeSpin { 
    0%, 100% { transform: rotate(0deg) scale(1); } 
    25% { transform: rotate(-10deg) scale(1.1); }
    75% { transform: rotate(10deg) scale(1.1); }
  }
</style>
</head>
<body>
  <div class="wrap">
    <h1>Happy Birthday, {{ name }} 🎉</h1>
    <p>All the best wishes from {{ owner }}.</p>
    <div class="cake">🎂</div>
  </div>
  
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      function shootConfetti() {
        confetti({
          particleCount: 200,
          spread: 120,
          origin: { y: 0.5 },
          colors: ['#667eea', '#764ba2', '#f093fb', '#4facfe', '#00f2fe', '#ff6b6b', '#ffe66d']
        });
      }
      
      shootConfetti();
      setTimeout(shootConfetti, 400);
      setTimeout(shootConfetti, 800);
      
      setInterval(function() {
        confetti({
          particleCount: 3,
          angle: 60,
          spread: 55,
          origin: { x: 0 },
          colors: ['#667eea', '#764ba2', '#f093fb']
        });
        confetti({
          particleCount: 3,
          angle: 120,
          spread: 55,
          origin: { x: 1 },
          colors: ['#4facfe', '#00f2fe', '#ff6b6b']
        });
      }, 250);
    });
  </script>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    """Shows the login page."""
    error = request.args.get('error')
    return render_template_string(LOGIN_HTML, owner=OWNER, error=error)

@app.route('/greet', methods=['POST'])
def greet():
    """Handles the name check and shows the greeting page."""
    name = (request.form.get('name') or '').strip()
    normalized_name = name.lower()

    person_key = None

    if normalized_name in ['fatemeh', 'فاطمه']:
        person_key = 'fatemeh'
    elif normalized_name in ['mohammad hassan', 'محمد حسن']:
        person_key = 'mohammad_hassan'
        
    if person_key:
        person_data = MESSAGES[person_key]
        return render_template_string(
            GREET_HTML, 
            name=person_data['name'], 
            message=person_data['message'], 
            owner=OWNER
        )
    else:
        error_msg = "This page isn't for you 😏🤔"
        return redirect(url_for('index', error=error_msg))

@app.route('/finale')
def finale():
    """Shows the final page with confetti."""
    name = request.args.get('name', 'Friend')
    return render_template_string(FINAL_HTML, name=name, owner=OWNER)

if __name__ == '__main__':
    # This block is for LOCAL TESTING only.
    # PythonAnywhere and Serv00 will IGNORE this.
    app.run(host='0.0.0.0', port=8000, debug=True)
