"""
Code that will save the data correctly to the nosql solution (aka data swamp lol bring on the inevitable mess)
"""
import json

from typing import Dict, Any, List
from datetime import datetime
from pathlib import Path

from spiders.custom_errors import reraise


class DataSaver:
    def __init__(
        self,
        name: str,
        sub_folders: List[str],
        spider: str,
        folder_name: str,
    ) -> None:
        self.name = name
        self.sub_folders = sub_folders
        self.spider = spider
        self.folder_name = folder_name

    @property
    def folder_name(self) -> str:
        """Getter for folder_name"""
        return self._folder_name

    @folder_name.setter
    def folder_name(self, desired_name: str) -> None:
        """Establish the desired folder structure, currently done local but ideally eventually done in a cloud storage
        somewhere.

        Parameters
        ----------
        desired_name : Name of folder that you will set up.
        """
        for sub_folder in self.sub_folders:
            try:
                Path(f'{desired_name}/{self.spider}/{sub_folder}').mkdir(parents=True, exist_ok=True)

            except Exception as e:  # will this ever error? how?
                reraise(e, f"Oh cock! Failed to set up desired folder {desired_name}/{self.spider}/{sub_folder}!")

            self._folder_name = desired_name

    def save_data(
        self,
        to_save: str,
        sub_folder: str = '',
    ) -> None:
        """Save the serialised object to the desired location, currently local only.

        Parameters
        ----------
        to_save : Dictionary in serialised form i.e. no shit dtypes pls.
        sub_folder : Name of sub folder to put data in if desired.
        """
        time_of_save = datetime.now().strftime(format='%Y%m%d%H%M%S')

        with open(
            f'{self.folder_name}/{self.spider}/{sub_folder}/{self.name}_{time_of_save}.json',
            'w',
            encoding='utf-8'
        ) as f:
            json.dump(to_save, f, ensure_ascii=False, indent=4)

    @staticmethod
    def connect_to_dbase_or_some_shit():
        pass  # probs the dbase is a class attr? let's have a look online for a bit.
