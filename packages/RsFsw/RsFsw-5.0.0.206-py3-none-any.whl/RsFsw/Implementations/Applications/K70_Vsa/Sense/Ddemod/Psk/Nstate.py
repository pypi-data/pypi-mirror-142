from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nstate:
	"""Nstate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nstate", core, parent)

	def set(self, pskn_state: float) -> None:
		"""SCPI: [SENSe]:DDEMod:PSK:NSTate \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.psk.nstate.set(pskn_state = 1.0) \n
		Together with DDEMod:PSK:FORMat, this command defines the demodulation order for PSK (see also [SENSe:]DDEMod:PSK:FORMat)
		. Depending on the demodulation format and state, the following orders are available:
			Table Header: <PSKNSTATe> / FORMat / Order \n
			- 2 / any / BPSK
			- 2 / NPI2 / Pi/2-BPSK
			- 2 / DPI2 / Pi/2-DBPSK
			- 8 / NORMal / 8PSK
			- 8 / DIFFerential / D8PSK
			- 8 / N3Pi8 / 3pi/8-8PSK (EDGE)
			- 8 / PI8D8PSK / Pi/8-D8PSK \n
			:param pskn_state: 2 | 8
		"""
		param = Conversions.decimal_value_to_str(pskn_state)
		self._core.io.write(f'SENSe:DDEMod:PSK:NSTate {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:PSK:NSTate \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.psk.nstate.get() \n
		Together with DDEMod:PSK:FORMat, this command defines the demodulation order for PSK (see also [SENSe:]DDEMod:PSK:FORMat)
		. Depending on the demodulation format and state, the following orders are available:
			Table Header: <PSKNSTATe> / FORMat / Order \n
			- 2 / any / BPSK
			- 2 / NPI2 / Pi/2-BPSK
			- 2 / DPI2 / Pi/2-DBPSK
			- 8 / NORMal / 8PSK
			- 8 / DIFFerential / D8PSK
			- 8 / N3Pi8 / 3pi/8-8PSK (EDGE)
			- 8 / PI8D8PSK / Pi/8-D8PSK \n
			:return: pskn_state: 2 | 8"""
		response = self._core.io.query_str(f'SENSe:DDEMod:PSK:NSTate?')
		return Conversions.str_to_float(response)
