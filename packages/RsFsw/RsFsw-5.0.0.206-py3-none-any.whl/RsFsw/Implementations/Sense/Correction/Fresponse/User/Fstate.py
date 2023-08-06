from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fstate:
	"""Fstate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fstate", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:FSTate \n
		Snippet: driver.sense.correction.fresponse.user.fstate.set(state = False) \n
		Activates or deactivates the use of additional frequency response (.fres) files. The correction data is these files is
		applied after any correction settings in active touchstone files. For details, see 'Frequency response correction (R&S
		FSW-K544) '. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Activates the files. ON | 1 Deactivates the files.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:CORRection:FRESponse:USER:FSTate {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:FSTate \n
		Snippet: value: bool = driver.sense.correction.fresponse.user.fstate.get() \n
		Activates or deactivates the use of additional frequency response (.fres) files. The correction data is these files is
		applied after any correction settings in active touchstone files. For details, see 'Frequency response correction (R&S
		FSW-K544) '. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Activates the files. ON | 1 Deactivates the files."""
		response = self._core.io.query_str(f'SENSe:CORRection:FRESponse:USER:FSTate?')
		return Conversions.str_to_bool(response)
