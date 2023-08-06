from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rlength:
	"""Rlength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rlength", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:ADEMod:RLENgth \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.ademod.rlength.get() \n
		This command returns the record length set up for current measurement settings. Note that this command is maintained for
		compatibility reasons only. Use the [SENSe:]RLENgth? command for new remote control programs. \n
			:return: sample_count: No help available"""
		response = self._core.io.query_str(f'SENSe:ADEMod:RLENgth?')
		return Conversions.str_to_float(response)
