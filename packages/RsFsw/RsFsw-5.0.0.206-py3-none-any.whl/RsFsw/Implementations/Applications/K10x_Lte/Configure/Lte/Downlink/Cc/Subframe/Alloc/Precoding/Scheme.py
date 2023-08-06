from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scheme:
	"""Scheme commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scheme", core, parent)

	def set(self, scheme: enums.PrecodingScheme, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:SUBFrame<sf>:ALLoc<al>:PRECoding[:SCHeme] \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.subframe.alloc.precoding.scheme.set(scheme = enums.PrecodingScheme.BF, carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default, allocation = repcap.Allocation.Default) \n
		This command selects the precoding scheme of an allocation. \n
			:param scheme: NONE Do not use a precoding scheme. BF Use beamforming scheme. SPM Use spatial multiplexing scheme. TXD Use transmit diversity scheme.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
			:param allocation: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(scheme, enums.PrecodingScheme)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc{allocation_cmd_val}:PRECoding:SCHeme {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default, allocation=repcap.Allocation.Default) -> enums.PrecodingScheme:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:SUBFrame<sf>:ALLoc<al>:PRECoding[:SCHeme] \n
		Snippet: value: enums.PrecodingScheme = driver.applications.k10Xlte.configure.lte.downlink.cc.subframe.alloc.precoding.scheme.get(carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default, allocation = repcap.Allocation.Default) \n
		This command selects the precoding scheme of an allocation. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
			:param allocation: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: scheme: NONE Do not use a precoding scheme. BF Use beamforming scheme. SPM Use spatial multiplexing scheme. TXD Use transmit diversity scheme."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc{allocation_cmd_val}:PRECoding:SCHeme?')
		return Conversions.str_to_scalar_enum(response, enums.PrecodingScheme)
