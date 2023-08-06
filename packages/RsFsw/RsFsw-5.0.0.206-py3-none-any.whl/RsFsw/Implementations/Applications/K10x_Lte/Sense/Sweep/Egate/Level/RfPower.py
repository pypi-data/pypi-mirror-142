from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfPower:
	"""RfPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfPower", core, parent)

	def set(self, level: float, instrument=repcap.Instrument.Default) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:LEVel<ant>:RFPower \n
		Snippet: driver.applications.k10Xlte.sense.sweep.egate.level.rfPower.set(level = 1.0, instrument = repcap.Instrument.Default) \n
		No command help available \n
			:param level: No help available
			:param instrument: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Level')
		"""
		param = Conversions.decimal_value_to_str(level)
		instrument_cmd_val = self._cmd_group.get_repcap_cmd_value(instrument, repcap.Instrument)
		self._core.io.write(f'SENSe:SWEep:EGATe:LEVel{instrument_cmd_val}:RFPower {param}')

	def get(self, instrument=repcap.Instrument.Default) -> float:
		"""SCPI: [SENSe]:SWEep:EGATe:LEVel<ant>:RFPower \n
		Snippet: value: float = driver.applications.k10Xlte.sense.sweep.egate.level.rfPower.get(instrument = repcap.Instrument.Default) \n
		No command help available \n
			:param instrument: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Level')
			:return: level: No help available"""
		instrument_cmd_val = self._cmd_group.get_repcap_cmd_value(instrument, repcap.Instrument)
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:LEVel{instrument_cmd_val}:RFPower?')
		return Conversions.str_to_float(response)
