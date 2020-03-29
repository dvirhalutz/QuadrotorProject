# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rosplan_knowledge_msgs/GetMetricServiceRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GetMetricServiceRequest(genpy.Message):
  _md5sum = "d41d8cd98f00b204e9800998ecf8427e"
  _type = "rosplan_knowledge_msgs/GetMetricServiceRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """


"""
  __slots__ = []
  _slot_types = []

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetMetricServiceRequest, self).__init__(*args, **kwds)

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rosplan_knowledge_msgs/GetMetricServiceResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import rosplan_knowledge_msgs.msg
import genpy
import diagnostic_msgs.msg

class GetMetricServiceResponse(genpy.Message):
  _md5sum = "d8654505c165321f0d5dd974ec4ca392"
  _type = "rosplan_knowledge_msgs/GetMetricServiceResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """rosplan_knowledge_msgs/KnowledgeItem metric


================================================================================
MSG: rosplan_knowledge_msgs/KnowledgeItem
# A knowledge item used to represent a piece of the state in ROSPlan

uint8 INSTANCE = 0
uint8 FACT = 1
uint8 FUNCTION = 2
uint8 EXPRESSION = 3
uint8 INEQUALITY = 4

uint8 knowledge_type

# time at which this knowledge becomes true
time initial_time

# knowledge is explicitly false
bool is_negative

#---------
# INSTANCE
#---------

# instance knowledge_type
string instance_type
string instance_name

#----------------------
# PREDICATE OR FUNCTION
#----------------------

# attribute knowledge_type
string attribute_name
diagnostic_msgs/KeyValue[] values

#---------
# FUNCTION
#---------

# function value
float64 function_value

#-----------
# EXPRESSION
#-----------

string optimization
rosplan_knowledge_msgs/ExprComposite expr

#-----------
# INEQUALITY
#-----------

rosplan_knowledge_msgs/DomainInequality ineq

================================================================================
MSG: diagnostic_msgs/KeyValue
string key # what to label this value when viewing
string value # a value to track over time

================================================================================
MSG: rosplan_knowledge_msgs/ExprComposite
# A message used to represent a numerical expression; composite type (2/2)
# stores an array of ExprBase as prefix notation

# components
ExprBase[] tokens

================================================================================
MSG: rosplan_knowledge_msgs/ExprBase
# A message used to represent a numerical expression; base types (1/2)

# expression types
uint8 CONSTANT = 0
uint8 FUNCTION = 1
uint8 OPERATOR = 2
uint8 SPECIAL  = 3

# operators
uint8 ADD    = 0
uint8 SUB    = 1
uint8 MUL    = 2
uint8 DIV    = 3
uint8 UMINUS = 4

# special types
uint8 HASHT      = 0
uint8 TOTAL_TIME = 1
uint8 DURATION   = 2

# expression base type
uint8 expr_type

# constant value
float64 constant

# function
rosplan_knowledge_msgs/DomainFormula function

# operator
uint8 op

# special
uint8 special_type

================================================================================
MSG: rosplan_knowledge_msgs/DomainFormula
# A message used to represent an atomic formula from the domain.
# typed_parameters matches label -> type
string name
diagnostic_msgs/KeyValue[] typed_parameters

================================================================================
MSG: rosplan_knowledge_msgs/DomainInequality
# A message used to store the numeric effects of an action
# Can be grounded or ungrounded

uint8 GREATER   = 0
uint8 GREATEREQ = 1
uint8 LESS      = 2
uint8 LESSEQ    = 3
uint8 EQUALS    = 4

uint8 comparison_type

rosplan_knowledge_msgs/ExprComposite LHS
rosplan_knowledge_msgs/ExprComposite RHS

bool grounded
"""
  __slots__ = ['metric']
  _slot_types = ['rosplan_knowledge_msgs/KnowledgeItem']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       metric

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetMetricServiceResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.metric is None:
        self.metric = rosplan_knowledge_msgs.msg.KnowledgeItem()
    else:
      self.metric = rosplan_knowledge_msgs.msg.KnowledgeItem()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_B2IB().pack(_x.metric.knowledge_type, _x.metric.initial_time.secs, _x.metric.initial_time.nsecs, _x.metric.is_negative))
      _x = self.metric.instance_type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.metric.instance_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.metric.attribute_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.metric.values)
      buff.write(_struct_I.pack(length))
      for val1 in self.metric.values:
        _x = val1.key
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.value
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_get_struct_d().pack(self.metric.function_value))
      _x = self.metric.optimization
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.metric.expr.tokens)
      buff.write(_struct_I.pack(length))
      for val1 in self.metric.expr.tokens:
        _x = val1
        buff.write(_get_struct_Bd().pack(_x.expr_type, _x.constant))
        _v1 = val1.function
        _x = _v1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(_v1.typed_parameters)
        buff.write(_struct_I.pack(length))
        for val3 in _v1.typed_parameters:
          _x = val3.key
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val3.value
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_get_struct_2B().pack(_x.op, _x.special_type))
      buff.write(_get_struct_B().pack(self.metric.ineq.comparison_type))
      length = len(self.metric.ineq.LHS.tokens)
      buff.write(_struct_I.pack(length))
      for val1 in self.metric.ineq.LHS.tokens:
        _x = val1
        buff.write(_get_struct_Bd().pack(_x.expr_type, _x.constant))
        _v2 = val1.function
        _x = _v2.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(_v2.typed_parameters)
        buff.write(_struct_I.pack(length))
        for val3 in _v2.typed_parameters:
          _x = val3.key
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val3.value
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_get_struct_2B().pack(_x.op, _x.special_type))
      length = len(self.metric.ineq.RHS.tokens)
      buff.write(_struct_I.pack(length))
      for val1 in self.metric.ineq.RHS.tokens:
        _x = val1
        buff.write(_get_struct_Bd().pack(_x.expr_type, _x.constant))
        _v3 = val1.function
        _x = _v3.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(_v3.typed_parameters)
        buff.write(_struct_I.pack(length))
        for val3 in _v3.typed_parameters:
          _x = val3.key
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val3.value
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_get_struct_2B().pack(_x.op, _x.special_type))
      buff.write(_get_struct_B().pack(self.metric.ineq.grounded))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.metric is None:
        self.metric = rosplan_knowledge_msgs.msg.KnowledgeItem()
      end = 0
      _x = self
      start = end
      end += 10
      (_x.metric.knowledge_type, _x.metric.initial_time.secs, _x.metric.initial_time.nsecs, _x.metric.is_negative,) = _get_struct_B2IB().unpack(str[start:end])
      self.metric.is_negative = bool(self.metric.is_negative)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.metric.instance_type = str[start:end].decode('utf-8')
      else:
        self.metric.instance_type = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.metric.instance_name = str[start:end].decode('utf-8')
      else:
        self.metric.instance_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.metric.attribute_name = str[start:end].decode('utf-8')
      else:
        self.metric.attribute_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.metric.values = []
      for i in range(0, length):
        val1 = diagnostic_msgs.msg.KeyValue()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.key = str[start:end].decode('utf-8')
        else:
          val1.key = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.value = str[start:end].decode('utf-8')
        else:
          val1.value = str[start:end]
        self.metric.values.append(val1)
      start = end
      end += 8
      (self.metric.function_value,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.metric.optimization = str[start:end].decode('utf-8')
      else:
        self.metric.optimization = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.metric.expr.tokens = []
      for i in range(0, length):
        val1 = rosplan_knowledge_msgs.msg.ExprBase()
        _x = val1
        start = end
        end += 9
        (_x.expr_type, _x.constant,) = _get_struct_Bd().unpack(str[start:end])
        _v4 = val1.function
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v4.name = str[start:end].decode('utf-8')
        else:
          _v4.name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v4.typed_parameters = []
        for i in range(0, length):
          val3 = diagnostic_msgs.msg.KeyValue()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.key = str[start:end].decode('utf-8')
          else:
            val3.key = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.value = str[start:end].decode('utf-8')
          else:
            val3.value = str[start:end]
          _v4.typed_parameters.append(val3)
        _x = val1
        start = end
        end += 2
        (_x.op, _x.special_type,) = _get_struct_2B().unpack(str[start:end])
        self.metric.expr.tokens.append(val1)
      start = end
      end += 1
      (self.metric.ineq.comparison_type,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.metric.ineq.LHS.tokens = []
      for i in range(0, length):
        val1 = rosplan_knowledge_msgs.msg.ExprBase()
        _x = val1
        start = end
        end += 9
        (_x.expr_type, _x.constant,) = _get_struct_Bd().unpack(str[start:end])
        _v5 = val1.function
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v5.name = str[start:end].decode('utf-8')
        else:
          _v5.name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v5.typed_parameters = []
        for i in range(0, length):
          val3 = diagnostic_msgs.msg.KeyValue()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.key = str[start:end].decode('utf-8')
          else:
            val3.key = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.value = str[start:end].decode('utf-8')
          else:
            val3.value = str[start:end]
          _v5.typed_parameters.append(val3)
        _x = val1
        start = end
        end += 2
        (_x.op, _x.special_type,) = _get_struct_2B().unpack(str[start:end])
        self.metric.ineq.LHS.tokens.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.metric.ineq.RHS.tokens = []
      for i in range(0, length):
        val1 = rosplan_knowledge_msgs.msg.ExprBase()
        _x = val1
        start = end
        end += 9
        (_x.expr_type, _x.constant,) = _get_struct_Bd().unpack(str[start:end])
        _v6 = val1.function
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v6.name = str[start:end].decode('utf-8')
        else:
          _v6.name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v6.typed_parameters = []
        for i in range(0, length):
          val3 = diagnostic_msgs.msg.KeyValue()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.key = str[start:end].decode('utf-8')
          else:
            val3.key = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.value = str[start:end].decode('utf-8')
          else:
            val3.value = str[start:end]
          _v6.typed_parameters.append(val3)
        _x = val1
        start = end
        end += 2
        (_x.op, _x.special_type,) = _get_struct_2B().unpack(str[start:end])
        self.metric.ineq.RHS.tokens.append(val1)
      start = end
      end += 1
      (self.metric.ineq.grounded,) = _get_struct_B().unpack(str[start:end])
      self.metric.ineq.grounded = bool(self.metric.ineq.grounded)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_B2IB().pack(_x.metric.knowledge_type, _x.metric.initial_time.secs, _x.metric.initial_time.nsecs, _x.metric.is_negative))
      _x = self.metric.instance_type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.metric.instance_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.metric.attribute_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.metric.values)
      buff.write(_struct_I.pack(length))
      for val1 in self.metric.values:
        _x = val1.key
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.value
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_get_struct_d().pack(self.metric.function_value))
      _x = self.metric.optimization
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.metric.expr.tokens)
      buff.write(_struct_I.pack(length))
      for val1 in self.metric.expr.tokens:
        _x = val1
        buff.write(_get_struct_Bd().pack(_x.expr_type, _x.constant))
        _v7 = val1.function
        _x = _v7.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(_v7.typed_parameters)
        buff.write(_struct_I.pack(length))
        for val3 in _v7.typed_parameters:
          _x = val3.key
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val3.value
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_get_struct_2B().pack(_x.op, _x.special_type))
      buff.write(_get_struct_B().pack(self.metric.ineq.comparison_type))
      length = len(self.metric.ineq.LHS.tokens)
      buff.write(_struct_I.pack(length))
      for val1 in self.metric.ineq.LHS.tokens:
        _x = val1
        buff.write(_get_struct_Bd().pack(_x.expr_type, _x.constant))
        _v8 = val1.function
        _x = _v8.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(_v8.typed_parameters)
        buff.write(_struct_I.pack(length))
        for val3 in _v8.typed_parameters:
          _x = val3.key
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val3.value
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_get_struct_2B().pack(_x.op, _x.special_type))
      length = len(self.metric.ineq.RHS.tokens)
      buff.write(_struct_I.pack(length))
      for val1 in self.metric.ineq.RHS.tokens:
        _x = val1
        buff.write(_get_struct_Bd().pack(_x.expr_type, _x.constant))
        _v9 = val1.function
        _x = _v9.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(_v9.typed_parameters)
        buff.write(_struct_I.pack(length))
        for val3 in _v9.typed_parameters:
          _x = val3.key
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val3.value
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_get_struct_2B().pack(_x.op, _x.special_type))
      buff.write(_get_struct_B().pack(self.metric.ineq.grounded))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.metric is None:
        self.metric = rosplan_knowledge_msgs.msg.KnowledgeItem()
      end = 0
      _x = self
      start = end
      end += 10
      (_x.metric.knowledge_type, _x.metric.initial_time.secs, _x.metric.initial_time.nsecs, _x.metric.is_negative,) = _get_struct_B2IB().unpack(str[start:end])
      self.metric.is_negative = bool(self.metric.is_negative)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.metric.instance_type = str[start:end].decode('utf-8')
      else:
        self.metric.instance_type = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.metric.instance_name = str[start:end].decode('utf-8')
      else:
        self.metric.instance_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.metric.attribute_name = str[start:end].decode('utf-8')
      else:
        self.metric.attribute_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.metric.values = []
      for i in range(0, length):
        val1 = diagnostic_msgs.msg.KeyValue()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.key = str[start:end].decode('utf-8')
        else:
          val1.key = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.value = str[start:end].decode('utf-8')
        else:
          val1.value = str[start:end]
        self.metric.values.append(val1)
      start = end
      end += 8
      (self.metric.function_value,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.metric.optimization = str[start:end].decode('utf-8')
      else:
        self.metric.optimization = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.metric.expr.tokens = []
      for i in range(0, length):
        val1 = rosplan_knowledge_msgs.msg.ExprBase()
        _x = val1
        start = end
        end += 9
        (_x.expr_type, _x.constant,) = _get_struct_Bd().unpack(str[start:end])
        _v10 = val1.function
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v10.name = str[start:end].decode('utf-8')
        else:
          _v10.name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v10.typed_parameters = []
        for i in range(0, length):
          val3 = diagnostic_msgs.msg.KeyValue()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.key = str[start:end].decode('utf-8')
          else:
            val3.key = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.value = str[start:end].decode('utf-8')
          else:
            val3.value = str[start:end]
          _v10.typed_parameters.append(val3)
        _x = val1
        start = end
        end += 2
        (_x.op, _x.special_type,) = _get_struct_2B().unpack(str[start:end])
        self.metric.expr.tokens.append(val1)
      start = end
      end += 1
      (self.metric.ineq.comparison_type,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.metric.ineq.LHS.tokens = []
      for i in range(0, length):
        val1 = rosplan_knowledge_msgs.msg.ExprBase()
        _x = val1
        start = end
        end += 9
        (_x.expr_type, _x.constant,) = _get_struct_Bd().unpack(str[start:end])
        _v11 = val1.function
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v11.name = str[start:end].decode('utf-8')
        else:
          _v11.name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v11.typed_parameters = []
        for i in range(0, length):
          val3 = diagnostic_msgs.msg.KeyValue()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.key = str[start:end].decode('utf-8')
          else:
            val3.key = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.value = str[start:end].decode('utf-8')
          else:
            val3.value = str[start:end]
          _v11.typed_parameters.append(val3)
        _x = val1
        start = end
        end += 2
        (_x.op, _x.special_type,) = _get_struct_2B().unpack(str[start:end])
        self.metric.ineq.LHS.tokens.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.metric.ineq.RHS.tokens = []
      for i in range(0, length):
        val1 = rosplan_knowledge_msgs.msg.ExprBase()
        _x = val1
        start = end
        end += 9
        (_x.expr_type, _x.constant,) = _get_struct_Bd().unpack(str[start:end])
        _v12 = val1.function
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v12.name = str[start:end].decode('utf-8')
        else:
          _v12.name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v12.typed_parameters = []
        for i in range(0, length):
          val3 = diagnostic_msgs.msg.KeyValue()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.key = str[start:end].decode('utf-8')
          else:
            val3.key = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.value = str[start:end].decode('utf-8')
          else:
            val3.value = str[start:end]
          _v12.typed_parameters.append(val3)
        _x = val1
        start = end
        end += 2
        (_x.op, _x.special_type,) = _get_struct_2B().unpack(str[start:end])
        self.metric.ineq.RHS.tokens.append(val1)
      start = end
      end += 1
      (self.metric.ineq.grounded,) = _get_struct_B().unpack(str[start:end])
      self.metric.ineq.grounded = bool(self.metric.ineq.grounded)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_Bd = None
def _get_struct_Bd():
    global _struct_Bd
    if _struct_Bd is None:
        _struct_Bd = struct.Struct("<Bd")
    return _struct_Bd
_struct_B2IB = None
def _get_struct_B2IB():
    global _struct_B2IB
    if _struct_B2IB is None:
        _struct_B2IB = struct.Struct("<B2IB")
    return _struct_B2IB
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_d = None
def _get_struct_d():
    global _struct_d
    if _struct_d is None:
        _struct_d = struct.Struct("<d")
    return _struct_d
_struct_2B = None
def _get_struct_2B():
    global _struct_2B
    if _struct_2B is None:
        _struct_2B = struct.Struct("<2B")
    return _struct_2B
class GetMetricService(object):
  _type          = 'rosplan_knowledge_msgs/GetMetricService'
  _md5sum = 'd8654505c165321f0d5dd974ec4ca392'
  _request_class  = GetMetricServiceRequest
  _response_class = GetMetricServiceResponse