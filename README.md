# md2pdfy
Convert markdown files into PDF format. This tool uses Chrome printing functionality, so rendered PDFs look good.
Output files can be styled with CSS and page properties (margins, scale, etc.) can be specified.

# Installation
You can install this package via pip:
```
pip install md2pdfy
```
This program uses Chrome to render PDFs, so you must have *Google Chrome* and its *WebDrivers* installed.
Correct version of WebDrivers can be installed automatically from this package too, like this:
```
md2pdfy . --install-driver
```
Before running this program, installed **WebDrivers must be added to PATH**. 
After you do that, you can convert one or multiple md files to pdf with calling `md2pdfy` command.

# Usage
Typical usage of this tool looks something like this:
```
md2pdfy example1.md example2.md --css-style style.css --landscape -o result.pdf
```
For the full list of command-line options and arguments, see below:
```
usage: md2pdfy [-h] [-o OUTPUT] [-i] [-cpdf] [-chtml] [-css CSS_STYLE] [-pw PAPER_WIDTH]
               [-ph PAPER_HEIGHT] [-mt MARGIN_TOP] [-mb MARGIN_BOTTOM] [-ml MARGIN_LEFT]
               [-mr MARGIN_RIGHT] [-nobg] [-s SCALE] [--prefer-css-page-size] [-l]
               md_file [md_file ...]
                   
Compile an e-book in PDF format from multiple markdown files

positional arguments:
  md_file               input markdown file name

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output merged pdf file name
  -i, --install-driver  installs required web driver version and quits, ignoring other
                        arguments
  -cpdf, --create-pdf   creates pdf file for each md file in the separate_pdfs folder
  -chtml, --create-html
                        creates html file for each md file in the separate_htmls folder, be
                        aware that moving these html files break image references
  -css CSS_STYLE, --css-style CSS_STYLE
                        path to css file if you want to change the style of generated htmls
  -pw PAPER_WIDTH, --paper-width PAPER_WIDTH
                        paper width in inches. defaults to 8.5 inches
  -ph PAPER_HEIGHT, --paper-height PAPER_HEIGHT
                        paper height in inches. defaults to 11 inches
  -mt MARGIN_TOP, --margin-top MARGIN_TOP
                        top margin in inches. defaults to 0 inches
  -mb MARGIN_BOTTOM, --margin-bottom MARGIN_BOTTOM
                        bottom margin in inches. defaults to 0 inches
  -ml MARGIN_LEFT, --margin-left MARGIN_LEFT
                        left margin in inches. defaults to 0 inches
  -mr MARGIN_RIGHT, --margin-right MARGIN_RIGHT
                        right margin in inches. defaults to 0 inches
  -nobg, --no-background
                        do not print background graphics
  -s SCALE, --scale SCALE
                        scale of the webpage rendering. defaults to 1
  --prefer-css-page-size
                        whether or not to prefer page size as defined by css. defaults to
                        false, in which case the content will be scaled to fit the paper size
  -l, --landscape       paper orientation. defaults to false
```
