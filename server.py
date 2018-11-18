from importlib import import_module

from flask import Flask


app = Flask(__name__)
app.config.from_pyfile('config.cfg')

#put in your app names
moduleNames = ['root']

for module in moduleNames:
    globals()[module] = import_module(module)

for module in moduleNames:
    if module != 'root':
        app.register_blueprint(getattr(globals()[module].urls, module), url_prefix='/' + module, template_folder=module)
    else:
        app.register_blueprint(getattr(root.urls, "root"), url_prefix='/', template_folder='root')

if __name__ == "__main__":
    app.run(host='localhost')
