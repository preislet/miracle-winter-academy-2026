// Make Markdown task lists clickable and remember their state in this browser.
(function () {
  function init() {
    var boxes = document.querySelectorAll(".md-typeset .task-list-item input[type=checkbox]");
    boxes.forEach(function (box, i) {
      var key = "miracle-checklist:" + location.pathname + ":" + i;
      box.disabled = false;
      try {
        var saved = localStorage.getItem(key);
        if (saved !== null) box.checked = saved === "1";
      } catch (e) { /* storage unavailable: still clickable, just not remembered */ }
      box.addEventListener("change", function () {
        try { localStorage.setItem(key, box.checked ? "1" : "0"); } catch (e) {}
      });
    });
  }
  if (typeof document$ !== "undefined") document$.subscribe(init);
  else document.addEventListener("DOMContentLoaded", init);
})();
