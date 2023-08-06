from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Detector:
	"""Detector commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("detector", core, parent)

	def set(self, detector: enums.DetectorA, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> None:
		"""SCPI: CALCulate<n>:DELTamarker<m>:FUNCtion:FMEasurement:DETector \n
		Snippet: driver.calculate.deltaMarker.function.fmeasurement.detector.set(detector = enums.DetectorA.ACSine, window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		This command selects the detector for a specific marker during the final measurement. If the marker is not yet active,
		the command also turns the marker on. \n
			:param detector: OFF no final measurement is performed AVER average detector CAV CISPR Average detector CRMS RMS Average detector POS maximum peak detector QPE quasipeak detector
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
		"""
		param = Conversions.enum_scalar_to_str(detector, enums.DetectorA)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		self._core.io.write(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:FUNCtion:FMEasurement:DETector {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> enums.DetectorA:
		"""SCPI: CALCulate<n>:DELTamarker<m>:FUNCtion:FMEasurement:DETector \n
		Snippet: value: enums.DetectorA = driver.calculate.deltaMarker.function.fmeasurement.detector.get(window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		This command selects the detector for a specific marker during the final measurement. If the marker is not yet active,
		the command also turns the marker on. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
			:return: detector: OFF no final measurement is performed AVER average detector CAV CISPR Average detector CRMS RMS Average detector POS maximum peak detector QPE quasipeak detector"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:FUNCtion:FMEasurement:DETector?')
		return Conversions.str_to_scalar_enum(response, enums.DetectorA)
