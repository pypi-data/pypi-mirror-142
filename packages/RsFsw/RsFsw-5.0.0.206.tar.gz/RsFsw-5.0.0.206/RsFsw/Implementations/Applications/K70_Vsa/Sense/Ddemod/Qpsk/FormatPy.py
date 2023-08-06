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

	def set(self, qpsk_format: enums.QpskFormat) -> None:
		"""SCPI: [SENSe]:DDEMod:QPSK:FORMat \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.qpsk.formatPy.set(qpsk_format = enums.QpskFormat.DIFFerential) \n
		This command defines the demodulation order for QPSK. \n
			:param qpsk_format: NORMal | DIFFerential | NPI4 | DPI4 | OFFSet | SOFFset | N3Pi4 NORMal Demodulation order QPSK is used. DIFFerential Demodulation order DQPSK is used. NPI4 Demodulation order π/4 QPSK is used. DPI4 Demodulation order π/4 DQPSK is used. OFFSet Demodulation order OQPSK is used. N3PI4 Demodulation order 3π/4 QPSK is used. SOFFset Shaped Offset QPSK
		"""
		param = Conversions.enum_scalar_to_str(qpsk_format, enums.QpskFormat)
		self._core.io.write(f'SENSe:DDEMod:QPSK:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.QpskFormat:
		"""SCPI: [SENSe]:DDEMod:QPSK:FORMat \n
		Snippet: value: enums.QpskFormat = driver.applications.k70Vsa.sense.ddemod.qpsk.formatPy.get() \n
		This command defines the demodulation order for QPSK. \n
			:return: qpsk_format: NORMal | DIFFerential | NPI4 | DPI4 | OFFSet | SOFFset | N3Pi4 NORMal Demodulation order QPSK is used. DIFFerential Demodulation order DQPSK is used. NPI4 Demodulation order π/4 QPSK is used. DPI4 Demodulation order π/4 DQPSK is used. OFFSet Demodulation order OQPSK is used. N3PI4 Demodulation order 3π/4 QPSK is used. SOFFset Shaped Offset QPSK"""
		response = self._core.io.query_str(f'SENSe:DDEMod:QPSK:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.QpskFormat)
