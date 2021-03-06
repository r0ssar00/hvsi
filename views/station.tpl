%today = datetime.datetime.now()
%eight30 = datetime.datetime(today.year, today.month, today.day, 8, 00, 0, 0)
%four30 = datetime.datetime(today.year, today.month, today.day, 18, 00, 0, 0)
%cinclude part_html_decl
<head>
%	cinclude head
</head>
%cinclude part_html_body
			%s=i18n[lang]['pages'][page]
%		if not started and hasattr(request, 'station') and request.station:
				<h3>{{i18n[lang]['pages'][page]['errors']['notstarted']}}</h3>
				<br/>
%		else:
%			  # don't show the form if we're a station and we're not in the window
%			  if eight30 <= today <= four30 or (hasattr(request, 'admin') and request.admin):
				%i=s['checkin']
				<h3>{{i['title']}}</h3>
%			  if 'section' in globals() and section == 'checkin':
%			   if error:
					<div style="color: red;">
					{{i18n[lang]['pages'][page]['errors'][err]}}
				</div>
%			   end
%			  end
				<form action="/station/checkin" method="post">
					<div>
						<label for="user_id">
							%r = i18n[lang]['pages']['register']
							{{i['userid']}}: <em>({{r['username']}}, {{r['twitter']}}, {{r['email']}}, {{r['student_num']}})</em>
							%del r
						</label>
					</div>
					<div>
						<input type="textbox" name="user_id" />
					</div>
					<div>
						<label for="submit">
							&nbsp;
						</label>
					</div>
					<div>
						<input type="submit" name="submit" value="{{i['submit']}}" />
					</div>
					%del i
				</form>
				<br/>
				<br/>
%			  end
				%i=s['tag']
				<h3>{{i['title']}}</h3>
%			  if 'section' in globals() and section == 'kill':
%			   if error:
				<div style="color: red;">
					{{i18n[lang]['pages'][page]['errors'][err]}}
				</div>
%			   end
%			  end
				<form action="/station/tag" method="post">
					<div>
						<label for="tagger_id">
							%r = i18n[lang]['pages']['register']
							{{i['taggerid']}}: <em>({{r['username']}}, {{r['twitter']}}, {{r['email']}}, {{r['student_num']}})</em>
							%del r
						</label>
					</div>
					<div>
						<input type="textbox" name="tagger_id" />
					</div>
					<div>
						<label for="taggee_id">
							{{i['taggeeid']}}: <em>(game id)</em>
						</label>
					</div>
					<div>
						<input type="textbox" name="taggee_id" />
					</div>
					<div>
						<label for="submit">
							&nbsp;
						</label>
					</div>
					<div>
						<input type="submit" name="submit" value="{{i['submit']}}" />
					</div>
					%del i
				</form>
				<br/>
				<br/>
%		end
				%i=s['activate']
				<h3>{{i['title']}}</h3>
%			  if 'section' in globals() and section == 'activate':
%			   if error:
				<div style="color: red;">
					{{i18n[lang]['pages'][page]['errors'][err]}}
				</div>
			   %end
			  %end
			  	<form action="/station/activate" method="post">
			  		<div>
			  			<label for="user_id">
			  				%r = i18n[lang]['pages']['register']
			  				{{i['userid']}}: <em>({{r['student_num']}})</em>
			  				%del r
			  			</label>
			  		</div>
			  		<div>
			  			<input type="textbox" name="user_id" />
			  		</div>
			  		<div>
			  			<label for="submit">
			  				&nbsp;
			  			</label>
			  		</div>
			  		<div>
			  			<input type="submit" name="submit" value="{{i['submit']}}" />
			  		</div>
			  	</form>
			  	<br/>
			  	<br/>
%		if not started and hasattr(request, 'station') and request.station:
%			pass
%		else:
				%i=s['cure']
				<h3>{{i['title']}}</h3>
%			  if 'section' in globals() and section == 'cure':
%			   if error:
				<div style="color: red;">
					{{i18n[lang]['pages'][page]['errors'][err]}}
				</div>
%			   end
%			  end
				<form action="/station/cure" method="post">
					<div>
						<label for="user_id">
							%r = i18n[lang]['pages']['register']
							{{i['userid']}}: <em>({{r['username']}}, {{r['twitter']}}, {{r['email']}}, {{r['student_num']}})</em>
							%del r
						</label>
					</div>
					<div>
						<input type="textbox" name="user_id" />
					</div>
					<div>
						<label for="cure_id">
							{{i['cureid']}}:
						</label>
					</div>
					<div>
						<input type="textbox" name="cure_id" />
					</div>
					<div>
						<label for="submit">
							&nbsp;
						</label>
					</div>
					<div>
						<input type="submit" name="submit" value="{{i['submit']}}" />
					</div>
					%del i
				</form>
				<br/>
%		end
%			cinclude post lang='e',template_settings=dict(noescape=True)
			<br/>
			</div>
%cinclude part_html_sidebar
</body>
</html>
