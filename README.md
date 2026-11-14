# Bar Menu Builder - Cherry Street

A one-page app for Andolini's Cherry Street managers to edit the Bar Vitelli drink menu (front and back) and print it on 8.5 x 11 paper.

## Using it

Open `index.html` in Chrome, or the GitHub Pages address once Pages is turned on for this repo. Edit on the left, check the page on the right, then press **Print this side** or **Print both sides** and choose "Save as PDF" or a printer.

- Changes are saved in the browser on that computer only.
- **History** keeps a version each time someone prints or presses **Save version** (newest 60).

## Changing the app

`index.html` is generated. Edit the files in `src/` and rebuild:

```
python3 src/build.py
```

| File | What it is |
|---|---|
| `src/template.html` | The app: styles, editor and page layout |
| `src/seed.json` | The starting menu (Cherry Street front and back) |
| `src/logo.svg`, `src/wm.txt` | Toolbar logo and the page watermark |
| `src/*.woff2` | Fonts, embedded into `index.html` at build time |

Fonts are Montserrat and Sofia Sans Extra Condensed, both free under the SIL Open Font License. They stand in for the Gotham cuts used in the original Figma menus, so the print is close to the originals but not identical.
