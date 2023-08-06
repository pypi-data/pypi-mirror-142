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

	def set(self, format_py: enums.IqResultDataFormat) -> None:
		"""SCPI: TRACe:IQ:DATA:FORMat \n
		Snippet: driver.applications.k60Transient.trace.iq.data.formatPy.set(format_py = enums.IqResultDataFormat.COMPatible) \n
		This command selects the order of the I/Q data. \n
			:param format_py: COMPatible | IQBLock | IQPair COMPatible I and Q values are separated and collected in blocks: A block (512k) of I values is followed by a block (512k) of Q values, followed by a block of I values, followed by a block of Q values etc. (I,I,I,I,Q,Q,Q,Q,I,I,I,I,Q,Q,Q,Q...) IQBLock First all I-values are listed, then the Q-values (I,I,I,I,I,I,...Q,Q,Q,Q,Q,Q) IQPair One pair of I/Q values after the other is listed (I,Q,I,Q,I,Q...) .
		"""
		param = Conversions.enum_scalar_to_str(format_py, enums.IqResultDataFormat)
		self._core.io.write(f'TRACe:IQ:DATA:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.IqResultDataFormat:
		"""SCPI: TRACe:IQ:DATA:FORMat \n
		Snippet: value: enums.IqResultDataFormat = driver.applications.k60Transient.trace.iq.data.formatPy.get() \n
		This command selects the order of the I/Q data. \n
			:return: format_py: COMPatible | IQBLock | IQPair COMPatible I and Q values are separated and collected in blocks: A block (512k) of I values is followed by a block (512k) of Q values, followed by a block of I values, followed by a block of Q values etc. (I,I,I,I,Q,Q,Q,Q,I,I,I,I,Q,Q,Q,Q...) IQBLock First all I-values are listed, then the Q-values (I,I,I,I,I,I,...Q,Q,Q,Q,Q,Q) IQPair One pair of I/Q values after the other is listed (I,Q,I,Q,I,Q...) ."""
		response = self._core.io.query_str(f'TRACe:IQ:DATA:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.IqResultDataFormat)
