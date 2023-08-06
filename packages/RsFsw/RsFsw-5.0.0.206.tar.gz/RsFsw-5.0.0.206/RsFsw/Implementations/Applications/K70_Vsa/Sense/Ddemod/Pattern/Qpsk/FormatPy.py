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

	def set(self, qpsk_format: enums.QpskFormat) -> None:
		"""SCPI: [SENSe]:DDEMod:PATTern:QPSK:FORMat \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.pattern.qpsk.formatPy.set(qpsk_format = enums.QpskFormat.DIFFerential) \n
		This command defines the demodulation order for QPSK for the pattern. This command is only available if the additional
		Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:param qpsk_format: NORMal | DIFFerential NORMal Demodulation order QPSK is used. DIFFerential Demodulation order DQPSK is used.
		"""
		param = Conversions.enum_scalar_to_str(qpsk_format, enums.QpskFormat)
		self._core.io.write(f'SENSe:DDEMod:PATTern:QPSK:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.QpskFormat:
		"""SCPI: [SENSe]:DDEMod:PATTern:QPSK:FORMat \n
		Snippet: value: enums.QpskFormat = driver.applications.k70Vsa.sense.ddemod.pattern.qpsk.formatPy.get() \n
		This command defines the demodulation order for QPSK for the pattern. This command is only available if the additional
		Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:return: qpsk_format: NORMal | DIFFerential NORMal Demodulation order QPSK is used. DIFFerential Demodulation order DQPSK is used."""
		response = self._core.io.query_str(f'SENSe:DDEMod:PATTern:QPSK:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.QpskFormat)
