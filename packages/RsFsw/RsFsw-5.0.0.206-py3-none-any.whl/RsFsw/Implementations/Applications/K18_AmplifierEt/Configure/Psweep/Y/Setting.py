from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Setting:
	"""Setting commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("setting", core, parent)

	def set(self, setting: enums.PsweepSetting) -> None:
		"""SCPI: CONFigure:PSWeep:Y:SETTing \n
		Snippet: driver.applications.k18AmplifierEt.configure.psweep.y.setting.set(setting = enums.PsweepSetting.BIAS) \n
		This command selects the parameter type for the second parameter controlled by the parameter sweep. \n
			:param setting: BIAS Controls the envelope bias. DELay Controls the delay between envelope and RF signal. FREQuency Controls the frequency. POWer Controls the output level.
		"""
		param = Conversions.enum_scalar_to_str(setting, enums.PsweepSetting)
		self._core.io.write(f'CONFigure:PSWeep:Y:SETTing {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PsweepSetting:
		"""SCPI: CONFigure:PSWeep:Y:SETTing \n
		Snippet: value: enums.PsweepSetting = driver.applications.k18AmplifierEt.configure.psweep.y.setting.get() \n
		This command selects the parameter type for the second parameter controlled by the parameter sweep. \n
			:return: setting: BIAS Controls the envelope bias. DELay Controls the delay between envelope and RF signal. FREQuency Controls the frequency. POWer Controls the output level."""
		response = self._core.io.query_str(f'CONFigure:PSWeep:Y:SETTing?')
		return Conversions.str_to_scalar_enum(response, enums.PsweepSetting)
