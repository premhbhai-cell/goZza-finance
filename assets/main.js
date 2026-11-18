(function () {
  var PHONE = "918130112531";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var DPR = Math.min(window.devicePixelRatio || 1, 2);
  document.documentElement.classList.add("js");

  /* ---------- mobile menu ---------- */
  var btns = document.querySelectorAll(".menu-btn");
  var menu = document.querySelector(".mobile-menu");
  if (btns.length && menu) {
    function setMenu(open) {
      menu.classList.toggle("open", open);
      document.body.classList.toggle("menu-open", open);
      btns.forEach(function (b) { b.setAttribute("aria-expanded", open ? "true" : "false"); });
    }
    btns.forEach(function (b) {
      b.addEventListener("click", function () { setMenu(!menu.classList.contains("open")); });
    });
    menu.addEventListener("click", function (e) { if (e.target.closest("a")) setMenu(false); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });
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

  /* ---------- helpers ---------- */
  function cleanPhone(v) {
    var d = String(v || "").replace(/[\s\-()]/g, "").replace(/^\+?91/, "");
    return /^[6-9]\d{9}$/.test(d) ? "+91 " + d : "";
  }
  function slug(t) { return String(t).toLowerCase().replace(/\s+/g, "-"); }
  function inr(n) { return "\u20B9" + Math.round(n).toLocaleString("en-IN"); }

  /* ---------- apps filter via #hash (e.g. apps.html#loans) ---------- */
  var h0 = decodeURIComponent(location.hash.slice(1));
  if (h0) chips.forEach(function (c) { if (slug(c.getAttribute("data-filter")) === h0) c.click(); });

  /* ---------- calculators ---------- */
  function calcOut(kind, a, r, y) {
    var main, v1, v2, pct, rm = r / 1200, n = y * 12;
    if (kind === "emi") {
      var e = rm ? a * rm * Math.pow(1 + rm, n) / (Math.pow(1 + rm, n) - 1) : a / n;
      var tot = e * n; main = e; v1 = a; v2 = tot - a; pct = a / tot;
    } else if (kind === "sip") {
      var fv = rm ? a * ((Math.pow(1 + rm, n) - 1) / rm) * (1 + rm) : a * n;
      main = fv; v1 = a * n; v2 = fv - a * n; pct = v1 / fv;
    } else if (kind === "lump") {
      var f = a * Math.pow(1 + r / 100, y);
      main = f; v1 = a; v2 = f - a; pct = a / f;
    } else {
      var m = rm ? a * rm / ((Math.pow(1 + rm, n) - 1) * (1 + rm)) : a / n;
      main = m; v1 = m * n; v2 = a - m * n; pct = v1 / a;
    }
    return { main: main, v1: v1, v2: v2, pct: Math.max(0, Math.min(1, pct)) };
  }
  document.querySelectorAll(".calc[data-calc]").forEach(function (box) {
    var kind = box.getAttribute("data-calc");
    var nums = {}, rngs = {};
    box.querySelectorAll("[data-k]").forEach(function (i) { nums[i.getAttribute("data-k")] = i; });
    box.querySelectorAll("[data-r]").forEach(function (i) { rngs[i.getAttribute("data-r")] = i; });
    function val(k) {
      var el = nums[k], v = parseFloat(el.value);
      if (isNaN(v)) v = parseFloat(el.min);
      return Math.min(parseFloat(el.max), Math.max(parseFloat(el.min), v));
    }
    function paint() {
      var o = calcOut(kind, val("amt"), val("rate"), val("yrs"));
      box.querySelector('[data-o="main"]').textContent = inr(o.main);
      box.querySelector('[data-o="v1"]').textContent = inr(o.v1);
      box.querySelector('[data-o="v2"]').textContent = inr(o.v2);
      box.querySelector('[data-o="donut"]').style.setProperty("--pct", (o.pct * 100).toFixed(1) + "%");
    }
    Object.keys(nums).forEach(function (k) {
      rngs[k].addEventListener("input", function () { nums[k].value = rngs[k].value; paint(); });
      nums[k].addEventListener("input", function () { var v = parseFloat(nums[k].value); if (!isNaN(v)) rngs[k].value = v; paint(); });
      nums[k].addEventListener("change", function () { nums[k].value = val(k); rngs[k].value = nums[k].value; paint(); });
    });
    paint();
  });
  document.querySelectorAll("[data-tab]").forEach(function (t) {
    t.addEventListener("click", function () {
      document.querySelectorAll("[data-tab]").forEach(function (x) { x.classList.toggle("on", x === t); });
      document.querySelectorAll("#calculators .calc").forEach(function (c) { c.hidden = c.getAttribute("data-calc") !== t.getAttribute("data-tab"); });
    });
  });

  /* ---------- call-back form -> WhatsApp ---------- */
  document.querySelectorAll("form[data-wa-form]").forEach(function (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var n = f.elements["name"].value.trim(), ph = cleanPhone(f.elements["phone"].value), sv = f.elements["service"].value;
      var err = f.querySelector(".err");
      if (!n || !ph) { err.textContent = !n ? "Please enter your name." : "Please enter a valid 10-digit mobile number."; err.classList.add("on"); return; }
      err.classList.remove("on");
      var t = "Hello Gozza Finance, please call me back.\nName: " + n + "\nPhone: " + ph + "\nService: " + sv;
      window.open("https://wa.me/" + PHONE + "?text=" + encodeURIComponent(t), "_blank", "noopener");
    });
  });

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
      var ph = form.elements["phone"] ? cleanPhone(form.elements["phone"].value) : "";
      var err = form.querySelector(".err");
      if (!n || (form.elements["phone"] && !ph)) { if (err) { err.textContent = !n ? "Please enter your name." : "Please enter a valid 10-digit mobile number."; err.classList.add("on"); } return; }
      if (err) err.classList.remove("on");
      var t = "Hello Gozza Finance,\nName: " + n + (ph ? "\nPhone: " + ph : "") + "\nService: " + s + (m ? "\nMessage: " + m : "");
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
    ".diagram", ".vision .v", ".goal", ".seg", ".cat", ".how > div", ".why > div", ".stats > div", ".calc", ".cb", ".principles > div", ".docs li", ".trust", ".sec > .wrap > .eyebrow", ".sec > .wrap > h2", ".sec > .wrap > p", ".service-hero > *",
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
  document.querySelectorAll(".col-stats b,.stats b").forEach(function (b) {
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
})();
