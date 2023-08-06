from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.EgateType) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:TYPE \n
		Snippet: driver.sense.sweep.egate.typePy.set(type_py = enums.EgateType.EDGE) \n
		This command selects the way gated measurements are triggered. \n
			:param type_py: LEVel The trigger event for the gate to open is a particular power level. After the gate signal has been detected, the gate remains open until the signal disappears. Note: If you perform gated measurements in combination with the IF Power trigger, the R&S FSW ignores the holding time for frequency sweep, FFT sweep, zero span and I/Q mode measurements. EDGE The trigger event for the gate to open is the detection of the signal edge. After the gate signal has been detected, the gate remains open until the gate length is over.
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.EgateType)
		self._core.io.write(f'SENSe:SWEep:EGATe:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.EgateType:
		"""SCPI: [SENSe]:SWEep:EGATe:TYPE \n
		Snippet: value: enums.EgateType = driver.sense.sweep.egate.typePy.get() \n
		This command selects the way gated measurements are triggered. \n
			:return: type_py: LEVel The trigger event for the gate to open is a particular power level. After the gate signal has been detected, the gate remains open until the signal disappears. Note: If you perform gated measurements in combination with the IF Power trigger, the R&S FSW ignores the holding time for frequency sweep, FFT sweep, zero span and I/Q mode measurements. EDGE The trigger event for the gate to open is the detection of the signal edge. After the gate signal has been detected, the gate remains open until the gate length is over."""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.EgateType)
