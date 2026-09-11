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
  # 1 puts the heading above the content and gives the section the full
  # width (col-lg-12), matching the Research section. With 2 the heading
  # sits in a narrow left gutter and the content is squeezed into col-lg-8,
  # which left the two-column layout below far too cramped.
  columns = "1"

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

Teaching and education are an integral part of our institute's mission. All of our courses—which are heavily influenced by our research—are taught in English. We offer lectures for students from various disciplines, but our core lectures are aimed at computer science students:

<div class="tw">
<div class="tw-main">

<div class="tw-head">
  <span class="tw-col-title">Courses</span>
  <label class="tw-pick" for="tw-select">Semester <select id="tw-select"></select></label>
</div>

<section class="tw-sem" data-code="WS26/27">

### Winter semester 2026/27

**Practical:**

- [Applied Deep Learning in Medicine](https://kiinformatik.mri.tum.de/de/practicalalex) (IN2106, IN4314)

**Lecture:**

- Künstliche Intelligenz in der Medizin I (IN2403)
- Foundations of AI in Biomedicine (CIT423005) — *exclusively for AI in Biomedicine students*
- Multimodal AI in Medicine (CIT423009)
- Trustworthy AI for Medicine (CIT423007)

**Seminar:**

- Research Skills and Methods (CIT422000) — *exclusively for AI in Biomedicine students*
- Master's Seminar: Large Language Models in Medicine (IN2107)
- Master's Seminar: AI Research in the Large Language Models Era (IN2107)

</section>

<section class="tw-sem" data-code="SS26">

### Summer semester 2026

**Practical:**

- [Applied Deep Learning in Medicine](https://kiinformatik.mri.tum.de/de/practicalalex) (IN2106, IN4314)

**Lecture:**

- Artificial Intelligence in Medicine II (IN2408)

**Seminar:**

- [Implicit Neural Representation and Neural Fields](https://kiinformatik.mri.tum.de/de/seminarharvey) (IN2107)
- [Deep Learning for Inverse Problems in Medical Imaging](https://kiinformatik.mri.tum.de/de/seminarsevgi) (IN2107)

</section>

<section class="tw-sem" data-code="WS25/26">

### Winter semester 2025/26

**Practical:**

- [Applied Deep Learning in Medicine](https://kiinformatik.mri.tum.de/de/practicalalex) (IN2106, IN4314)

**Lecture:**

- Künstliche Intelligenz in der Medizin I (IN2403)
- Multi-modal AI in Medicine (CIT423009)

**Seminar:**

- Trustworthy AI for Medicine (IN2107, IN45048)
- [Multi-modal AI for Medicine](https://kiinformatik.mri.tum.de/de/seminarharvey-multi-modal-ai-medicine) (IN2107, IN45072)

</section>

<div class="tw-evergreen">

Practicals and seminars take the individual subject areas further, with students applying what they learn in direct contact with our lecturers.

For medical students we offer the elective **Computer Science for Medical Students**: AI methods, above all neural networks, and their use in medicine. Students learn the theory, write their first Python, and train a network of their own.

</div>

</div>

<aside class="tw-side">

<div class="tw-card">

**Elite Master's programme**

## AI in Biomedicine

Our chair takes part in this Elite Master's programme, with Prof. Daniel Rückert as programme speaker. A research-oriented two-year degree at TUM in cooperation with Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU), it bridges computer science, engineering and medicine to train AI experts who pair technical depth with biomedical domain knowledge, and prepares them for academic research and industry. An optional Research Excellence Certificate is available.

More details on the [programme website](https://www.cit.tum.de/en/cit/studies/degree-programs/ai-in-biomedicine/).

Applications can be submitted every year between February 1 and May 31. If you have questions regarding the application, please contact [app-msaibm.asa@xcit.tum.de](mailto:app-msaibm.asa@xcit.tum.de).

<a class="btn btn-primary" href="https://www.cit.tum.de/en/cit/studies/degree-programs/ai-in-biomedicine/" target="_blank" rel="noopener">Programme website&nbsp;→</a>

</div>

<div class="tw-card">

**Work with us**

## Theses, internships and student positions

In addition to lectures, seminars, and internships, we offer a range of bachelor's, master's and IDP projects. All current openings are listed on the CIT thesis portal:

<a class="btn btn-outline-primary" href="https://thesis.aet.cit.tum.de/?groups=c9a54897-40cb-4cdb-87ce-171f33b0a7e2" target="_blank" rel="noopener">Browse our open projects&nbsp;→</a>

</div>

</aside>
</div>

<style>
/* Teaching: courses on the left, the two things a prospective student can act
   on pinned to the right. Everything inside the wrappers is ordinary Markdown,
   so adding a course is still one bullet and adding a semester is one
   <section> around the same Markdown as before.
   Values follow Wowchemy: 1rem/1.5 body, headings at weight 500, #dee2e6
   rules, rgba(0,0,0,.54) for secondary text. */
.tw{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(0,1fr);gap:2rem;align-items:start}
.tw-head{display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap;
  margin-bottom:1rem;padding-bottom:.5rem;border-bottom:1px solid #dee2e6}
.tw-col-title{font-size:1.25rem;font-weight:500}
.tw-pick{font-size:.875rem;color:rgba(0,0,0,.54);margin:0}
.tw-pick select{font:inherit;font-size:1rem;color:#212529;padding:.3rem .5rem;margin-left:.4rem;
  border:1px solid #dee2e6;background:#fff}
.tw-sem h3{font-size:1.25rem;font-weight:500;line-height:1.2;margin:0 0 .75rem}
.tw-sem p{margin:0 0 .25rem;font-size:.875rem;color:rgba(0,0,0,.54)}
.tw-sem p strong{font-weight:400}
.tw-sem ul{margin:0 0 1rem;padding-left:1.25rem}
.tw-sem li{margin-bottom:.15rem}
.tw-evergreen{margin-top:1.5rem;padding-top:1.125rem;border-top:1px solid #dee2e6;
  font-size:.875rem;color:rgba(0,0,0,.54)}
.tw-card{border:1px solid #dee2e6;padding:1.125rem;margin-bottom:1.25rem}
.tw-card > p:first-child{font-size:.875rem;letter-spacing:.03em;color:rgba(0,0,0,.54);margin:0 0 .375rem}
.tw-card > p:first-child strong{font-weight:400}
.tw-card h2{font-size:1.25rem;font-weight:500;line-height:1.2;margin:0 0 .5rem}
.tw-card p{font-size:.875rem}
.tw-card ul{list-style:none;padding:0;margin:0 0 .875rem;padding-top:.75rem;border-top:1px solid #dee2e6}
.tw-card li{font-size:.875rem;margin-bottom:.25rem}
@media (max-width:800px){
  .tw{grid-template-columns:1fr}
  /* The programme card is the strongest recruiting asset, so it leads here. */
  .tw-side{order:-1}
}
</style>

<script>
/* Progressive enhancement: without JavaScript every semester stays visible,
   which is how this section behaved before. With it, the dropdown shows one
   semester at a time, newest first - the order the sections are written in. */
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
