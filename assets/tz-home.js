/* ── Hero carousel (seamless infinite loop — always moves forward) ── */
  (function(){
    var track = document.getElementById('heroTrack');
    if (!track) return;
    var realSlides = Array.prototype.slice.call(track.children);
    var realCount = realSlides.length;
    if (realCount < 2) return;
    var firstClone = realSlides[0].cloneNode(true);
    var lastClone = realSlides[realCount - 1].cloneNode(true);
    track.appendChild(firstClone);
    track.insertBefore(lastClone, realSlides[0]);

    var curIdx = 1, heroTimer, animating = false;
    function setX(animate) {
      if (animate) {
        track.style.transition = 'transform .7s cubic-bezier(.4,0,.2,1)';
        track.style.transform = 'translateX(-' + (curIdx * 100) + '%)';
      } else {
        track.style.transition = 'none';
        track.style.transform = 'translateX(-' + (curIdx * 100) + '%)';
        void track.offsetWidth; /* force reflow so the next move animates */
      }
    }
    function updateDots() {
      var active = (curIdx - 1 + realCount) % realCount;
      document.querySelectorAll('.hero-dot').forEach(function(d, i){ d.classList.toggle('on', i === active); });
    }
    window.heroMove = function(dir) {
      if (animating) return;
      animating = true;
      curIdx += dir;
      setX(true); updateDots();
    };
    window.heroGo = function(i) {
      if (animating) return;
      curIdx = i + 1;
      setX(true); updateDots();
    };
    track.addEventListener('transitionend', function() {
      if (curIdx === 0) { curIdx = realCount; setX(false); }
      else if (curIdx === realCount + 1) { curIdx = 1; setX(false); }
      animating = false;
    });
    function heroAuto() { heroTimer = setInterval(function(){ window.heroMove(1); }, 5000); }
    var hero = document.querySelector('.hero');
    hero.addEventListener('mouseenter', function(){ clearInterval(heroTimer); });
    hero.addEventListener('mouseleave', heroAuto);
    var startX = 0;
    hero.addEventListener('touchstart', function(e){ startX = e.touches[0].clientX; clearInterval(heroTimer); }, { passive: true });
    hero.addEventListener('touchend', function(e){ var diff = startX - e.changedTouches[0].clientX; if (Math.abs(diff) > 50) window.heroMove(diff > 0 ? 1 : -1); heroAuto(); });

    setX(false); updateDots(); heroAuto();
  })();

  /* ── Row scroll ── */
  function scrollRow(id, d) { document.getElementById(id).scrollBy({ left: d * 480, behavior: 'smooth' }); }

  /* ── Wishlist toggle ── */
  function toggleWish(btn) {
    var on = btn.classList.toggle('on');
    btn.textContent = on ? '♥' : '♡';
  }

  /* ── Mobile nav ── */
  function openMob() { document.getElementById('mobOverlay').classList.add('on'); document.getElementById('mobDrawer').classList.add('on'); }
  function closeMob() { document.getElementById('mobOverlay').classList.remove('on'); document.getElementById('mobDrawer').classList.remove('on'); }

  /* ── Cart drawer ── */
  function openCart() { document.getElementById('cartOverlay').classList.add('on'); document.getElementById('cartDrawer').classList.add('on'); }
  function closeCart() { document.getElementById('cartOverlay').classList.remove('on'); document.getElementById('cartDrawer').classList.remove('on'); }

  /* ── Cart qty ── */
  function cartQty(btn, d) {
    var span = btn.parentElement.querySelector('span');
    var n = Math.max(1, parseInt(span.textContent) + d);
    span.textContent = n;
  }

  /* ── Randomize product ratings (4-5 stars) ── */
  function randomizeRatings() {
    document.querySelectorAll('.pcard-stars').forEach(el => {
      var stars = Math.random() < 0.5 ? 4 : 5;
      var reviews = Math.floor(Math.random() * (400 - 30) + 30);
      el.innerHTML = '★'.repeat(stars) + ' <span>(' + reviews + ')</span>';
    });
  }
  randomizeRatings();
