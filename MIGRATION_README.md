# Data Migration Instructions

This script migrates your content from the legacy WordPress (Divi) site to the new 3D Web Experience.

## Prerequisites
1.  **Export XML**: Go to your WordPress Admin -> Tools -> Export -> Content (All). Download the XML file.
2.  **Place File**: Save the file as `data/export.xml` in this project folder (or anywhere else).

## How to Run

Open your terminal and run:

```bash
# Default (looks for ./data/export.xml)
node scripts/migrate-divi.js

# Custom Path
node scripts/migrate-divi.js ./path/to/your-file.xml
```

## What it does
1.  **Cleans Divi Shortcodes**: Strips `[et_pb_section]` and other Divi tags, keeping your text clean.
2.  **Optimizes Images**: Downloads featured images and converts them to optimized WebP format in `public/images/posts/`.
3.  **Maps Categories**: Translates old categories to the new "Scientific" tags.
4.  **Generates Data**: Updates `src/data/posts.json` which instantly updates the Blog Listing and 3D Cards.
