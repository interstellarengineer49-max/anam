from pathlib import Path

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Hello Anam</title>
<style>
*{box-sizing:border-box}
body{
  margin:0; min-height:100vh; display:flex; align-items:center; justify-content:center;
  font-family:Inter,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  background:radial-gradient(circle at top,#26345f 0%,#11162d 42%,#070a14 100%);
  color:#fff; overflow:hidden;
}
body:before,body:after{
  content:""; position:fixed; width:280px;height:280px;border-radius:50%;
  filter:blur(90px);opacity:.25;pointer-events:none;
}
body:before{background:#8b5cf6;top:-80px;left:-70px}
body:after{background:#38bdf8;bottom:-100px;right:-80px}
.card{
  width:min(92vw,560px); min-height:430px; padding:42px 30px;
  border:1px solid rgba(255,255,255,.13); border-radius:28px;
  background:rgba(255,255,255,.075); backdrop-filter:blur(18px);
  box-shadow:0 25px 80px rgba(0,0,0,.35);
  display:flex; align-items:center; justify-content:center; text-align:center;
  position:relative;
}
.screen{display:none;width:100%;animation:fade .45s ease}
.screen.active{display:block}
@keyframes fade{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
h1{font-size:clamp(30px,7vw,48px);margin:0 0 16px}
h2{font-size:clamp(24px,5vw,34px);margin:0 0 18px}
p{font-size:18px;line-height:1.65;color:#d8def0;margin:0 auto 28px;max-width:440px}
.small{font-size:14px;color:#aeb7d1}
.progress{position:absolute;top:18px;left:30px;right:30px;height:4px;background:rgba(255,255,255,.12);border-radius:4px;overflow:hidden}
.progress-bar{height:100%;width:14%;background:#a78bfa;border-radius:4px;transition:width .35s ease}
.back{position:absolute;top:32px;left:24px;padding:7px 12px;margin:0;background:transparent;box-shadow:none;color:#bfc8e5;font-size:14px}
.back:hover{background:rgba(255,255,255,.08);filter:none}
button{
  border:0; border-radius:999px; padding:14px 25px; margin:6px;
  font-size:16px; font-weight:700; cursor:pointer; color:white;
  background:linear-gradient(135deg,#8b5cf6,#6366f1);
  box-shadow:0 10px 25px rgba(99,102,241,.25);
  transition:.2s transform,.2s filter;
}
button:hover{transform:translateY(-2px);filter:brightness(1.08)}
button.secondary{background:rgba(255,255,255,.10);box-shadow:none}
.heart{font-size:38px;margin-bottom:12px}
.choice{display:block;width:min(100%,390px);margin:10px auto}
.mood-label{font-size:14px;color:#aeb7d1;margin:0 0 12px}
.moods{display:flex;justify-content:center;gap:8px;margin:0 auto 16px;flex-wrap:wrap}
.mood{width:54px;height:54px;padding:0;margin:0;border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.08);box-shadow:none;font-size:25px;transition:.2s transform,.2s background,.2s border-color}
.mood:hover,.mood.selected{background:rgba(167,139,250,.28);border-color:#c4b5fd;transform:translateY(-4px) scale(1.06);filter:none}
textarea{width:min(100%,390px);min-height:105px;resize:vertical;padding:14px;border:1px solid rgba(255,255,255,.18);border-radius:14px;background:rgba(0,0,0,.16);color:white;font:inherit;outline:none}
textarea:focus{border-color:#a78bfa;box-shadow:0 0 0 3px rgba(167,139,250,.2)}
.status{min-height:24px;color:#fca5a5;font-size:14px;margin:8px 0}
.reaction{min-height:24px;color:#c4b5fd;font-size:15px;margin:-12px auto 18px;opacity:0;transition:opacity .25s ease}
.reaction.visible{opacity:1}
.count{font-size:12px;color:#aeb7d1;text-align:right;width:min(100%,390px);margin:5px auto 0}
.summary{font-size:15px;color:#cbd5e1;line-height:1.6;margin:0 auto 22px;max-width:390px}
.success{color:#86efac}
.spark{position:fixed;top:-20px;font-size:22px;pointer-events:none;animation:fall 2.4s linear forwards;z-index:2}
@keyframes fall{to{transform:translateY(110vh) rotate(260deg);opacity:0}}
</style>
</head>
<body>
<div class="card">
  <div class="progress" aria-label="Conversation progress"><div class="progress-bar" id="progressBar"></div></div>
  <button class="back" id="backButton" onclick="back()" aria-label="Go back">← Back</button>

  <section class="screen active" id="s1">
    <div class="heart">👋</div>
    <h1>Hello Anam</h1>
    <p>I wanted to ask you something.</p>
    <button onclick="go(2)">Okay, ask me</button>
  </section>

  <section class="screen" id="s2">
    <h2>Can I be honest?</h2>
    <p>I've noticed you've been a little distant these past two days, and I just wanted to understand.</p>
    <div class="reaction" id="reaction2" aria-live="polite"></div>
    <button onclick="choose(3, 'Thanks for hearing me out.')">Yes</button>
    <button class="secondary" onclick="choose(4, 'That is okay. Take your time.')">Not right now</button>
  </section>

  <section class="screen" id="s3">
    <h2>What happened?</h2>
    <p>Did I do something that upset you or make you uncomfortable?</p>
    <div class="mood-label">How are you feeling right now?</div>
    <div class="moods" role="group" aria-label="Choose your mood">
      <button class="mood" onclick="setMood(this, 'Okay')" aria-label="Okay">🙂</button>
      <button class="mood" onclick="setMood(this, 'Unsure')" aria-label="Unsure">😕</button>
      <button class="mood" onclick="setMood(this, 'Sad')" aria-label="Sad">😔</button>
      <button class="mood" onclick="setMood(this, 'Annoyed')" aria-label="Annoyed">😣</button>
      <button class="mood" onclick="setMood(this, 'Tired')" aria-label="Tired">😴</button>
    </div>
    <div class="reaction" id="reaction3" aria-live="polite"></div>
    <button class="choice" onclick="choose(5, 'I am listening.')">I want to tell you</button>
    <button class="choice secondary" onclick="choose(6, 'I respect that.')">I need some space</button>
    <p class="small">Whatever it is, you can be honest. I won't pressure you.</p>
  </section>

  <section class="screen" id="s4">
    <h2>No problem.</h2>
    <p>Take your time. I just wanted to ask rather than make assumptions.</p>
    <button onclick="go(7)">Got it</button>
  </section>

  <section class="screen" id="s5">
    <h2>Thank you.</h2>
    <p>Just tell me honestly when you're comfortable. I'll listen.</p>
    <textarea id="message" placeholder="You can write it here..." aria-label="Your message"></textarea>
    <div class="count" id="count">0 / 500</div>
    <div class="status" id="status" role="status"></div>
    <button onclick="sendMessage()">Send message</button>
    <button class="secondary" onclick="go(7)">Maybe later</button>
  </section>

  <section class="screen" id="s6">
    <h2>I understand.</h2>
    <p>I'll give you some space. Take care.</p>
  </section>

  <section class="screen" id="s7">
    <h2>That's all I wanted to say.</h2>
    <p class="summary" id="summary">No pressure. I hope everything is okay.</p>
    <button class="secondary" onclick="copySummary()">Copy summary</button>
    <div class="status" id="copyStatus" role="status"></div>
    <button onclick="restart()">Start over</button>
  </section>

</div>
<script>
let current = 1;
const history = [];
const totalSteps = 7;
const choices = [];
let mood = '';

function go(n, save = true){
  if (save && n !== current) history.push(current);
  document.querySelectorAll('.screen').forEach(x=>x.classList.remove('active'));
  document.getElementById('s'+n).classList.add('active');
  current = n;
  document.getElementById('progressBar').style.width = `${Math.max(14, (n / totalSteps) * 100)}%`;
  document.getElementById('backButton').style.visibility = n === 1 ? 'hidden' : 'visible';
  if(n === 7){
    const moodText = mood ? `You said you feel ${mood.toLowerCase()}. ` : '';
    document.getElementById('summary').textContent = moodText + 'No pressure. ' + (choices.length ? choices.join(' ') : 'I hope everything is okay.');
    celebrate();
  }
}

function choose(n, reaction){
  choices.push(reaction);
  const reactionBox = document.getElementById(`reaction${current}`);
  reactionBox.textContent = reaction;
  reactionBox.classList.add('visible');
  setTimeout(() => go(n), 350);
}

function setMood(button, selectedMood){
  document.querySelectorAll('.mood').forEach(item => item.classList.remove('selected'));
  button.classList.add('selected');
  mood = selectedMood;
  const reactionBox = document.getElementById('reaction3');
  reactionBox.textContent = `${selectedMood} is okay. Thank you for telling me.`;
  reactionBox.classList.add('visible');
}

function back(){
  const previous = history.pop();
  if(previous) go(previous, false);
}

function sendMessage(){
  const message = document.getElementById('message').value.trim();
  const status = document.getElementById('status');
  if(!message){
    status.textContent = 'Write something first, even if it is just one sentence.';
    document.getElementById('message').focus();
    return;
  }
  status.textContent = 'Your message is ready to share.';
  status.classList.add('success');
  setTimeout(() => go(7), 500);
}

function copySummary(){
  const summary = document.getElementById('summary').textContent;
  const showCopied = () => {
    const copyStatus = document.getElementById('copyStatus');
    copyStatus.textContent = 'Summary copied.';
    copyStatus.classList.add('success');
  };
  if(navigator.clipboard){
    navigator.clipboard.writeText(summary).then(showCopied);
  } else {
    const helper = document.createElement('textarea');
    helper.value = summary;
    document.body.appendChild(helper);
    helper.select();
    document.execCommand('copy');
    helper.remove();
    showCopied();
  }
}

function celebrate(){
  for(let i = 0; i < 14; i++){
    const spark = document.createElement('span');
    spark.className = 'spark';
    spark.textContent = ['✦','♥','✧'][i % 3];
    spark.style.left = `${8 + Math.random() * 84}%`;
    spark.style.animationDelay = `${Math.random() * .7}s`;
    document.body.appendChild(spark);
    setTimeout(() => spark.remove(), 3200);
  }
}

function restart(){
  history.length = 0;
  choices.length = 0;
  mood = '';
  document.querySelectorAll('.mood').forEach(item => item.classList.remove('selected'));
  document.getElementById('message').value = '';
  document.getElementById('count').textContent = '0 / 500';
  document.getElementById('status').textContent = '';
  document.getElementById('copyStatus').textContent = '';
  go(1, false);
}

document.getElementById('message').addEventListener('input', event => {
  const message = event.target.value.slice(0, 500);
  event.target.value = message;
  document.getElementById('count').textContent = `${message.length} / 500`;
});

document.addEventListener('keydown', event => {
  if(event.key === 'Escape') back();
  if(event.key === 'Enter' && current === 1) go(2);
});
go(1, false);
</script>
</body>
</html>'''

path = Path(__file__).with_name("hello_anam.html")
path.write_text(html, encoding="utf-8")
print(f"Created: {path}")
