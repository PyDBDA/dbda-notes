import argparse
import os
import re
import unicodedata

import nbconvert
import nbformat
import jinja2


def _slugify(s, max_len=None):
    s = unicodedata.normalize('NFKD', s.lower())
    s = re.sub(r'\W+', '-', s)
    return s[:max_len]


def notebook_to_html(notebook_file):
    notebook = nbformat.read(notebook_file, nbformat.NO_CONVERT)
    html_exporter = nbconvert.HTMLExporter()
    (body, resources) = html_exporter.from_notebook_node(notebook)
    return body


def convert_notebooks(notebook_files, dest):
    os.makedirs(dest, exist_ok=True)

    output_fnames = []
    for notebook_file in notebook_files:
        path, fname = os.path.split(notebook_file)
        fname, ext = os.path.splitext(fname)
        output_fname = '%s.html' % _slugify(fname)
        output_fnames.append((fname, output_fname))

        output_file = os.path.join(dest, output_fname)
        with open(output_file, 'wt') as f:
            f.write(notebook_to_html(notebook_file))

    return output_fnames


def write_index(html_files, template_file, dest):
    template = jinja2.Template(open(template_file).read())
    html = template.render(html_files=html_files)
    output_file = os.path.join(dest, 'index.html')

    with open(output_file, 'wt') as f:
        f.write(html)

    return html


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert notebooks to html')
    parser.add_argument('sources', metavar='source', nargs='+',
            help='.ipynb source files to convert')
    parser.add_argument('--dest', '-d', default='docs/',
            help='destination directory for html output')
    parser.add_argument('--template', '-t',
            help='path for the index template')
    args = parser.parse_args()

    html_files = convert_notebooks(args.sources, args.dest)

    template = (args.template if args.template
            else os.path.join(args.dest, '_index.jinja2'))

    write_index(html_files, template, args.dest)
