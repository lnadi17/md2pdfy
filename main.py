import argparse
import markdown
import random
from pdfy import Pdfy
from os import path, mkdir, remove
from glob import glob
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from PyPDF2 import PdfFileMerger
from string import ascii_lowercase
from shutil import copy2, move


def main():
    parser = argparse.ArgumentParser(description="Compile an e-book in PDF format from multiple markdown files")
    parser.add_argument('md_file',
                        help='input markdown file name',
                        type=str,
                        nargs='+')
    parser.add_argument('-o', '--output',
                        help="output merged pdf file name",
                        type=str,
                        default="book")
    parser.add_argument('-i', '--install-driver',
                        help="installs required web driver version and quits, ignoring other arguments",
                        action='store_true')
    parser.add_argument('-cpdf', '--create-pdf',
                        help="creates pdf file for each md file in the separate_pdfs folder",
                        action='store_true')
    parser.add_argument('-chtml', '--create-html',
                        help="creates html file for each md file in the separate_htmls folder, "
                             "be aware that moving these html files break image references",
                        action='store_true')
    parser.add_argument('-css', '--css-style',
                        help="path to css file if you want to change the style of generated htmls",
                        type=str)
    parser.add_argument('-pw', '--paper-width',
                        help="paper width in inches. defaults to 8.5 inches",
                        type=float,
                        default=8.5)
    parser.add_argument('-ph', '--paper-height',
                        help="paper height in inches. defaults to 11 inches",
                        type=float,
                        default=11)
    parser.add_argument('-mt', '--margin-top',
                        help="top margin in inches. defaults to 0 inches",
                        type=float,
                        default=0)
    parser.add_argument('-mb', '--margin-bottom',
                        help="bottom margin in inches. defaults to 0 inches",
                        type=float,
                        default=0)
    parser.add_argument('-ml', '--margin-left',
                        help="left margin in inches. defaults to 0 inches",
                        type=float,
                        default=0)
    parser.add_argument('-mr', '--margin-right',
                        help="right margin in inches. defaults to 0 inches",
                        type=float,
                        default=0)
    parser.add_argument('-nobg', '--no-background',
                        help="do not print background graphics",
                        action="store_false")
    parser.add_argument('-s', '--scale',
                        help="scale of the webpage rendering. defaults to 1",
                        type=float,
                        default=1)
    parser.add_argument('--prefer-css-page-size',
                        help="whether or not to prefer page size as defined by css. "
                             "defaults to false, in which case the content will be scaled to fit the paper size",
                        action='store_true')
    parser.add_argument('-l', '--landscape',
                        help="paper orientation. defaults to false",
                        action="store_true")
    args = parser.parse_args()

    if args.install_driver:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        return

    input_files = []
    # expand wildcard if program is called from windows shell
    # (linux shell expands wildcards by itself, but it doesn't break the code)
    if len(args.md_file) == 1:
        for arg in glob(args.md_file[0]):
            input_files.append(arg)
    else:
        for arg in args.md_file:
            if path.exists(arg):
                input_files.append(arg)
    if not input_files:
        raise Exception("Sorry, input files don't exist or they're entered incorrectly")

    p = Pdfy()
    pdf_names = []
    for file in input_files:
        with open(file, 'r', encoding='utf-8') as src:
            markdown_content = src.read()
            html_content = markdown.markdown(markdown_content)
            html_content = change_img_src(html_content, path.join(path.dirname(file), "{}"))

            if args.css_style:
                html_content = str(f'''
                                <!DOCTYPE html>
                                <html>
                                    <head>
                                        <link rel="stylesheet" href="{args.css_style}">
                                    </head>
                                    <body>
                                        {html_content}
                                    </body>
                                </html>''')

            # get the name part of input file
            name = path.splitext(path.basename(file))[0]

            # write html content into file with a random name
            random_name_html = name + '_' + ''.join(random.choices(ascii_lowercase, k=5)) + '.html'
            with open(random_name_html, 'w', encoding="utf-8") as dst:
                dst.write(html_content)

            random_name_pdf = name + '_' + ''.join(random.choices(ascii_lowercase, k=5)) + '.pdf'
            pdf_names.append(random_name_pdf)
            p.html_to_pdf(random_name_html, random_name_pdf, options={"paperWidth": args.paper_width,
                                                                      "paperHeight": args.paper_height,
                                                                      "marginTop": args.margin_top,
                                                                      "marginBottom": args.margin_right,
                                                                      "marginLeft": args.margin_left,
                                                                      "marginRight": args.margin_right,
                                                                      "printBackground": args.no_background,
                                                                      "preferCSSPageSize": args.prefer_css_page_size,
                                                                      "scale": args.scale,
                                                                      "landscape": args.landscape})

            # move temporary htmls into dedicated folder else remove them
            # we'll do the same to the pdfs after merging them
            if args.create_html:
                if not path.exists('separate_htmls/'):
                    mkdir('separate_htmls/')
                # change img sources so they don't break after moving
                with open(random_name_html, 'w', encoding="utf-8") as dst:
                    html_content = change_img_src(html_content, "../{}")
                    dst.write(html_content)
                # move html file into dedicated folder
                move(random_name_html, 'separate_htmls/{}.html'.format(name))
                # if present, copy css file too
                if args.css_style:
                    copy2(args.css_style, 'separate_htmls')
            else:
                remove(random_name_html)

    # merge generated pdfs
    merger = PdfFileMerger()
    for pdf in pdf_names:
        merger.append(pdf)
    merger.write(args.output + '.pdf')
    merger.close()

    for pdf in pdf_names:
        if args.create_pdf:
            if not path.exists('separate_pdfs/'):
                mkdir('separate_pdfs/')
            move(pdf, 'separate_pdfs/{}.pdf'.format(name))
        else:
            remove(pdf)


# changes image source in html string
# example: if previous image src="foo.img" and function argument formatting="../{}", then img src="../foo.img"
def change_img_src(html_string, formatting="{}"):
    # replace image src base paths in generated html string
    bs = BeautifulSoup(html_string, 'html.parser')
    for img in bs.find_all('img'):
        img['src'] = formatting.format(img['src']).replace('\\', '/')
    return str(bs)


if __name__ == '__main__':
    main()
