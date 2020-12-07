playlist_dict = {
	'name'		: 'Patagonia Bus',
	'created_by': 'Colt Stelle',
	'songs'		: [
		{
			'name'		: 'Turn it off',
			'artist'	: ['Culture Artisto'],
			'album'		: 'French R',
			'date'		: '2017-10-31',
			'duration'	: 3.5
		},
		{
			'name'		: 'Turn it on',
			'artist'	: ['Culture Artisto Pro'],
			'album'		: 'French RR',
			'date'		: '2017-12-31',
			'duration'	: 3.6
		}
	]
}

total_duration = sum(song['duration'] for song in playlist_dict['songs'])

print(f'the total song duration is {total_duration}')

