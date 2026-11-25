// "Add to calendar" dropdown: close on outside click / Escape, copy the subscription link.
(function () {
  function init() {
    var menus = document.querySelectorAll("details.cal-dropdown");
    if (!menus.length) return;
    document.addEventListener("click", function (e) {
      menus.forEach(function (d) { if (!d.contains(e.target)) d.open = false; });
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") menus.forEach(function (d) { d.open = false; });
    });
    document.querySelectorAll("a.cal-copy").forEach(function (a) {
      a.addEventListener("click", function (e) {
        e.preventDefault();
        var label = a.lastChild, original = label.textContent;
        var done = function (text) {
          label.textContent = text;
          setTimeout(function () { label.textContent = original; }, 2000);
        };
        if (navigator.clipboard) {
          navigator.clipboard.writeText(a.dataset.url).then(
            function () { done(" Link copied!"); },
            function () { window.prompt("Copy this link:", a.dataset.url); }
          );
        } else {
          window.prompt("Copy this link:", a.dataset.url);
        }
      });
    });
  }
  if (typeof document$ !== "undefined") document$.subscribe(init);
  else document.addEventListener("DOMContentLoaded", init);
})();
