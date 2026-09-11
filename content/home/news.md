+++
# A News section created with the Pages widget.
# This section displays recent blog posts from `content/news/`.

widget = "pages"  # See https://sourcethemes.com/academic/docs/page-builder/
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 35  # Order that this section will appear.

title = "News"
subtitle = ""

[content]
  # Page type to display. E.g. post, talk, or publication.
  page_type = "post"
  
  # Choose how much pages you would like to display (0 = all pages)
  # A ceiling rather than the selection itself - the `featured` filter below
  # decides what is eligible. Raise it if there are ever more than five worth
  # showing at once.
  count = 5

  # Show the lab's Bluesky posts beside the news list.
  # Handled by layouts/partials/widgets/pages.html; the feed itself is fetched
  # at deploy time into data/bluesky.json by .github/scripts/fetch_bluesky.py.
  bluesky_feed = true
  
  # Choose how many pages you would like to offset by
  offset = 0

  # Page order. Descending (desc) or ascending (asc) date.
  order = "desc"

  # Always offer the full archive underneath the list, not only when there
  # happen to be more posts than fit. The link points at the post section,
  # which Hugo already generates at /post/.
  [content.archive]
    enable = true
    text = "All news"

  # Filter posts.
  #
  # `featured = true` is what makes this section a selection rather than a feed:
  # only posts carrying `featured: true` in their own front matter appear here.
  # Everything else is still published and still listed under "All news" at
  # /post/ - it just does not claim a place on the homepage.
  #
  # To put a post here, set `featured: true` at the top of it. To take one down,
  # set it back to false. Nothing else moves.
  [content.filters]
    tag = ""
    category = ""
    publication_type = ""
    author = ""
    exclude_featured = false
    featured = true
  
[design]
  # Full width, with the heading above the content - the same layout the
  # Research section uses. Needed because this section now has a sidebar.
  columns = "1"

  # Toggle between the various page layout types.
  #   1 = List
  #   2 = Compact
  #   3 = Card
  #   4 = Citation (publication only)
  view = 2
  
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


