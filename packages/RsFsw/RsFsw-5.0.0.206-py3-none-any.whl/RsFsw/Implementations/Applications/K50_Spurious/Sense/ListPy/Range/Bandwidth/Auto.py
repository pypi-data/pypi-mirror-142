from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:BANDwidth:AUTO \n
		Snippet: driver.applications.k50Spurious.sense.listPy.range.bandwidth.auto.set(state = False, rangePy = repcap.RangePy.Default) \n
		Activates or deactivates automatic definition of the RBW for individual ranges. If necessary, the range is divided
		further into segments. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.bool_to_str(state)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:BANDwidth:AUTO {param}')

	def get(self, state: bool, rangePy=repcap.RangePy.Default) -> bool:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:BANDwidth:AUTO \n
		Snippet: value: bool = driver.applications.k50Spurious.sense.listPy.range.bandwidth.auto.get(state = False, rangePy = repcap.RangePy.Default) \n
		Activates or deactivates automatic definition of the RBW for individual ranges. If necessary, the range is divided
		further into segments. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		param = Conversions.bool_to_str(state)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{rangePy_cmd_val}:BANDwidth:AUTO? {param}')
		return Conversions.str_to_bool(response)
