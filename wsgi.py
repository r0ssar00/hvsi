import bottle, os, sys, datetime, urlimport, time
static_root = os.getcwd()
__all__ = ['application']
try:
	from settings import instanceconfig
	os.environ['TZ'] = instanceconfig.timezone
	time.tzset()
	import controller
	application = bottle.default_app()
	application.catchall = False
	if instanceconfig.debug == True:
		from werkzeug.debug import DebuggedApplication
		application = DebuggedApplication(application, evalex=True)
	elif not instanceconfig.debug:
		import paste.exceptions.errormiddleware
		# monkey-patch in logging to datestamped files or gmail
		# the latter is needed when access to datestamped files is impossible
		import exception_logging
		paste.exceptions.errormiddleware.reporter = exception_logging
		from paste.exceptions.errormiddleware import ErrorMiddleware
		application = ErrorMiddleware(application,
									  debug=False,
									  error_log=instanceconfig.exceptionpath,
									  error_email=instanceconfig.smtp_to,
									  from_address=instanceconfig.smtp_from,
									  smtp_server=instanceconfig.smtp_server,
									  smtp_username=instanceconfig.smtp_user,
									  smtp_password=instanceconfig.smtp_pass,
									  error_subject_prefix=instanceconfig.host + ' error:')
except Exception, e:
	print "Couldn't load main app, traceback follows.  Starting config app instead."
	import traceback
	traceback.print_exc()
	import config_app
	application = config_app.app

