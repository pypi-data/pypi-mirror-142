from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, cal_state: enums.CalibrationScope = None) -> None:
		"""SCPI: CALibration[:ALL] \n
		Snippet: driver.calibration.all.set(cal_state = enums.CalibrationScope.ACLear) \n
		This command initiates a calibration (self-alignment) routine and queries if calibration was successful.
		During the acquisition of correction data the instrument does not accept any remote control commands. Note:If you start a
		self-alignment remotely, then select the 'Local' softkey while the alignment is still running, the instrument only
		returns to the manual operation state after the alignment is completed. In order to recognize when the acquisition of
		correction data is completed, the MAV bit in the status byte can be used. If the associated bit is set in the Service
		Request Enable (SRE) register, the instrument generates a service request after the acquisition of correction data has
		been completed. \n
			:param cal_state: No help available
		"""
		param = ''
		if cal_state:
			param = Conversions.enum_scalar_to_str(cal_state, enums.CalibrationScope)
		self._core.io.write(f'CALibration:ALL {param}'.strip())
