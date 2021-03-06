# coding=utf-8
i18n = {
	'name': 'Humans vs Infected',
	'lang': 'English',
	'pass': 'Password Reset',
	'nav': {
		'home':'Home',
		'blog':'Blog',
		'missions':'Missions',
		'party':'Party',
		'register':'Registration',
		'rules':'Rules',
		'stats':'Stats',
		'station':'Station Operations'
	},
	'navd': {
		'game': 'Game'
	},
	'profile': 'User Profile',
	'player_status': {
		'state': 'State',
		'active': 'Active',
		'inactive': 'Inactive',
		'human': 'Human',
		'zombie': 'Zombie',
		'banned': 'Banned'
	},
	'pages': {
		'countdown': {
			'title': 'Countdown / Compte à Rebours'
		},
		'index': {
			'title': 'Home'
		},
		'login': {
			'title': 'Login'
		},
		'blog': {
			'title': 'Blog'
		},
		'thanks': {
			'title': 'Thanks',
			'thanks': 'Thanks for registering, redirecting you back to the main page...'
		},
		'party': {
			'title': 'Party'
		},
		'missions': {
			'title': 'Missions'
		},
		'rules': {
			'title': 'Rules'
		},
		'login': {
			'title': 'Login',
			'nouser': 'No such user or incorrect password'
		},
		'graph': {
			'title': 'Statistics',
			'zombiecount24': 'Zombie Count (24 hours)',
			'zombiecountw': 'Zombie Count (Week)',
			'player': 'Players',
			'time': 'Time',
			'topzombies': 'Top Zombies',
			'count': 'Count'
		},
		'create_editpost': {
			'missinginfo': 'Missing a field, make sure all fields have beein submitted.',
			'unknown': 'Unknown error occured, please try again.',
			'nopostpid': "A post with this ID doesn't exist.",
			'post_title': 'Title',
			'post_content': 'Content',
			'allow_comments': 'Allow Comments?',
			'cancel': 'Cancel'
		},
		'post_create': {
			'submit': 'Create',
			'title': 'Create Post'
		},
		'post_edit': {
			'submit': 'Edit',
			'title': 'Edit Post'
		},
		'game': {
			'title': 'Game Control',
			'start': 'Start Game',
			'end': 'End Game',
			'startr': 'Open Registrations',
			'endr': 'Close Registrations',
			'encount': 'Enable Countdown',
			'discount': 'Disable Countdown'
		},
		'register': {
			'title': 'Registration',
			'name': 'Name (first and last)',
			'username': 'Username',
			'password': 'Password',
			'password_confirm': 'Password (confirm)',
			'language': 'Language',
			'student_num': 'Student Number',
			'email': 'Email',
			'twitter': 'Twitter',
			'cell': 'Cell Number',
			'gameid': 'Game ID',
			'yes': 'Yes',
			'no': 'No',
			'optional': 'Optional',
			'required': 'Required',
			'register': 'Register',
			'userinfo': 'Player Information',
			'eula': 'Safety and Liability',
			'safety': 'I have read and accepted the',	# format in page: page['safety'] a(text=page['safetyrules'])
			'safetyrules': 'safety rules',
			'liability': 'I have read and accepted the',# same format
			'liabilitywaiver': 'liability waiver',
			'userexists': 'User already registered.',
			'changedlater': 'Can be changed later',
			'missinginfo': 'Please make sure all required fields are filled in',
			'wronginfo': 'Incorrect information submitted',
			'noslash': 'No slashes are permitted in usernames',
			'liability_read': 'The liability waiver has not been read',
			'safety_read': 'The safety rules have not been read',
			'liability_err': 'You may not register unless you agree to the terms in the liability waiver',
			'safety_err': 'You may not register unless you agree to the safety rules',
			'human?': 'Are you human? (Zombies not allowed!)',
			'badanswer': 'Incorrect response to verification question',
			'question': {
				'arithmetic': ['What is the result of %(left)s %(op)s %(right)s?'],
				'logic': ['Is %(left)s %(op)s %(right)s?  Yes or No'],
				'wo': 'Type the answer as a word.'
			}
		},
		'eula': {
			'title': 'Safety and Liability',
			'agree': 'Agree'
		},
		'webcheckin': {
			'title': 'Web Checkin',
			'already': 'You have already used your web checkin.',
			'notice': 'You have one web checkin, select the checkbox and click "Web Checkin" to use it.',
			'confirm': 'Confirm',
			'notconfirmed': 'You did not click the "Confirm" checkbox.',
			'soon': 'Your last check-in was less than 5 hours ago.',
			'human': 'Player is not a human.',
			'kit': 'Player has not picked up kit',
			'opererations': 'Unknown error'
		},
		'pass_reset': {
			'title': 'Password Reset',
			'success': 'Your password has been reset to your student number',
			'submit': 'Reset password',
			'wronginfo': 'Incorrect information submitted'
		},
		'station': {
			'title': 'Station Operations',
			'checkin': {
				'title': 'Player Checkin',
				'userid': 'User ID',
				'submit': 'Checkin'
			},
			'cure': {
				'title': 'Cure Zombie',
				'userid': 'User ID',
				'cureid': 'Cure Card ID',
				'submit': 'Cure'
			},
			'tag': {
				'title': 'Register Tag',
				'taggerid': 'Zombie',
				'taggeeid': 'Victim',
				'submit': 'Tag',
				'game': 'Game not started'
			},
			'activate': {
				'title': 'Player Activation',
				'userid': 'User ID',
				'submit': 'Activate'
			},
			'baduser': 'No such user(s)',
			'game': 'Game not started',
			'generic': 'Error',
			'errors': {
				'notzombie': 'A player must be a zombie',
				'nothuman': 'A player must be a human',
				'noplayer': 'No player with that ID exists',
				'nohuman': 'No human with that ID exists',
				'nozombie': 'No zombie with that ID exists',
				'notstarted': 'Game not started',
				'kithuman': 'Human has not picked up kit',
				'kitzobie': 'Zombie has not picked up kit',
				'wtf': 'You are not a station and yet you managed to get this far.  Congratulations, now email me how you did it: r0ssar00@gmail.com',
				'unknown': 'Unknown error',
				'nouid': 'No user ID given',
				'nocid': 'No card ID given',
				'toosoon': 'Player checking in too soon',
				'disq': 'Cure card with this ID was disqualified',
				'used': 'Cure card with this ID was already used',
				'activated': 'Player has already been activated',
				'exp': 'Cure card expired'
			}
		},
		'users': {
			'title': 'Users',
			'table': {
				'id': 'ID',
				'username': 'Username',
				'game_id': 'Game ID',
				'name': 'Name',
				'status': 'Status',
				'signedin': 'Active'
			},
			'search_heading': 'Retrieve User',
			'match_on': 'Match via',
			'retrieve': 'Retrieve',
			'nouser': 'No user with the specified %s exists',
			'email': 'email',
			'twitter': 'twitter',
			'cell': 'cell',
			'student_num': 'student number'
		},
		'user_edit': {
			'title': '',
			'editing': 'Editing',
			'oldpass': 'Old Password',
			'userinfo': 'Basic User Data',
			'passchange': 'Change Password',
			'zero': 'Patient Zero?',
			'makezero': 'Make this player Patient Zero'
		},
		'cures': {
			'title': 'Cure Cards',
			'table': {
				'id': 'ID',
				'username': 'Username',
				'time': 'Time Used',
				'expiry': 'Expiry Date',
				'disqualified': 'Disqualified',
				'disqualify': 'Disqualify',
				'qualify': 'Qualify',
				'used': 'Used',
				'cardid': 'Card ID',
				'delete': 'Delete?'
			},
			'addcure': 'Add Cure',
			'deletecures': 'Delete Cures'
		},
		'cure_edit': {
			'title': 'Edit Cure',
		},
		'tags': {
			'title': 'Edit Tags',
			'submit': 'Delete Tag(s)',
			'vs': 'vs',
			'table': {
				'id': 'Tag ID',
				'method': 'Report Method',
				'time': 'Time',
				'killer': 'Tagger',
				'victim': 'Victim',
				'delete': 'Delete?',
				'cure': 'Cure Victim?'
			}
		},
		'tag': {
			'title': 'Register A Tag',
			'tag': 'Tag',
			'unknown': 'Unknown error',
			'duplicate': 'Duplicate found, reload the page and try again'
		},
		'checkins': {
			'title': 'Checkins',
			'addcheckin': 'Add Checkin',
			'delcheckin': 'Delete Checkin',
			'add': 'Add',
			'delete': 'Delete',
			'table': {
				'id': 'ID',
				'time': 'Time',
				'location': 'Location'
			}
		},
		'email': {
			'title': 'Mass Email',
			'nomsg': 'No body for email',
			'nosubj': 'No subject given',
			'nocon': 'Unable to connect to SMTP server',
			'badlogin': 'Unable to login to SMTP server',
			'nosend': 'Unable to send email, try again'
		},
		'user_view': {
			'title': '',
			'none': 'None',
			'stats': 'Statistics',
			'kills': 'Tags',
			'deaths': 'Deaths',
			'cures': '# Used cure cards',
			'checkin': 'Last checkin',
			'edit': 'Edit',
			'activate': 'Activate Player',
			'kitted': 'Player has accepted liability + safety rules and has received kit?',
			'tags': 'Tags involving this player',
			'and': 'and',
			'checkins': 'Checkin Editor'
		},
		'http_error': {
			'title': 'Error',
			'sorry_part_1': 'Sorry, the requested URL',
			'sorry_part_2': 'caused an error',
			'back': 'Back'
		}
	},
	'sidebar': {
		'status': {
			'title': 'Status',
			'subtitle': '',
			'by': 'by',
			'kills': 'Tags',
			'humans': 'Humans',
			'zombies': 'Zombies',
			'users': 'Players',
			'used_cures': 'Used Cures',
			'unused_cures': 'Unused Cures',
			'regtag': 'Register a Tag',
			'died': 'Died',
			'cured': 'Cured',
			'zero': 'Patient Zero'
		},
		'controls': {
			'title': 'Control Panel',
			'subtitle': '',
			'station': 'Station Operations',
			'userlist': 'User List',
			'curelist': 'Cure Cards',
			'taglist': 'Tags'
		}
	},
	'post': {
		'edit_post': 'Edit post',
		'edit_entry': 'Edit this entry',
		'delete_post': 'Delete post',
		'delete_entry': 'Delete this entry',
		'permalink': 'Permanent link to',	# Permanent link to PostName
		'comment': {
			'on': 'Comment on',				# Comment on PostName
			'reply': 'Reply'
		},
		'comment_form': {
			'comments': 'Comments',
			'submit': 'Submit'
		},
		'nocomments': 'No comments yet',
		'postyourcomment': 'Post your comments',
		'cancelreply': 'Click here to cancel reply.'
	},
	'loggedinas': 'Logged in as',			# logged in as UserName
	'logoutof': 'Log out of this account',
	'altlang': {
		'key': 'f',
		'name': u'Français'
	},
	'days': [
		'Sunday',
		'Monday',
		'Tuesday',
		'Wednesday',
		'Thursday',
		'Friday',
		'Saturday'
	],
	'email': {
		'subject': 'HvsI: Auto-tag',
		'message': 'You have been auto-tagged because you did not check-in twice today.\nPlease stop by a station and exchange your bandanna.'
	},
	'passemail': {
		'subject': 'HvsI: Password Reset Request',
		'message': 'You have requested a password reset, open http://hvsi.ca/?key=%s to continue.'
	},
	'logout': 'Logout',
	'app': {
		'languages': ['English', 'Français'],
		'name': 'HvsI',
		'language': 'Language',
		'pages': {
			'register': {
				'title': 'Register',
				'inprogress': 'Registering&#8230;',
				'complete': 'Registration Complete',
				'complete_msg': 'Visit an HvsI station starting %1$s at %2$s to pick up your kit.',
				'errors': {
					'invalid_email': 'This email address is invalid',
					'dup': 'A user already exists with some or all of this identifying information.',
					'pass': 'Passwords do not match; check your spelling and try again.',
					'other': 'An internal error occured, please try again.',
					'bad': 'Registration Failed'
				}
			},
			'login': {
				'title': 'Login',
				'inprogress': 'Logging in&#8230;',
				'error_failed': 'Login failed'
			},
			'forgot_password': {
				'title': 'Recover lost password',
				'ok': 'An email was sent to the address associated with the specified username.  Follow the instructions within to reset your password.',
				'fail': 'No account with the specified username.  Check spelling and try again.'
			},
			'post': {
				'no_posts': 'No blog posts yet'
			},
			'tag': {
				'human_go': 'Tag!',
				'human_scan': 'Scan',
				'human_hint': 'Human Code',
				'zombie_hint': 'Zombie Username'
			}
		},
		'fields': {
			'name': 'Name',
			'username': 'Username',
			'email': 'Email address',
			'password': 'Password',
			'password_confirm': 'Password (confirm)',
			'language': 'Language',
			'student_number': 'Student Number',
			'cell': 'Cell Number (optional)',
			'twitter': 'Twitter Handle (optional)'
		},
		'tabs': [
			'Info',
			'Blog',
			'Tag',
			'Profile',
			'Station',
			'Admin'
		]
	}
}
