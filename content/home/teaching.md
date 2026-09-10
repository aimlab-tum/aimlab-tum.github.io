+++
# An instance of the Blank widget — the Teaching section text.
# Documentation: https://wowchemy.com/docs/page-builder/

widget = "blank"
headless = false  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 60  # Order that this section will appear.

title = "Teaching"
subtitle = ""

[design]
  # Choose how many columns the section has. Valid values: 1 or 2.
  columns = "2"

[design.background]
  # Apply a background color, gradient, or image.
  #   Uncomment (by removing `#`) an option to apply it.
  #   Choose a light or dark text color by setting `text_color_light`.
  #   Any HTML color name or Hex value is valid.

  # Background color.
  # color = "navy"

  # Background image.
  # image = "background.jpg"  # Name of image in `static/media/`.
  # image_darken = 0.6  # Darken the image? Range 0-1 where 0 is transparent and 1 is opaque.

[advanced]
  # Custom CSS.
  css_style = ""

  # CSS class.
  css_class = ""
+++


<div class="tw">
<div class="tw-main">

<div class="tw-head">
  <h4>Courses</h4>
  <label class="tw-pick" for="tw-select">Semester
    <select id="tw-select"></select>
  </label>
</div>

<div class="tw-semesters">

<section class="tw-sem" data-code="WS26/27" data-label="Winter semester 2026/27">
  <p class="tw-label">Winter semester 2026/27</p>
  <div class="tw-cat">
    <h6>Lectures</h6>
    <div class="tw-course">Künstliche Intelligenz in der Medizin I<span class="tw-code">IN2403</span></div>
    <div class="tw-course">Foundations of AI in Biomedicine<span class="tw-code">CIT423005</span>
      <div class="tw-note">AI in Biomedicine students only</div></div>
    <div class="tw-course">Multimodal AI in Medicine<span class="tw-code">CIT423009</span></div>
    <div class="tw-course">Trustworthy AI for Medicine<span class="tw-code">CIT423007</span></div>
  </div>
  <div class="tw-cat">
    <h6>Practical</h6>
    <div class="tw-course"><a href="https://kiinformatik.mri.tum.de/de/practicalalex">Applied Deep Learning in Medicine</a><span class="tw-code">IN2106 · IN4314</span></div>
  </div>
  <div class="tw-cat">
    <h6>Seminars</h6>
    <div class="tw-course">Research Skills and Methods<span class="tw-code">CIT422000</span>
      <div class="tw-note">AI in Biomedicine students only</div></div>
    <div class="tw-course">Master's Seminar: Large Language Models in Medicine<span class="tw-code">IN2107</span></div>
    <div class="tw-course">Master's Seminar: AI Research in the Large Language Models Era<span class="tw-code">IN2107</span></div>
  </div>
</section>

<section class="tw-sem" data-code="SS26" data-label="Summer semester 2026">
  <p class="tw-label">Summer semester 2026</p>
  <div class="tw-cat">
    <h6>Lecture</h6>
    <div class="tw-course">Artificial Intelligence in Medicine II<span class="tw-code">IN2408</span></div>
  </div>
  <div class="tw-cat">
    <h6>Practical</h6>
    <div class="tw-course"><a href="https://kiinformatik.mri.tum.de/de/practicalalex">Applied Deep Learning in Medicine</a><span class="tw-code">IN2106 · IN4314</span></div>
  </div>
  <div class="tw-cat">
    <h6>Seminars</h6>
    <div class="tw-course"><a href="https://kiinformatik.mri.tum.de/de/seminarharvey">Implicit Neural Representation and Neural Fields</a><span class="tw-code">IN2107</span></div>
    <div class="tw-course"><a href="https://kiinformatik.mri.tum.de/de/seminarsevgi">Deep Learning for Inverse Problems in Medical Imaging</a><span class="tw-code">IN2107</span></div>
  </div>
</section>

<section class="tw-sem" data-code="WS25/26" data-label="Winter semester 2025/26">
  <p class="tw-label">Winter semester 2025/26</p>
  <div class="tw-cat">
    <h6>Lectures</h6>
    <div class="tw-course">Künstliche Intelligenz in der Medizin I<span class="tw-code">IN2403</span></div>
    <div class="tw-course">Multi-modal AI in Medicine<span class="tw-code">CIT423009</span></div>
  </div>
  <div class="tw-cat">
    <h6>Practical</h6>
    <div class="tw-course"><a href="https://kiinformatik.mri.tum.de/de/practicalalex">Applied Deep Learning in Medicine</a><span class="tw-code">IN2106 · IN4314</span></div>
  </div>
  <div class="tw-cat">
    <h6>Seminars</h6>
    <div class="tw-course">Trustworthy AI for Medicine<span class="tw-code">IN2107 · IN45048</span></div>
    <div class="tw-course"><a href="https://kiinformatik.mri.tum.de/de/seminarharvey-multi-modal-ai-medicine">Multi-modal AI for Medicine</a><span class="tw-code">IN2107 · IN45072</span></div>
  </div>
</section>

</div>

<div class="tw-evergreen">
  <h6>Computer Science for Medical Students</h6>
  <p>Offered as an elective for medical students. The course gives insights into AI methods — especially neural
  networks — and their applications in medicine. Alongside the theoretical basics, students gain first practical
  experience with Python and train their own neural networks.</p>
</div>

</div>

<aside class="tw-side">

<div class="tw-card">
  <p class="tw-kicker">Elite Master's programme</p>
  <h5>AI in Biomedicine</h5>
  <p>A research-oriented two-year programme bridging computer science, engineering and medicine, offered by the
  Technical University of Munich together with Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU). Prof.
  Daniel Rückert is programme speaker.</p>
  <dl class="tw-facts">
    <div><dt>Apply</dt><dd>1 February – 31 May, every year</dd></div>
    <div><dt>Length</dt><dd>2 years, optional Research Excellence Certificate</dd></div>
    <div><dt>At the chair</dt><dd>2 courses reserved for AIBM students</dd></div>
  </dl>
  <a class="btn btn-primary" href="https://www.cit.tum.de/en/cit/studies/degree-programs/ai-in-biomedicine/" target="_blank" rel="noopener">Programme website&nbsp;→</a>
  <p class="tw-small">Questions about applying: <a href="mailto:app-msaibm.asa@xcit.tum.de">app-msaibm.asa@xcit.tum.de</a></p>
</div>

<div class="tw-card">
  <p class="tw-kicker">Work with us</p>
  <h5>Theses &amp; student projects</h5>
  <p>Bachelor's, master's and IDP projects, internships and student research assistant positions. Every current
  opening is listed on the CIT thesis portal.</p>
  <a class="btn btn-outline-primary" href="https://thesis.aet.cit.tum.de/?groups=c9a54897-40cb-4cdb-87ce-171f33b0a7e2" target="_blank" rel="noopener">Browse our open projects&nbsp;→</a>
</div>

</aside>
</div>

<style>
/* Teaching section: courses on the left, the two things a prospective student
   can act on pinned to the right. Prefixed .tw- throughout so nothing collides
   with Bootstrap or the theme. Values follow Wowchemy: 1rem/1.5 body, headings
   at weight 500, #dee2e6 rules, rgba(0,0,0,.54) for secondary text. */
.tw{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(0,1fr);gap:2rem;align-items:start}
.tw-head{display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap;
  margin-bottom:1rem;padding-bottom:.5rem;border-bottom:1px solid #dee2e6}
.tw-head h4{margin:0;font-size:1.25rem;font-weight:500}
.tw-pick{font-size:.875rem;color:rgba(0,0,0,.54);margin:0}
.tw-pick select{font:inherit;font-size:1rem;color:#212529;padding:.3rem .5rem;margin-left:.4rem;
  border:1px solid #dee2e6;background:#fff}
.tw-sem{margin-bottom:1.5rem}
.tw-label{font-size:1.25rem;font-weight:500;line-height:1.2;margin:0 0 .75rem}
.tw-cat{margin:0 0 1rem}
.tw-cat h6{margin:0 0 .25rem;font-size:.875rem;font-weight:400;letter-spacing:.03em;color:rgba(0,0,0,.54)}
.tw-course{padding:.25rem 0}
.tw-code{font-size:.875rem;color:rgba(0,0,0,.54);margin-left:.5rem;white-space:nowrap}
.tw-note{font-size:.875rem;color:rgba(0,0,0,.54);font-style:italic}
.tw-evergreen{margin-top:1.5rem;padding-top:1.125rem;border-top:1px solid #dee2e6}
.tw-evergreen h6{margin:0 0 .25rem;font-size:1rem;font-weight:500}
.tw-evergreen p{margin:0;font-size:.875rem;color:rgba(0,0,0,.54)}
.tw-card{border:1px solid #dee2e6;padding:1.125rem;margin-bottom:1.25rem}
.tw-kicker{font-size:.875rem;letter-spacing:.03em;color:rgba(0,0,0,.54);margin:0 0 .375rem}
.tw-card h5{margin:0 0 .5rem;font-size:1.25rem;font-weight:500}
.tw-card p{margin:0 0 .75rem;font-size:.875rem}
.tw-facts{margin:0 0 .875rem;padding-top:.75rem;border-top:1px solid #dee2e6}
.tw-facts div{display:flex;gap:.625rem;font-size:.875rem}
.tw-facts dt{font-weight:400;color:rgba(0,0,0,.54);flex:0 0 6.5rem}
.tw-facts dd{margin:0}
.tw-small{font-size:.875rem;color:rgba(0,0,0,.54);margin:.625rem 0 0}
@media (max-width:800px){
  .tw{grid-template-columns:1fr}
  /* The programme card is the strongest recruiting asset, so it leads on narrow screens. */
  .tw-side{order:-1}
}
</style>

<script>
/* Progressive enhancement: without JavaScript every semester stays visible,
   which is the behaviour this section had before. With it, the dropdown shows
   one semester at a time, newest first. */
(function () {
  var sems = Array.prototype.slice.call(document.querySelectorAll('.tw-sem'));
  var select = document.getElementById('tw-select');
  if (!sems.length || !select) return;
  sems.forEach(function (s, i) {
    var o = document.createElement('option');
    o.value = i;
    o.textContent = s.getAttribute('data-code');
    select.appendChild(o);
  });
  function show(i) {
    sems.forEach(function (s, j) { s.style.display = (j === +i) ? '' : 'none'; });
  }
  select.addEventListener('change', function (e) { show(e.target.value); });
  show(0);
})();
</script>
