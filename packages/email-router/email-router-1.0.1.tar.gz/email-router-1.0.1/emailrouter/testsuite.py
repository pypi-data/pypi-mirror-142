import logging
import os

import yaml

from emailrouter import Email, Router


logger = logging.getLogger(__name__)


class Tester:
    def __init__(self, test_root):
        self.test_root = test_root

    def run_test(self, test_name):
        logger.info('Running test %s.', test_name)
        with open('test.yml') as f:
            test_config = yaml.safe_load(f.read())
        router = Router.from_yaml_file(test_config['config'])

        success = 0
        total = len(test_config['emails'])
        for email in test_config['emails']:
            em = Email.from_file(email['file'])
            actual = router.execute(em)
            if actual == email['expected']:
                success += 1
            else:
                logging.error(
                    'Test %s - %s failed. Expected: %s. Actual: %s.',
                    test_name,
                    email['name'],
                    email['expected'],
                    actual,
                )
        logging.info('Test %s results: %d/%d.', test_name, success, total)
        return success == total

    def test_all(self):
        pwd = os.getcwd()

        success = 0
        total = 0
        for d in os.listdir(self.test_root):
            path = os.path.join(self.test_root, d)
            if not os.path.isdir(path) or 'test.yml' not in os.listdir(path):
                continue
            os.chdir(path)
            try:
                success += self.run_test(d)
            except:  # noqa
                logging.exception('Test %s crashed.', d)
            total += 1
            os.chdir(pwd)
        logging.info('Tests: %d/%d', success, total)
        return success == total
