# Avilo

**(road to 100 million evaluation)**

Avilo is an educational SaaS app for children, built as a native iOS app.

## Stack

- **Client:** Swift + SwiftUI (iOS 17+), Xcode
- **Backend:** Supabase (Postgres, Auth, Storage)
- **Subscriptions:** StoreKit 2 (family/school plans)
- **Analytics:** privacy-first, COPPA-compliant (no third-party ad trackers)

## Getting started

1. Clone: `git clone https://github.com/arminnnkarimiii/Avilo.git`
2. Open `Avilo.xcodeproj` in Xcode (added in the first app commit).
3. Create a branch per task, open a PR, and have your collaborator review.

## Folder map

```
avilo/
├── assets/avi/
│   ├── poses/               12 original Avi poses (white background)
│   ├── poses-transparent/   the same poses, transparent (use in the app)
│   └── wardrobe/            avi-base.png + 14 outfits + placements.json
├── content/
│   └── activities.json      480 activities (8 worlds × 3 age bands × 20)
├── design/
│   └── screens/             the 17 canvas screens, numbered in app order (read-only copies)
├── docs/
│   └── PLAN.md              all product decisions
├── scripts/
│   └── build_catalog.py     regenerates content/activities.json
├── CLAUDE.md                rules for Claude Code
└── README.md
```

Live designs: [Design system](https://claude.ai/artifact/N7TC8gcLqnGgG4VnR2LDom) · [App screens canvas](https://claude.ai/artifact/BZJyrBo6UDQA6NaEGRfWNv). The SwiftUI app will go in `app/`.

## Principles

- Child safety and privacy first (COPPA, Apple Kids Category guidelines).
- Simple, playful, accessible UI.
- Small, reviewed PRs.