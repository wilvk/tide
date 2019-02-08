import importlib
import sys
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path
from editor_base import editor_base

class EditorWrapper(editor_base):

    _editor_name = None

    _editor_object = None

    _editors_list = []

    def __init__(self, editor_name):
        self._editor_name = editor_name
        self.__set_editor_object()

    def __set_editor_object(self):
        self.__get_editors_list()
        self.__validate_and_create_editor_object()

    def __validate_and_create_editor_object(self):
        if self._editor_name.lower() in self._editors_list:
            return self.__create_editor_object()
        else:
            raise TypeError("error: python file for editor: " + self._editor_name + " is not a valid action")

    def __create_editor_object(self):
        editor_module = "editor_wrappers." + self._editor_name
        importlib.import_module(editor_module)
        self._editor_object = getattr(sys.modules[editor_module], self._editor_name)

    def __get_editors_list(self):
        if not self._editors_list:
            script_path = os.path.dirname(os.path.realpath(__file__))
            editors_path = os.path.join(script_path, "editor_wrappers")
            editor_files = [f for f in listdir(editors_path) if isfile(join(editors_path, f))]
            for editor_file in editor_files:
                if Path(editor_file).suffix.lower() == ".py" and editor_file.lower() != "__init__.py":
                    self._editors_list.append(Path(editor_file).stem.lower())

    @staticmethod
    def set_dictionary_value(parent_keys, value):
        self._editor_object.set_dictionary_value(parent_keys, value)

    def set_editor_dictionary(self, config_dictionary):
        self._editor_object.set_editor_dictionary(config_dictionary)

    def get_config_location(self):
        self._editor_object.get_config_location()