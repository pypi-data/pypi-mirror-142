# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['concise_concepts',
 'concise_concepts.conceptualizer',
 'concise_concepts.examples']

package_data = \
{'': ['*'], 'concise_concepts': ['.pytest_cache/*', '.pytest_cache/v/cache/*']}

install_requires = \
['gensim>=4,<5', 'spacy>=3,<4']

setup_kwargs = {
    'name': 'concise-concepts',
    'version': '0.1.0',
    'description': 'This repository contains an easy and intuitive approach to zero-shot and few-shot NER using internal spaCy embeddings.',
    'long_description': '# Concise Concepts\nWhen wanting to apply NER to concise concepts, it is really easy to come up with examples, but pretty difficult to train an entire pipeline. Concise Concepts uses word similarity based on few-shots to get you going with easy!\n\n# Install\n``` pip install classy-classification```\n\n# Quickstart\n```\nimport spacy\nimport concise_concepts\n\ndata = {\n    "fruit": ["apple", "pear", "orange"],\n    "vegetable": ["broccoli", "spinach", "tomato"],\n    "meat": ["chicken", "beef", "pork", "fish", "lamb"]\n}\n\ntext = """\n    Heat the oil in a large pan and add the Onion, celery and carrots. \n    Cook over a medium–low heat for 10 minutes, or until softened. \n    Add the courgette, garlic, red peppers and oregano and cook for 2–3 minutes.\n    Later, add some oranges and chickens. """\n\nnlp = spacy.load(\'en_core_web_lg\')\nnlp.add_pipe("concise_concepts", config={"data": data})\ndoc = nlp(text)\n\nprint([(ent.text, ent.label_) for ent in doc.ents])\n# Output:\n#\n# [(\'Onion\', \'VEGETABLE\'), (\'Celery\', \'VEGETABLE\'), (\'carrots\', \'VEGETABLE\'), \n#  (\'garlic\', \'VEGETABLE\'), (\'red peppers\', \'VEGETABLE\'), (\'oranges\', \'FRUIT\'), \n#  (\'chickens\', \'MEAT\')]\n\n',
    'author': 'David Berenstein',
    'author_email': 'david.m.berenstein@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pandora-intelligence/concise-concepts',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
