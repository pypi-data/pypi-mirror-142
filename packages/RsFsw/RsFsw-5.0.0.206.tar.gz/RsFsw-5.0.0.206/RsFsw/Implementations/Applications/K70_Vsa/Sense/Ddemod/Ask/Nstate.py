from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nstate:
	"""Nstate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nstate", core, parent)

	def set(self, askn_state: float) -> None:
		"""SCPI: [SENSe]:DDEMod:ASK:NSTate \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.ask.nstate.set(askn_state = 1.0) \n
		This command defines the specific demodulation mode for ASK. \n
			:param askn_state: 2 | 4 2 OOK 4 4ASK
		"""
		param = Conversions.decimal_value_to_str(askn_state)
		self._core.io.write(f'SENSe:DDEMod:ASK:NSTate {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:ASK:NSTate \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.ask.nstate.get() \n
		This command defines the specific demodulation mode for ASK. \n
			:return: askn_state: 2 | 4 2 OOK 4 4ASK"""
		response = self._core.io.query_str(f'SENSe:DDEMod:ASK:NSTate?')
		return Conversions.str_to_float(response)
