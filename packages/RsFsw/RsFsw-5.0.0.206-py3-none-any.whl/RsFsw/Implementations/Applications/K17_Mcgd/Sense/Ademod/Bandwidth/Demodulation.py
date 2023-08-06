from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Demodulation:
	"""Demodulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("demodulation", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:ADEMod:BWIDth:DEModulation \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.ademod.bandwidth.demodulation.get() \n
		This command queries the measurement bandwidth. Note that this command is maintained for compatibility reasons only. Use
		[SENSe:]BANDwidth:DEMod? for new remote control programs. \n
			:return: span: Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:ADEMod:BWIDth:DEModulation?')
		return Conversions.str_to_float(response)
