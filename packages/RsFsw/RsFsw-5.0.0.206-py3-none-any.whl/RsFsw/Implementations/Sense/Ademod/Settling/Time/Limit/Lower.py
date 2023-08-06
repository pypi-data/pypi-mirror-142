from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lower:
	"""Lower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lower", core, parent)

	def set(self, position: float) -> None:
		"""SCPI: [SENSe]:ADEMod:SETTling:TIME:LIMit:LOWer \n
		Snippet: driver.sense.ademod.settling.time.limit.lower.set(position = 1.0) \n
		Defines the upper limit of the settling time corridor. The value is defined with reference to the reference value, see
		also method RsFsw.Display.Window.Subwindow.Trace.Y.Scale.Rvalue.set and [SENSe:]ADEMod:PM:RPOint[:X]. For details, see
		'Settling time'. \n
			:param position: Unit: depends on result type
		"""
		param = Conversions.decimal_value_to_str(position)
		self._core.io.write(f'SENSe:ADEMod:SETTling:TIME:LIMit:LOWer {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADEMod:SETTling:TIME:LIMit:LOWer \n
		Snippet: value: float = driver.sense.ademod.settling.time.limit.lower.get() \n
		Defines the upper limit of the settling time corridor. The value is defined with reference to the reference value, see
		also method RsFsw.Display.Window.Subwindow.Trace.Y.Scale.Rvalue.set and [SENSe:]ADEMod:PM:RPOint[:X]. For details, see
		'Settling time'. \n
			:return: position: Unit: depends on result type"""
		response = self._core.io.query_str(f'SENSe:ADEMod:SETTling:TIME:LIMit:LOWer?')
		return Conversions.str_to_float(response)
