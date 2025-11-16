from flask import Flask, request, render_template_string

app = Flask(name) OWNER = "Arshia"

INDEX_HTML = ''' <!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Message for Fatemeh</title>
  <style>
    body{font-family:system-ui,Segoe UI,Roboto,Helvetica,Arial;display:flex;min-height:100vh;align-items:center;justify-content:center;background:#0f172a;color:#e6edf3;margin:0}
    .card{width:92%;max-width:720px;background:linear-gradient(180deg,#081126 0%,#071025 100%);padding:28px;border-radius:14px;box-shadow:0 10px 30px rgba(2,6,23,.6)}
    h1{margin:0 0 8px;font-size:22px}
    p{margin:6px 0 14px;line-height:1.45}
    label{display:block;margin-top:8px;font-size:13px;color:#9fb0d6}
    input[type=text]{width:100%;padding:10px;border-radius:8px;border:1px solid rgba(255,255,255,.06);background:rgba(255,255,255,.02);color:inherit}
    .btn{display:inline-block;margin-top:12px;padding:10px 14px;border-radius:10px;border:0;background:#7c3aed;color:white;cursor:pointer}
    .error{color:#ff7b7b;margin-top:10px}
  </style>
</head>
<body>
  <div class="card">
    <h1>Hello 👋</h1>
    <p>This small page is a birthday surprise prepared by {{ owner }}. Please enter your name to continue.</p><form method="post" action="/check">
  <label for="name">Your name</label>
  <input id="name" name="name" type="text" autocomplete="off" required>
  <button class="btn" type="submit">Open</button>
</form>

{% if error %}
  <div class="error">{{ error }}</div>
{% endif %}

  </div>
</body>
</html>
'''ACCESS_HTML = ''' <!doctype html>

<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Welcome</title>
<style>
  body{font-family:system-ui,Segoe UI,Roboto,Helvetica,Arial, sans-serif;background:#071022;color:#e6edf3;display:flex;align-items:center;justify-content:center;min-height:100vh;margin:0}
  .box{width:94%;max-width:820px;padding:28px;border-radius:12px;background:linear-gradient(180deg,#07102a,#041021);box-shadow:0 14px 40px rgba(2,6,23,.6)}
  h2{margin:0 0 8px}
  p{margin:6px 0 12px}
  .cake{white-space:pre;font-family:monospace;background:linear-gradient(90deg,#071022,#06182b);padding:12px;border-radius:8px}
  .action{margin-top:10px}
  .btn{padding:10px 14px;border-radius:10px;border:0;background:#06b6d4;color:#062024;cursor:pointer}
</style>
</head>
<body>
  <div class="box">
    <h2>Welcome, {{ visitor }}</h2>
    <p>You're the one who unlocked this. A small message from {{ owner }}:</p>
    <div class="cake">{{ message_block }}</div>
    <div class="action">
      <form method="get" action="/blow">
        <button class="btn">Blow out the candles</button>
      </form>
    </div>
  </div>
</body>
</html>
'''FINAL_HTML = ''' <!doctype html>

<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Happy Birthday</title>
<style>
  body{font-family:system-ui,Segoe UI,Roboto,Helvetica,Arial;background:#061227;color:#eaf6ff;display:flex;align-items:center;justify-content:center;min-height:100vh;margin:0}
  .wrap{width:94%;max-width:820px;padding:28px;border-radius:12px;background:linear-gradient(180deg,#051022,#041020);box-shadow:0 12px 36px rgba(2,6,23,.6)}
  h1{margin:0 0 6px}
  p{margin:6px 0 12px}
  .cake{white-space:pre;font-family:monospace;margin-top:10px}
</style>
</head>
<body>
  <div class="wrap">
    <h1>Happy Birthday, {{ visitor }} 🎉</h1>
    <p>Hope your day is relaxed, fun, and full of small lovely moments. Best wishes from {{ owner }}.</p>
    <div class="cake">{{ small_cake }}</div>
  </div>
</body>
</html>
'''SMALL_CAKE = """ , , , (|/) -*- (|/) | |  ==  HAPPY BIRTHDAY == (___) """

MESSAGE_BLOCK = ( "Dear Fatemeh,

" "Wishing you a relaxed and joyful birthday. I hope the year ahead brings you good moments, " "new experiences, and people who make you smile. Enjoy your day!

" "— Arshia" )

@app.route('/', methods=['GET']) def index(): return render_template_string(INDEX_HTML, owner=OWNER, error=None)

@app.route('/check', methods=['POST']) def check(): name = (request.form.get('name') or '').strip() if name.lower() != 'fatemeh': return render_template_string(INDEX_HTML, owner=OWNER, error='This page is not for you.') return render_template_string(ACCESS_HTML, visitor=name, owner=OWNER, message_block=MESSAGE_BLOCK)

@app.route('/blow', methods=['GET']) def blow(): return render_template_string(FINAL_HTML, visitor='Fatemeh', owner=OWNER, small_cake=SMALL_CAKE)

if name == 'main': app.run(host='0.0.0.0', port=8000)
