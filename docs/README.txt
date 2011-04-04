dolmen.template
***************

`dolmen.template` makes it possible to use chameleon templates in dolmen views.

Currently support for chameleon genshi templates and chameleon zope
page templates is provided.

For more information on Grok and Chameleon templates see:

- http://grok.zope.org/
- http://chameleon.repoze.org/
- http://pypi.python.org/pypi/Chameleon
- http://pypi.python.org/pypi/chameleon.genshi

.. contents::

Requirements
============

- Chameleon templates (`Chameleon`).
- Chameleon genshi templates (`chameleon.genshi`).
- dolmen.view

Installation
============

To use Chameleon page templates with dolmen all you need is to install
dolmen.template as an egg and include its ZCML. The best place to do
this is to make `dolmen.template` a dependency of your application by
adding it to your ``install_requires`` list in ``setup.cfg``. If you
used dolmenproject to create your application ``setup.py`` is located in the
project root. It should look something like this::

   install_requires=['setuptools',
                     'dolmen.template',
                     # Add extra requirements here
                     ],

Then include ``dolmen.template`` in your ``configure.zcml``. If you
used dolmenproject to create your application it's at
``src/<projectname>/configure.zcml``. Add the include line after the
include line for grok, but before the grokking of the current
package. It should look something like this::

      <include package="dolmen.view" />
      <include package="dolmen.template" />  
      <grok:grok package="." />

If you use ``autoInclude`` in your ``configure.zcml``, you should not
have to do this latter step.

Then run ``bin/buildout`` again. You should now see buildout saying
something like::

   Getting distribution for 'dolmen.template'.
   Got dolmen.template 0.1.

That's all. You can now start using Chameleon page templates in your
Dolmen application.


Usage
=====

To use a template just do this

from dolmen.template import TemplateView, PageTemplate
class MyView(TemplateView):
    template = PageTemplate('templates/myview.cpt')

You can use Chameleon page templates by simply assigning the "template"
class variable of TemplateView to a filename of the Chameleon genshi
templates or Chameleon Zope page templates.  Although chameleon
templates themselves do not have a standard for the file extensions
for templates, Dolmen needs to have an association between an
extension and a type so it knows which type of template each template
is.  `dolmen.template` defines the following extensions:

* ``.cpt`` (``Chameleon page template``) for Chameleon page templates

* ``.cg`` (``Chameleon genshi template``) for chameleon driven genshi
  templates

* ``.cgt`` (``Chameleon genshi text template``) for chameleon driven
  genshi text templates

You can also use Chameleon page templates inline.  The syntax for this
is::

   from dolmen.template.components import ChameleonPageTemplate
   index = ChameleonPageTemplate('<html>the html code</html>') 

Or if you use files::

   from dolmen.template.genshi.components import ChameleonPageTemplateFile
   index = ChameleonPageTemplateFile(filename='thefilename.html')

