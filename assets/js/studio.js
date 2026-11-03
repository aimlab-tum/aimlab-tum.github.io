/* The year tabs on /publications/. Without this script every year is open;
   with it, one at a time, and the arrow keys move between the tabs. */
(function () {
  'use strict';

  document.querySelectorAll('.ds-tabs').forEach(function (root) {
    var tabs = Array.prototype.slice.call(root.querySelectorAll('[role=tab]'));
    if (!tabs.length) return;

    function select(i, focus) {
      tabs.forEach(function (tab, n) {
        var on = n === i;
        tab.setAttribute('aria-selected', String(on));
        tab.tabIndex = on ? 0 : -1;
        var panel = document.getElementById(tab.getAttribute('aria-controls'));
        if (panel) panel.hidden = !on;
      });
      if (focus) tabs[i].focus();
    }

    tabs.forEach(function (tab, i) {
      tab.addEventListener('click', function () { select(i); });
      tab.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowRight') select((i + 1) % tabs.length, true);
        if (e.key === 'ArrowLeft') select((i - 1 + tabs.length) % tabs.length, true);
      });
    });
    select(0);
  });
})();
