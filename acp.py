# Demo: https://arshiastest.pythonanywhere.com
# It can be deployed on "PythonAnywhere" and "Serv00".
from flask import Flask, request, render_template_string, redirect, url_for


class PrefixMiddleware(object):
    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):
        environ['SCRIPT_NAME'] = self.prefix
        return self.app(environ, start_response)

app = Flask(__name__)
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/birthday-acp')
OWNER = "Arshia"
MESSAGES = {
    "fatemeh": {
        "name": "Fatemeh",
        "message": """Happy Birthday, Fatemeh 🥳
It's been so great getting to know you in our class. You're a wonderful friend.
I hope you have an amazing day and a fantastic year ahead, full of happiness, health, and success ✨💛""",
    },
    "mohammad_hassan": {
        "name": "Mohammad Hassan",
        "message": """Happy Birthday, Mohammad Hassan 🎉
Man, it's been fun having you in class all this time. You're a great guy.
Wishing you a very happy birthday and an awesome year. Hope it's filled with good times and new achievements.
Cheers 🤍🍻""",
    },
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
      background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 25%, #ff9a9e 50%, #fad0c4 75%, #ffd1ff 100%);
      background-size: 400% 400%;
      animation: gradientShift 15s ease infinite;
      color: #fff;
      position: relative;
      overflow: hidden;
      padding: 16px;
    }
    @keyframes gradientShift {
      0%, 100% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
    }
    .confetti { position: absolute; width: 10px; height: 10px; background: #f0f; opacity: 0.8; animation: fall linear infinite; top: 0; pointer-events: none; }
    @keyframes fall {
    from { transform: translateY(0) rotate(0deg); }
    to { transform: translateY(100vh) rotate(720deg); }
    }
    .card {
      width: 100%;
      max-width: 400px;
      background: rgba(255, 255, 255, 0.95);
      padding: 32px 24px;
      border-radius: 20px;
      box-shadow: 0 15px 40px rgba(0,0,0,0.2);
      backdrop-filter: blur(20px);
      border: 2px solid rgba(255,255,255,0.3);
    }
    @keyframes fadeInUp {
      from { opacity: 0; transform: translateY(40px) scale(0.95); }
      to { opacity: 1; transform: translateY(0) scale(1); }
    }
    h1 {
      margin: 0 0 10px;
      font-size: 26px;
      font-weight: 700;
      background: linear-gradient(135deg, #ff9a9e, #fad0c4);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      text-align: center;
    }
    p {
      margin: 0 0 20px;
      line-height: 1.5;
      color: #555;
      text-align: left;
      font-size: 14px;
    }
    label {
      display: block;
      margin-top: 8px;
      font-size: 13px;
      color: #666;
      font-weight: 600;
    }
    input[type=text] {
      width: 100%;
      padding: 12px 14px;
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
      border-color: #ff9a9e;
      box-shadow: 0 0 0 4px rgba(255, 154, 158, 0.1);
    }
    .btn {
      display: block;
      width: 100%;
      margin-top: 16px;
      padding: 13px;
      border-radius: 12px;
      border: 0;
      background: linear-gradient(135deg, #ff9a9e, #fad0c4);
      color: white;
      cursor: pointer;
      font-size: 15px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.3s;
      font-family: 'Poppins', sans-serif;
      box-shadow: 0 4px 15px rgba(255, 154, 158, 0.4);
    }
    .btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(255, 154, 158, 0.6);
    }
    .btn:active {
      transform: translateY(0);
    }
    .error {
      color: #e74c3c;
      margin-top: 14px;
      font-size: 13px;
      text-align: center;
      font-weight: 500;
    }
    .emoji { font-size: 42px; text-align: center; margin-bottom: 14px; animation: bounce 2s infinite; }
    @keyframes bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
  </style>
</head>
<body>
  <div class="card">
    <div class="emoji">🎁</div>
    <h1>Hello dear</h1>
    <p>This is a small birthday surprise prepared by {{ owner }}. Please enter your name to continue.</p>
    <form method="post" action="/birthday-acp/greet">
      <label for="name">Your name:</label>
      <input id="name" name="name" type="text" autocomplete="off" required>
      <button class="btn" type="submit">Open Your Gift 🎉</button>
    </form>
    {% if error %}
      <div class="error">{{ error }}</div>
    {% endif %}
  </div>
  <script>
    for(let i=0;i<70;i++){
      const c=document.createElement('div');
      c.className='confetti';
      c.style.left=Math.random()*100+'%';
      c.style.top = Math.random() * -20 + 'px';
      c.style.background=['#ff6b6b','#4ecdc4','#ffe66d','#a8e6cf','#ffd3b6'][Math.floor(Math.random()*5)];
      c.style.animationDuration=(Math.random()*4+3)+'s';
      c.style.animationDelay=Math.random()*3+'s';
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
  body { font-family: 'Poppins', sans-serif; background: linear-gradient(135deg, #ffecd2, #fcb69f, #ff9a9e, #fad0c4, #ffd1ff); background-size: 400% 400%; animation: gradientShift 15s ease infinite; color: #fff; display: flex; align-items: center; justify-content: center; min-height: 100vh; padding: 16px; position: relative; overflow-x: hidden; }
  @keyframes gradientShift { 0%, 100% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } }
  .balloon { position: absolute; font-size: 2.5rem; animation: float 6s ease-in-out infinite; opacity: 0; transition: opacity 1.5s ease-out; }
  @keyframes float { 0%, 100% { transform: translateY(0) rotate(0deg); } 50% { transform: translateY(-30px) rotate(10deg); } }
  .box { width: 100%; max-width: 480px; padding: 28px 20px; border-radius: 20px; background: rgba(255, 255, 255, 0.95); box-shadow: 0 15px 40px rgba(0,0,0,0.2); animation: fadeInUp 0.8s ease-out; backdrop-filter: blur(20px); border: 2px solid rgba(255,255,255,0.3); }
  @keyframes fadeInUp { from { opacity: 0; transform: translateY(40px) scale(0.95); } to { opacity: 1; transform: translateY(0) scale(1); } }
  p { color: #555; font-size: 14px; line-height: 1.5; margin: 0 0 14px; text-align: left; }
  .message-block { white-space: pre-wrap; font-family: 'Poppins', sans-serif; background: linear-gradient(135deg, rgba(255,154,158,0.1), rgba(250,208,196,0.1)); padding: 18px; border-radius: 14px; font-size: 14px; line-height: 1.7; color: #333; border: 2px solid rgba(255,154,158,0.2); min-height: 120px; }
  .cake-area { text-align: center; margin: 20px 0 16px; }
  .cake { font-size: 5rem; animation: cakeBounce 2s infinite; }
  @keyframes cakeBounce { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }
  .candles { font-size: 2.8rem; letter-spacing: 6px; margin-top: -20px; animation: flicker 1.5s infinite alternate; transition: all 0.3s ease-out; }
  @keyframes flicker { 0% { opacity: 1; } 100% { opacity: 0.8; } }
  .action { margin-top: 10px; text-align: center; }
  .btn { display: inline-block; padding: 13px 24px; border-radius: 14px; border: 0; background: linear-gradient(135deg, #ff9a9e, #fad0c4); color: white; cursor: pointer; font-size: 14px; font-weight: 600; text-decoration: none; transition: all 0.3s; font-family: 'Poppins', sans-serif; box-shadow: 0 6px 20px rgba(255, 154, 158, 0.4); }
  .btn:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(255, 154, 158, 0.6); }
  .btn:active { transform: translateY(0); }
  .info-guide { opacity: 0; visibility: hidden; transition: opacity 0.5s ease-in-out; color: #6c757d; font-size: 0.875em; text-align: center; margin-bottom: 15px; }
  .info-guide.visible { opacity: 1; visibility: visible; }
  .hidden { display: none; }

  .volume-meter-container { margin-top: 20px; text-align: center; }
  .volume-meter-container p { color: #666; font-size: 13px; margin-bottom: 5px; }
  .volume-meter { width: 100%; height: 10px; background: #e0e0e0; border-radius: 5px; overflow: hidden; }
  .volume-bar { height: 100%; width: 0%; background: linear-gradient(90deg, #4ecdc4, #44a3a0); transition: width 0.1s ease-out; }
</style>
</head>
<body>

  <div class="balloon" style="top:15%;left:5%;animation-delay:1s;">🎈</div>
  <div class="balloon" style="top:20%;right:8%;animation-delay:2s;">🎈</div>
  <div class="balloon" style="bottom:15%;left:10%;animation-delay:1s;">🎈</div>
  <div class="balloon" style="bottom:25%;right:5%;animation-delay:1.5s;">🎈</div>

  <div class="box">
    <p>From {{ owner }}:</p>
    <div class="message-block" id="message-block"></div>
    <div class="cake-area">
      <div class="candles" id="candles">🕯️🕯️🕯️</div>
      <div class="cake">🎂</div>
    </div>
    <div class="info-guide" id="info-guide">click on this button 👇</div>
    <div class="action">
      <button id="blow-btn" class="btn">Make a wish & Get Ready to Blow</button>
      <a id="fallback-link" href="{{ url_for('finale', name=name) }}" class="btn hidden">Continue to your gift</a>
    </div>
    <div class="volume-meter-container hidden" id="volume-meter-container">
      <p>Microphone Level (Blow when the bar is full):</p>
      <div class="volume-meter">
        <div id="volume-bar" class="volume-bar"></div>
      </div>
    </div>
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const balloons = document.querySelectorAll('.balloon'); balloons.forEach(b => b.style.opacity = 1);
      function typeWriter(element, text, speed = 40) { let i = 0; element.innerHTML = ""; return new Promise((resolve) => { function typing() { if (i < text.length) { element.innerHTML += text.charAt(i); i++; setTimeout(typing, speed); } else { resolve(); } } typing(); }); }
      const message = {{ message | tojson }};
      const messageBlock = document.getElementById('message-block');
      if (messageBlock) { typeWriter(messageBlock, message).then(() => { document.getElementById('info-guide').classList.add('visible'); }); }

      const blowBtn = document.getElementById('blow-btn');
      const fallbackLink = document.getElementById('fallback-link');
      const infoGuide = document.getElementById('info-guide');
      const candles = document.getElementById('candles');
      const volumeBar = document.getElementById('volume-bar');
      const volumeContainer = document.getElementById('volume-meter-container');
      const finalUrl = "{{ url_for('finale', name=name) }}";

      let audioContext;

      // تابع برای رفتن به صفحه بعد
      function goToNextPage() {
        window.location.href = finalUrl;
      }

      blowBtn.addEventListener('click', () => {
          if (!audioContext) {
              audioContext = new (window.AudioContext || window.webkitAudioContext)();
          }

          if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
              navigator.mediaDevices.getUserMedia({
                  audio: {
                      echoCancellation: false,
                      noiseSuppression: false,
                      autoGainControl: false
                  }
              })
              .then(stream => {
                  infoGuide.textContent = "Great! Now, make a wish and blow hard into the mic!";
                  blowBtn.classList.add('hidden');
                  volumeContainer.classList.remove('hidden');

                  const source = audioContext.createMediaStreamSource(stream);
                  const analyser = audioContext.createAnalyser();
                  analyser.fftSize = 256;
                  source.connect(analyser);

                  const bufferLength = analyser.frequencyBinCount;
                  const dataArray = new Uint8Array(bufferLength);

                  const THRESHOLD = 5500;
                  const REQUIRED_BLOW_FRAMES = 10;
                  let blowDetectedFrames = 0;
                  let isBlown = false;

                  function checkVolume() {
                      if (isBlown) return;

                      analyser.getByteFrequencyData(dataArray);
                      let sum = 0;
                      for (let i = 0; i < bufferLength; i++) {
                          sum += dataArray[i];
                      }
                      const volume = sum;

                      const volumePercentage = Math.min(100, (volume / 2));
                      if (volumeBar) {
                          volumeBar.style.width = volumePercentage + '%';
                      }

                      if (volume > THRESHOLD) {
                          blowDetectedFrames++;
                          console.log("Above threshold! Sustained for:", blowDetectedFrames, "frames.");
                          if (blowDetectedFrames >= REQUIRED_BLOW_FRAMES) {
                              isBlown = true;
                              console.log("✅ SUSTAINED BLOW DETECTED!");

                              infoGuide.textContent = "Wish Granted! ✨";
                              volumeContainer.classList.add('hidden');
                              candles.style.opacity = 0;
                              setTimeout(() => {
                                  candles.textContent = "💨💨💨";
                                  candles.style.opacity = 1;
                              }, 200);

                              stream.getTracks().forEach(track => track.stop());
                              source.disconnect();
                              analyser.disconnect();

                              setTimeout(goToNextPage, 1500);
                          }
                      } else {
                          // اگر صدا قطع شد، شمارنده را ریست کن
                          blowDetectedFrames = 0;
                      }

                      if (!isBlown) {
                          requestAnimationFrame(checkVolume);
                      }
                  }
                  checkVolume();
              })
              .catch(err => {
                  console.error("Microphone error:", err);
                  infoGuide.textContent = "Microphone not working? No problem, click the button below.";
                  blowBtn.classList.add('hidden');
                  fallbackLink.classList.remove('hidden');
              });
          } else {
              infoGuide.textContent = "Your browser doesn't support this feature. Click below.";
              blowBtn.classList.add('hidden');
              fallbackLink.classList.remove('hidden');
          }
      });
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
    background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 25%, #ff9a9e 50%, #fad0c4 75%, #ffd1ff 100%);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    text-align: center;
    padding: 16px;
  }
  @keyframes gradientShift {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
  }
  .wrap {
    width: 100%;
    max-width: 480px;
    padding: 36px 28px;
    border-radius: 20px;
    background: rgba(255, 255, 255, 0.95);
    box-shadow: 0 15px 40px rgba(0,0,0,0.2);
    animation: fadeInScale 1s ease-out;
    backdrop-filter: blur(20px);
    border: 2px solid rgba(255,255,255,0.3);
  }
  @keyframes fadeInScale {
    from { opacity: 0; transform: scale(0.8) rotate(-5deg); }
    to { opacity: 1; transform: scale(1) rotate(0deg); }
  }
  h1 {
    margin: 0 0 10px;
    font-size: 30px;
    font-weight: 700;
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: titlePulse 2s infinite;
  }
  @keyframes titlePulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }
  p {
    margin: 0 0 16px;
    font-size: 16px;
    color: #555;
    font-weight: 500;
  }
  F {
    margin: 0 0 16px;
    font-size: 15px;
    color: #555;
    font-weight: 500;
  }
  .cake {
    font-size: 6rem;
    margin-top: 16px;
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
    <h1>Happy Birthday {{ name }} 🎉</h1>
    <p>Congratulations on surviving another trip around the sun without being abducted by aliens 👽👾👻<br><br></p>
    <f>All the best wishes from <b>{{ owner }}</b> 🤍</f>
    <div class="cake">🎂</div>
  </div>
  <audio id="background-music" loop>
    <source src="{{ url_for('static', filename='h.mp3') }}"  type="audio/mpeg">
  </audio>
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const music = document.getElementById('background-music');
      const savedTime = localStorage.getItem('musicTime');
      let hasInteracted = false;
      
      function startMusic() {
        if (!hasInteracted) {
          // اگر زمان ذخیره شده وجود دارد، از آن استفاده کن
          if (savedTime) {
            music.currentTime = parseFloat(savedTime);
          }
          
          // سعی کن موسیقی را پخش کن
          music.play().catch(e => console.error("Autoplay was prevented:", e));
          hasInteracted = true;
        }
      }

      // شروع پخش موسیقی با کمی تأخیر
      setTimeout(startMusic, 100);

      // ذخیره زمان موسیقی قبل از ترک صفحه
      window.addEventListener('beforeunload', function() {
        localStorage.setItem('musicTime', music.currentTime);
      });

      function shootConfetti() {
        confetti({
          particleCount: 200,
          spread: 120,
          origin: { y: 0.5 },
          colors: ['#ff9a9e', '#fad0c4', '#ffecd2', '#fcb69f', '#ffd1ff', '#ff6b6b', '#ffe66d']
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
          colors: ['#ff9a9e', '#fad0c4', '#ffecd2']
        });
        confetti({
          particleCount: 3,
          angle: 120,
          spread: 55,
          origin: { x: 1 },
          colors: ['#fcb69f', '#ffd1ff', '#ff6b6b']
        });
      }, 250);
    });
  </script>
</body>
</html>
"""
@app.route("/", methods=["GET"])
def index():
    error = request.args.get("error")
    return render_template_string(LOGIN_HTML, owner=OWNER, error=error)
@app.route("/greet", methods=["POST"])
def greet():
    name = (request.form.get("name") or "").strip()
    normalized_name = name.lower()
    person_key = None
    if normalized_name in [
        "fatemeh",
        "fateme",
        "fatima",
        "fati",
        "فاطمه",
        "فاطی",
    ]:
        person_key = "fatemeh"
    elif normalized_name in [
        "mohammad hassan",
        "mohamad hasan",
        "mohamad",
        "mmd",
        "محمد حسن",
        "محمد",
        "ممد",
    ]:
        person_key = "mohammad_hassan"
    if person_key:
        person_data = MESSAGES[person_key]
        return render_template_string(
            GREET_HTML,
            name=person_data["name"],
            message=person_data["message"],
            owner=OWNER,
        )
    else:
        error_msg = "This page isn't for you 😏🤔"
        return redirect(url_for("index", error=error_msg))
@app.route("/finale")
def finale():
    name = request.args.get("name", "Friend")
    return render_template_string(FINAL_HTML, name=name, owner=OWNER)

if __name__ == "__main__":
    # This block is for LOCAL TESTING only.
    # PythonAnywhere and Serv00 will IGNORE this.
    # app.run(host="0.0.0.0", port=8000, debug=False,ssl_context='adhoc')
    app.run(host="0.0.0.0", port=8076, debug=False)
