from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:ADEMod:SRATe \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.ademod.symbolRate.get() \n
		This command returns the sample rate set up for current measurement settings. Note that this command is maintained for
		compatibility reasons only. Use [SENSe:]SRATe? for new remote control programs. \n
			:return: sample_rate: No help available"""
		response = self._core.io.query_str(f'SENSe:ADEMod:SRATe?')
		return Conversions.str_to_float(response)
