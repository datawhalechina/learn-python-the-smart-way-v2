<!-- Cal inline embed code begins -->
<div style="width:150%;height:120%;overflow:scroll" id="my-cal-inline"></div>
<script type="text/javascript">
  (function (C, A, L) { let p = function (a, ar) { a.q.push(ar); }; let d = C.document; C.Cal = C.Cal || function () { let cal = C.Cal; let ar = arguments; if (!cal.loaded) { cal.ns = {}; cal.q = cal.q || []; d.head.appendChild(d.createElement("script")).src = A; cal.loaded = true; } if (ar[0] === L) { const api = function () { p(api, arguments); }; const namespace = ar[1]; api.q = api.q || []; typeof namespace === "string" ? (cal.ns[namespace] = api) && p(api, ar) : p(cal, ar); return; } p(cal, ar); }; })(window, "https://app.cal.com/embed/embed.js", "init");
Cal("init", "p2s-office-hours", {origin:"https://cal.com"});

  Cal.ns["p2s-office-hours"]("inline", {
	elementOrSelector:"#my-cal-inline",
	calLink: "learn-python-the-smart-way/p2s-office-hours",
	layout: "month_view"
  });
  
  Cal.ns["p2s-office-hours"]("ui", {"styles":{"branding":{"brandColor":"#000000"}},"hideEventTypeDetails":false,"layout":"month_view"});
  </script>
  <!-- Cal inline embed code ends --> 