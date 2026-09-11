# AI in Medicine — lab website

Hugo site for the AI in Medicine lab at TUM, built on
[Wowchemy](https://github.com/wowchemy/wowchemy-hugo-modules) (the theme formerly known as
Hugo Academic).

Published at **https://aimlab-tum.github.io/**. Moving `aim-lab.io` here is the last step of
the migration off the old two-repository setup — see [MIGRATION.md](MIGRATION.md).

**You never build this site by hand.** Push a change and GitHub Actions builds and deploys it.
No generated HTML lives in this repo.

## Contributing without write access

Lab members do not need to be repository collaborators. They can file a
[form](.github/ISSUE_TEMPLATE/new-member.yml) to add or update a profile, which a maintainer
turns into a pull request with one label, or edit any file through GitHub's web editor, which
forks and opens a pull request for them automatically. See [CONTRIBUTING.md](CONTRIBUTING.md), and [WORKFLOW.md](WORKFLOW.md)
for diagrams of how publishing and contributing actually flow.

## Publishing a change

1. Edit a Markdown file under `content/` — on a branch, or directly in the GitHub web editor.
2. Open a pull request. The **Build check** workflow builds the site and fails the PR if you
   broke something. The built site is attached to the run as a downloadable artifact.
3. Merge to `main`. The **Deploy site** workflow builds and publishes to GitHub Pages, usually
   within a couple of minutes.

That's it. There is no second repo to push to and no local Hugo to keep in sync.

## Where things live

| What | Where |
|---|---|
| Homepage sections (news, people, research, teaching, vacancies, contact) | `content/home/*.md` |
| Research areas (the Research carousel) | `content/research/<area>/index.md` (+ `figure.png`) |
| Team member profiles | `content/authors/<Name>/_index.md` (+ `avatar.jpg`) |
| Publications | `content/publication/` |
| Blog / news posts | `content/post/` |
| Open theses | `content/theses/` |
| Site title, base URL, taxonomies | `config/_default/config.toml` |
| Theme options, colours, contact details | `config/_default/params.toml` |
| Navigation menu | `config/_default/menus.toml` |
| Custom styling | `assets/scss/custom.scss` |
| Custom widget templates | `layouts/partials/widgets/` |
| Shortcodes | `layouts/shortcodes/` |
| Images and files served as-is | `static/` |

## Running it locally (optional)

You only need this for a live preview while editing. If you skip it, the **Build check** on
your pull request attaches the built site to the run as a downloadable artifact, which gets
you the same thing without installing anything.

### What you need

**Hugo 0.74.3 extended** and **Go 1.19**, the versions the workflows pin. Go has to be on your
PATH because the theme is pulled as a Hugo Module rather than vendored into the repository.

Both are old enough that a package manager will hand you something newer. Use the pinned ones,
so what you see locally is what the deploy produces — the theme is from 2020 and nothing later
has been tried against it. Fetch them and keep them out of the way:

```bash
mkdir -p ~/.local/opt/aimlab-toolchain && cd ~/.local/opt/aimlab-toolchain

curl -sSL -o go.tgz https://go.dev/dl/go1.19.13.linux-amd64.tar.gz
tar xzf go.tgz && rm go.tgz

curl -sSL -o hugo.tgz \
  https://github.com/gohugoio/hugo/releases/download/v0.74.3/hugo_extended_0.74.3_Linux-64bit.tar.gz
tar xzf hugo.tgz hugo && rm hugo.tgz
```

On macOS, swap `linux-amd64` for `darwin-arm64` (or `darwin-amd64`) and
`Linux-64bit` for `macOS-64bit`. Then put both on your PATH for the session:

```bash
export PATH="$HOME/.local/opt/aimlab-toolchain:$HOME/.local/opt/aimlab-toolchain/go/bin:$PATH"
```

It must be the **extended** build of Hugo. The plain build has no SCSS support and stops with
`TOCSS ... you need to install Hugo Extended` before it renders anything.

### Start it

```bash
./view.sh          # hugo server --disableFastRender --i18n-warnings
```

Then open <http://localhost:1313>. The first run spends a while pulling the theme module down
through Go; after that a rebuild is well under a second and the page reloads itself.

### Viewing it from another machine

`view.sh` binds to localhost, so a server you are working on over SSH is not reachable from
your laptop's browser. Tunnel to it rather than exposing the port:

```bash
ssh -N -L 1313:localhost:1313 you@the-server      # run this on your laptop
```

Then open <http://localhost:1313> locally. Live reload works through the tunnel.

### Building the way the deploy does

To check what CI will produce, without touching the running server:

```bash
HUGO_ENV=production HUGO_RESOURCEDIR=/tmp/aimlab-res \
  hugo --gc --minify -b "https://aimlab-tum.github.io/" -d /tmp/aimlab-build
```

`HUGO_RESOURCEDIR` matters. Hugo caches compiled SCSS in `resources/`, and `--gc` collects
what the running `hugo server` is still holding open — the server then 500s until you restart
it. Pointing the build at its own directory keeps the two apart. (`--resourceDir` is not a
flag in 0.74.3; it has to be the environment variable.)

### Two things that will confuse you

**Editing a research area does not live-reload.** `content/research/` is rendered into the
homepage by a shortcode that reads another section, and Hugo's dependency tracking does not
follow that, so the page will not update. Restart `./view.sh`. Every other kind of content
reloads normally, and a deploy build is always complete.

**`public/` is not the site.** It is gitignored and nothing in the repository is generated.
If you see stale output, you are looking at a build directory, not at what deploys.

## Adding something

Everything is Markdown with TOML front matter. The table above says where each kind lives; the
three common ones:

| To add | Do this |
|---|---|
| A person | A folder under `content/authors/` with an `_index.md` and an `avatar.jpg`. Or have them file the [form](.github/ISSUE_TEMPLATE/new-member.yml) and label the issue. |
| A publication | A file under `content/publication/`. |
| A research area | A folder under `content/research/` with an `index.md`, and a `figure.png` beside it if there is one. Order is the `weight` in the front matter; the carousel slide, its numbering and its anchor build themselves. `content/research/opportunistic-cardiac-mri/index.md` is a `draft` that shows every option with a comment on each, so copy that one. |

## How deployment works

`.github/workflows/deploy.yml` runs on every push to `main`:

```
push to main → checkout → Go 1.19 + Hugo 0.74.3-extended → hugo --gc --minify
             → upload-pages-artifact → deploy-pages → live site
```

Pages is configured with **Settings → Pages → Source: GitHub Actions**, so the deploy comes
from the workflow artifact rather than from a branch. `public/` is gitignored and exists only
on the runner.

Hugo and Go versions are pinned in both workflows to the versions the site was originally built
with. Bump them in a pull request so the build check tells you whether the upgrade is safe.

## Notes

- `static/admin/` is a Netlify CMS admin UI shipped by the `netlify-cms-academic` module. It
  needs Netlify Identity / git-gateway to work and is not wired up on GitHub Pages.
- `static/CNAME` claims the custom domain `aim-lab.io`. It lives in `static/` because Hugo
  only copies that directory into the build — a `CNAME` at the repository root would never
  reach the deployed site, and the custom domain would be dropped on the next deploy. See
  [MIGRATION.md](MIGRATION.md).
