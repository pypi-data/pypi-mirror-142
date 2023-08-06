from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ratio:
	"""Ratio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ratio", core, parent)

	def set(self, unit: enums.UnitMode, powerMeter=repcap.PowerMeter.Default) -> None:
		"""SCPI: UNIT:PMETer<p>:POWer:RATio \n
		Snippet: driver.unit.pmeter.power.ratio.set(unit = enums.UnitMode.DB, powerMeter = repcap.PowerMeter.Default) \n
		This command selects the unit for relative power sensor measurements. \n
			:param unit: DB | PCT
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.UnitMode)
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		self._core.io.write(f'UNIT:PMETer{powerMeter_cmd_val}:POWer:RATio {param}')

	# noinspection PyTypeChecker
	def get(self, powerMeter=repcap.PowerMeter.Default) -> enums.UnitMode:
		"""SCPI: UNIT:PMETer<p>:POWer:RATio \n
		Snippet: value: enums.UnitMode = driver.unit.pmeter.power.ratio.get(powerMeter = repcap.PowerMeter.Default) \n
		This command selects the unit for relative power sensor measurements. \n
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
			:return: unit: DB | PCT"""
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		response = self._core.io.query_str(f'UNIT:PMETer{powerMeter_cmd_val}:POWer:RATio?')
		return Conversions.str_to_scalar_enum(response, enums.UnitMode)
