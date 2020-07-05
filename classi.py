from pyppeteer import launch
import asyncio

class Classi():
	def __init__(self, username, password):
		self.payload = {
			'id': username,
			'password': password,
		}
	async def __aenter__(self):
		self._browser = await launch(headless=True)
		self._page = await self._browser.newPage()
		await self._page.goto('https://auth.classi.jp/students')
		await self._page.type('input[name=classi_id]', self.payload['id'])
		await self._page.type('input[name=password]', self.payload['password'])
		await self._page.click('button[name=button]')
		await asyncio.wait([self._page.waitForNavigation()])
		return self
	async def post_today_report(self, note):
		await self._page.goto('https://study.classi.jp/')
		await self._page.waitForSelector('button[class="btn btn-default btn-sm mb15"]')
		await self._page.click('button[class="btn btn-default btn-sm mb15"]')
		await self._page.waitForSelector('textarea[name=note]')
		await self._page.type('textarea[name=note]', note, {'clear': True})
		await self._page.click('button[class="btn btn-primary btn-lg"]')
		await self._page.goto('https://platform.classi.jp/')
		await asyncio.wait([self._page.waitForNavigation()])
	async def __aexit__(self, exc_type, exc, tb):
		await self._browser.close()
class Subject():
	def __init__(self, id, note):
		self.id = id
		self.note = note