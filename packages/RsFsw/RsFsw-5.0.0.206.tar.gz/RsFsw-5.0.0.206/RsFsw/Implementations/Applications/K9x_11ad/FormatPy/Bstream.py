from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bstream:
	"""Bstream commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bstream", core, parent)

	def set(self, bitstream_format: enums.BitstreamFormat) -> None:
		"""SCPI: FORMat:BSTReam \n
		Snippet: driver.applications.k9X11Ad.formatPy.bstream.set(bitstream_format = enums.BitstreamFormat.HEXadecimal) \n
		Switches the format of the bitstream between octet and hexadecimal values. \n
			:param bitstream_format: OCTet | HEXadecimal
		"""
		param = Conversions.enum_scalar_to_str(bitstream_format, enums.BitstreamFormat)
		self._core.io.write(f'FORMat:BSTReam {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.BitstreamFormat:
		"""SCPI: FORMat:BSTReam \n
		Snippet: value: enums.BitstreamFormat = driver.applications.k9X11Ad.formatPy.bstream.get() \n
		Switches the format of the bitstream between octet and hexadecimal values. \n
			:return: bitstream_format: OCTet | HEXadecimal"""
		response = self._core.io.query_str(f'FORMat:BSTReam?')
		return Conversions.str_to_scalar_enum(response, enums.BitstreamFormat)
