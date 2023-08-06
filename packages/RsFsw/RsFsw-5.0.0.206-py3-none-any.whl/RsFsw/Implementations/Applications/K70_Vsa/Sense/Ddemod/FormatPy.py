from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPy:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, group: enums.DdemGroup) -> None:
		"""SCPI: [SENSe]:DDEMod:FORMat \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.formatPy.set(group = enums.DdemGroup.APSK) \n
		This command selects the digital demodulation mode. \n
			:param group: MSK | PSK | QAM | QPSK | FSK | ASK | APSK | UQAM QPSK Quad Phase Shift Key PSK Phase Shift Key MSK Minimum Shift Key QAM Quadrature Amplitude Modulation FSK Frequency Shift Key ASK Amplitude Shift Keying APSK Amplitude Phase Shift Keying UQAM User-defined modulation (loaded from file, see [SENSe:]DDEMod:USER:NAME)
		"""
		param = Conversions.enum_scalar_to_str(group, enums.DdemGroup)
		self._core.io.write(f'SENSe:DDEMod:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DdemGroup:
		"""SCPI: [SENSe]:DDEMod:FORMat \n
		Snippet: value: enums.DdemGroup = driver.applications.k70Vsa.sense.ddemod.formatPy.get() \n
		This command selects the digital demodulation mode. \n
			:return: group: MSK | PSK | QAM | QPSK | FSK | ASK | APSK | UQAM QPSK Quad Phase Shift Key PSK Phase Shift Key MSK Minimum Shift Key QAM Quadrature Amplitude Modulation FSK Frequency Shift Key ASK Amplitude Shift Keying APSK Amplitude Phase Shift Keying UQAM User-defined modulation (loaded from file, see [SENSe:]DDEMod:USER:NAME)"""
		response = self._core.io.query_str(f'SENSe:DDEMod:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.DdemGroup)
