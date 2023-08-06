from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, standard: enums.SpectrumMaskStandard) -> None:
		"""SCPI: CONFigure:BURSt:SPECtrum:MASK:SELect \n
		Snippet: driver.applications.k91Wlan.configure.burst.spectrum.mask.select.set(standard = enums.SpectrumMaskStandard.ETSI) \n
		This command sets the Spectrum Emission Mask (SEM) measurement type. \n
			:param standard: IEEE | ETSI | User User Settings and limits are configured via a user-defined XML file. Load the file using method RsFsw.Applications.K91_Wlan.MassMemory.Load.Sem.State.set. IEEE Settings and limits are as specified in the IEEE Std 802.11n™-2009 Figure 20-17—Transmit spectral mask for 20 MHz transmission. For other IEEE standards see the parameter values in the table below. After a query, IEEE is returned for all IEEE standards. ETSI Settings and limits are as specified in the ETSI standard.
		"""
		param = Conversions.enum_scalar_to_str(standard, enums.SpectrumMaskStandard)
		self._core.io.write(f'CONFigure:BURSt:SPECtrum:MASK:SELect {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SpectrumMaskStandard:
		"""SCPI: CONFigure:BURSt:SPECtrum:MASK:SELect \n
		Snippet: value: enums.SpectrumMaskStandard = driver.applications.k91Wlan.configure.burst.spectrum.mask.select.get() \n
		This command sets the Spectrum Emission Mask (SEM) measurement type. \n
			:return: standard: IEEE | ETSI | User User Settings and limits are configured via a user-defined XML file. Load the file using method RsFsw.Applications.K91_Wlan.MassMemory.Load.Sem.State.set. IEEE Settings and limits are as specified in the IEEE Std 802.11n™-2009 Figure 20-17—Transmit spectral mask for 20 MHz transmission. For other IEEE standards see the parameter values in the table below. After a query, IEEE is returned for all IEEE standards. ETSI Settings and limits are as specified in the ETSI standard."""
		response = self._core.io.query_str(f'CONFigure:BURSt:SPECtrum:MASK:SELect?')
		return Conversions.str_to_scalar_enum(response, enums.SpectrumMaskStandard)
