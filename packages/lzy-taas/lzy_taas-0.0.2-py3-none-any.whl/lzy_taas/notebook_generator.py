import json
from uuid import uuid4


class NotebookGenerator:
    def __init__(self, path=None, notebook_id=None):
        self._nb_path = f"main-{uuid4()}.ipynb" if path is None else path
        self._notebook_id = str(uuid4()) if notebook_id is None else notebook_id

        self._notebook = {
            "nbformat": 4,
            "nbformat_minor": 5,
            "metadata": {
                "notebookPath": self._nb_path,
                "notebookId": self._notebook_id,
                "kernelspec": {
                    "name": "python3",
                    "description": "IPython kernel implementation for Yandex DataSphere",
                    "spec": {
                        "language": "python",
                        "display_name": "Yandex DataSphere Kernel",
                        "codemirror_mode": "python",
                        "argv": [
                            "/bin/true"
                        ],
                        "env": {},
                        "help_links": []
                    },
                    "resources": {},
                    "display_name": "Yandex DataSphere Kernel"
                }
            },
            "cells": []
        }

    def __generate_cell(self, cell_id, source):
        return {
            "cell_type": "code",
            "source": source,
            "metadata": {
                "cellId": cell_id
            },
            "outputs": [],
            "execution_count": None
        }

    def append_cell(self, source):
        cell_id = str(uuid4())
        self._notebook['cells'].append(self.__generate_cell(cell_id, source))

        return cell_id

    def add_cell(self, index, source):
        cell_id = str(uuid4())
        self._notebook['cells'].insert(index, self.__generate_cell(cell_id, source))

        return cell_id

    def cell_count(self):
        return len(self._notebook['cells'])

    def get_id(self):
        return self._notebook_id

    def get_path(self):
        return self._nb_path

    def get_file(self, file_path=None):
        if file_path is None:
            file_path = self._nb_path
        with open(file_path, "w") as f:
            json.dump(self._notebook, f, ensure_ascii=False)

        return file_path



