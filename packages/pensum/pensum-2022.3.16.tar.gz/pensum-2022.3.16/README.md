# Pensum

Pense-bête de lignes de commande… en ligne de commande, inspiré
par TaskWarrior.

Chaque entrée (note) du pense-bête est en Mardown.

La commande `pm` permet de naviguer parmi ces notes et aussi de les exporter.

Chaque note du pense-bête est/peut être constitué de :

- Un titre
- Une liste de tags. Les tags de pensum peuvent gérer une variante au pluriel.
- Une commande « principale ». C’est la commande qui vous semble la plus appropriée et rapide.
- Une discussion. Dans cette section, vous pouvez indiquer des alternatives, etc.

[Un exemple de notes](example/base/build.md)

## Ce qu’est / n’est pas Pensum

Pensum est :

- Un pense-bête
- Un générateur de documentation *personnelle*

Pensum n’est pas :

- Un système de documentation complet. Pensum n’est pas `sphinx`, etc.

## Usage

```bash
pm ls [<tag>]
pm cat <note_id> [-d] [-s] [-t]
pm new <note_id> [<note_title>]
pm find <request>
pm build <format> [<output_folder>] [--verbose]
pm option (set|get) [<option_name>] [<option_value>] [--verbose]
pm help [<topic>]
```

### list

```bash
$ pm ls disques

                                    Notes
 ┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
 ┃ ID           ┃ Title                                 ┃              Tags ┃
 ┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
 │ voir-disques │ Voir les disques/partitions montables │ disque, partition │
 └──────────────┴───────────────────────────────────────┴───────────────────┘
```

### cat

```bash
$ pm cat build

 ╔═══════════════════════════════════════════════════════════════════════════╗
 ║                            Build Pensum notes                             ║
 ╚═══════════════════════════════════════════════════════════════════════════╝

 How to build Pensum notes in HTML and other formats.


                                    Command

 ┌───────────────────────────────────────────────────────────────────────────┐
 │ psm build html mynotes/                                                   │
 └───────────────────────────────────────────────────────────────────────────┘


                                  Discussion

  • mynotes/ is the output folder for your “compiled” notes.
  • html is the output format

 For more information during the building process, add --verbose.

 To list available build formats, use the help command :

 ┌───────────────────────────────────────────────────────────────────────────┐
 │ $ psm help buildformats                                                   │
 └───────────────────────────────────────────────────────────────────────────┘
```

### search

#### Search by tag

```bash
$ pm find @pensum

                     Notes
 ┏━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
 ┃ ID    ┃ Title              ┃          Tags ┃
 ┡━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
 │ build │ Build Pensum notes │ pensum, build │
 └───────┴────────────────────┴───────────────┘
```

#### Search by title

```bash
$ pm find "notes"

                     Notes
 ┏━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
 ┃ ID    ┃ Title              ┃          Tags ┃
 ┡━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
 │ build │ Build Pensum notes │ pensum, build │
 └───────┴────────────────────┴───────────────┘
```

### build

Exporter toutes les notes en HTML dans le dossier `foo` :

```bash
psm build html foo/
```

## Installation

### Prérequis

- [docopt](https://github.com/docopt)
- [appdirs](https://pypi.org/project/appdirs/)
- [rich](https://pypi.org/project/rich/)
- [pypandoc](https://pypi.org/project/pypandoc/)
- [stop-words](https://pypi.org/project/stop-words/)

### Via PIP

```bash
pip install pensum
```

### Via les sources

Installez le `wheel` présent dans `downloads` :

```
sudo pip3 install downloads/pensum-[VERSION]-py3-none-any.whl
```

---

Pour créer et installer le paquet python :

```
make install
```

## Configurer

## Contribuer

### Créer un format d’export

Se référer au fichier [builders.py](pensum/builders.py), particulièrement aux 
classes `pensum.builders.Builder` et `pensum.builders.HTML` pour un exemple.

Une fois la classe de génération intégrée, ajouter le format à 
`pensum.builders.FORMATS`.
