+++
# The research areas, one directory per area.
#
# Adding an area means adding a folder here with an index.md - no template, no
# stylesheet and no script has to be touched, and nothing is repeated anywhere
# else. The Research section on the homepage renders whatever is in here, in
# `weight` order.
#
# These pages are not published on their own: they are parts of the homepage
# section, and the headings they produce there keep the anchors that the old
# hand-written markup had, so /#ai-for-vision still resolves.
#
# One thing to know when editing these locally: `hugo server` does not notice
# that the homepage depends on them, so a change here will not live-reload.
# Restart ./view.sh to see it. That is Hugo's dependency tracking for a
# shortcode that reads another section, not these build flags - it behaves the
# same when the pages are rendered. A deploy build is always complete.
title = "Research areas"

[_build]
  render = false
  list = "never"

[cascade._build]
  render = false
  list = "local"
+++
