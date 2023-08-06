from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, meas_only_on_patt: enums.SyncMode) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:MODE \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.sync.mode.set(meas_only_on_patt = enums.SyncMode.MEAS) \n
		This command sets the vector analyzer so that the measurement is performed only if the measurement was synchronous to the
		selected sync pattern. The command is available only if the pattern search is activated (see
		[SENSe:]DDEMod:SEARch:SYNC:STATe) . \n
			:param meas_only_on_patt: MEAS | SYNC MEAS The measurement is performed independently of successful synchronization SYNC The measured values are displayed and considered in the error evaluation only if the set sync pattern was found. Bursts with a wrong sync pattern (sync not found) are ignored. If an invalid or no sync pattern is found, the measurement waits and resumes running only when a valid sync pattern is found.
		"""
		param = Conversions.enum_scalar_to_str(meas_only_on_patt, enums.SyncMode)
		self._core.io.write(f'SENSe:DDEMod:SEARch:SYNC:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SyncMode:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:MODE \n
		Snippet: value: enums.SyncMode = driver.applications.k70Vsa.sense.ddemod.search.sync.mode.get() \n
		This command sets the vector analyzer so that the measurement is performed only if the measurement was synchronous to the
		selected sync pattern. The command is available only if the pattern search is activated (see
		[SENSe:]DDEMod:SEARch:SYNC:STATe) . \n
			:return: meas_only_on_patt: MEAS | SYNC MEAS The measurement is performed independently of successful synchronization SYNC The measured values are displayed and considered in the error evaluation only if the set sync pattern was found. Bursts with a wrong sync pattern (sync not found) are ignored. If an invalid or no sync pattern is found, the measurement waits and resumes running only when a valid sync pattern is found."""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:SYNC:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.SyncMode)
