(function () {
  var PHONE = "918130112531";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var DPR = Math.min(window.devicePixelRatio || 1, 2);
  document.documentElement.classList.add("js");

  /* ---------- mobile menu ---------- */
  var btn = document.querySelector(".menu-btn");
  var menu = document.querySelector(".mobile-menu");
  if (btn && menu) {
    btn.addEventListener("click", function () {
      var open = menu.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  /* ---------- apps filter ---------- */
  var chips = document.querySelectorAll("[data-filter]");
  var tiles = document.querySelectorAll(".tile[data-cat]");
  chips.forEach(function (c) {
    c.addEventListener("click", function () {
      chips.forEach(function (x) { x.classList.remove("on"); });
      c.classList.add("on");
      var f = c.getAttribute("data-filter");
      tiles.forEach(function (t) { t.hidden = !(f === "all" || t.getAttribute("data-cat") === f); });
    });
  });

  /* ---------- news load more ---------- */
  var more = document.getElementById("load-more");
  if (more) {
    more.addEventListener("click", function () {
      document.querySelectorAll("[data-extra]").forEach(function (el) { el.hidden = false; });
      more.hidden = true;
    });
  }

  /* ---------- contact form -> WhatsApp ---------- */
  var form = document.getElementById("enquiry");
  if (form) {
    var q = new URLSearchParams(location.search).get("service");
    var sel = form.querySelector("select");
    if (q && sel) {
      for (var i = 0; i < sel.options.length; i++) if (sel.options[i].value === q) sel.selectedIndex = i;
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var n = form.elements["name"].value.trim();
      var s = form.elements["service"].value;
      var m = form.elements["message"].value.trim();
      var t = "Hello Gozza Finance,\nName: " + n + "\nService: " + s + (m ? "\nMessage: " + m : "");
      window.open("https://wa.me/" + PHONE + "?text=" + encodeURIComponent(t), "_blank", "noopener");
    });
  }

  /* ---------- hero headline: word-by-word rise ---------- */
  if (!reduce) {
    document.querySelectorAll("h1.display").forEach(function (h) {
      var idx = 0;
      (function walk(node) {
        Array.prototype.slice.call(node.childNodes).forEach(function (n) {
          if (n.nodeType === 3) {
            var frag = document.createDocumentFragment();
            n.textContent.split(/(\s+)/).forEach(function (part) {
              if (!part) return;
              if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(" ")); return; }
              var w = document.createElement("span"); w.className = "w"; w.style.setProperty("--wi", idx++);
              var s = document.createElement("span"); s.textContent = part; w.appendChild(s); frag.appendChild(w);
            });
            node.replaceChild(frag, n);
          } else if (n.nodeType === 1) walk(n);
        });
      })(h);
    });
  }

  /* ---------- scroll reveal ---------- */
  var revealSel = [
    ".hero-inner > *", ".col-stats > div", ".col > .pad > *", ".mock .chartframe", ".apps-list a", ".vision-dark .vp",
    ".news-list a", ".faq details", ".arch .card", ".sv-grid .card", ".tile", ".acard", ".steps li", ".block",
    ".rows .row", ".cta-band", ".photos div", ".info a", "form.enq", ".article-head > *", ".cover", ".chartframe.solo",
    ".diagram", ".vision .v", ".sec > .wrap > .eyebrow", ".sec > .wrap > h2", ".sec > .wrap > p", ".service-hero > *",
    ".articles .acard", ".grid .tile", ".chips"
  ].join(",");
  var seen = new Set(), rvEls = [];
  document.querySelectorAll(revealSel).forEach(function (el) {
    if (seen.has(el) || el.closest(".strip")) return;
    seen.add(el); el.classList.add("rv");
    var sib = el.parentElement ? Array.prototype.indexOf.call(el.parentElement.children, el) : 0;
    el.style.setProperty("--d", Math.min(sib, 6));
    rvEls.push(el);
  });
  if ("IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { threshold: 0.08, rootMargin: "0px 0px -6% 0px" });
    rvEls.forEach(function (el) { io.observe(el); });
    document.querySelectorAll(".chartframe").forEach(function (el) { if (!el.classList.contains("rv")) io.observe(el); });
  } else {
    rvEls.forEach(function (el) { el.classList.add("in"); });
    document.querySelectorAll(".chartframe").forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- count-up numbers ---------- */
  document.querySelectorAll(".col-stats b").forEach(function (b) {
    var txt = b.textContent.trim();
    if (!/^\d+$/.test(txt) || reduce || !("IntersectionObserver" in window)) return;
    var target = parseInt(txt, 10), done = false;
    var o = new IntersectionObserver(function (es) {
      if (!es[0].isIntersecting || done) return; done = true; o.disconnect();
      var t0 = performance.now(), dur = 1100;
      (function step(t) {
        var p = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - p, 3);
        b.textContent = Math.round(target * e);
        if (p < 1) requestAnimationFrame(step);
      })(t0);
    }, { threshold: 0.6 });
    b.textContent = "0"; o.observe(b);
  });

  /* ---------- card glow follows cursor ---------- */
  document.querySelectorAll(".card,.tile,.acard").forEach(function (c) {
    c.addEventListener("pointermove", function (e) {
      var r = c.getBoundingClientRect();
      c.style.setProperty("--mx", (e.clientX - r.left) + "px");
      c.style.setProperty("--my", (e.clientY - r.top) + "px");
    });
  });

  /* ---------- vision highlight ---------- */
  var vps = document.querySelectorAll(".vision-dark .vp");
  if (vps.length && "IntersectionObserver" in window) {
    var vio = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { vps.forEach(function (v) { v.classList.remove("on"); }); e.target.classList.add("on"); } });
    }, { rootMargin: "-40% 0px -40% 0px" });
    vps.forEach(function (v) { vio.observe(v); });
  } else { vps.forEach(function (v) { v.classList.add("on"); }); }

  /* ---------- dotted bands (wave / strip) ---------- */
  document.querySelectorAll("canvas.dots").forEach(function (cv) {
    var ctx = cv.getContext("2d"), W, H, pts = [], vis = true;
    var color = cv.getAttribute("data-color") || "#8bbcff";
    var mode = cv.getAttribute("data-mode") || "wave";
    function build() {
      var r = cv.getBoundingClientRect();
      W = cv.width = Math.max(1, r.width * DPR); H = cv.height = Math.max(1, r.height * DPR);
      pts = [];
      var n = Math.round(W / (mode === "wave" ? 2.6 : 8));
      for (var i = 0; i < n; i++) {
        var x = Math.random() * W, t = x / W, y;
        if (mode === "wave") {
          var c = H * (0.95 - 0.75 * t);
          y = c + (Math.random() - 0.5) * H * (0.25 + 0.9 * t) + (Math.random() < 0.3 ? (Math.random() - 0.5) * H : 0);
        } else y = Math.random() * H;
        pts.push({ x: x, y: y, r: (mode === "wave" ? 0.7 + Math.pow(Math.random(), 3) * 7 : 0.8 + Math.random() * 2.2) * DPR, p: Math.random() * 6.28, s: 0.2 + Math.random() * 0.5, a: 0.35 + Math.random() * 0.65 });
      }
    }
    function draw(tm) {
      if (vis) {
        ctx.clearRect(0, 0, W, H); ctx.fillStyle = color;
        for (var i = 0; i < pts.length; i++) {
          var p = pts[i];
          var dx = reduce ? 0 : Math.sin(tm / 1800 * p.s + p.p) * 4 * DPR;
          var dy = reduce ? 0 : Math.cos(tm / 2100 * p.s + p.p) * 4 * DPR;
          ctx.globalAlpha = reduce ? p.a : p.a * (0.55 + 0.45 * Math.sin(tm / 900 * p.s + p.p));
          ctx.beginPath(); ctx.arc(p.x + dx, p.y + dy, p.r, 0, 6.2832); ctx.fill();
        }
        ctx.globalAlpha = 1;
      }
      if (!reduce) requestAnimationFrame(draw);
    }
    build(); requestAnimationFrame(draw);
    window.addEventListener("resize", build);
    if ("IntersectionObserver" in window) new IntersectionObserver(function (es) { vis = es[0].isIntersecting; }).observe(cv);
  });

  /* ---------- SPARKLES ---------- */
  var PAL = {
    dark: ["#ffffff", "#d6e6ff", "#8bbcff", "#6aa6ff", "#4d8dff"],
    light: ["#2f6bff", "#4d8dff", "#8bbcff", "#a9c8ff"]
  };
  var hosts = [];
  function star(ctx, x, y, r) {
    var k = r * 0.16;
    ctx.beginPath();
    ctx.moveTo(x, y - r); ctx.lineTo(x + k, y - k); ctx.lineTo(x + r, y); ctx.lineTo(x + k, y + k);
    ctx.lineTo(x, y + r); ctx.lineTo(x - k, y + k); ctx.lineTo(x - r, y); ctx.lineTo(x - k, y - k);
    ctx.closePath(); ctx.fill();
  }
  function Sparkle(host) {
    var self = this;
    this.host = host;
    this.mode = host.getAttribute("data-sp") || "dark";
    this.dens = parseFloat(host.getAttribute("data-sp-density") || "1");
    this.cv = document.createElement("canvas"); this.cv.className = "sp-cv"; this.cv.setAttribute("aria-hidden", "true");
    host.insertBefore(this.cv, host.firstChild);
    this.ctx = this.cv.getContext("2d");
    this.pts = []; this.vis = false; this.mx = -999; this.my = -999;
    this.size();
    if ("ResizeObserver" in window) new ResizeObserver(function () { self.size(); }).observe(host);
    else window.addEventListener("resize", function () { self.size(); });
    if ("IntersectionObserver" in window) new IntersectionObserver(function (es) { self.vis = es[0].isIntersecting; }).observe(host);
    else this.vis = true;
    host.addEventListener("pointermove", function (e) {
      var r = host.getBoundingClientRect(); self.mx = (e.clientX - r.left) * DPR; self.my = (e.clientY - r.top) * DPR;
    });
    host.addEventListener("pointerleave", function () { self.mx = self.my = -999; });
    hosts.push(this);
  }
  Sparkle.prototype.size = function () {
    var r = this.host.getBoundingClientRect();
    this.W = this.cv.width = Math.max(1, Math.round(r.width * DPR));
    this.H = this.cv.height = Math.max(1, Math.round(r.height * DPR));
    var area = (r.width * r.height) / 1000;
    var n = Math.max(14, Math.min(120, Math.round(area / 9 * this.dens)));
    var pal = PAL[this.mode] || PAL.dark, pts = [];
    for (var i = 0; i < n; i++) {
      var isStar = Math.random() < 0.45;
      pts.push({
        x: Math.random() * this.W, y: Math.random() * this.H,
        r: (isStar ? 3 + Math.random() * 7 : 0.9 + Math.random() * 2.2) * DPR,
        star: isStar, c: pal[(Math.random() * pal.length) | 0],
        ph: Math.random() * 6.28, sp: 0.6 + Math.random() * 1.6,
        vy: -(0.02 + Math.random() * 0.1) * DPR, vx: (Math.random() - 0.5) * 0.05 * DPR,
        base: this.mode === "light" ? 0.35 : 0.5
      });
    }
    this.pts = pts;
    if (reduce) this.draw(0);
  };
  Sparkle.prototype.draw = function (t) {
    var ctx = this.ctx, W = this.W, H = this.H;
    ctx.clearRect(0, 0, W, H);
    var R = 130 * DPR;
    for (var i = 0; i < this.pts.length; i++) {
      var p = this.pts[i];
      if (!reduce) {
        p.y += p.vy; p.x += p.vx + Math.sin(t / 2600 + p.ph) * 0.05 * DPR;
        if (p.y < -12) { p.y = H + 12; p.x = Math.random() * W; }
        if (p.x < -12) p.x = W + 12; if (p.x > W + 12) p.x = -12;
      }
      var tw = reduce ? 0.7 : Math.pow((Math.sin(t / 1000 * p.sp + p.ph) + 1) / 2, p.star ? 2.2 : 1.2);
      var boost = 0, dx = p.x - this.mx, dy = p.y - this.my, d2 = dx * dx + dy * dy;
      if (d2 < R * R) boost = 1 - Math.sqrt(d2) / R;
      var a = Math.min(1, p.base * 0.4 + tw * (1 - p.base * 0.4) + boost * 0.6);
      var r = p.r * (0.55 + 0.45 * tw + boost * 0.9);
      ctx.fillStyle = p.c;
      ctx.globalAlpha = a * (p.star ? 1 : 0.8);
      if (p.star) {
        star(ctx, p.x, p.y, r);
        if (r > 6 * DPR) { ctx.globalAlpha = a * 0.16; ctx.beginPath(); ctx.arc(p.x, p.y, r * 1.5, 0, 6.2832); ctx.fill(); }
      } else { ctx.beginPath(); ctx.arc(p.x, p.y, r, 0, 6.2832); ctx.fill(); }
    }
    ctx.globalAlpha = 1;
  };
  document.querySelectorAll(".sp").forEach(function (el) { new Sparkle(el); });
  if (!reduce) {
    (function loop(t) {
      for (var i = 0; i < hosts.length; i++) if (hosts[i].vis) hosts[i].draw(t);
      requestAnimationFrame(loop);
    })(0);
  }
})();
