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

	def set(self, meas_only_on_burst: enums.BurstMode) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:BURSt:MODE \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.burst.mode.set(meas_only_on_burst = enums.BurstMode.BURS) \n
		This command sets the vector analyzer so that a measurement is performed only if a burst is found.
		The command is available only if the burst search is activated (see [SENSe:]DDEMod:SEARch:BURSt:STATe) . \n
			:param meas_only_on_burst: MEAS | BURS MEAS Measurement is always performed BURS Measurement is performed only if a burst is found
		"""
		param = Conversions.enum_scalar_to_str(meas_only_on_burst, enums.BurstMode)
		self._core.io.write(f'SENSe:DDEMod:SEARch:BURSt:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.BurstMode:
		"""SCPI: [SENSe]:DDEMod:SEARch:BURSt:MODE \n
		Snippet: value: enums.BurstMode = driver.applications.k70Vsa.sense.ddemod.search.burst.mode.get() \n
		This command sets the vector analyzer so that a measurement is performed only if a burst is found.
		The command is available only if the burst search is activated (see [SENSe:]DDEMod:SEARch:BURSt:STATe) . \n
			:return: meas_only_on_burst: MEAS | BURS MEAS Measurement is always performed BURS Measurement is performed only if a burst is found"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:BURSt:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.BurstMode)
