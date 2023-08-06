from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqMcomp:
	"""IqMcomp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqMcomp", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:TRACking:IQMComp \n
		Snippet: driver.applications.k9X11Ad.sense.tracking.iqMcomp.set(state = False) \n
		Activates or deactivates the compensation for I/Q mismatch (gain imbalance, quadrature offset, I/Q skew, see 'Modulation
		accuracy parameters') . \n
			:param state: ON | OFF | 1 | 0 ON | 1 Compensation for gain imbalance, quadrature offset, and I/Q skew impairments is applied. OFF | 0 Compensation is not applied; this setting is required for measurements strictly according to the IEEE 802.11ad standard
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:TRACking:IQMComp {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:TRACking:IQMComp \n
		Snippet: value: bool = driver.applications.k9X11Ad.sense.tracking.iqMcomp.get() \n
		Activates or deactivates the compensation for I/Q mismatch (gain imbalance, quadrature offset, I/Q skew, see 'Modulation
		accuracy parameters') . \n
			:return: state: ON | OFF | 1 | 0 ON | 1 Compensation for gain imbalance, quadrature offset, and I/Q skew impairments is applied. OFF | 0 Compensation is not applied; this setting is required for measurements strictly according to the IEEE 802.11ad standard"""
		response = self._core.io.query_str(f'SENSe:TRACking:IQMComp?')
		return Conversions.str_to_bool(response)
