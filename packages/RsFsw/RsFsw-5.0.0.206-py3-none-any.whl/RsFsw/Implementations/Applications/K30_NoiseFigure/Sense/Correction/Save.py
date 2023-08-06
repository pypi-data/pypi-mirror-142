from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Save:
	"""Save commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("save", core, parent)

	def set(self, save_file_path: str) -> None:
		"""SCPI: [SENSe]:CORRection:SAVE \n
		Snippet: driver.applications.k30NoiseFigure.sense.correction.save.set(save_file_path = '1') \n
		Queries and sets the calibration results save filepath and if set saves the calibration results. \n
			:param save_file_path: No help available
		"""
		param = Conversions.value_to_quoted_str(save_file_path)
		self._core.io.write(f'SENSe:CORRection:SAVE {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:CORRection:SAVE \n
		Snippet: value: str = driver.applications.k30NoiseFigure.sense.correction.save.get() \n
		Queries and sets the calibration results save filepath and if set saves the calibration results. \n
			:return: save_file_path: No help available"""
		response = self._core.io.query_str(f'SENSe:CORRection:SAVE?')
		return trim_str_response(response)
