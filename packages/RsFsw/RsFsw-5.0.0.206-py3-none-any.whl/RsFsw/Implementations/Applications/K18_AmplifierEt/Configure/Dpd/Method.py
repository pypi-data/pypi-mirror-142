from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Method:
	"""Method commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("method", core, parent)

	def set(self, method: enums.DpdMethod) -> None:
		"""SCPI: CONFigure:DPD:METHod \n
		Snippet: driver.applications.k18AmplifierEt.configure.dpd.method.set(method = enums.DpdMethod.GENerator) \n
		This command selects the method with which the application determines the DPD.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on polynomial DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) . \n
			:param method: GENerator Signal generator applies the DPD parameters calculated by the amplifier application to the generated RF signal in real-time. Option R&S SMW-K541 is required on the generator for this method. WFILe Signal generator applies the DPD to the generated RF signal through a waveform file. No additional equipment is required on the signal generator for this method. Use method RsFsw.Applications.K18_AmplifierEt.Configure.Dpd.File.Generate.set to actually generate the DPD and transfer it to the generator.
		"""
		param = Conversions.enum_scalar_to_str(method, enums.DpdMethod)
		self._core.io.write(f'CONFigure:DPD:METHod {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DpdMethod:
		"""SCPI: CONFigure:DPD:METHod \n
		Snippet: value: enums.DpdMethod = driver.applications.k18AmplifierEt.configure.dpd.method.get() \n
		This command selects the method with which the application determines the DPD.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on polynomial DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) . \n
			:return: method: GENerator Signal generator applies the DPD parameters calculated by the amplifier application to the generated RF signal in real-time. Option R&S SMW-K541 is required on the generator for this method. WFILe Signal generator applies the DPD to the generated RF signal through a waveform file. No additional equipment is required on the signal generator for this method. Use method RsFsw.Applications.K18_AmplifierEt.Configure.Dpd.File.Generate.set to actually generate the DPD and transfer it to the generator."""
		response = self._core.io.query_str(f'CONFigure:DPD:METHod?')
		return Conversions.str_to_scalar_enum(response, enums.DpdMethod)
