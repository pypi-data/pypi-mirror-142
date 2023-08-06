from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nstate:
	"""Nstate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nstate", core, parent)

	def set(self, nstate: float) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:NSTate \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.sync.nstate.set(nstate = 1.0) \n
		This command selects the degree of modulation (number of permitted states) . The pattern must have been selected before
		using [SENSe:]DDEMod:SEARch:SYNC:NAME. The number of permitted states depends on the modulation mode. \n
			:param nstate: No help available
		"""
		param = Conversions.decimal_value_to_str(nstate)
		self._core.io.write(f'SENSe:DDEMod:SEARch:SYNC:NSTate {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:NSTate \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.search.sync.nstate.get() \n
		This command selects the degree of modulation (number of permitted states) . The pattern must have been selected before
		using [SENSe:]DDEMod:SEARch:SYNC:NAME. The number of permitted states depends on the modulation mode. \n
			:return: nstate: No help available"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:SYNC:NSTate?')
		return Conversions.str_to_float(response)
