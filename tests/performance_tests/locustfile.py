from locust import HttpUser, task


class ProjectPerfTest(HttpUser):
	@task
	def homme(self):
		self.client.get('/')

	@task(3)
	def login(self):
		response = self.client.get('/showSummary')