[n] Move startup logic out of `from tide import Tide` and place in `Tide.__init__`
[x] add callbacks from editor
[x] implement receiver: "tide" in stdio stdin for atide
[x] add non-blocking infinite loop to cli
[x] convert tests from nose to pytest
[x] run tests in a docker container
[x] add simple tests based on stdio and to build an understanding of how config items should work
[x] implement startup complete callback
[x] fix startup_complete showing in atide - library issue
[x] fix stdio reading to handle doing all buffer startup
[x] implement local server for IDEs that don't have python integrated
[x] abstract all vim-related code:
  - `./defaults/actions/set_buffer.py`
[x] `update internal._buffer_caches` for template buffers
[x] stop stdio read taking up all processor
[x] do tracing on tide package to determine what is holding package open after shutdown
[x] implement a shutdown/stop_tide call
[x] do cleanup in test_config_yaml.py correcly
[x] move stdio functions to under editor_wrappers 
[x] move stdio editor functions into folder under editor_wrappers
[n] use object in stdio request and response objects
[n] move common classes into module paths - action, command, config, editor, filter, logging, helpers
[n] implement shutdown/stop command from editor
[n] move filters into config. convert code to regexes or code in yaml.
[n] ability to define filters in config as well as files - to use a parser - https://en.wikipedia.org/wiki/Compiler-compiler - and - https://en.wikipedia.org/wiki/Yacc
[x] fix tests
[x] write more tests
[x] add tests for callbacks
[x] determine tests to be created for stdio and add config
[x] move to github.com/tide
[x] fix log.py permission denied when file to write to is set without a path
[x] fix function_args in function_args with stdio
[x] allow editor type to be set on startup
[x] move before_command, command and after_command to tide from vgdb (and so it doesn't need to be implemented in atide)
[x] remove function_args showing in input_args with stdio
[?] reconcile missing buffer_name 
[x] create Config().getEvents() and getBuffers() methods
[x] consoloidate filter, action and editor_wrapper classes find files functionality into separate class
[x] rework config command stuff into smaller, more manageable classes. add tests
[?] refactor out dict checks in run_command
[x] refactor run_config_command to be smaller and testable
[x] create a CommandProcessSettings object for config settings in CommandProcess __init__
[x] add makefile for all commands
[x] refactor action_name and type in Action and ConfigCommandItem
[x] fix filter.py to use python_file.py
[x] create a filter path helpers class filter_paths
[x] fix recursive info registers when added to do_buffer_diff in assembly config
    and refactor command comfig item to allow any type of config command in event_args
[x] fix vg_registers not updating for stdio on stepi command
  {"command":{"action":"set_config_dictionary_item","value":""},"sender":"editor","receiver":"tide","has_callback":false,"event_id":"102722b2-c158-497b-ae54-45b4646a7f5e"}
[x] add more fine-grained unit tests
[x] complete SysPathContainer and tests
[x] add tests and config for buffers
[n] clean up having both function_args and event_input_args in function_args (possibly rename) ./defaults/actions/run_editor_function.py
    (see test_c info_source vs set_highlight_line)
[x] add codecov to make file
[x] create a common object creation class - filters, editor_wrappers, etc.
[x] place logical components into separate folders - use modules approach with __init__.py files add packages to lib_paths.py
[x] make option for commands to not show for users (user_callable) for atide - this is an editor-specific thing from the config
[-] rename editor references to interface - maybe later
[x] add linting and docker container for linting
[x] split config source into base, environment and default - possibly remove default config location as it's not really required
[x] clean up path_helpers and config_source and log.py
[x] set linting rules for pylint
[x] fix tests
[x] create a build pipeline in shippable.io and add shippable.yml to repo
[x] rework stdio class and rename
[x] fix window split in vgdb for test_c plugin
[x] fix the excluded_lines not working
[x] look at implementing filters as regex in config where possible. look at lex language options where not possible
[n] prevent new objects being created every time the filters are run - use dict like for config filters
[x] untangle config_source path_hlpers cyclic dependency
[x] fix pylint container
[n] move command_action_condition and command_action_converter to config_command path
[x] refactor vim81 run_editor_function
[n] refactor filter modules to separate directory
[x] add more comprehensive tests (some, not all done)
[x] refactor config_command_buffer to not require so many variables
[n] possibly move buffer_cache setting closer to command_output - currently only in config_command_buffer_cache
[x] fix tests for vim - vgdb
[x] add print to stdout logging function using colourised tty [INFO] [module] [message] ..
[x] fix assembly not stepping through to third page of disassembly
[x] have the ability to show info at startup for settings, etc.
[x]  and have ability to log actions, filters, functions, etc to a buffer to make debugging easier
[x] fix up tests for command_handler_2
[l] have ability for buffer to be able to set filter by name (would override filter for buffer if it exists)
[x] add tests for run_command_with_match
[x] implement plugin for python - to use pdb module
[x] fix tests
[x] test on linux
[x] fix vg_template updating after step for test_c - showing old line numbers e.g. 6 instead of 7
[x] fix buffer jitter in atide on vg_code
[x] fix atide not updating template for test_c
[x] create a dev environment setup section to the Makefile - install all other repos, dependencies, etc.
[x] fix python plugin not setting breakpoint and continue not running
[x] allow run_command_with_match to match on multiple groups in line for array - e.g in python break lists breakpoints and line and filename need to be caught together
[x] get/test python plugin working in atide
[n] abstract the command_handler into an interface called handler_interface
[x] change run_command to use interpolation and convert run_command_string to use run_command
[x] fix tide crashing after make vim_python finishes debugging
[n] add templates to config
