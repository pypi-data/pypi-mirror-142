from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, type_py: enums.MdpdWaveformType) -> None:
		"""SCPI: CONFigure:MDPD:WAVeform:SELect \n
		Snippet: driver.applications.k18AmplifierEt.configure.mdpd.waveform.select.set(type_py = enums.MdpdWaveformType.DDPD) \n
		Selects the type of DPD waveform to be used. \n
			:param type_py: DDPD Uses a direct DPD waveform. MDPD Uses a memory polynomial DPD waveform.
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.MdpdWaveformType)
		self._core.io.write(f'CONFigure:MDPD:WAVeform:SELect {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.MdpdWaveformType:
		"""SCPI: CONFigure:MDPD:WAVeform:SELect \n
		Snippet: value: enums.MdpdWaveformType = driver.applications.k18AmplifierEt.configure.mdpd.waveform.select.get() \n
		Selects the type of DPD waveform to be used. \n
			:return: type_py: DDPD Uses a direct DPD waveform. MDPD Uses a memory polynomial DPD waveform."""
		response = self._core.io.query_str(f'CONFigure:MDPD:WAVeform:SELect?')
		return Conversions.str_to_scalar_enum(response, enums.MdpdWaveformType)
