import os
import stat
import sys
from collections import OrderedDict
from pprint import pformat

from lumo.proc.date import strftime
from lumo.proc.explore import git_enable
from lumo.utils.exithook import wrap_before
from .experiment import Experiment
from ..proc.dist import is_main
from ..utils.safe_io import IO


class ExpHook:
    INFOs = None

    def regist(self, exp: Experiment): self.exp = exp

    def on_start(self, exp: Experiment, *args, **kwargs): pass

    def on_end(self, exp: Experiment, end_code=0, *args, **kwargs): pass

    def on_progress(self, exp: Experiment, step, *args, **kwargs): pass

    def on_newpath(self, exp: Experiment, *args, **kwargs): pass


class LastCmd(ExpHook):
    def on_start(self, exp: Experiment, *args, **kwargs):
        argv = exp.exec_argv
        fn = f'run_{os.path.basename(argv[1])}.sh'

        strings = OrderedDict.fromkeys([i.lstrip('#').strip() for i in IO.load_text(fn).split('\n')])

        cur = f"{' '.join(argv)} $@"
        if cur in strings:
            strings.pop(cur)

        with open(fn, 'w', encoding='utf-8') as w:
            w.write('\n'.join([f'# {i}' for i in strings.keys()]))
            w.write('\n\n')
            w.write(cur)

        st = os.stat(fn)
        os.chmod(fn, st.st_mode | stat.S_IEXEC)


# class LogCmd(ExpHook):
#     """a './cache/cmds.log' file will be generated, """
#
#     def on_start(self, exp: Experiment, *args, **kwargs):
#         from lumo.proc.date import strftime
#         fn = exp.project_cache_fn(f'{strftime("%y-%m-%d")}.log', 'cmds')
#         res = exp.exec_argv
#
#         with open(fn, 'a', encoding='utf-8') as w:
#             w.write(f'{strftime("%H:%M:%S")}, {exp.test_root}, {res[0]}, {exp.commit_hash}\n')
#             res[0] = os.path.basename(res[0])
#             w.write(f"> {' '.join(res)}")
#             w.write('\n\n')


# class LogTestGlobally(ExpHook):
#     def on_start(self, exp: Experiment, *args, **kwargs):
#         fn = os.path.join(libhome(), FN.TESTLOG)
#         with open(fn, 'a', encoding='utf-8') as w:
#             w.write(f'{exp.test_root}\n')
#

# class LogTestLocally(ExpHook):
#     def on_start(self, exp: Experiment, *args, **kwargs):
#         local_ = local_dir()
#         if local_ is None:
#             return
#         fn = os.path.join(local_, FN.TESTLOG)
#         with open(fn, 'a', encoding='utf-8') as w:
#             w.write(f'{exp.test_root}\n')

#
# class RegistRepo(ExpHook):
#     def on_start(self, exp: Experiment, *args, **kwargs):
#         from ..proc.const import FN
#         from ..proc.const import CFG
#         from lumo.utils import safe_io as io
#         fn = os.path.join(libhome(), FN.REPOSJS)
#         res = None
#         if os.path.exists(fn):
#             res = io.load_json(fn)
#         if res is None:
#             res = {}
#
#         inner = res.setdefault(exp.project_hash, {})
#         inner['name'] = exp.project_name
#         repos = inner.setdefault('repo', [])
#         if exp.project_root not in repos:
#             repos.append(exp.project_root)
#         storages = inner.setdefault('exp_root', [])
#         if exp.exp_root not in storages:
#             storages.append(exp.exp_root)
#
#         io.dump_json(res, fn)


class PathRecord(ExpHook):

    def on_newpath(self, exp: Experiment, *args, **kwargs):
        super().on_newpath(exp, *args, **kwargs)


class Diary(ExpHook):
    def on_start(self, exp: Experiment, *args, **kwargs):
        super().on_start(exp, *args, **kwargs)
        with open(exp.root_branch.file(f'{strftime("%y%m%d")}.log', 'diary'), 'a') as w:
            w.write(f'{strftime("%H:%M:%S")}, {exp.test_root}\n')


class RecordAbort(ExpHook):
    def regist(self, exp: Experiment):
        super().regist(exp)
        wrap_before(self.exc_end)

    def exc_end(self, exc_type, exc_val, exc_tb):
        import traceback
        res = traceback.format_exception(exc_type, exc_val, exc_tb)
        res = [i for i in res if 'in _newfunc' not in i]
        self.exp.dump_string('exception', "".join(res))
        self.exp.end(
            end_code=1,
            exc_type=traceback.format_exception_only(exc_type, exc_val)[-1].strip()
        )


class LogCMDAndTest(ExpHook):
    def on_start(self, exp: Experiment, *args, **kwargs):
        pass
        # get_global_logger().raw(f"{exp.test_root} | {' '.join(sys.argv)}")

    def on_end(self, exp: Experiment, *args, **kwargs):
        from lumo.kit.logger import get_global_logger
        get_global_logger().raw(f"{exp.test_root} | {' '.join(sys.argv)}")


class TimeMonitor(ExpHook):
    def _create_agent(self, exp: Experiment):
        import subprocess, sys
        from lumo.kit import agent
        cmd = [
            sys.executable, '-m', agent.__spec__.name,
            f"--state_key=state",
            f"--pid={os.getpid()}",
            f"--test_name={exp.test_name}",
            f"--exp_name={exp.exp_name}",
            f"--argv={exp.exp_name}",
            # f"--params={sys.argv}" # TODO add sys.argv
        ]
        subprocess.Popen(' '.join(cmd),
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,
                         start_new_session=True)

    def on_start(self, exp: Experiment, *args, **kwargs):
        super().on_start(exp)
        self._create_agent(exp)
        exp.dump_info('state', {
            'start': strftime(),
            'end': strftime()
        })


class GitCommit(ExpHook):
    INFOs = 'git'

    def on_start(self, exp: Experiment, *args, **kwargs):
        if git_enable() and is_main():
            from lumo.utils.repository import commit
            commit_ = commit(key='lumo', info=exp.test_root)
            commit_hex = commit_.hexsha[:8]

            if commit_ is not None:
                exp.dump_info('git', {
                    'commit': commit_hex,
                    'repo': exp.project_root,
                })


class ExecuteInfo(ExpHook):
    INFOs = 'execute'

    def regist(self, exp: Experiment):
        super().regist(exp)
        exp.dump_info('execute', {
            'repo': exp.project_root,
            'cwd': os.getcwd(),
            'exec_file': sys.argv[0],
            'exec_bin': sys.executable,
            'exec_argv': sys.argv
        })


class LockFile(ExpHook):
    INFOs = 'lock'

    def on_start(self, exp: Experiment, *args, **kwargs):
        from lumo.proc.dependency import get_lock
        exp.dump_info('lock', get_lock('torch', 'numpy'))


class FinalReport(ExpHook):
    def on_end(self, exp: Experiment, end_code=0, *args, **kwargs):
        # if end_code == 0:
        print('Successful Experiment.')
        # print('')
        print('Use paths')
        print(pformat(exp.paths))
