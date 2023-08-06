from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Flist:
	"""Flist commands group definition. 8 total commands, 7 Subgroups, 1 group commands
	Repeated Capability: FileList, default value after init: FileList.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("flist", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_fileList_get', 'repcap_fileList_set', repcap.FileList.Nr1)

	def repcap_fileList_set(self, fileList: repcap.FileList) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to FileList.Default
		Default value after init: FileList.Nr1"""
		self._cmd_group.set_repcap_enum_value(fileList)

	def repcap_fileList_get(self) -> repcap.FileList:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def size(self):
		"""size commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_size'):
			from .Size import Size
			self._size = Size(self._core, self._cmd_group)
		return self._size

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import Catalog
			self._catalog = Catalog(self._core, self._cmd_group)
		return self._catalog

	@property
	def remove(self):
		"""remove commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_remove'):
			from .Remove import Remove
			self._remove = Remove(self._core, self._cmd_group)
		return self._remove

	@property
	def select(self):
		"""select commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_select'):
			from .Select import Select
			self._select = Select(self._core, self._cmd_group)
		return self._select

	@property
	def insert(self):
		"""insert commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_insert'):
			from .Insert import Insert
			self._insert = Insert(self._core, self._cmd_group)
		return self._insert

	@property
	def magnitude(self):
		"""magnitude commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_magnitude'):
			from .Magnitude import Magnitude
			self._magnitude = Magnitude(self._core, self._cmd_group)
		return self._magnitude

	@property
	def phase(self):
		"""phase commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_phase'):
			from .Phase import Phase
			self._phase = Phase(self._core, self._cmd_group)
		return self._phase

	def clear(self, inputIx=repcap.InputIx.Default, fileList=repcap.FileList.Default) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:INPut<ip>:USER:FLISt<fli>:CLEar \n
		Snippet: driver.sense.correction.fresponse.inputPy.user.flist.clear(inputIx = repcap.InputIx.Default, fileList = repcap.FileList.Default) \n
		Removes all frequency response (.fres) files in the current configuration for the selected or all input types. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:param fileList: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Flist')
		"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		fileList_cmd_val = self._cmd_group.get_repcap_cmd_value(fileList, repcap.FileList)
		self._core.io.write(f'SENSe:CORRection:FRESponse:INPut{inputIx_cmd_val}:USER:FLISt{fileList_cmd_val}:CLEar')

	def clear_with_opc(self, inputIx=repcap.InputIx.Default, fileList=repcap.FileList.Default, opc_timeout_ms: int = -1) -> None:
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		fileList_cmd_val = self._cmd_group.get_repcap_cmd_value(fileList, repcap.FileList)
		"""SCPI: [SENSe]:CORRection:FRESponse:INPut<ip>:USER:FLISt<fli>:CLEar \n
		Snippet: driver.sense.correction.fresponse.inputPy.user.flist.clear_with_opc(inputIx = repcap.InputIx.Default, fileList = repcap.FileList.Default) \n
		Removes all frequency response (.fres) files in the current configuration for the selected or all input types. \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:param fileList: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Flist')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:CORRection:FRESponse:INPut{inputIx_cmd_val}:USER:FLISt{fileList_cmd_val}:CLEar', opc_timeout_ms)

	def clone(self) -> 'Flist':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Flist(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
