from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class User:
	"""User commands group definition. 24 total commands, 6 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("user", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def adjust(self):
		"""adjust commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_adjust'):
			from .Adjust import Adjust
			self._adjust = Adjust(self._core, self._cmd_group)
		return self._adjust

	@property
	def refresh(self):
		"""refresh commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_refresh'):
			from .Refresh import Refresh
			self._refresh = Refresh(self._core, self._cmd_group)
		return self._refresh

	@property
	def store(self):
		"""store commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_store'):
			from .Store import Store
			self._store = Store(self._core, self._cmd_group)
		return self._store

	@property
	def flist(self):
		"""flist commands group. 7 Sub-classes, 1 commands."""
		if not hasattr(self, '_flist'):
			from .Flist import Flist
			self._flist = Flist(self._core, self._cmd_group)
		return self._flist

	@property
	def slist(self):
		"""slist commands group. 7 Sub-classes, 2 commands."""
		if not hasattr(self, '_slist'):
			from .Slist import Slist
			self._slist = Slist(self._core, self._cmd_group)
		return self._slist

	def preset(self, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:INPut<ip>:USER:PRESet \n
		Snippet: driver.sense.correction.fresponse.inputPy.user.preset(inputIx = repcap.InputIx.Default) \n
		Restores the default frequency response correction settings (containing only files specific to the R&S FSW itself) .
		Frequency response correction using .fres files is deactivated. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'SENSe:CORRection:FRESponse:INPut{inputIx_cmd_val}:USER:PRESet')

	def preset_with_opc(self, inputIx=repcap.InputIx.Default, opc_timeout_ms: int = -1) -> None:
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		"""SCPI: [SENSe]:CORRection:FRESponse:INPut<ip>:USER:PRESet \n
		Snippet: driver.sense.correction.fresponse.inputPy.user.preset_with_opc(inputIx = repcap.InputIx.Default) \n
		Restores the default frequency response correction settings (containing only files specific to the R&S FSW itself) .
		Frequency response correction using .fres files is deactivated. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:CORRection:FRESponse:INPut{inputIx_cmd_val}:USER:PRESet', opc_timeout_ms)

	def load(self, file_path: str, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:INPut<ip>:USER:LOAD \n
		Snippet: driver.sense.correction.fresponse.inputPy.user.load(file_path = '1', inputIx = repcap.InputIx.Default) \n
		Loads a stored user-defined frequency response correction scenario. \n
			:param file_path: string
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.value_to_quoted_str(file_path)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'SENSe:CORRection:FRESponse:INPut{inputIx_cmd_val}:USER:LOAD {param}')

	def clone(self) -> 'User':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = User(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
