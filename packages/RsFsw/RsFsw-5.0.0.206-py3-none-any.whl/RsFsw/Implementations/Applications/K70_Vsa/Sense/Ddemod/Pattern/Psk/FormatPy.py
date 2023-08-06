from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPy:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, psk_format: enums.PskFormat) -> None:
		"""SCPI: [SENSe]:DDEMod:PATTern:PSK:FORMat \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.pattern.psk.formatPy.set(psk_format = enums.PskFormat.DIFFerential) \n
		Together with DDEMod:PATT:PSK:NST, this command defines the demodulation order for PSK for the pattern (see also
		[SENSe:]DDEMod:PATTern:PSK:NSTate) .
			Table Header: NSTATe / <PSKformat> / Order \n
			- 2 / NORMal / BPSK
			- 8 / NORMal / 8PSK
			- 8 / DIFFerential / D8PSK
		This command is only available if the additional Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:param psk_format: NORMal | DIFFerential
		"""
		param = Conversions.enum_scalar_to_str(psk_format, enums.PskFormat)
		self._core.io.write(f'SENSe:DDEMod:PATTern:PSK:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PskFormat:
		"""SCPI: [SENSe]:DDEMod:PATTern:PSK:FORMat \n
		Snippet: value: enums.PskFormat = driver.applications.k70Vsa.sense.ddemod.pattern.psk.formatPy.get() \n
		Together with DDEMod:PATT:PSK:NST, this command defines the demodulation order for PSK for the pattern (see also
		[SENSe:]DDEMod:PATTern:PSK:NSTate) .
			Table Header: NSTATe / <PSKformat> / Order \n
			- 2 / NORMal / BPSK
			- 8 / NORMal / 8PSK
			- 8 / DIFFerential / D8PSK
		This command is only available if the additional Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:return: psk_format: NORMal | DIFFerential"""
		response = self._core.io.query_str(f'SENSe:DDEMod:PATTern:PSK:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.PskFormat)
