import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from jenkins_tasks import DevOpsJenkins

class TestJenkins(unittest.TestCase):

    def test_build(self):
        # Given
        task = DevOpsJenkins()
        task.input_properties = {
            'url': 'http://localhost:8082',
            'username': 'admin',
            'password': 'Master@28'
        }

        # When
        task.execute_task()

        # Then
        self.assertEqual(task.get_output_properties()['response'], 'SUCCESS')

if __name__ == '__main__':
    unittest.main()