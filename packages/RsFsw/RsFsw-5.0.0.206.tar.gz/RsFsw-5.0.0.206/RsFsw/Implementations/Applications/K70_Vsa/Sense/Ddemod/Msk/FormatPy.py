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

	def set(self, msk_format: enums.MskFormat) -> None:
		"""SCPI: [SENSe]:DDEMod:MSK:FORMat \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.msk.formatPy.set(msk_format = enums.MskFormat.DIFFerential) \n
		This command defines the specific demodulation order for MSK. \n
			:param msk_format: TYPe1 | TYPe2 | NORMal | DIFFerential TYPE1 | NORMal Demodulation order MSK is used. TYPE2 | DIFFerential Demodulation order DMSK is used.
		"""
		param = Conversions.enum_scalar_to_str(msk_format, enums.MskFormat)
		self._core.io.write(f'SENSe:DDEMod:MSK:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.MskFormat:
		"""SCPI: [SENSe]:DDEMod:MSK:FORMat \n
		Snippet: value: enums.MskFormat = driver.applications.k70Vsa.sense.ddemod.msk.formatPy.get() \n
		This command defines the specific demodulation order for MSK. \n
			:return: msk_format: TYPe1 | TYPe2 | NORMal | DIFFerential TYPE1 | NORMal Demodulation order MSK is used. TYPE2 | DIFFerential Demodulation order DMSK is used."""
		response = self._core.io.query_str(f'SENSe:DDEMod:MSK:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.MskFormat)
