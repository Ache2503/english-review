import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from seeds.seed_runner import run_seed_file


class SeedRunnerTests(unittest.TestCase):
    def test_run_seed_file_executes_main_function(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            marker = os.path.join(tmpdir, 'seed_ran.txt')
            script = os.path.join(tmpdir, 'sample_seed.py')
            with open(script, 'w', encoding='utf-8') as fh:
                fh.write(
                    "def main():\n"
                    f"    open(r'{marker}', 'w', encoding='utf-8').write('ok')\n"
                )

            success, message = run_seed_file(script)

            self.assertTrue(success)
            self.assertTrue(os.path.exists(marker))
            self.assertEqual(open(marker, 'r', encoding='utf-8').read(), 'ok')


if __name__ == '__main__':
    unittest.main()
