from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, window_function: enums.WindowFunction, halfDecadeRange=repcap.HalfDecadeRange.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<hd>:IQWindow:TYPE \n
		Snippet: driver.applications.k40PhaseNoise.sense.listPy.range.iqWindow.typePy.set(window_function = enums.WindowFunction.BHARris, halfDecadeRange = repcap.HalfDecadeRange.Default) \n
		This command selects the window function for a particular half decade. Window functions are available for I/Q sweep mode. \n
			:param window_function: RECTangular | GAUSsian | CHEByshev | BHARris | SWEPt
			:param halfDecadeRange: optional repeated capability selector. Default value: Rng_1Hz_3Hz (settable in the interface 'Range')
		"""
		param = Conversions.enum_scalar_to_str(window_function, enums.WindowFunction)
		halfDecadeRange_cmd_val = self._cmd_group.get_repcap_cmd_value(halfDecadeRange, repcap.HalfDecadeRange)
		self._core.io.write(f'SENSe:LIST:RANGe{halfDecadeRange_cmd_val}:IQWindow:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, halfDecadeRange=repcap.HalfDecadeRange.Default) -> enums.WindowFunction:
		"""SCPI: [SENSe]:LIST:RANGe<hd>:IQWindow:TYPE \n
		Snippet: value: enums.WindowFunction = driver.applications.k40PhaseNoise.sense.listPy.range.iqWindow.typePy.get(halfDecadeRange = repcap.HalfDecadeRange.Default) \n
		This command selects the window function for a particular half decade. Window functions are available for I/Q sweep mode. \n
			:param halfDecadeRange: optional repeated capability selector. Default value: Rng_1Hz_3Hz (settable in the interface 'Range')
			:return: window_function: RECTangular | GAUSsian | CHEByshev | BHARris | SWEPt"""
		halfDecadeRange_cmd_val = self._cmd_group.get_repcap_cmd_value(halfDecadeRange, repcap.HalfDecadeRange)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{halfDecadeRange_cmd_val}:IQWindow:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.WindowFunction)
