from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uncertainty:
	"""Uncertainty commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uncertainty", core, parent)

	@property
	def hot(self):
		"""hot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hot'):
			from .Hot import Hot
			self._hot = Hot(self._core, self._cmd_group)
		return self._hot

	@property
	def cold(self):
		"""cold commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cold'):
			from .Cold import Cold
			self._cold = Cold(self._core, self._cmd_group)
		return self._cold

	def set(self, uncertainty: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:UNCertainty:ENR:CALibration:UNCertainty \n
		Snippet: driver.applications.k30NoiseFigure.calculate.uncertainty.enr.calibration.uncertainty.set(uncertainty = 1.0, window = repcap.Window.Default) \n
		This command defines the uncertainty of a calibration noise source.
		This command is available when [SENSe:]CORRection:ENR:COMMon and [SENSe:]CORRection:ENR:COMMon are off. If a smart noise
		source is used for calibration, the uncertainty values defined in the SNS table are used. \n
			:param uncertainty: Uncertainty value of the noise source. Refer to the data sheet of the noise source to determine its uncertainty. Unit: DB
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(uncertainty)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:UNCertainty:ENR:CALibration:UNCertainty {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:UNCertainty:ENR:CALibration:UNCertainty \n
		Snippet: value: float = driver.applications.k30NoiseFigure.calculate.uncertainty.enr.calibration.uncertainty.get(window = repcap.Window.Default) \n
		This command defines the uncertainty of a calibration noise source.
		This command is available when [SENSe:]CORRection:ENR:COMMon and [SENSe:]CORRection:ENR:COMMon are off. If a smart noise
		source is used for calibration, the uncertainty values defined in the SNS table are used. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: uncertainty: Uncertainty value of the noise source. Refer to the data sheet of the noise source to determine its uncertainty. Unit: DB"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:UNCertainty:ENR:CALibration:UNCertainty?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Uncertainty':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Uncertainty(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
