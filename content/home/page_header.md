+++
# The Welcome section: a photo carousel with the opening lines over it.
# The heading lives in the body rather than in `title` so that it can sit
# inside the image band; the rest of the copy follows below it on white.
widget = "blank"  # See https://sourcethemes.com/academic/docs/page-builder/
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 10  # Order that this section will appear.
title = ""
subtitle = ""

[design]
  # Full width, so the photo band can run edge to edge.
  columns = "1"
+++

<div class="hero-band" id="hero-band">

<figure class="hero-shot is-on" style="--scrim:.62">
  <img src="/media/lab_retreat_winter.jpg" alt="The lab on a winter retreat in the Alps" width="1920" height="1440">
</figure>
<figure class="hero-shot" style="--scrim:.75">
  <img src="/media/lab_retreat_summer.jpg" alt="The lab on its summer retreat in Obertraun, Austria" width="1920" height="1114" loading="lazy">
</figure>
<figure class="hero-shot" style="--scrim:.63">
  <img src="/media/lab_retreat_winter_2024.jpg" alt="The lab on the 2024 winter retreat" width="800" height="600" loading="lazy">
</figure>
<figure class="hero-shot" style="--scrim:.71">
  <img src="/media/miccai_2024.jpg" alt="The lab at MICCAI 2024 in Marrakech" width="1200" height="900" loading="lazy">
</figure>

<div class="hero-inner">
  <div class="hero-copy">
    <h1>Welcome</h1>
    <p class="hero-tagline">Chair of AI in Healthcare and Medicine</p>
    <p class="hero-lead">Our interdisciplinary team from computer science, engineering and medicine develops
    algorithms and methods for the analysis and interpretation of biomedical data.</p>
  </div>
</div>

<button class="hero-arrow hero-prev" type="button" aria-label="Previous photo">&lsaquo;</button>
<button class="hero-arrow hero-next" type="button" aria-label="Next photo">&rsaquo;</button>
<div class="hero-dots" id="hero-dots"></div>

</div>

In addition to creating new and pioneering approaches in the fields of data science, artificial intelligence (AI) and machine learning (ML), clinical translation to improve medical care and thus provide concrete benefits for patients is another research focus of the Chair.

The Chair focuses on basic research in the following areas
- AI for the early detection, prediction and diagnosis of diseases
- AI for personalized interventions and therapies
- AI for the identification of new biomarkers and targets for therapy 
- safe, robust and interpretable AI approaches
- AI approaches to preserve privacy

We are particularly interested in applications in medical imaging and radiology. One focus is neuroradiology, e.g. better understanding of brain development (in utero and ex utero) and improving the diagnosis and stratification of patients with dementia, stroke and traumatic brain injury. In addition, applications for the detection and diagnosis of cardiovascular diseases and cancer are another research focus.

Find our lab on [LinkedIn](https://www.linkedin.com/company/tum-aim-lab) and [Bluesky](https://bsky.app/profile/tum-aim-lab.bsky.social).

We currently have no vacancies for PhD students or post-docs.

<script>
/* Welcome carousel. Progressive enhancement: with JavaScript off the first
   photograph stays put and the section reads exactly as it should - the arrows
   and dots are the only things that stop working. */
(function () {
  var band = document.getElementById('hero-band');
  if (!band) return;
  var shots = Array.prototype.slice.call(band.querySelectorAll('.hero-shot'));
  var dots = document.getElementById('hero-dots');
  if (shots.length < 2) return;
  var at = 0;

  shots.forEach(function (s, i) {
    var b = document.createElement('button');
    b.type = 'button';
    b.setAttribute('aria-label', 'Show photo ' + (i + 1) + ' of ' + shots.length);
    b.addEventListener('click', function () { go(i); });
    dots.appendChild(b);
  });

  function go(i) {
    at = (i + shots.length) % shots.length;
    shots.forEach(function (s, j) { s.classList.toggle('is-on', j === at); });
    Array.prototype.forEach.call(dots.children, function (b, j) {
      b.setAttribute('aria-current', j === at ? 'true' : 'false');
    });
  }
  band.querySelector('.hero-prev').addEventListener('click', function () { go(at - 1); });
  band.querySelector('.hero-next').addEventListener('click', function () { go(at + 1); });

  band.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowLeft') { go(at - 1); }
    if (e.key === 'ArrowRight') { go(at + 1); }
  });

  var x0 = null;
  band.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, {passive: true});
  band.addEventListener('touchend', function (e) {
    if (x0 === null) { return; }
    var dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 40) { go(at + (dx < 0 ? 1 : -1)); }
    x0 = null;
  });

  go(0);
})();
</script>
