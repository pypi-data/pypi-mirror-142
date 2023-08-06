# Pensum build formats

Do all Pensum build configurations with `pm set builders.BUILDFORMAT.settingName VALUE`.

For example, with HTML builder, setting the CSS for every note :

```bash
$ pm option set builders.html.css_note /home/user/pensum_note.css
```

Pensum builders are a combination of Python and Pandoc.

## Build formats

### HTML - `html`
    
Renders notes as HTML pages.

- `html.css_toc` : CSS file for index / table of contents page.
- `html.css_note` : CSS file for note pages.

### DokuWiki - `dokuwiki`

DokuWiki page format.

### MediaWiki - `mediawiki`

MediaWiki page format.

### Pensum - `pensum`

Build Pensum notes into Pensum notes (Markdown). Yes. Mainly an example for developer(s).

