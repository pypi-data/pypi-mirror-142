from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nstate:
	"""Nstate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nstate", core, parent)

	def set(self, apskn_state: float) -> None:
		"""SCPI: [SENSe]:DDEMod:APSK:NSTate \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.apsk.nstate.set(apskn_state = 1.0) \n
		This command defines the specific demodulation mode for APSK. \n
			:param apskn_state: 16 | 32 16 16APSK 32 32APSK
		"""
		param = Conversions.decimal_value_to_str(apskn_state)
		self._core.io.write(f'SENSe:DDEMod:APSK:NSTate {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:APSK:NSTate \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.apsk.nstate.get() \n
		This command defines the specific demodulation mode for APSK. \n
			:return: apskn_state: 16 | 32 16 16APSK 32 32APSK"""
		response = self._core.io.query_str(f'SENSe:DDEMod:APSK:NSTate?')
		return Conversions.str_to_float(response)
