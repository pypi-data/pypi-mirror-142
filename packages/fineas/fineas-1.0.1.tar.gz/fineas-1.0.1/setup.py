# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fineas']

package_data = \
{'': ['*']}

install_requires = \
['wrapt>=1.14.0,<2.0.0']

setup_kwargs = {
    'name': 'fineas',
    'version': '1.0.1',
    'description': 'A simple, decorator-based, transition-focused Finite State Machine implementation.',
    'long_description': "# Fineas\n\nA simple, thread-safe, decorator-based, transition-focused Finite State Machine implementation.\n\nPossible Use Cases:\n- Configuration management from multiple sources.\n- Keeping track of state during complex system startup.\n- Tracking state while parsing.\n\n```python\nfrom fineas import state_machine\n\n\n@state_machine(initial_state='new', store_history=True)\nclass TestMachine:\n    def __init__(self):\n        self.config = None\n\n    @state_machine.transition(\n        source=['new', 'invalid_configuration'],\n        dest='configured',\n        error_state='invalid_configuration')\n    def got_config(self, config):\n        # validate config\n        self.config = config\n\n    @state_machine.transition(source='configured', dest='scheduled')\n    def ready(self):\n        pass\n\n    @state_machine.transition(\n        source='scheduled',\n        dest='scheduled',\n        error_state='canceled',\n        failed_state='retry')\n    def run(self, fail_transition):\n        # do work\n        status = self._do_work()\n\n        if not status:\n            fail_transition()\n\n    @state_machine.transition(\n        source='retry',\n        dest='run',\n        error_state='canceled',\n        failed_state='too_many_failures'\n    )\n    def try_again(self, times, fail_transition):\n        for i in range(times):\n            if self._do_work():\n                return\n        fail_transition()\n\n    @state_machine.transition(\n        source=['retry', 'too_many_failures'],\n        dest='cancelled'\n    )\n    def abandon(self):\n        pass\n\n    @state_machine.transition(\n        source='too_many_failures',\n        dest='configured'\n    )\n    def reconfigure(self, config):\n        self.config = config\n\n    def _do_work(self):\n        pass\n\n\nt = TestMachine()\nt.got_config(None)\nt.ready()\nt.run()\nt.try_again(3)\nt.abandon()\n\n\nprint(t.history)\n\nprint(t.state)\n```\n\n## Quickstart\n1) Decorate a class with `@fineas.state_machine(initial_state='new')`.  You must pass a value for \n   `initial_state`.\n2) Define a method that implements the work required to transition form one or more source states\n   to a single destination state.  Decorate that method with \n   `@fineas.transition(source='new', dest='ready')`.\n3)  That's it!  Each instance of your decorated class is its own state machine.  You may check its\ncurrent state with its `state` attribute, and, if you've enabled `record_history`, you can access\n    its transition history with its `history` attribute.\n\n## Overview\nTo turn each instance of a class into a state machine, simply decorate it with \n`@fineas.state_machine()`.  You must pass an `initial_state` value to `@fineas.state_machine()`.\nThis will be the state every instance of your type starts in.  You can also enable recording state\ntransitions with the `record_history` flag; this is useful while developing finite state machines.\n\nEvery transition in your state machine is represented by a method inside the class you annotated \nwith `@fineas.state_machihe()`.  To turn a method into a transition, decorate it with \n`@fineas.transition()` and supply one or more source states for the transition, and exactly one\ndestination state.  You can also define a state to transition to if an exception is raised inside \nyour method (there is also a flag to enable or disable re-raising that exception).  If your method\naccepts a parameter named `fail_transition`, its value will be a callable your method can invoke to\ncause the transition to fail while still allowing your method to return a value to its caller.  You\nmay also pass a `fail_state` parameter to the decorator, and when `fail_transition` is invoked, your\ninstance will be transitioned to the given state.\n\nWhen any method annotated with `@fineas.transistion()` is called, the following steps happen:\n\n1) Acquire a lock over the receiving instance.\n1) Fineas validates that the receiving instance's state is in the sources passed to \n   `@fineas.transition()`\n   - If it is not, a TransitionException is raised.\n1) The decorated method is invoked, passing `fail_transistion` if able.\n1) If the decorated method raises an exception:\n   - If `error_state` was passed, immediately transition to that state.\n   - If `reraise_error` is True, re-raise the exception.\n   - Return.\n1) If `fail_transition` was called:\n   - If 'fail_state' was passed, immediately transition to that state.\n1) If no exception was raised and `fail_transition` was not called, transition to the destination\n   state and return the value returned by the decorated method.\n   \n## Requirements\n\nPython 3.6 or higher\n\nwrapt 1.12.x\n\n## Release Notes\n1.0.1 (12 March, 2021):\n- Minor Cleanup\n- Move to poetry\n- Basic test coverage\n- Bump to 1.0.0 due to no issues being found in the last year.\n\n0.1.0 (07 March, 2021):\n- Initial Release\n",
    'author': 'Chris Blades',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
