from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.UwbDemodMode) -> None:
		"""SCPI: [SENSe]:DEMod:MODE \n
		Snippet: driver.applications.k149Uwb.sense.demod.mode.set(mode = enums.UwbDemodMode.BPRF) \n
		Defines the demodulation mode (the demodulation standard) . \n
			:param mode: HRP | BPRF | HPRF
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.UwbDemodMode)
		self._core.io.write(f'SENSe:DEMod:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.UwbDemodMode:
		"""SCPI: [SENSe]:DEMod:MODE \n
		Snippet: value: enums.UwbDemodMode = driver.applications.k149Uwb.sense.demod.mode.get() \n
		Defines the demodulation mode (the demodulation standard) . \n
			:return: mode: HRP | BPRF | HPRF"""
		response = self._core.io.query_str(f'SENSe:DEMod:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.UwbDemodMode)
