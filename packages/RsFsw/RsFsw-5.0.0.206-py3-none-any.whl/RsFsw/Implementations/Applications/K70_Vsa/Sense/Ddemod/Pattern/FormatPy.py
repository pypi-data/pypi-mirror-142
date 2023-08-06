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

	def set(self, group: enums.DdemGroup) -> None:
		"""SCPI: [SENSe]:DDEMod:PATTern:FORMat \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.pattern.formatPy.set(group = enums.DdemGroup.APSK) \n
		This command selects the pattern demodulation mode. Some modes can only be queried as they are not supported for the two
		modulations feature, but could be set when 'Same as Data Symbols' is selected. \n
			:param group: MSK | PSK | QAM | QPSK | FSK | ASK | APSK | UQAM
		"""
		param = Conversions.enum_scalar_to_str(group, enums.DdemGroup)
		self._core.io.write(f'SENSe:DDEMod:PATTern:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DdemGroup:
		"""SCPI: [SENSe]:DDEMod:PATTern:FORMat \n
		Snippet: value: enums.DdemGroup = driver.applications.k70Vsa.sense.ddemod.pattern.formatPy.get() \n
		This command selects the pattern demodulation mode. Some modes can only be queried as they are not supported for the two
		modulations feature, but could be set when 'Same as Data Symbols' is selected. \n
			:return: group: MSK | PSK | QAM | QPSK | FSK | ASK | APSK | UQAM"""
		response = self._core.io.query_str(f'SENSe:DDEMod:PATTern:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.DdemGroup)
