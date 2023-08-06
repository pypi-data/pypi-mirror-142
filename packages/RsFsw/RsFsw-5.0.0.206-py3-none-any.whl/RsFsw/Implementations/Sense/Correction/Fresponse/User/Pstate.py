from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pstate:
	"""Pstate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pstate", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:PSTate \n
		Snippet: driver.sense.correction.fresponse.user.pstate.set(state = False) \n
		Activates or deactivates the preview of the user correction files for all input types. Note that this function is only
		available for remote operation. The preview cannot be switched back on in manual operation. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:CORRection:FRESponse:USER:PSTate {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:PSTate \n
		Snippet: value: bool = driver.sense.correction.fresponse.user.pstate.get() \n
		Activates or deactivates the preview of the user correction files for all input types. Note that this function is only
		available for remote operation. The preview cannot be switched back on in manual operation. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SENSe:CORRection:FRESponse:USER:PSTate?')
		return Conversions.str_to_bool(response)
