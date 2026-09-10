# Making this repository the live lab website

This repository is intended to become the home of the AI in Medicine website. It already
contains everything needed: the Hugo source and a CI pipeline that builds and publishes it.
What remains is switching the public domain over to it.

## Where things stand

| | Repository | Role |
|---|---|---|
| **This repo** | `aimlab-tum/aimlab-tum.github.io` | Source + CI. Publishes to `https://aimlab-tum.github.io/` |
| Old source | `danielrueckert/website_source` | The Hugo project this content came from |
| Old output | `danielrueckert/danielrueckert.github.io` | Built HTML only; currently serves `aim-lab.io` |

The old pair is joined by `public/` being a git **submodule** of the source repo pointing at
the output repo, which is why publishing used to mean building locally with the right Hugo
version and pushing to two repositories in the right order. Miss a step and they drift. The
output repo's `.git` reached 175 MB, and a one-paragraph bio edit rewrote several thousand
generated files, because the nav and author lists are baked into every page.

None of that applies here. `public/` is gitignored, no generated HTML is committed, and
nobody needs Hugo installed.

## What has been verified

Proven on a sandbox copy of this exact tree before it was brought here:

- Hugo **0.74.3-extended** resolves the Oct-2020 Wowchemy modules through the Go proxy with
  no changes to `go.mod`. A full build takes about **50 seconds**.
- The CI build produces a **page-for-page identical** site to production: both sitemaps list
  **242 URLs** and the path sets match exactly.
- The contribution pipeline works end to end: an approved issue becomes a validated,
  built, reviewed pull request.

## Steps to go live on aim-lab.io

1. **Enable Pages.** Settings → Pages → Source: **GitHub Actions**. The `enablement: true`
   flag in `deploy.yml` cannot do this for you — `GITHUB_TOKEN` is refused with
   `Resource not accessible by integration` when creating a Pages site.
2. **Let Actions open pull requests.** Settings → Actions → General → Workflow permissions →
   tick **Allow GitHub Actions to create and approve pull requests**. Without it the member
   request workflow still builds and pushes its branch, but hands you a compare link instead
   of opening the pull request itself.
3. **Create the `approved` label.** It is the gate for the member request workflow. The
   `new-member` and `update-profile` labels are optional — GitHub silently drops labels that
   do not exist, so the workflow also identifies a request from the shape of its body.
4. **Check the site** at `https://aimlab-tum.github.io/` and compare it against `aim-lab.io`.
   The two should be identical apart from absolute URLs.
5. **Move the domain.** Order matters — GitHub will not let two repositories claim one
   domain, and `aim-lab.io` is unreachable in the gap between releasing and reclaiming it.

   1. *(optional, ~30 min ahead)* In Namecheap, lower the TTL on the `www` record from
      `Automatic` (1800 s) to 1-5 minutes, so the later change propagates quickly. Lowering
      a TTL only helps if done before the switch — resolvers keep the old value until the
      old TTL expires.
   2. Remove the custom domain from `danielrueckert/danielrueckert.github.io`
      (Settings → Pages). **This must be first.**
   3. Set `aim-lab.io` as the custom domain here, immediately after.
   4. Merge the `static/CNAME` change, so deploys keep the domain rather than dropping it.
      Do not merge it earlier: deploying a CNAME for a domain another repository still owns
      can fail the deploy.
   5. In Namecheap → Advanced DNS, repoint the `www` CNAME from `danielrueckert.github.io.`
      to `aimlab-tum.github.io.` **Nothing else changes** — the apex `A` records
      (`185.199.108-111.153`) are GitHub's shared Pages IPs and already correct, and the
      `TXT` record is SPF for email forwarding, so deleting it would break mail.
   6. Wait for the TLS certificate, then enable **Enforce HTTPS**. Until it is issued,
      `https://aim-lab.io` returns a certificate error; this is expected.
   7. Restore the `www` TTL to `Automatic` once confirmed.

   `baseurl` in `config/_default/config.toml` is already `https://aim-lab.io/`; CI overrides
   it per build, so it only affects anyone running Hugo locally.

   Worth doing afterwards: verify the domain for the `aimlab-tum` organisation
   (Organization settings → Pages → Verified domains). Neither owner has verified it —
   there is no `_github-pages-challenge-*` TXT record for the domain — and verifying
   prevents anyone else claiming it later.
6. **Archive, do not delete,** `danielrueckert.github.io` and `website_source`. They are the
   rollback: if anything goes wrong, restore the custom domain to the old output repo and the
   site is back within minutes.

## Deliberately not done

Upgrading Wowchemy 5.0.0-beta.0 and Hugo 0.74.3, both from 2020. Versions are pinned in the
workflows so CI reproduces the current site exactly. Do the upgrade **after** the cutover, in
a pull request, so `preview.yml` shows what breaks before it is live rather than after.

## Known content issues, not blockers

- `content/home/publications.md` hardcodes `<img src="/home/*.png">` and `](/author/...)`
  paths. These work at a domain root, and broke only when the site was served from a
  subpath during testing. Worth converting to Hugo shortcodes eventually.
- `static/admin/` is a Netlify CMS UI shipped by the `netlify-cms-academic` module. It needs
  Netlify Identity to function and does nothing on GitHub Pages. Removing it means dropping
  that module import from `config/_default/config.toml`.
- `content/theses/` contains a directory whose name begins with a non-breaking space. It
  builds correctly, but it is a trap for anyone matching on that path.
