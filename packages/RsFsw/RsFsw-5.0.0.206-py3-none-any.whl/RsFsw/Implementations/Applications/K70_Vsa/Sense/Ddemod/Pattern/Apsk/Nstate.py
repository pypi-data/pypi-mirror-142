from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nstate:
	"""Nstate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nstate", core, parent)

	def set(self, apskn_state: float) -> None:
		"""SCPI: [SENSe]:DDEMod:PATTern:APSK:NSTate \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.pattern.apsk.nstate.set(apskn_state = 1.0) \n
		This command defines the demodulation order for APSK for the pattern (see also [SENSe:]DDEMod:PATTern:FORMat) . Depending
		on the demodulation state, the following orders are available:
			Table Header: <APSKNstate> / Order \n
			- 16 / 16APSK
			- 32 / 32APSK
		This command is only available if the additional Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:param apskn_state: 16 | 32
		"""
		param = Conversions.decimal_value_to_str(apskn_state)
		self._core.io.write(f'SENSe:DDEMod:PATTern:APSK:NSTate {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:PATTern:APSK:NSTate \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.pattern.apsk.nstate.get() \n
		This command defines the demodulation order for APSK for the pattern (see also [SENSe:]DDEMod:PATTern:FORMat) . Depending
		on the demodulation state, the following orders are available:
			Table Header: <APSKNstate> / Order \n
			- 16 / 16APSK
			- 32 / 32APSK
		This command is only available if the additional Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:return: apskn_state: 16 | 32"""
		response = self._core.io.query_str(f'SENSe:DDEMod:PATTern:APSK:NSTate?')
		return Conversions.str_to_float(response)
