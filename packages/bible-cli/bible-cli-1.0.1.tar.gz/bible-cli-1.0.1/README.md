# Bible Cli

## Description

This simple CLI tool allows the user to query 5-6 translations of the Bible. It is built on 
Tim Morgan's [Bible API](https://bible-api.com/). The primary packages used are:
- Typer
- Rich
- Requests

## Usage

```
Usage: bible-cli [OPTIONS] BOOK CHAPTER

Arguments:
  BOOK     The book of the bible  [required]
  CHAPTER  The chapter(s) to select. Ex: 1; 1-2  [required]

Options:
  --verses TEXT                   The verse range. Ex: 1-10
  --translation [cherokee|bbe|kjv|web|oeb-cw|webbe|oeb-us|clementine|almeida|rccv]
                                  Translation to use  [default:
                                  Translation.WEB]
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.
  ```

### Example

```
bible-cli john 3 --verses 3 --translation kjv

Reference: John 3:15
Translation: King James Version
 15 ┃ That whosoever believeth in him should not perish, but have eternal life. 
```