from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self) -> float:
		"""SCPI: FETCh:MACCuracy:GIMBalance:CURRent[:RESult] \n
		Snippet: value: float = driver.applications.k18AmplifierEt.fetch.maccuracy.gimbalance.current.result.get() \n
		This command queries the Gain Imbalance as shown in the Result Summary. \n
			:return: gain_imbalance: numeric value Minimum, maximum or current Gain Imbalance, depending on the command syntax. Unit: dB"""
		response = self._core.io.query_str(f'FETCh:MACCuracy:GIMBalance:CURRent:RESult?')
		return Conversions.str_to_float(response)
