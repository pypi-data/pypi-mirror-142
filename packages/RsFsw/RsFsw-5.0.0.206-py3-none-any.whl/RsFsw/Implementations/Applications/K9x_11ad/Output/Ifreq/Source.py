from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, source: enums.OutputIfSource) -> None:
		"""SCPI: OUTPut:IF:SOURce \n
		Snippet: driver.applications.k9X11Ad.output.ifreq.source.set(source = enums.OutputIfSource.IF) \n
		Defines the type of signal available at one of the output connectors of the R&S FSW. \n
			:param source: IF The measured IF value is available at the IF/VIDEO/DEMOD output connector. The frequency at which the IF value is provided is defined using the method RsFsw.Applications.K9x_11ad.Output.Ifreq.IfFrequency.set command.
		"""
		param = Conversions.enum_scalar_to_str(source, enums.OutputIfSource)
		self._core.io.write(f'OUTPut:IF:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.OutputIfSource:
		"""SCPI: OUTPut:IF:SOURce \n
		Snippet: value: enums.OutputIfSource = driver.applications.k9X11Ad.output.ifreq.source.get() \n
		Defines the type of signal available at one of the output connectors of the R&S FSW. \n
			:return: source: IF The measured IF value is available at the IF/VIDEO/DEMOD output connector. The frequency at which the IF value is provided is defined using the method RsFsw.Applications.K9x_11ad.Output.Ifreq.IfFrequency.set command."""
		response = self._core.io.query_str(f'OUTPut:IF:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.OutputIfSource)
