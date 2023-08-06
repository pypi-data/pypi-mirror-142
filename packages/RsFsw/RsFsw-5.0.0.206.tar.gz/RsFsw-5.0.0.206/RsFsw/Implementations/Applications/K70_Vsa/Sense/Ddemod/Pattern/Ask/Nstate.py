from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nstate:
	"""Nstate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nstate", core, parent)

	def set(self, askn_state: float) -> None:
		"""SCPI: [SENSe]:DDEMod:PATTern:ASK:NSTate \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.pattern.ask.nstate.set(askn_state = 1.0) \n
		This command defines the demodulation order for ASK for the pattern (see also [SENSe:]DDEMod:PATTern:FORMat) . Depending
		on the demodulation state, the following orders are available:
			Table Header: <ASKNstate> / Order \n
			- 2 / 2ASK
			- 4 / 4ASK
		This command is only available if the additional Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:param askn_state: 2 | 4
		"""
		param = Conversions.decimal_value_to_str(askn_state)
		self._core.io.write(f'SENSe:DDEMod:PATTern:ASK:NSTate {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:PATTern:ASK:NSTate \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.pattern.ask.nstate.get() \n
		This command defines the demodulation order for ASK for the pattern (see also [SENSe:]DDEMod:PATTern:FORMat) . Depending
		on the demodulation state, the following orders are available:
			Table Header: <ASKNstate> / Order \n
			- 2 / 2ASK
			- 4 / 4ASK
		This command is only available if the additional Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:return: askn_state: 2 | 4"""
		response = self._core.io.query_str(f'SENSe:DDEMod:PATTern:ASK:NSTate?')
		return Conversions.str_to_float(response)
