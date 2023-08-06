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

	def set(self, eq_format: enums.FileFormatDdem) -> None:
		"""SCPI: [SENSe]:DDEMod:EQUalizer:FILE:FORMat \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.equalizer.file.formatPy.set(eq_format = enums.FileFormatDdem.FRES) \n
		Determines the file format for stored equalizer results. \n
			:param eq_format: VAE | FRES VAE To be used as an equalizer file in VSA applications FRES To be used as a user-defined frequency response correction file in any other application that supports it
		"""
		param = Conversions.enum_scalar_to_str(eq_format, enums.FileFormatDdem)
		self._core.io.write(f'SENSe:DDEMod:EQUalizer:FILE:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FileFormatDdem:
		"""SCPI: [SENSe]:DDEMod:EQUalizer:FILE:FORMat \n
		Snippet: value: enums.FileFormatDdem = driver.applications.k70Vsa.sense.ddemod.equalizer.file.formatPy.get() \n
		Determines the file format for stored equalizer results. \n
			:return: eq_format: VAE | FRES VAE To be used as an equalizer file in VSA applications FRES To be used as a user-defined frequency response correction file in any other application that supports it"""
		response = self._core.io.query_str(f'SENSe:DDEMod:EQUalizer:FILE:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.FileFormatDdem)
