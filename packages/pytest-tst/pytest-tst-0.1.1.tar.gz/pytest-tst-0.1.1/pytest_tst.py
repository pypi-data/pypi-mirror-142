import pytest
from pytest import ExitCode


def pytest_addoption(parser):
    opts = parser.getgroup('tst')

    opts.addoption('--tst',
        action='store_true',
        default=False,
        help='Customize output to run from tst'
    )

    opts.addoption('--clean',
        action='store_true',
        default=False,
        help='Clean output in tst mode'
    )


@pytest.hookimpl(tryfirst=True)
def pytest_load_initial_conftests(args):
    if "--tst" not in args:
        # not --tst option in command line
        return

    # import module under test
    try:
        from tst.undertest import __test_files, __cline_files, __cline_target
        import tst.undertest as undertest
    except ImportError as e:
        raise Exception("failed importing tst.undertest")

    if undertest.__filename is None:
        if undertest.__candidates:
            raise pytest.UsageError("tst: ambiguous target for tst")
        else:
            raise pytest.UsageError("tst: no target file for tst")

    # case 1: pytest --tst (no target, no further filenames in cmd line)
    if not __cline_files: # and, thus, not __cline_target
        # make pytest collect tests in __filename
        args.extend(reversed(__test_files))
        args.append(undertest.__filename)

    # case 2: --tst <target> (with no other filename in cmd line)
    elif __cline_target and __cline_files == [undertest.__filename] or not __cline_files:
        # make pytest collect tests in all __test_files
        args.extend(reversed(__test_files))

    # case 3: pytest ... <filename> ... --tst <target> ... <filename>
    elif __cline_target and __cline_files != [undertest.__filename]:
        # make pytest NOT collect tests from __filename (target)
        args.remove(undertest.__filename)

    if '--clean' in args:
        args.append("--quiet")
        args.append("--capture=no")
        args.append("--no-summary")
        args.append("--color=no")
        args.append("-o console_output_style=none")


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    if session.config.getoption('--tst'):
        if exitstatus == ExitCode.TESTS_FAILED: # or exitstatus == ExitCode.NO_TESTS_COLLECTED:
            session.exitstatus = ExitCode.OK
