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

	def set(self, slope: enums.IqResultDataFormat) -> None:
		"""SCPI: TRACe:IQ:DATA:FORMat \n
		Snippet: driver.applications.k18AmplifierEt.trace.iq.data.formatPy.set(slope = enums.IqResultDataFormat.COMPatible) \n
		Defines the I/Q data format. \n
			:param slope: COMPatible | IQBLock | IQPair
		"""
		param = Conversions.enum_scalar_to_str(slope, enums.IqResultDataFormat)
		self._core.io.write(f'TRACe:IQ:DATA:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.IqResultDataFormat:
		"""SCPI: TRACe:IQ:DATA:FORMat \n
		Snippet: value: enums.IqResultDataFormat = driver.applications.k18AmplifierEt.trace.iq.data.formatPy.get() \n
		Defines the I/Q data format. \n
			:return: slope: COMPatible | IQBLock | IQPair"""
		response = self._core.io.query_str(f'TRACe:IQ:DATA:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.IqResultDataFormat)
