from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tradeoff:
	"""Tradeoff commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tradeoff", core, parent)

	def set(self, power_linearity_tradeoff: float) -> None:
		"""SCPI: CONFigure:DPD:TRADeoff \n
		Snippet: driver.applications.k18AmplifierEt.configure.dpd.tradeoff.set(power_linearity_tradeoff = 1.0) \n
		This command defines the power / linearity tradeoff for polynomial DPD calculation.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on polynomial DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) . \n
			:param power_linearity_tradeoff: numeric value Unit: PCT
		"""
		param = Conversions.decimal_value_to_str(power_linearity_tradeoff)
		self._core.io.write(f'CONFigure:DPD:TRADeoff {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:DPD:TRADeoff \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.dpd.tradeoff.get() \n
		This command defines the power / linearity tradeoff for polynomial DPD calculation.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on polynomial DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) . \n
			:return: power_linearity_tradeoff: numeric value Unit: PCT"""
		response = self._core.io.query_str(f'CONFigure:DPD:TRADeoff?')
		return Conversions.str_to_float(response)
