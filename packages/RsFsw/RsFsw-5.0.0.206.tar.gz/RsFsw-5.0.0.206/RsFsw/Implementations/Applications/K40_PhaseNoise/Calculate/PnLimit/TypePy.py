from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, shape: enums.LimitShape, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:PNLimit:TYPE \n
		Snippet: driver.applications.k40PhaseNoise.calculate.pnLimit.typePy.set(shape = enums.LimitShape.FC1, window = repcap.Window.Default) \n
		This command selects the shape of a phase noise limit line. \n
			:param shape: NONE | FC1 | FC2 | FC3 | FC4 | FC5 FC1 Limit line defined by the noise floor and 1 corner frequency. FC2 Limit line defined by the noise floor and 2 corner frequencies. FC3 Limit line defined by the noise floor and 3 corner frequencies. FC4 Limit line defined by the noise floor and 4 corner frequencies. FC5 Limit line defined by the noise floor and 5 corner frequencies. NONE No limit line.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(shape, enums.LimitShape)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:PNLimit:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.LimitShape:
		"""SCPI: CALCulate<n>:PNLimit:TYPE \n
		Snippet: value: enums.LimitShape = driver.applications.k40PhaseNoise.calculate.pnLimit.typePy.get(window = repcap.Window.Default) \n
		This command selects the shape of a phase noise limit line. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: shape: NONE | FC1 | FC2 | FC3 | FC4 | FC5 FC1 Limit line defined by the noise floor and 1 corner frequency. FC2 Limit line defined by the noise floor and 2 corner frequencies. FC3 Limit line defined by the noise floor and 3 corner frequencies. FC4 Limit line defined by the noise floor and 4 corner frequencies. FC5 Limit line defined by the noise floor and 5 corner frequencies. NONE No limit line."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:PNLimit:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.LimitShape)
