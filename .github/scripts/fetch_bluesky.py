"""Fetch the lab's recent Bluesky posts into data/bluesky.json.

Run in CI before Hugo builds. Images are downloaded into
static/media/bluesky/ and referenced locally, so a visitor's browser never
contacts Bluesky and no third party sees their IP address - which is what
lets this sit on a university page without a new privacy disclosure.

The public AT Protocol API needs no key and no account.

    python3 .github/scripts/fetch_bluesky.py [handle]

If the fetch fails the script leaves the existing data in place and exits 0,
so a Bluesky outage can never fail a deploy.
"""

import hashlib
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.request

HANDLE = sys.argv[1] if len(sys.argv) > 1 else "tum-aim-lab.bsky.social"
API = "https://public.api.bsky.app/xrpc"
LIMIT = 8
ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "bluesky.json"
MEDIA = ROOT / "static" / "media" / "bluesky"
UA = {"User-Agent": "aim-lab-website (+https://aim-lab.io)"}


def get(url, raw=False):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45) as r:
        return r.read() if raw else json.load(r)


def save_image(url, stem):
    """Copy an image into static/ and return its site-relative path."""
    if not url:
        return ""
    try:
        blob = get(url, raw=True)
    except Exception as exc:
        print(f"::warning::could not download {url}: {exc}")
        return ""
    MEDIA.mkdir(parents=True, exist_ok=True)
    name = f"{stem}-{hashlib.sha1(url.encode()).hexdigest()[:8]}.jpg"
    (MEDIA / name).write_bytes(blob)
    return f"/media/bluesky/{name}"


def main():
    try:
        profile = get(f"{API}/app.bsky.actor.getProfile?actor={HANDLE}")
        feed = get(
            f"{API}/app.bsky.feed.getAuthorFeed"
            f"?actor={HANDLE}&limit={LIMIT}&filter=posts_no_replies"
        )["feed"]
    except (urllib.error.URLError, urllib.error.HTTPError, KeyError, ValueError) as exc:
        print(f"::warning::Bluesky fetch failed ({exc}); keeping the existing feed.")
        return 0

    posts = []
    for item in feed:
        post = item["post"]
        record = post.get("record", {})
        embed = post.get("embed") or {}
        kind = embed.get("$type", "")
        rkey = post["uri"].rsplit("/", 1)[-1]
        image, alt, external = "", "", None
        if "images" in kind and embed.get("images"):
            first = embed["images"][0]
            image = save_image(first.get("thumb"), rkey)
            alt = first.get("alt", "")[:200]
        elif "external" in kind:
            ext = embed["external"]
            external = {"title": ext.get("title", "")[:120], "url": ext.get("uri", "")}
            image = save_image(ext.get("thumb"), rkey)
        posts.append({
            "text": record.get("text", ""),
            "date": record.get("createdAt", "")[:10],
            "url": f"https://bsky.app/profile/{profile['handle']}/post/{rkey}",
            "image": image,
            "alt": alt,
            "external": external,
            "likes": post.get("likeCount", 0),
            "reposts": post.get("repostCount", 0),
            "replies": post.get("replyCount", 0),
        })

    data = {
        "profile": {
            "name": profile.get("displayName", HANDLE),
            "handle": profile["handle"],
            "url": f"https://bsky.app/profile/{profile['handle']}",
            "avatar": save_image(profile.get("avatar"), "avatar"),
            "followers": profile.get("followersCount", 0),
        },
        "posts": posts,
    }
    DATA.parent.mkdir(parents=True, exist_ok=True)
    DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {DATA.relative_to(ROOT)} with {len(posts)} posts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
