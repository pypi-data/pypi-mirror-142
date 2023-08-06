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

	def set(self, qam_format: enums.QamFormat) -> None:
		"""SCPI: [SENSe]:DDEMod:PATTern:QAM:FORMat \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.pattern.qam.formatPy.set(qam_format = enums.QamFormat.DIFFerential) \n
		This command defines the specific demodulation order for QAM for the pattern. This command is only available if the
		additional Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:param qam_format: NORMal | DIFFerential NORMal Demodulation order QAM is used. DIFFerential Demodulation order DQAM is used.
		"""
		param = Conversions.enum_scalar_to_str(qam_format, enums.QamFormat)
		self._core.io.write(f'SENSe:DDEMod:PATTern:QAM:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.QamFormat:
		"""SCPI: [SENSe]:DDEMod:PATTern:QAM:FORMat \n
		Snippet: value: enums.QamFormat = driver.applications.k70Vsa.sense.ddemod.pattern.qam.formatPy.get() \n
		This command defines the specific demodulation order for QAM for the pattern. This command is only available if the
		additional Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:return: qam_format: NORMal | DIFFerential NORMal Demodulation order QAM is used. DIFFerential Demodulation order DQAM is used."""
		response = self._core.io.query_str(f'SENSe:DDEMod:PATTern:QAM:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.QamFormat)
