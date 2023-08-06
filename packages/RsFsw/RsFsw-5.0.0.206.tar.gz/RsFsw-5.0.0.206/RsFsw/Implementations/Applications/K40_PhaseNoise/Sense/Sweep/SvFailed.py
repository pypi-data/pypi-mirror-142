from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SvFailed:
	"""SvFailed commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("svFailed", core, parent)

	def set(self, state: enums.AutoMode) -> None:
		"""SCPI: [SENSe]:SWEep:SVFailed \n
		Snippet: driver.applications.k40PhaseNoise.sense.sweep.svFailed.set(state = enums.AutoMode.AUTO) \n
		This command turns repeated tries to start the measurement if signal verification fails on and off. \n
			:param state: ON | OFF | AUTO If on, the application tries to verify the signal once and then aborts the measurement if verification has failed.
		"""
		param = Conversions.enum_scalar_to_str(state, enums.AutoMode)
		self._core.io.write(f'SENSe:SWEep:SVFailed {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AutoMode:
		"""SCPI: [SENSe]:SWEep:SVFailed \n
		Snippet: value: enums.AutoMode = driver.applications.k40PhaseNoise.sense.sweep.svFailed.get() \n
		This command turns repeated tries to start the measurement if signal verification fails on and off. \n
			:return: state: ON | OFF | AUTO If on, the application tries to verify the signal once and then aborts the measurement if verification has failed."""
		response = self._core.io.query_str(f'SENSe:SWEep:SVFailed?')
		return Conversions.str_to_scalar_enum(response, enums.AutoMode)
