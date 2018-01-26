from jinja2.environment import Environment
from jinja2.loaders import PackageLoader
from execute.execute import execute
from root import root
import os

def generate(template_name, output_name, render_vars):
    env = Environment(trim_blocks=True, lstrip_blocks=True, loader=PackageLoader("generation", "templates"))
   # env.filters['readFromFile'] = readFromFile
    template = env.get_template(template_name)
    rendered = template.render(render_vars)
    print(rendered)
    # i pisemo u fajl
    file_name = os.path.join(root, "output", output_name)
    print(file_name)
    with open(file_name, "w+") as f:
        f.write(rendered)

def readFromFile():
    filenameR = os.path.abspath("../forms/forms.tx")
    fileR = open(filenameR, 'r')

    filenameW = os.path.abspath("../generation/templates/form_gramatika.html")
    fileW = open(filenameW, 'w')

    fileW.write('{% extends "base.html" %}')
    fileW.write('{% block body_content %}')
    fileW.write('<h1>Gramatika rodoslova</h1>')
    for line in fileR:
        fileW.write( line + '<br/>')
    fileW.write('{% endblock %}')

    fileW.close()
    fileR.close()

def noviTip(tip):
    filename = os.path.abspath("../output/gramatikaSaNovimTipom.html")
    file = open(filename, 'a+')
    for line in file:
        if line.contains('TitulaTip:'):
            file.write("'" + tip + "'")
    file.close()

def main(debug=False):
    model = execute(os.path.join(root, "forms"), 'forms.tx', 'example.form', debug, debug)
    generate("form_template.html", "form.html", {"rodoslov": model})
    readFromFile()
    generate("form_gramatika.html", "gramatika.html", {"rodoslov": model})
    noviTip('kralj')

if __name__ == '__main__':
    main(True)
