+++
# News on the homepage: the featured posts as a grid of tiles, the newest one
# large, with the lab's Bluesky feed beside them. Every post is at /news/;
# `featured: true` in a post's front matter puts it here.

widget = "news_grid"
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 35  # Order that this section will appear.

title = "News"
subtitle = ""

[content]
  # How many posts to show.
  count = 5

  # The lab's Bluesky posts beside the list, read from data/bluesky.json,
  # which .github/scripts/fetch_bluesky.py refreshes at deploy time.
  bluesky_feed = true

  [content.filters]
    # Only posts marked `featured: true`.
    featured = true

[design.background]
  # Apply a background color, gradient, or image.
  #   Uncomment (by removing `#`) an option to apply it.
  #   Choose a light or dark text color by setting `text_color_light`.
  #   Any HTML color name or Hex value is valid.

  # Background color.
  # color = "navy"

  # Background gradient.
  # gradient_start = "DeepSkyBlue"
  # gradient_end = "SkyBlue"

  # Background image.
  # image = "background.jpg"  # Name of image in `static/media/`.
  # image_darken = 0.6  # Darken the image? Range 0-1 where 0 is transparent and 1 is opaque.

  # Text color (true=light or false=dark).
  # text_color_light = true

[advanced]
 # Custom CSS.
 css_style = ""

 # CSS class.
 css_class = ""
+++
