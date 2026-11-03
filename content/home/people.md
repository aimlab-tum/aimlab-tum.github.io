+++
# People on the homepage: the chair, a mosaic of the team's faces, the head
# count per group and a button to the full list at /people/. The full list is
# content/people.md; the groups below are the ones it counts and shows, in
# this order. Alumni and the mental health managers are listed there too, but
# the homepage counts only the current team.

widget = "people_teaser"
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 30  # Order that this section will appear.

title = "People"
subtitle = ""

[content]
  # Choose which groups/teams of users to display.
  #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
  user_groups = ["Chair",
                 "Management",
                 "Senior Researchers",
                 "Researchers",
                 "Collaborators",
                 "Visitors",
                 "Alumni",
                 "Mental Health Managers"]

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
