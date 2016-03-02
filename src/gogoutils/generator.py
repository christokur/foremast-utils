class GeneratorError(Exception):
    pass


class Generator(object):
    """Generates application details"""

    def __init__(self, project, repo, env='dev'):

        if not all([project, repo, env]):
            error = 'project, repo or env may not be "None" or emtpy'
            raise GeneratorError(error)

        self.project = project.lower()
        self.repo = repo.lower()
        self.env = env.lower()
        self.app = '{0}{1}'.format(project, repo)

    def app_name(self):
        """Generate application name"""
        return self.app

    def dns_elb(self):
        """Generate dns domain"""
        dns = '{0}.{1}.{2}.example.com'.format(
            self.repo,
            self.project,
            self.env
        )

        return dns

    def dns_instance(self):
        """Generate dns instance"""

        instance = '{0}{1}-xx.{2}.example.com'.format(
            self.repo,
            self.project,
            self.env,
        )

        return instance

    def dns(self):
        """Combined dns details"""
        dns = {
            'elb': self.dns_elb(),
            'instance': self.dns_instance(),
        }

        return dns

    def iam(self):
        """Generate iam details"""

        iam_base_name = '{0}_{1}'.format(
            self.project,
            self.repo,
        )

        iam = {}

        iam['user'] = iam_base_name
        iam['group'] = self.project

        iam['role'] = '{0}_role'.format(
            iam_base_name,
        )

        iam['policy'] = '{0}_policy'.format(
            iam_base_name,
        )

        return iam

    def archaius(self):
        """Generate archaius bucket path"""
        archaius = {}

        archaius['s3'] = 'archaius-{0}/{1}/{2}{1}/'.format(
            self.env,
            self.project,
            self.repo,
        )

        return archaius

    def jenkins(self):
        """Generate jenkins job details"""

        job = {}

        job['name'] = '{0}_{1}'.format(
            self.project,
            self.repo,
        )

        return job

    def gitlab(self):
        """Generate gitlab details"""

        git = {}

        git['main'] = '{0}/{1}'.format(
            self.project,
            self.repo,
        )

        git['qe'] = '{0}/{1}-qa'.format(
            self.project,
            self.repo,
        )

        git['config'] = '{0}/{1}-config'.format(
            self.project,
            self.repo,
        )

        return git