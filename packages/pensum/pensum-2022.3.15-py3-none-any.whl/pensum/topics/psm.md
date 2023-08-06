# Pensum command line : `psm` command

## Getting / Setting Pensum options

Pensum are named after the following syntax :

- `option_name`
- `option_group.option_name`
- `option_group.option_subgroup.option_name`

To get or set options, use `psm option` with the correct operation parameter (`get` or `set`).

> `pensum option get` will output all Pensum options.

To set option, use `psm option` with the following syntax :

```bash
$ psm option set option_name VALUE
$ psm option set option_group.option_name VALUE
$ psm option set option_group.option_subgroup.option_name VALUE
```

Boolean value are set with "yes" or "no" :

```bash
$ psm option set psm.pager.help yes
```

## Search across notes

Use `pensum find` to search across notes.

Search is always case insensitive.

### Search by title

```bash
# Search for notes containing "extract"
$ psm find extract
```

#### Search and user language

In order to Pensum to make better search by notes titles, you might need to set the `lang` option to [your language code](https://en.wikipedia.org/wiki/ISO_639-1).

For example :

```bash
# french / français
$ psm option set lang fr

# spanish / español
$ psm option set lang es
```

### Search by tag

To search notes by tag, prefix your search by `@`.

```bash
# Search for notes with the "PHP" tag.
$ psm find @PHP
```

## Enable/Disable pagers

By default `psm` use a pager only to display help topics like this one.

You can adjust that behaviour with `psm option set psm.pager.COMMAND false_or_true`.

For example :

```bash
# Disable pager in help command
$ psm option set psm.pager.help no

# Enable pager in cat command
$ psm option set psm.pager.cat yes
```

Commands adjustable are `help`, `cat`, `ls` and `search`.

