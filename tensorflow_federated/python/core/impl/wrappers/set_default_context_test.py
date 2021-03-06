# Lint as: python3
# Copyright 2018, The TensorFlow Federated Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from absl.testing import absltest

from tensorflow_federated.python.core.impl import execution_context
from tensorflow_federated.python.core.impl.context_stack_test_utils import TestContext
from tensorflow_federated.python.core.impl.wrappers.get_context_stack import get_context_stack
from tensorflow_federated.python.core.impl.wrappers.set_default_context import set_default_context


class SetDefaultContextTest(absltest.TestCase):

  def test_set_dafault_context(self):
    ctx_stack = get_context_stack()
    self.assertIsInstance(ctx_stack.current, execution_context.ExecutionContext)
    foo = TestContext('foo')
    set_default_context(foo)
    self.assertIs(ctx_stack.current, foo)
    set_default_context()
    self.assertIsInstance(ctx_stack.current, execution_context.ExecutionContext)


if __name__ == '__main__':
  absltest.main()
