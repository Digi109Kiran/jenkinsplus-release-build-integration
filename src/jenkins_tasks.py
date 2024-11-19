from digitalai.release.integration import BaseTask
import jenkins
import time


class DevOpsJenkins(BaseTask):
    def execute(self) -> None:
        # Process input
        server = self.input_properties['url']
        if server is None:
            raise ValueError("Server field cannot be empty")
        username = self.input_properties['username']
        password = self.input_properties['password']

        self.jenkins_server = jenkins.Jenkins(server, username=username, password=password)
        user = self.jenkins_server.get_whoami()
        version = self.jenkins_server.get_version()
        print("Jenkins Version: {}".format(version))
        print("Jenkins User: {}".format(user['id']))

        next_build_number = self.jenkins_server.get_job_info('Test')['nextBuildNumber']
        print("next_build_number : {}".format(next_build_number))
        self.jenkins_server.build_job('Test', parameters=None, token=None)
        time.sleep(10)
        response = self.jenkins_server.get_build_info('Test', next_build_number)
        print("build_info : {}".format(response))
        self.set_output_property('response', response['result'])
        print("response['result'] : {}".format(response['result']))


if __name__ == "__main__":
    NAME_OF_JOB = "<job_name>"
    TOKEN_NAME = "<token>"
    # Example Parameter
    PARAMETERS = {'project': 'devops'}
    jenkins_obj = DevOpsJenkins()
    output = jenkins_obj.build_job(NAME_OF_JOB, PARAMETERS, TOKEN_NAME)
    print("Jenkins Build URL: {}".format(output['url']))
