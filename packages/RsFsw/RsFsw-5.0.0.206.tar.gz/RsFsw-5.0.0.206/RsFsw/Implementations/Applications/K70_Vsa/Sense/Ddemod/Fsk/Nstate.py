from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nstate:
	"""Nstate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nstate", core, parent)

	def set(self, fskn_state: float) -> None:
		"""SCPI: [SENSe]:DDEMod:FSK:NSTate \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.fsk.nstate.set(fskn_state = 1.0) \n
		This command defines the demodulation of the FSK modulation scheme. \n
			:param fskn_state: 2 | 4 | 8 | 16 2 2FSK 4 4FSK 8 8FSK 16 16FSK
		"""
		param = Conversions.decimal_value_to_str(fskn_state)
		self._core.io.write(f'SENSe:DDEMod:FSK:NSTate {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:FSK:NSTate \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.fsk.nstate.get() \n
		This command defines the demodulation of the FSK modulation scheme. \n
			:return: fskn_state: 2 | 4 | 8 | 16 2 2FSK 4 4FSK 8 8FSK 16 16FSK"""
		response = self._core.io.query_str(f'SENSe:DDEMod:FSK:NSTate?')
		return Conversions.str_to_float(response)
