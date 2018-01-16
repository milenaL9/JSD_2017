from jinja2.environment import Environment
from jinja2.loaders import PackageLoader
from execute.execute import execute
from root import root
import os


def generate(template_name, output_name, render_vars):
    env = Environment(trim_blocks = True, lstrip_blocks = True, loader = PackageLoader("generation", "templates"))
    env.filters['covertComponentType'] = covertComponentType
    template = env.get_template(template_name) #ucitavamo template
    rendered = template.render(render_vars) #renderujemo prosledjujuci varijable, tj. ecample.png
    print(rendered)
    #i pisemo u fajl
    file_name = os.path.join(root, "output", output_name)
    print(file_name)
    with open(file_name, "w+") as f:
        f.write(rendered)

#2)Napisati filter kojim se konvertuje tip komponente (componentType) u tip input polja (text,
#checkbox...) i iskoristiti ga za zadavanje type atributa pri generisanju. U example.forms dodati i jedan
#checkbox.
def covertComponentType(componentType):
    if (componentType == 'TextField') or (componentType == 'TextArea'):
        type = 'text'
    elif componentType == 'Checkbox':
        type = 'checkbox'

    return type

#kreiranje textX modela(example.png)
#prosledjujemo putanju do tx fajla
#generate - naziv templatea koji se evaluira ... i recnik varijabli koji ce se proslediti samom templateu
def main(debug = False):
    
    model = execute(os.path.join(root, "forms"), 'forms.tx', 'example.form', debug, debug)
    generate("form_template.html", "form.html", {"html" : model}) #ovde smo naveli naziv output fajla
    
if __name__ == '__main__':
    main(True)

