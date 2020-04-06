# Autosquare

A very small python utility script to call the (rather scary)
ImageMagick's `convert` script

```bash
convert <input> -set option:size '%[fx:min(w,h)]x%[fx:min(w,h)]' xc:none +swap -gravity center -composite <output>
```

as found on [Super User](https://superuser.com/a/635198).

## Quick Start

```bash
git clone https://github.com/mikeevmm/Autosquare
cd Autosquare
bash install.sh
autosquare --help
```
