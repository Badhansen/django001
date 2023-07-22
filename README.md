# django001

To contribute to this project, follow the steps below:
### 1. Clone the repository

```
git clone https://github.com/Badhansen/django001.git
```

### 2. Create your own virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

Virtual environments are where dependencies are stored, similar to `node_modules` in JavaScript. Every time you start your machine, you must activate the virtual environment using `source venv/bin/activate`.

*Here are some useful links that I used to create this project*
- [Install pyenv](https://opensource.com/article/19/5/python-3-default-mac) alternative to `venv` Virtual Environments.
- [Managing pyenv, virtualenv, and pyenv-virtualenv](https://gist.github.com/Badhansen/19100e5548ef154360361ab7f45c183f), this link help me a lot managing all environment and django projects.
- [Interested in pyenv read this as well](https://realpython.com/intro-to-pyenv/)



### 3. Install your requirements

```
pip install -r requirements.txt
```

This will install all the necessary dependencies for the project.

## Development

Before the development and runnig phase, please go to the any of the project and start the server by running:

```bash
python manage.py runserver
```

Remember to activate the virtual environment (`source venv/bin/activate`) or if you are using pyenv (`pyenv activate vname`) every time you work on the project to ensure you're using the correct Python version and dependencies.

## Contribution

If you wish to contribute to this project, please create a new branch and submit a pull request with your changes. We welcome contributions from the community!

## License

This project is licensed under the [MIT License](LICENSE).
```

Feel free to modify and expand the `README.md` file to include any additional information about your project, such as project description, features, usage instructions, or anything else that would be relevant for contributors and users.