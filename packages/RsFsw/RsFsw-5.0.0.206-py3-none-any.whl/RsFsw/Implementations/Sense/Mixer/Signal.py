from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Signal:
	"""Signal commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("signal", core, parent)

	def set(self, state: enums.State) -> None:
		"""SCPI: [SENSe]:MIXer:SIGNal \n
		Snippet: driver.sense.mixer.signal.set(state = enums.State.ALL) \n
		This command specifies whether automatic signal detection is active or not. Note that automatic signal identification is
		only available for measurements that perform frequency sweeps (not in vector signal analysis or the I/Q Analyzer, for
		instance) . The 'Auto ID' function is now also available for 'Spectrum emission mask (SEM) measurement' and 'Spurious
		emissions measurement' using an external mixer. \n
			:param state: OFF | ON | AUTO | ALL OFF | ON | AUTO | ALL OFF No automatic signal detection is active. ON Automatic signal detection (Signal ID) is active. AUTO Automatic signal detection (Auto ID) is active. ALL Both automatic signal detection functions (Signal ID+Auto ID) are active.
		"""
		param = Conversions.enum_scalar_to_str(state, enums.State)
		self._core.io.write(f'SENSe:MIXer:SIGNal {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.State:
		"""SCPI: [SENSe]:MIXer:SIGNal \n
		Snippet: value: enums.State = driver.sense.mixer.signal.get() \n
		This command specifies whether automatic signal detection is active or not. Note that automatic signal identification is
		only available for measurements that perform frequency sweeps (not in vector signal analysis or the I/Q Analyzer, for
		instance) . The 'Auto ID' function is now also available for 'Spectrum emission mask (SEM) measurement' and 'Spurious
		emissions measurement' using an external mixer. \n
			:return: state: OFF | ON | AUTO | ALL OFF | ON | AUTO | ALL OFF No automatic signal detection is active. ON Automatic signal detection (Signal ID) is active. AUTO Automatic signal detection (Auto ID) is active. ALL Both automatic signal detection functions (Signal ID+Auto ID) are active."""
		response = self._core.io.query_str(f'SENSe:MIXer:SIGNal?')
		return Conversions.str_to_scalar_enum(response, enums.State)
