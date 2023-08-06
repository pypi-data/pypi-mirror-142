from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Acquire:
	"""Acquire commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("acquire", core, parent)

	def set(self, meas_type: enums.CorrectionMeasType) -> None:
		"""SCPI: [SENSe]:CORRection:COLLect[:ACQuire] \n
		Snippet: driver.sense.correction.collect.acquire.set(meas_type = enums.CorrectionMeasType.OPEN) \n
		This command initiates a reference measurement (calibration) . The reference measurement is the basis for the measurement
		normalization. The result depends on whether a reflection measurement or transmission measurement is performed (see
		[SENSe:]CORRection:METHod) . To obtain a correct reference measurement, a complete sweep with synchronization to the end
		of the sweep must have been carried out. This is only possible in the single sweep mode. This command is only available
		if External Generator Control (R&S FSW-B10) is installed and active. \n
			:param meas_type: THRough | OPEN THRough 'TRANsmission' mode: calibration with direct connection between generator and device input 'REFLection' mode: calibration with short circuit at the input OPEN only allowed in 'REFLection' mode: calibration with open input
		"""
		param = Conversions.enum_scalar_to_str(meas_type, enums.CorrectionMeasType)
		self._core.io.write(f'SENSe:CORRection:COLLect:ACQuire {param}')
