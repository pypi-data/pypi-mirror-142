from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPy:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, psk_format: enums.PskFormat) -> None:
		"""SCPI: [SENSe]:DDEMod:PSK:FORMat \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.psk.formatPy.set(psk_format = enums.PskFormat.DIFFerential) \n
		Together with DDEMod:PSK:NST, this command defines the demodulation order for PSK (see also [SENSe:]DDEMod:PSK:NSTate) .
		Depending on the demodulation format and state, the following orders are available:
			Table Header: NSTATe / <PSKformat> / Order \n
			- 2 / NORMal / BPSK
			- 2 / NPI2 / Pi/2-BPSK
			- 2 / MNPI2 / Pi/2-BPSK
			- 2 / DPI2 / Pi/2-DBPSK
			- 8 / NORMal / 8PSK
			- 8 / DIFFerential / D8PSK
			- 8 / N3Pi8 / 3pi/8-8PSK (EDGE)
			- 8 / PI8D8PSK / Pi/8-D8PSK \n
			:param psk_format: NORMal | DIFFerential | N3Pi8 | PI8D8psk | NPI2 | DPI2 | MNPi2
		"""
		param = Conversions.enum_scalar_to_str(psk_format, enums.PskFormat)
		self._core.io.write(f'SENSe:DDEMod:PSK:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PskFormat:
		"""SCPI: [SENSe]:DDEMod:PSK:FORMat \n
		Snippet: value: enums.PskFormat = driver.applications.k70Vsa.sense.ddemod.psk.formatPy.get() \n
		Together with DDEMod:PSK:NST, this command defines the demodulation order for PSK (see also [SENSe:]DDEMod:PSK:NSTate) .
		Depending on the demodulation format and state, the following orders are available:
			Table Header: NSTATe / <PSKformat> / Order \n
			- 2 / NORMal / BPSK
			- 2 / NPI2 / Pi/2-BPSK
			- 2 / MNPI2 / Pi/2-BPSK
			- 2 / DPI2 / Pi/2-DBPSK
			- 8 / NORMal / 8PSK
			- 8 / DIFFerential / D8PSK
			- 8 / N3Pi8 / 3pi/8-8PSK (EDGE)
			- 8 / PI8D8PSK / Pi/8-D8PSK \n
			:return: psk_format: NORMal | DIFFerential | N3Pi8 | PI8D8psk | NPI2 | DPI2 | MNPi2"""
		response = self._core.io.query_str(f'SENSe:DDEMod:PSK:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.PskFormat)
