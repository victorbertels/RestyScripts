[{_id: '5f9fd1ed8139f0781cb7a153', _created: '2020-11-02T09:31:25.134000Z', _updated: '2021-02-18T10:28:58.000000Z', _etag: '1a1583ad390df677142c9cb3d986babb9caf9fe1', account: '5c6fdf3fc6489f0001961cdf', name: 'victor.tester12345@gmail.com', email: 'victor.tester12345@gmail.com', function: '', profileImageURL: 'https://lh3.googleusercontent.com/-0qyr0ubcFMQ/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucka9VdGYJFIhbQ7YGMjgsZZKXV2Sg/s96-c/photo.jpg', oauthProvider: 'google-oauth2', oauthProviderId: 'google-oauth2|109569698273299429013', locations: [], roles: [2, 6000, 6001, 8500, 8510, 9000, 11000, 12010, 12050, 12100, 15500, 16000, 17000, 17001, 17500, 18000, 18550, 19000, 19500, 20000, 20500, 21000, 21500, 21550, 22000, 22100, 22500, 23000, 23050, 23100, 23150, 23200, 23250, 23300, 23350, 24000, 25500, 28000], groups: ['5d4d5e3bf133a500012058c5', '5e7b24e334c93a000186f53e', '5fc1115c9fa0292bf60e589f']}]

for us in users:
	new_group = ['602e2c108a0a621797d4cfce'] 
	old_group = us.get('groups')
	new_group = old_group + new_group
	print(new_group)

for role in users:
	new_role = [40000]
	old_role_list = role.get('roles')
	new_role_list = old_role_list + new_role
	print(new_role_list)
