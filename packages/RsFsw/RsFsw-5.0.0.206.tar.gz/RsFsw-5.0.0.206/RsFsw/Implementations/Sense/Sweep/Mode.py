from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.SweepModeC) -> None:
		"""SCPI: [SENSe]:SWEep:MODE \n
		Snippet: driver.sense.sweep.mode.set(mode = enums.SweepModeC.AUTO) \n
		This command selects the spurious emission and spectrum emission mask measurements. You can select other measurements
		with
			INTRO_CMD_HELP: For triggered gated measurements,only the following gate trigger sources are supported: \n
			- method RsFsw.Calculate.Marker.Function.Power.State.set \n
			:param mode: LIST | AUTO | ESPectrum AUTO Turns on basic spectrum measurements. ESPectrum Turns on spectrum emission mask measurements. LIST Turns on spurious emission measurements.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SweepModeC)
		self._core.io.write(f'SENSe:SWEep:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SweepModeC:
		"""SCPI: [SENSe]:SWEep:MODE \n
		Snippet: value: enums.SweepModeC = driver.sense.sweep.mode.get() \n
		This command selects the spurious emission and spectrum emission mask measurements. You can select other measurements
		with
			INTRO_CMD_HELP: For triggered gated measurements,only the following gate trigger sources are supported: \n
			- method RsFsw.Calculate.Marker.Function.Power.State.set \n
			:return: mode: LIST | AUTO | ESPectrum AUTO Turns on basic spectrum measurements. ESPectrum Turns on spectrum emission mask measurements. LIST Turns on spurious emission measurements."""
		response = self._core.io.query_str(f'SENSe:SWEep:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.SweepModeC)
